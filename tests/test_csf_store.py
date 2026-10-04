import sqlite3
import tempfile
import unittest
from pathlib import Path

import csf_analyst_store as store
from csf_information_flows import INFORMATION_FLOW_EDGES


class CsfStoreTests(unittest.TestCase):
    """Regression coverage for the records the standalone analyst actually uses."""

    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temporary_directory.name) / "csf-analyst.db"
        self.connection = store.connect_db(self.database_path)
        store.init_db(self.connection)
        self.profile = store.create_csf_profile_definition(
            self.connection,
            "Test profile",
            "A single-user PC used for test records.",
            recorded_by="test-analyst",
        )
        self.profile_id = self.profile["profile_id"]

    def tearDown(self) -> None:
        self.connection.close()
        self.temporary_directory.cleanup()

    def test_initialization_seeds_frozen_profiles_and_selects_an_organizational_profile(self) -> None:
        profiles = store.list_csf_profile_definitions(self.connection)
        names = {profile["profile_name"] for profile in profiles}

        self.assertIn("NIST CSF 2.0 Base Profile", names)
        self.assertIn("Test profile", names)
        self.assertEqual("Test profile", store.get_active_csf_profile(self.connection)["profile_name"])

        frozen = next(profile for profile in profiles if profile["profile_name"] == "NIST CSF 2.0 Base Profile")
        self.assertEqual("frozen_base", frozen["profile_kind"])

    def test_information_flow_edge_table_supports_explicit_sources_and_external_sources(self) -> None:
        columns = {
            row["name"]
            for row in self.connection.execute("PRAGMA table_info(csf_information_flow_edges)").fetchall()
        }
        self.assertEqual(
            {
                "edge_id", "information_id", "source_kind", "source_subcategory_id",
                "external_source_label", "source_guidance", "consumer_subcategory_id",
                "dependency_kind", "use_reason", "provenance", "updated_at",
            },
            columns,
        )
        self.assertEqual(
            len(INFORMATION_FLOW_EDGES),
            self.connection.execute("SELECT COUNT(*) FROM csf_information_flow_edges").fetchone()[0],
        )

        self.connection.execute(
            """INSERT INTO csf_information_flow_edges(
                edge_id, information_id, source_kind, source_subcategory_id,
                external_source_label, source_guidance, consumer_subcategory_id,
                dependency_kind, use_reason, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                "test-edge-subcategory", "organizational_mission", "subcategory", "GV.OC-01",
                None, "A mission statement may provide this information.", "GV.RM-01",
                "planning_input", "Use mission objectives to establish risk objectives.", "2026-10-03T00:00:00Z",
            ),
        )
        self.connection.execute(
            """INSERT INTO csf_information_flow_edges(
                edge_id, information_id, source_kind, source_subcategory_id,
                external_source_label, source_guidance, consumer_subcategory_id,
                dependency_kind, use_reason, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                "test-edge-external", "external_legal_contractual_sources", "external", None,
                "External legal, regulatory, and contractual sources",
                "An applicable external requirement may provide this information.", "GV.OC-03",
                "required_input", "Identify applicable external requirements.", "2026-10-03T00:00:00Z",
            ),
        )
        self.connection.commit()

        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                """INSERT INTO csf_information_flow_edges(
                    edge_id, information_id, source_kind, source_subcategory_id,
                    source_guidance, consumer_subcategory_id, dependency_kind, use_reason, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    "test-edge-invalid", "organizational_mission", "external", "GV.OC-01",
                    "Invalid mixed source.", "GV.RM-01", "planning_input",
                    "This must fail the source-type check.", "2026-10-03T00:00:00Z",
                ),
            )

    def test_tier_guidance_separates_official_text_from_product_examples(self) -> None:
        guidance = store.list_csf_tier_guidance(self.connection)

        self.assertEqual([1, 2, 3, 4], [record["tier_level"] for record in guidance])
        tier_one = guidance[0]
        self.assertEqual("Partial", tier_one["tier_name"])
        self.assertIn("ad hoc", tier_one["official_governance_text"])
        self.assertIn("product-authored", tier_one["product_guidance_notice"])
        self.assertEqual(5, len(tier_one["transition_hints"]))
        self.assertIn("Risk decision owner", tier_one["transition_hints"][0]["example"])
        self.assertEqual("NIST Cybersecurity Framework (CSF) 2.0", tier_one["source_name"])
        self.assertIn("Appendix B, Table 2", tier_one["source_locator"])

    def test_profile_tiers_are_scoped_and_append_only(self) -> None:
        target = store.set_csf_profile_target_tier(
            self.connection,
            self.profile_id,
            3,
            "The organization intends to use an approved, repeatable risk process.",
            "test-analyst",
        )
        current = store.set_csf_profile_current_tier(
            self.connection,
            self.profile_id,
            2,
            "Risk decisions are informed, but reviews are not yet consistently repeatable.",
            "test-analyst",
        )
        events = store.list_csf_profile_tier_audit_events(self.connection, self.profile_id)

        self.assertEqual(3, target["target_tier_level"])
        self.assertEqual(2, current["current_tier_level"])
        self.assertEqual(
            ["current_tier_recorded", "target_tier_recorded"],
            [event["event_type"] for event in events],
        )
        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                "UPDATE csf_profile_tier_audit_events SET rationale = 'changed' WHERE tier_audit_event_id = ?",
                (events[0]["tier_audit_event_id"],),
            )

    def test_profile_tier_requires_an_organizational_profile_and_rationale(self) -> None:
        frozen = next(
            profile for profile in store.list_csf_profile_definitions(self.connection)
            if profile["profile_kind"] == "frozen_base"
        )
        with self.assertRaisesRegex(ValueError, "Tier rationale"):
            store.set_csf_profile_target_tier(self.connection, self.profile_id, 2, "", "test-analyst")
        with self.assertRaisesRegex(ValueError, "Organizational Profile"):
            store.set_csf_profile_target_tier(
                self.connection, frozen["profile_id"], 2, "Frozen profiles are source artifacts.", "test-analyst"
            )

    def test_profile_target_requires_reason_and_records_audit_history(self) -> None:
        with self.assertRaisesRegex(ValueError, "Target rationale"):
            store.set_csf_profile_outcome_target(
                self.connection,
                "Test profile",
                "GV.OC-01",
                "partly_implemented",
                "",
                recorded_by="test-analyst",
            )

        store.set_csf_profile_outcome_target(
            self.connection,
            "Test profile",
            "GV.OC-01",
            "partly_implemented",
            "The mission statement is documented but has not yet been shared.",
            recorded_by="test-analyst",
        )
        target = store.list_csf_profile_outcome_targets(self.connection, self.profile_id)["GV.OC-01"]
        events = store.list_csf_profile_audit_events(self.connection, "Test profile")

        self.assertEqual("partly_implemented", target["target_assessment_level"])
        self.assertEqual("The mission statement is documented but has not yet been shared.", target["target_reason"])
        self.assertTrue(any(event["event_type"] == "outcome_target_changed" for event in events))

    def test_current_assessment_is_profile_scoped_and_audited(self) -> None:
        store.set_current_csf_assessment(
            self.connection, self.profile_id, "GV.OC-01", "partly_implemented", "test-analyst"
        )
        current = store.list_current_csf_assessments(self.connection, self.profile_id)
        audit = store.list_csf_outcome_audit_events(self.connection, "GV.OC-01")

        self.assertEqual("partly_implemented", current["GV.OC-01"]["assessment_level"])
        self.assertTrue(any(event["event_type"] == "assessment_recorded" for event in audit))

    def test_evidence_can_support_an_outcome_and_an_action_with_auditable_links(self) -> None:
        evidence = store.create_csf_supporting_basis(
            self.connection,
            profile_id=self.profile_id,
            subcategory_id="GV.OC-01",
            basis_type="document",
            title="Approved mission statement",
            recorded_on="2026-10-02",
            created_by="test-analyst",
            assertion_text="The approved mission statement is available to staff.",
        )
        action = store.create_csf_reviewed_action(
            self.connection,
            profile_id=self.profile_id,
            subcategory_id="GV.OC-01",
            title="Share the mission statement",
            details="Send the approved statement to the people who use the PC.",
            rationale="They need the mission context for risk decisions.",
            action_status="planned",
            basis_ids=[evidence["basis_id"]],
            created_by="test-analyst",
        )

        displayed = store.list_csf_reviewed_actions(self.connection, self.profile_id, "GV.OC-01")
        detail = store.get_csf_evidence_detail(self.connection, self.profile_id, evidence["basis_id"])
        link_events = store.list_csf_evidence_link_audit_events(
            self.connection, self.profile_id, target_type="action", target_id=action["action_id"]
        )

        self.assertEqual([evidence["basis_id"]], displayed[0]["basis_ids"])
        self.assertEqual("Approved mission statement", detail["evidence"]["title"])
        self.assertTrue(any(event["event_type"] == "linked" for event in link_events))

    def test_action_updates_are_append_only_and_delete_cascades_to_updates(self) -> None:
        action = store.create_csf_reviewed_action(
            self.connection,
            profile_id=self.profile_id,
            subcategory_id="GV.OC-02",
            title="Document stakeholder needs",
            action_status="planned",
            created_by="test-analyst",
        )
        updated = store.update_csf_reviewed_action(
            self.connection,
            action_id=action["action_id"],
            title=action["title"],
            details="Record internal and external stakeholder needs.",
            rationale="The outcome requires those needs to be understood.",
            action_status="completed",
            progress_note="Completed the initial stakeholder review.",
            updated_by="test-analyst",
        )
        history = store.list_csf_reviewed_action_updates(self.connection, action["action_id"])

        self.assertEqual("completed", updated["action_status"])
        self.assertEqual(["completed", "planned"], [entry["action_status"] for entry in history])
        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                "UPDATE csf_reviewed_action_updates SET progress_note = 'changed' WHERE action_update_id = ?",
                (history[0]["action_update_id"],),
            )

        store.delete_csf_reviewed_action(self.connection, action["action_id"])
        self.assertEqual([], store.list_csf_reviewed_action_updates(self.connection, action["action_id"]))

    def test_action_and_evidence_records_do_not_cross_profile_boundaries(self) -> None:
        other_profile = store.create_csf_profile_definition(
            self.connection,
            "Other test profile",
            "A separate test context.",
            recorded_by="test-analyst",
        )
        evidence = store.create_csf_supporting_basis(
            self.connection,
            profile_id=self.profile_id,
            subcategory_id="GV.OC-01",
            basis_type="document",
            title="Profile one evidence",
            created_by="test-analyst",
        )

        with self.assertRaisesRegex(ValueError, "same Profile"):
            store.create_csf_reviewed_action(
                self.connection,
                profile_id=other_profile["profile_id"],
                subcategory_id="GV.OC-01",
                title="Other profile action",
                action_status="planned",
                basis_ids=[evidence["basis_id"]],
                created_by="test-analyst",
            )

    def test_named_plans_are_profile_scoped_and_actions_can_remain_unplanned(self) -> None:
        plan = store.create_csf_plan(
            self.connection,
            profile_id=self.profile_id,
            plan_name="Protect the PC's business use",
            purpose="Coordinate the highest-priority improvements.",
            plan_status="active",
            plan_priority="high",
            created_by="test-analyst",
        )
        action = store.create_csf_reviewed_action(
            self.connection,
            profile_id=self.profile_id,
            subcategory_id="GV.OC-01",
            title="Document the mission",
            action_status="planned",
            created_by="test-analyst",
        )

        assigned = store.set_csf_action_plan_and_priority(
            self.connection,
            action_id=action["action_id"],
            plan_id=plan["plan_id"],
            action_priority="critical",
            priority_rationale="The mission statement guides later risk decisions.",
            rationale="The action is ready for the active plan.",
            recorded_by="test-analyst",
        )
        plans = store.list_csf_plans(self.connection, self.profile_id)
        events = self.connection.execute(
            "SELECT event_type FROM csf_plan_audit_events WHERE action_id = ? ORDER BY recorded_at",
            (action["action_id"],),
        ).fetchall()

        self.assertEqual(plan["plan_id"], assigned["plan_id"])
        self.assertEqual("critical", assigned["action_priority"])
        self.assertEqual(1, plans[0]["action_count"])
        self.assertEqual(["action_assigned", "action_priority_changed"], [row["event_type"] for row in events])

        unplanned = store.set_csf_action_plan_and_priority(
            self.connection,
            action_id=action["action_id"],
            plan_id="",
            recorded_by="test-analyst",
        )
        self.assertIsNone(unplanned["plan_id"])
        self.assertEqual(1, self.connection.execute(
            "SELECT COUNT(*) FROM csf_plan_audit_events WHERE action_id = ? AND event_type = 'action_unplanned'",
            (action["action_id"],),
        ).fetchone()[0])
        self.assertEqual(1, len(store.list_csf_plans(self.connection, self.profile_id)))

        other_profile = store.create_csf_profile_definition(
            self.connection, "Plan isolation profile", "A separate plan context.", recorded_by="test-analyst"
        )
        other_plan = store.create_csf_plan(
            self.connection,
            profile_id=other_profile["profile_id"],
            plan_name="Other profile plan",
            created_by="test-analyst",
        )
        with self.assertRaisesRegex(ValueError, "action's Profile"):
            store.set_csf_action_plan_and_priority(
                self.connection,
                action_id=action["action_id"],
                plan_id=other_plan["plan_id"],
                recorded_by="test-analyst",
            )

    def test_frozen_profiles_cannot_own_plans_and_plan_audit_is_append_only(self) -> None:
        base = next(
            profile for profile in store.list_csf_profile_definitions(self.connection)
            if profile["profile_name"] == "NIST CSF 2.0 Base Profile"
        )
        with self.assertRaisesRegex(ValueError, "Organizational Profile"):
            store.create_csf_plan(
                self.connection,
                profile_id=base["profile_id"],
                plan_name="Not allowed",
            )

        plan = store.create_csf_plan(
            self.connection,
            profile_id=self.profile_id,
            plan_name="Audit test plan",
            created_by="test-analyst",
        )
        event_id = self.connection.execute(
            "SELECT plan_audit_event_id FROM csf_plan_audit_events WHERE plan_id = ?",
            (plan["plan_id"],),
        ).fetchone()[0]
        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                "UPDATE csf_plan_audit_events SET rationale = 'changed' WHERE plan_audit_event_id = ?",
                (event_id,),
            )

    def test_action_can_be_created_directly_in_a_plan_with_priority(self) -> None:
        plan = store.create_csf_plan(
            self.connection,
            profile_id=self.profile_id,
            plan_name="Direct assignment plan",
            created_by="test-analyst",
        )
        action = store.create_csf_reviewed_action(
            self.connection,
            profile_id=self.profile_id,
            subcategory_id="GV.OC-02",
            title="Understand stakeholder needs",
            action_status="planned",
            plan_id=plan["plan_id"],
            action_priority="high",
            priority_rationale="Needed before risk decisions can reflect stakeholder needs.",
            created_by="test-analyst",
        )
        events = self.connection.execute(
            "SELECT event_type FROM csf_plan_audit_events WHERE action_id = ? ORDER BY recorded_at",
            (action["action_id"],),
        ).fetchall()

        self.assertEqual(plan["plan_id"], action["plan_id"])
        self.assertEqual("high", action["action_priority"])
        self.assertEqual(["action_assigned", "action_priority_changed"], [row["event_type"] for row in events])

    def test_plan_fields_can_be_updated_with_auditable_history(self) -> None:
        plan = store.create_csf_plan(
            self.connection,
            profile_id=self.profile_id,
            plan_name="Initial plan",
            created_by="test-analyst",
        )
        updated = store.update_csf_plan(
            self.connection,
            plan_id=plan["plan_id"],
            plan_name="Customer-data plan",
            purpose="Coordinate actions that protect customer records.",
            plan_status="active",
            plan_priority="high",
            owner_name="Office manager",
            target_on="2026-12-31",
            rationale="The work is funded and ready to begin.",
            recorded_by="test-analyst",
        )
        events = store.list_csf_plan_audit_events(self.connection, self.profile_id)

        self.assertEqual("Customer-data plan", updated["plan_name"])
        self.assertEqual("active", updated["plan_status"])
        self.assertEqual("high", updated["plan_priority"])
        fields = {event["field_name"] for event in events if event["event_type"] == "plan_updated"}
        self.assertTrue({"plan_name", "purpose", "plan_status", "plan_priority", "owner_name", "target_on"}.issubset(fields))


if __name__ == "__main__":
    unittest.main()

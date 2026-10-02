import sqlite3
import tempfile
import unittest
from pathlib import Path

import csf_analyst_store as store


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


if __name__ == "__main__":
    unittest.main()

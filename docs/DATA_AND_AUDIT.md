# Data Model and Audit Behavior

## Database boundary

CSF Analyst uses one local SQLite file, normally `state\csf-analyst.db`.
Use this file only for CSF Analyst records.

## Primary records

| Record family | Main tables | Scope |
|---|---|---|
| Profile definitions and tailoring | `csf_profile_definitions`, `csf_profiles`, `csf_profile_outcome_targets` | Profile UUID |
| Current assessment | `csf_profile_current_assessments` | Profile UUID + Subcategory |
| Plans and action priority | `csf_plans`, `csf_plan_audit_events`, action plan/priority fields | Organizational Profile UUID; action assignment is optional |
| Actions and updates | `csf_reviewed_actions`, `csf_reviewed_action_updates` | Profile UUID + Subcategory |
| Evidence and links | `csf_supporting_basis`, `csf_evidence_outcome_links`, action/evidence link tables | Profile UUID; reusable within that Profile |
| Audit records | `csf_profile_audit_events`, `csf_outcome_audit_events`, `csf_evidence_link_audit_events` | Profile UUID and, where applicable, Subcategory/action/evidence |
| Control catalogs and mappings | `csf_reference_*`, `csf_*control*` tables | Shared source catalog; enabled per Profile |
| Tier guidance catalog | `csf_tier_guidance` | Shared, source-traceable catalog; not a Profile Tier assessment |
| Profile Tier characterization | `csf_profile_tier_assessments`, `csf_profile_tier_audit_events` | Organizational Profile UUID; analyst-recorded current/target Tier and rationale |

## Profile identity and isolation

An Organizational Profile has a UUID. All analyst-entered Tile 3 records are
keyed to that UUID so the same CSF outcome can have different targets, current
assessments, actions, and evidence in different Profiles.

Creating an Organizational Profile from a base, Community Profile, or another
Organizational Profile creates an independent profile artifact. Source lineage
is retained, but later changes do not silently propagate into the new Profile.

## Audit rules

- Profile creation, tailoring/status changes, target changes, current
  assessment changes, action changes, evidence creation, and evidence links
  are recorded as append-only events.
- A named Plan is a deliberate, profile-scoped governance record. Actions may
  be assigned to one Plan or left unplanned (`plan_id = NULL`); **Unplanned**
  is a reporting bucket, not a stored Plan. Plan creation, action assignment,
  reassignment, removal from a Plan, and action-priority changes have their
  own append-only plan audit events.
- Audit events record local timestamp, recorded-by identity, change summary,
  and the supplied reason or supporting reference when present.
- A Profile Tier is an analyst's documented characterization of governance and
  risk-management rigor. Target and current Tier values have separate
  rationales and append-only history; neither is calculated from controls or
  outcome assessments.
- Evidence has a recorded-on date and optional review-on date. A date supports
  later relevance review; it does not prove evidence remains current.
- Deleting an action removes its dependent update records. The action deletion
  is retained in the relevant audit history.

## Safe maintenance

Back up the complete SQLite file before a manual migration or source-catalog
refresh. Use application/store commands to change records; never edit tables
with ad hoc SQL unless performing a reviewed repair. A database backup is not
a substitute for the append-only audit history.

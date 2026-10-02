# CSF Information-Flow and Capability Maps

## Status and provenance

This document describes product-authored relationships among NIST CSF 2.0
Subcategory outcomes. It is not an official NIST dependency map, an
implementation sequence, or evidence of compliance.

The two maps are stored as readable Python source, then synchronized into
SQLite during database initialization:

| Source file | Purpose |
|---|---|
| `csf_information_flows.py` | Information items, sources, and downstream uses. |
| `csf_capability_dependencies.py` | Prerequisite/supporting capability relationships. |
| `csf_catalog.py` | Product-authored short outcome labels used consistently in the UI. |

The official CSF catalog remains unchanged in
`profiles/nist-csf-2.0-catalog.json`.

## Why there are two maps

| Map | Question | Edge meaning |
|---|---|---|
| Information flow | What information does this outcome make available, or need? | A named record, finding, decision, requirement, alert, or similar item passes to a later use. |
| Capability | What must substantially exist before another outcome can credibly be claimed? | A prerequisite, partial prerequisite, or supporting capability affects another outcome. No record is assumed to move. |

For example, stakeholder cybersecurity and privacy needs identified in
`GV.OC-02` can inform supplier requirements in `GV.SC-05`. That is an
information flow. Authentication in `PR.AA-03` is a capability prerequisite for
access permissions in `PR.AA-05`; it is not information handed between them.

## Edge rules

### Information flow

Add an edge only when all of the following are true:

1. A source can create, maintain, receive, or make available a specific named
   information item.
2. A receiving outcome uses that item for a decision, plan, or event activity.
3. The description does not claim that the source outcome completes the
   receiving outcome.
4. The relationship is a record/decision handoff, not merely a shared topic.

External sources are allowed when information begins outside a CSF outcome. Use
an `External:` source label rather than inventing an upstream CSF node.

### Capability

Choose the least forceful supported strength:

- `hard_gate` — a fully implemented claim for the dependent outcome is not
  credible without the prerequisite capability.
- `partial_gate` — the prerequisite materially limits the dependent outcome in
  relevant contexts, but both can mature together.
- `supporting_capability` — useful planning or assessment context, not a
  completion blocker.

Do not use a capability edge for an information handoff. Do not treat a shared
keyword, similar purpose, or convenient implementation order as a relationship.

## SQLite runtime tables

| Table | Purpose |
|---|---|
| `csf_information_items` | Canonical product-authored information item definitions. |
| `csf_subcategory_information_sources` | CSF or external source that can provide an item. |
| `csf_subcategory_information_uses` | CSF outcome that uses an item and why. |
| `csf_subcategory_capability_dependencies` | Prerequisite/dependent capability relationship and strength. |

Update source catalogs rather than directly editing these tables. `init_db()`
upserts source records into SQLite so source code remains the maintainable form.

## UI behavior

Tile 3 can show a short “Why this matters” explanation and an **Information
flow** button. The popup presents one-hop upstream and downstream relationships
for the selected Subcategory using short descriptions alongside CSF IDs.

Capability dependencies are stored but intentionally do not block assessment
buttons or hide actions. A future planning experience may use hard or partial
gates to explain a limitation, but it must still allow the analyst to plan
work, record evidence, and select an appropriate lower assessment.

## Maintenance checklist

Before adding or changing an edge, answer:

1. What exact item or capability is involved?
2. Which official outcome language supports this interpretation?
3. Is this an information handoff, a capability condition, or neither?
4. Does the text avoid claiming that NIST mandates the relationship?
5. Does the edge remain useful outside the original single-PC example?

After a source change, run the focused tests and verify that every official CSF
Subcategory remains represented in at least one map without adding artificial
edges simply to reach coverage.

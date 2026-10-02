# Product Scope and Boundaries

## Purpose

CSF Analyst helps an analyst reason about and document progress toward NIST
CSF 2.0 outcomes in a defined context. The first supported teaching context is
a single-user PC, but an Organizational Profile may describe another boundary.

The product's central distinction is deliberate:

```text
Official CSF outcome          = what the organization seeks to achieve
Profile tailoring             = why that outcome is in scope and its target
Action                        = work chosen to advance the outcome
Evidence and supporting basis = material used to support an assessment claim
Current assessment            = the analyst's recorded judgment today
```

None of those records alone establishes compliance.

## Authority boundaries

| Content | Authority | Product handling |
|---|---|---|
| CSF outcome and implementation examples | NIST | Retained as official source content. |
| Community Profile outcome selection and notes | Publishing organization | Stored as frozen, read-only source artifacts. |
| Informative control mapping | Source publisher/NIST | Identifies a relationship only; it is not an implementation instruction. |
| Plain-English guidance, action placeholders, flows, and capability maps | Product-authored | Clearly separate from official source content. |
| Target/current assessments, actions, evidence, and reasons | Analyst | Profile-scoped records with audit history. |

## Operating boundary

CSF Analyst works with Profiles, outcomes, assessments, actions, evidence, and
their audit history. It does not collect device telemetry or make automatic
implementation determinations.

## Current implementation limits

- The UI supports profile-scoped actions and evidence, but not a separate
  portfolio-level plan object for grouping and prioritizing actions.
- Evidence reference locations are descriptive fields; the app does not yet
  ingest or store the source document itself.
- Capability dependencies are stored and documented but do not yet block an
  assessment or drive a planning queue.
- NIST SP 800-53 is the first integrated control catalog. The schema is
  framework-neutral, but additional catalog importers require their own
  source, provenance, and review process.

## Design rules

1. Keep frozen source Profiles immutable.
2. Keep every Organizational Profile independently auditable after creation.
3. Do not modify official NIST content to express product interpretation.
4. Do not use color alone to convey a Function or state.
5. Do not turn an informative mapping into a compliance claim.
6. Do not make a missing record appear to be a satisfied outcome.

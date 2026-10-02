# Control-Mapping Relationship Classification

## Purpose

An official informative-reference mapping says a control and CSF outcome are
related. It does not establish implementation order, effectiveness, or whether
the control produces the outcome. This product-authored method records a
bounded interpretation of the existing mapping.

The method is framework-neutral. NIST SP 800-53 Rev. 5.2.0 is the first
integrated catalog, but it does not give NIST authority over the product's
relationship classifications.

## Required fields

Every classified mapping has one role and one scope.

| Field | Values | Meaning |
|---|---|---|
| `relationship_role` | `produces_outcome_information` | The control expressly creates information materially needed for the outcome. |
|  | `consumes_outcome_information` | The control expressly uses information materially relevant to the outcome. |
|  | `enables_outcome_capability` | The control expressly performs a material part of the outcome without an information handoff. |
|  | `context_only` | The mapping is broad, adjacent, or lacks support for a material relationship. |
| `relationship_scope` | `direct` | The control statement covers the relevant work without a material gap. |
|  | `partial` | It covers a material subset but omits another material part. |
|  | `indirect` | A clearly bounded product interpretation explains relevance; it cannot supply a missing material verb or object. |

`information_id` is required only for producer/consumer roles and must match a
supplied product information item exactly. It is empty for capability and
context-only roles.

## Classification rules

1. Classify from the official control statement and official CSF outcome, not
   from shared words such as risk, privacy, policy, supplier, or compliance.
2. Restate a specific verb and object from the control statement in the
   rationale. Do not import facts from another control.
3. A general policy, plan, program, assessment, or monitoring activity is not
   automatically an enabler of an organization-wide CSF outcome.
4. Use `partial` only for an express material subset. Use `context_only` for a
   broad topic or supporting condition.
5. Keep the rationale to one factual, high-school-level sentence.
6. Do not describe an action, make a compliance claim, or imply that NIST
   requires the product-authored classification.

## Review and provenance

AI may propose a classification for an already official-mapped pair. It does
not create a mapping and it is never sufficient review on its own. Preserve:

- control framework/version and official source;
- prompt/version and batch identifier, if AI assisted;
- draft/review status and reviewer decision;
- rationale and review timestamp.

Never overwrite a reviewed relationship with a later batch result. The source
catalog `csf_control_mapping_relationships.py` is the maintainable product
source for reviewed classifications; SQLite holds the runtime copy.

## Relationship to action guidance

Relationship classification and action placeholder text are separate. A
`context_only` mapping may still offer a helpful context-aware action example,
but it must not say the action is required by the control or by NIST. A direct
or partial relationship still requires an analyst to assess the selected
Profile context, evidence, and current implementation.

## Maintenance

Change this method only in response to a documented classification error or a
new supported relationship type. Update the associated batch generator,
source-catalog tests, and this document together; validate a small sample
before applying a change to a whole control framework.

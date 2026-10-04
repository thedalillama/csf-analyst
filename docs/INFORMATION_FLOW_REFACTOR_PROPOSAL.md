# Proposed information-flow refactor

## Status

**Migration complete.** The explicit v2 catalog is loaded into
`csf_information_flow_edges`, Tile 3 reads those direct paths, and the legacy
independent source/use tables have been retired.

The information-flow map is product-authored. It is an analyst aid derived
from interpretations of NIST CSF 2.0 outcomes; it is not a NIST dependency
map, a mandatory implementation order, or evidence of compliance.

## Problem with the current representation

The existing model separates sources from uses:

```text
information item <- many sources
information item -> many uses
```

The Tile 3 query joins those independent lists on `information_id`. For an
item with several sources and several uses, that makes every source appear to
provide the item to every consumer. That is a Cartesian interpretation, not a
recorded source-to-consumer fact.

Example: `asset_inventory` currently has four producers (hardware, software
and services, supplier services, and data) and eight consumers. The UI can
therefore imply 32 paths, even though most consumers need only one kind of
inventory.

Changing names alone cannot correct that behavior. The stored relationship
must represent one directed path at a time.

## Proposed model

Retain atomic information-item definitions, but replace the two independent
relationship tables with explicit paths.

```text
source outcome or external source
       |
       | produces / makes available
       v
atomic information item
       |
       | used by, with relationship strength and reason
       v
consumer outcome
```

Suggested SQLite table: `csf_information_flow_edges`.

| Column | Purpose |
| --- | --- |
| `edge_id` | Stable product-authored identifier. |
| `information_id` | FK to one atomic information item. |
| `source_kind` | `subcategory` or `external`. |
| `source_subcategory_id` | Producing CSF outcome when `source_kind` is `subcategory`; otherwise null. |
| `external_source_label` | Accurate source label when information originates outside the Core. |
| `source_guidance` | Examples of equivalent records or custom actions that can provide the item. |
| `consumer_subcategory_id` | CSF outcome that uses the item. |
| `dependency_kind` | `required_input`, `planning_input`, `event_input`, or `conditional_input`. |
| `use_reason` | Concise, user-facing explanation of the use. |
| `provenance` | Initially `product-authored-v2`; permits a future official-source citation without conflating the two. |
| `updated_at` | Catalog-maintenance timestamp. |

The unique key should be the complete semantic path: information item, source,
consumer, and dependency kind. This permits two distinct reasons only when
they are intentionally distinct relationships, rather than accidental joins.

## Atomic-item catalog decisions

### Keep as currently atomic

These remain one usable record or knowledge set:

- Organizational mission and objectives (`GV.OC-01`)
- Stakeholder cybersecurity and privacy needs (`GV.OC-02`)
- Legal, regulatory, and contractual requirements (`GV.OC-03`)
- Critical services and objectives (`GV.OC-04`)
- External dependencies (`GV.OC-05`)
- Risk assessment method (`GV.RM-06`)
- Supplier criticality (`GV.SC-04`)
- Network and data flows (`ID.AM-03`)
- Asset criticality and impact (`ID.AM-05`)
- Selected risk responses (`ID.RA-06`)
- Change and exception risk records (`ID.RA-07`)
- Secure-development performance results (`PR.PS-06`)
- Authorized adverse-event alerts (`DE.AE-06`)
- Monitoring findings and potentially adverse events
- Improvement lessons and opportunities
- Supplier requirements and agreements (`GV.SC-05`)
- Supply-chain program direction (`GV.SC-01`)
- Supplier lifecycle results (`GV.SC-07`)
- Threat intelligence (`ID.RA-02`)
- Restoration assets (`PR.DS-11`)
- Verified restoration assets (`RC.RP-03`)
- Log records (`PR.PS-04`)
- Event threat context (`DE.AE-07`)
- Triaged incident reports (`RS.MA-02`)
- Recovery initiation decision (`RS.MA-05`)
- Preserved investigation records (`RS.AN-06`)
- External vulnerability disclosures
- External legal, regulatory, and contractual sources
- Risk-management performance results
- Risk-management review findings
- Integrated supply-chain risk records

### Decompose before migration

| Current pooled item | Proposed atomic items | Reason |
| --- | --- | --- |
| Risk objectives, tolerance, and response direction | risk objectives; risk appetite and tolerance; risk-response direction | Each has a different source and different downstream decision. |
| Cybersecurity roles and authorities | organization cybersecurity roles; supplier and third-party roles | `GV.RR-02` and `GV.SC-02` are not interchangeable role records. |
| Asset inventory | hardware inventory; software/system/service inventory; supplier-service inventory; data inventory | The current four producers create distinct inventories, and consumers use different ones. |
| Validated vulnerabilities and relevant threats | validated vulnerability records; relevant threat records | Vulnerability discovery and threat identification are distinct findings. Keep external disclosures as a separate external-source item. |
| Risk scenarios and priorities | likelihood and impact analysis; prioritized risk records | `ID.RA-04` analyzes likelihood/impact while `ID.RA-05` establishes priority. |
| Incident analysis and response status | declared incident; incident investigation/root-cause record; incident scope and impact; response status | Declaration, analysis, scope, and response execution are distinct event records. |
| Recovery priorities and restoration status | recovery priorities/actions; restoration verification and normal-operation status | `RC.RP-02` chooses/actions recovery; `RC.RP-05` verifies the result. |
| Analyzed event information | event activity analysis; event impact and scope; incident declaration | The current three producers create different facts used at different response stages. |
| Incident priority and scope | incident priority; incident scope and impact | Priority drives escalation; scope and impact support recovery initiation. |

## Directed-edge roster: first review pass

This roster preserves useful current relationships, corrects known directional
errors, and identifies the item each path uses. `P` means planning input,
`R` required input subject to equivalent records, `E` event input, and `C`
conditional input. All paths below are product-authored interpretations.

### Governance and risk management

| Producer | Atomic item | Consumer | Kind |
| --- | --- | --- | --- |
| GV.OC-01 | organizational mission and objectives | GV.RM-01, ID.AM-05, ID.RA-04, RC.RP-04 | P |
| GV.OC-02 | stakeholder cybersecurity and privacy needs | GV.RM-01, GV.RM-05, GV.SC-01, GV.SC-05, RS.CO-02, RS.CO-03, RC.CO-03 | P; `GV.SC-05` R |
| External legal, regulatory, contractual sources | legal/regulatory/contractual requirements | GV.OC-03 | R |
| GV.OC-03 | legal/regulatory/contractual requirements | GV.PO-01, GV.PO-02, GV.SC-05, RS.CO-02, RC.CO-04 | P; `GV.SC-05` R |
| GV.OC-04 | critical services and objectives | ID.AM-05, ID.RA-04, PR.IR-03, RC.RP-02, RC.RP-04, RC.CO-03 | P; `RC.RP-02` and `RC.RP-04` R |
| GV.OC-05 | external dependencies | ID.AM-04, GV.SC-04, ID.RA-10, DE.CM-06, RC.RP-02, GV.SC-10 | P |
| GV.RM-01 | risk objectives | GV.PO-01, ID.RA-06, GV.RR-03, GV.RM-03, GV.RM-07 | P |
| GV.RM-02 | risk appetite and tolerance | GV.PO-01, ID.RA-06, GV.RM-03, GV.RM-07 | P |
| GV.RM-04 | risk-response direction | GV.PO-01, ID.RA-06, GV.RM-03 | P |
| GV.RM-06 | risk assessment method | ID.RA-04, ID.RA-05, ID.RA-06, ID.RA-07 | P |
| External measurement criteria | risk-management measures and thresholds | GV.OV-03 | P |
| External operational/evidence records | risk-management performance results | GV.OV-03 | R |
| GV.OV-03 | risk-management review findings | GV.OV-01, GV.OV-02, GV.PO-02 | P |

`GV.RM-01` no longer incorrectly produces measures, KPIs, KRIs, or thresholds.
Those must come from an external measurement or governance record unless a
future Core outcome is specifically designated as their source.

### Roles, suppliers, and assets

| Producer | Atomic item | Consumer | Kind |
| --- | --- | --- | --- |
| GV.RR-02 | organization cybersecurity roles | RS.MA-01, RC.RP-01 | R |
| GV.SC-02 | supplier and third-party roles | GV.SC-08 | R |
| GV.SC-04 | supplier criticality | GV.SC-05, GV.SC-06, ID.RA-10, GV.SC-07, GV.SC-09 | P; `ID.RA-10` R |
| GV.SC-05 | supplier requirements and agreements | GV.SC-08, GV.SC-10 | P |
| GV.SC-01 | supply-chain program direction | GV.SC-03, GV.SC-09 | R for `GV.SC-03`; P for `GV.SC-09` |
| GV.SC-07 | supplier lifecycle results | GV.SC-03, GV.SC-09 | R for `GV.SC-03`; P for `GV.SC-09` |
| GV.SC-03 | integrated supply-chain risk records | GV.RM-03 | P |
| ID.AM-01 | hardware inventory | ID.RA-01, ID.RA-09, PR.PS-03, DE.CM-09, ID.AM-08 | R |
| ID.AM-02 | software/system/service inventory | ID.RA-01, ID.RA-09, PR.PS-01, PR.PS-02, DE.CM-09, ID.AM-08 | R |
| ID.AM-04 | supplier-service inventory | GV.SC-10, ID.AM-08 | P; `ID.AM-08` R |
| ID.AM-07 | data inventory | DE.CM-09, ID.AM-08 | R |
| ID.AM-03 | network and data flows | PR.DS-02, PR.IR-01, DE.CM-01 | P |
| ID.AM-05 | asset criticality and impact | ID.RA-04, RC.RP-02, ID.AM-08 | P |

### Risk, protection, and monitoring

| Producer | Atomic item | Consumer | Kind |
| --- | --- | --- | --- |
| ID.RA-02 | threat intelligence | ID.RA-03, ID.RA-04, DE.AE-07 | P; `DE.AE-07` E |
| ID.RA-03 | relevant threat records | ID.RA-04, ID.RA-05 | R |
| ID.RA-01 | validated vulnerability records | ID.RA-04, ID.RA-05 | R |
| External disclosure sources | external vulnerability disclosures | ID.RA-08 | E |
| ID.RA-08 | validated vulnerability records | ID.RA-01 | P |
| ID.RA-04 | likelihood and impact analysis | ID.RA-05, ID.RA-06, GV.RM-03, GV.RM-07 | P; `ID.RA-05` R |
| ID.RA-05 | prioritized risk records | ID.RA-06, GV.RM-03, GV.RM-07 | R for `ID.RA-06`; P otherwise |
| ID.RA-06 | selected risk responses | PR.AA-05, PR.DS-01, PR.DS-02, PR.DS-10, PR.IR-03, GV.RM-03 | P |
| ID.RA-07 | change and exception risk records | ID.RA-06 | P |
| PR.PS-04 | log records | DE.CM-09 | P |
| DE.CM-01, DE.CM-02, DE.CM-03, DE.CM-06, DE.CM-09 | monitoring findings and potentially adverse events | DE.AE-02, DE.AE-03, DE.AE-04, DE.AE-08 | E |
| DE.AE-06 | authorized adverse-event alerts | DE.AE-08, RS.MA-02 | E |
| DE.AE-07 | event threat context | DE.AE-02, DE.AE-04 | E |

`DE.CM-02` is added as a physical-environment source of monitoring findings.
`PR.PS-04 -> DE.CM-09` and `ID.AM-03 -> DE.CM-01` are planning inputs, not
hard prerequisites.

### Incident response, recovery, and improvement

| Producer | Atomic item | Consumer | Kind |
| --- | --- | --- | --- |
| DE.AE-02 | event activity analysis | RS.MA-02 | E |
| DE.AE-04 | event impact and scope | RS.MA-02 | E |
| DE.AE-08 | declared incident | RS.MA-01, RS.MA-02, RC.RP-01 | E |
| RS.AN-03 | incident investigation/root-cause record | RS.MA-03, RS.MI-01, RS.MI-02, RS.AN-06, RS.AN-07, RS.AN-08 | E |
| RS.AN-06 | preserved investigation records | RS.AN-07, RS.AN-08 | E |
| RS.AN-08 | incident scope and impact | RS.MA-03, RS.MA-04, RS.MA-05 | E |
| RS.MA-02 | triaged incident reports | RS.MA-03 | E |
| RS.MA-03 | incident priority | RS.MA-04 | E |
| RS.MA-03 | incident scope and impact | RS.MA-05 | E |
| RS.MA-05 | recovery initiation decision | RC.RP-01 | E |
| RC.RP-02 | recovery priorities and actions | RC.RP-05, RC.RP-06, RC.CO-03 | E |
| PR.DS-11 | restoration assets | RC.RP-03 | E |
| RC.RP-03 | verified restoration assets | RC.RP-05 | E |
| RC.RP-05 | restoration verification and normal-operation status | RC.RP-06, RC.CO-03 | E |
| ID.IM-01, ID.IM-02, ID.IM-03 | improvement lessons and opportunities | GV.OV-01, GV.OV-02, GV.PO-02, ID.IM-04 | P |

The incident-response plan is not sourced from `RS.MA-01`, because that
outcome executes the plan. It becomes an external item such as **incident
response plan and coordination arrangements**, consumed by `RS.MA-01`,
`RC.RP-01`, and `GV.SC-08` where applicable.

## Decision contexts after atomic edges are accepted

Do not build these into workflow gates. They are a third, user-facing layer
that identifies useful information before a decision and shows what is still
unknown.

| Context | Essential | Recommended | Conditional |
| --- | --- | --- | --- |
| Risk response decision | prioritized risk record; objectives; appetite/tolerance; response direction | risk method; mission; critical services; asset impact | supplier criticality; legal obligations; change/exception record |
| Incident response | declared incident; incident-response plan; responsible roles; investigation/scope | alerts; threat context | supplier and third-party arrangements |
| Recovery planning | recovery initiation decision; recovery priorities; verified restoration assets | critical service and asset impact | supplier support arrangements |
| Supplier requirements | supplier criticality; supplier responsibilities | dependency inventory; legal/contractual requirements | supplier lifecycle findings |
| Policy maintenance | current policy/procedures; review findings | mission, requirements, and risk direction | material supplier or incident findings |

## Migration sequence after approval

1. Add the new edge table and source catalog without removing the current
   tables. **Completed.**
2. Populate the explicit atomic paths from the accepted roster. **Completed.**
3. Change Tile 3 queries and the information-flow popup to read only explicit
   edges.
4. Compare current and new coverage, count paths, and inspect every changed
   item in the UI.
5. Retire the old source/use tables only after an accepted migration and a
   backup confirms no needed facts were lost.

The capability map remains separate throughout. This refactor does not alter
the locked subcategory-level coverage map or any control-framework mapping.

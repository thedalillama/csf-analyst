# Architecture

## Runtime

`start-csf-analyst-ui.ps1` starts `csf_analyst_ui.py` on localhost. The UI is
a Python `ThreadingHTTPServer`; it renders the workspace and uses small HTML
fragments for in-place navigation and modal forms. It has one supported mode:
`analyst`.

The UI reads and writes only the database configured by
`AnalystStateDbPath`. Its default is `state\csf-analyst.db` relative to the
application directory.

## Main modules

| Module | Responsibility |
|---|---|
| `csf_analyst_ui.py` | Routes, HTML/CSS/JavaScript, profile selection, Tile 2 and Tile 3 rendering, and form handling. |
| `csf_analyst_store.py` | SQLite initialization, migrations, seed data, profile/action/evidence persistence, and import commands. |
| `csf_catalog.py` | Read-only adapter for the vendored official CSF catalog and shared product short labels. |
| `csf_guidance.py` | Product-authored plain-English outcome guidance and generic action placeholders. |
| `csf_information_flows.py` | Product-authored information-flow source catalog. |
| `csf_capability_dependencies.py` | Product-authored capability dependency source catalog. |
| `csf_control_mapping_relationships.py` | Product-authored control-to-outcome relationship classifications. |
| `csf_profile.py` | Product assessment-method metadata. |

## UI model

The top Function bar uses NIST's six-function palette. The selected Function
drives the Category and Subcategory workspace. Tile 2 shows official CSF or
selected Community Profile guidance. Tile 3 combines product guidance,
assessment state, actions, evidence, and the one-hop information-flow view.

Frozen Profiles remain browsable but are read-only. The UI hides creation
controls for actions and evidence, and the server rejects create/update/delete
requests for a frozen Profile so the restriction is not merely visual.

## Initialization and migrations

`init_db()` in `csf_analyst_store.py` applies additive migrations recorded in
`schema_migrations`. It also seeds the official base Profile, product-authored
guidance, information/capability maps, and installed source catalogs. Do not
edit a SQLite database directly to change product-authored source data; update
the Python source catalog and let initialization synchronize the runtime copy.

## Application boundary

The analyst runtime, database, launch script, source references, and tests
belong in this directory. Keep this codebase focused on analyst-entered CSF
records and their source-traceable reference material.

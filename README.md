# CSF Analyst

CSF Analyst is a local workspace for applying the NIST Cybersecurity Framework
(CSF) 2.0 to a defined context. It helps an analyst select and tailor a CSF
Profile, assess outcomes, record actions and evidence, and retain an auditable
history of decisions and changes.

It is a teaching and analysis tool. It does not certify compliance, replace an
auditor, or claim that an informative control mapping proves a CSF outcome.

## What it does

- Presents the official CSF 2.0 Functions, Categories, Subcategories, and
  implementation examples.
- Supports frozen NIST base and Community Profiles and editable Organizational
  Profiles.
- Keeps outcome tailoring, target assessments, current assessments, actions,
  evidence, and audit events scoped to an Organizational Profile UUID.
- Lets an Organizational Profile enable control catalogs, currently including
  NIST SP 800-53 Rev. 5.2.0 informative mappings.
- Shows product-authored information-flow guidance separately from official
  NIST content.

## What it does not do

- Treat a control, an action, or a piece of evidence as automatic proof that a
  CSF outcome is fully implemented.
- Permit edits to frozen NIST base or Community Profiles.

## Quick start

From this directory, create a local settings file and launch the workspace:

```powershell
Copy-Item .\csf-analyst.settings.example.json .\csf-analyst.settings.json
powershell -ExecutionPolicy Bypass -File .\start-csf-analyst-ui.ps1 -OpenBrowser
```

The default local URL is `http://127.0.0.1:8765/`. The default analyst database
is `state\csf-analyst.db`; it is local state and is intentionally ignored by
Git.

Run the focused regression suite from this directory:

```powershell
py -3.12 -m unittest tests.test_csf_catalog tests.test_csf_store
```

## Repository map

```text
csf-analyst/
|-- csf_analyst_ui.py             local analyst web application
|-- csf_analyst_store.py          SQLite schema, migrations, and data access
|-- csf_*.py                      CSF catalog adapters and product-authored maps
|-- profiles/                     vendored official CSF catalog
|-- reference-data/NIST/          retained official import sources and provenance
|-- state/                        local, untracked analyst database
|-- tests/                        focused catalog and store regression tests
|-- docs/                         maintenance documentation
`-- start-csf-analyst-ui.ps1      local launcher
```

## Documentation

- [Product scope and boundaries](docs/PRODUCT_SCOPE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Profiles and control catalogs](docs/PROFILES_AND_CATALOGS.md)
- [Data model and audit behavior](docs/DATA_AND_AUDIT.md)
- [Operations and testing](docs/OPERATIONS_AND_TESTING.md)
- [Information-flow and capability maps](docs/CSF_INFORMATION_AND_CAPABILITY_MAPS_REFERENCE.md)
- [Control-mapping relationship method](docs/CONTROL_MAPPING_RELATIONSHIP_CLASSIFICATION_REFERENCE.md)

## Source provenance

The official sources used to seed the NIST SP 800-53 catalog and its CSF 2.0
informative mappings are retained under `reference-data\NIST`. See that
directory's [provenance note](reference-data/NIST/README.md) before refreshing
or replacing imported records.

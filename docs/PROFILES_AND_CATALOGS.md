# Profiles and Control Catalogs

## Profile types

| Type | Editable? | Purpose |
|---|---:|---|
| NIST CSF base | No | Frozen record of the full official CSF 2.0 outcome set. |
| Community Profile | No | Frozen import of a published profile and its source-specific guidance. |
| Organizational Profile | Yes | An independent artifact tailored to the analyst's defined context. |

The top Profile selector can browse all profile types. Only an Organizational
Profile can create or edit actions, evidence, targets, current assessments, or
tailoring decisions.

## Creating and tailoring an Organizational Profile

An Organizational Profile starts from the frozen NIST base and may overlay a
Community Profile or copy another Organizational Profile. After creation it is
independent. For every Category and Subcategory, the editor records a status:

- `included` — selected for this Profile;
- `inherited` — copied from a selected Community/Profile source at creation;
- `out_of_scope` — deliberately excluded for this Profile; or
- `not_selected` — not part of the current working scope.

Included and inherited Subcategories can have a target assessment and a reason
for that target. Out-of-scope and unselected outcomes do not appear in the
regular workspace until the Profile is edited to include them.

## Control catalogs

Catalogs are source collections that may offer mapped controls when an action
is added. Enabling a catalog does not mean the organization has adopted or
implemented every control in it.

Catalog registration is shared, while enabled/disabled selection is stored per
Organizational Profile in `csf_profile_control_catalogs`. A frozen Profile may
be browsed but cannot change catalog selection.

NIST SP 800-53 Rev. 5.2.0 is the currently integrated catalog. Its CSF
informative mappings identify candidate connections only. The application
distinguishes the official mapping from any product-authored explanation.

## Community Profile imports

Keep the original source PDF and a reviewable intermediate spreadsheet under
`reference-data\NIST`. Import a Community Profile as a new frozen record with
its own UUID, source URL/version/review date, outcome selection, source notes,
and profile-specific guidance. Do not alter it after import; correct the source
spreadsheet and re-import as a distinct reviewed version if needed.

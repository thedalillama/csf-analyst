# Operations and Testing

## Local configuration

`csf-analyst.settings.json` is local-only. Start from
`csf-analyst.settings.example.json` and set paths only when the defaults do not
fit your environment. The settings file and `state/` are ignored by Git.

## Launch

```powershell
Set-Location C:\CodexTestWork\csf-analyst
powershell -ExecutionPolicy Bypass -File .\start-csf-analyst-ui.ps1 -OpenBrowser
```

The launcher stops an existing standalone analyst process before starting a new
one. The default endpoint is `http://127.0.0.1:8765/`.

## Verification

Run from the application directory:

```powershell
py -3.12 -m py_compile .\csf_analyst_ui.py .\csf_analyst_store.py
py -3.12 -m unittest tests.test_csf_catalog tests.test_csf_store
```

The focused suite currently contains 13 tests. Verify manually after UI work:

1. Select an Organizational Profile and confirm actions/evidence can be added.
2. Select the NIST base or a Community Profile and confirm Tile 3 is read-only.
3. Change a profile tailoring/target value, save it, and inspect the outcome
   history and profile audit log.
4. Add evidence and link/unlink it from an action; inspect the evidence and
   action histories.
5. Confirm the selected Function's NIST color appears in navigation and the
   guidance strip, including hover behavior.

## Database recovery

If the UI appears to have no profiles, first check `AnalystStateDbPath` in the
settings file. It must point to the intended `csf-analyst.db`; an empty new
database will seed the base profile but will not contain existing Organizational
Profiles, actions, or evidence.

Before moving or replacing the database, stop the UI and make a complete copy
of the `.db` file. Keep the matching `-wal` and `-shm` files if they exist.

## Source data refreshes

Do not refresh an official NIST catalog or Community Profile directly in a live
working database. Retain the new source artifact, record provenance, use a
development database, validate the import, then back up the working database
before applying a reviewed update.

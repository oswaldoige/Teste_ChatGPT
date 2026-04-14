---
name: "download-eproc-tjrj"
description: "Use when the user wants to download full process PDFs from TJRJ eproc from a provided process list, without mixing this step into the judicial-analysis skills."
---

# Download eproc TJRJ

## When to use
- Use before judicial analysis, when the user provides process numbers that must be downloaded from the TJRJ eproc.
- Use as part of the preprocessing layer, not as part of the judicial-drafting core.

## Workflow
1. Confirm the input list path or create a temporary `.txt` with one process number per line.
2. Use `scripts/run_download_eproc.py`.
3. Point the downloads and logs to isolated folders for the current batch.
4. Wait for manual login in the browser when prompted.
5. After the downloads finish, hand the resulting PDFs to `$pdf-json-triagem-tjrj`.

## Script
- `scripts/run_download_eproc.py`

## Notes
- This skill reuses `C:\download_eproc.py` through a wrapper, so the original script stays intact.
- Keep this skill separate from the revisor skills to avoid overloading the judicial-analysis flow.

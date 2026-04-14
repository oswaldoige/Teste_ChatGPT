---
name: "pdf-json-triagem-tjrj"
description: "Use when downloaded judicial PDFs need to be converted into .triagem.json files before the revisor starts the legal analysis."
---

# PDF para JSON de Triagem TJRJ

## When to use
- Use after the PDF download step and before the judicial-analysis step.
- Use when the user has a folder with process PDFs and wants `.triagem.json` files generated in the same folder.

## Workflow
1. Confirm the target folder that contains the PDFs.
2. Use `scripts/run_pdf_to_json.py`.
3. Preserve the full extracted text of the PDF and explicitly populate the `provas` field in the JSON whenever probative documents are detected.
4. Keep the generated `.triagem.json` files in the same folder as the PDFs.
5. Hand the resulting JSON files to the revisor core only after the conversion finishes.

## Script
- `scripts/run_pdf_to_json.py`

## Notes
- This skill is deliberately separate from the revisor skills so OCR and PDF preprocessing do not pollute the legal-analysis context.
- Proof documents matter. The conversion step must not collapse the dossier into only petitions and decisions; it must carry forward attachments and other probative material into the JSON structure.

---
name: "preprocessamento-processos-tjrj"
description: "Use when a batch of TJRJ process numbers must go through the preprocessing pipeline: system-specific PDF download, PDF-to-JSON conversion, and only then handoff to the judicial-analysis automation."
---

# Preprocessamento de Processos TJRJ

## When to use
- Use when the user wants a preprocessing pipeline before judicial analysis.
- Use when the flow is: process list -> download PDFs -> convert PDFs to `.triagem.json` -> handoff to the revisor core.

## Workflow
1. Read [pipeline.md](references/pipeline.md).
2. Keep the preprocessing layer separate from the judicial-analysis layer.
3. If the batch is homogeneous:
   - use `$download-pje-tjrj`; or
   - use `$download-eproc-tjrj`.
4. After downloads, always run `$pdf-json-triagem-tjrj`.
5. Confirm that the generated JSON files preserve proof documents in the `provas` field and in the extracted full text.
6. Only after the JSON files exist, hand the batch to the revisor core.

## Important truth
- Pure offline autodetection between `PJe` and `eproc` from the process number alone is not reliably safe.
- For mixed batches, prefer a list that already indicates the system, or run separate homogeneous rounds.

## Goal
- Prevent the revisor skills from absorbing browser automation, OCR, and download logic.
- Keep the judicial-analysis core focused on reading JSON and drafting rulings.

---
name: "sentenca-civel-tjrj"
description: "Use when drafting civil judgments for TJRJ, especially in recurring and highly standardized families such as Guarda Civil de Resende, Nova Escola, water and sewer cases from the 3o Nucleo 4.0, health, bank, and vehicle disputes."
---

# Sentenca Civel TJRJ

## When to use
- Use when the case is mature for judgment and the main task is to draft the sentence.

## Workflow
1. Apply the shared rules from `$revisor-base-tjrj`.
2. Apply `$roteamento-modelos-tjrj` to identify the canonical sentence folder before browsing the wider archive.
3. Choose and apply the material-family skill that best fits the case:
   - `$familia-consumidor-tjrj`
   - `$familia-civel-contratual-tjrj`
   - `$familia-fazenda-publica-tjrj`
4. Read [roteiro.md](references/roteiro.md).
5. Open [familias-padronizadas.md](references/familias-padronizadas.md) only to refine the recurring subfamily inside the chosen macrofamilia.
6. Always generate complete and concise `.docx` versions.
7. After the sentence draft is closed, also apply `$validacao-juris-sentenca-tjrj` to create the third validated `.docx` version with official jurisprudential support in the body of the reasoning.

## Output expectation
- Preserve the TJRJ tone and the model family structure.
- When a canonical sentence model already exists in `00_NUCLEO_OPERACIONAL`, treat it as the primary matrix and use the broader archive only as fallback or comparison support.
- When a highly aderent family model exists, keep the sentence visibly anchored to that model's structure rather than drafting a fresh prose architecture.
- When the decisive factual conclusion depends on identifiable proof, keep the reasoning tied to the main documentary or oral evidentiary anchors from the dossier, with `ID` in PJe or `Evento + sigla` in eproc/TJRJ.
- Keep the reasoning in prose, without serial numbering of paragraphs.
- Deliver three sentence artifacts by default: complete, concise, and jurisprudentially validated.

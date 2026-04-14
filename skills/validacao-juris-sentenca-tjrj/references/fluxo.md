# Fluxo

## Input minimum
- Dossier JSON or equivalent process source already used in the sentence.
- Existing complete sentence `.docx`.
- Existing concise sentence `.docx`, if available.

## Validation sequence
1. Reconfirm the exact controversy that the sentence actually resolves.
2. Separate what is ratio decisiva from what is only contextual narrative.
3. Search official precedents only for the ratio points that really matter.
4. Rank the findings:
   - Tema, tese, repetitivo, sumula, IRDR, IAC
   - Collegiate judgment directly aderent to the controversy
   - Official court page or official news item only as support, never as the main authority if the judgment itself is available
5. Discard precedents that are too generic, materially distinguishable, or older without compensating value.
6. Decide the treatment:
   - Keep the sentence as it stands
   - Refine the legal reasoning without changing the outcome
   - Correct the reasoning and the outcome
7. Create the third `.docx` validated version by cloning the complete sentence structure and inserting only the jurisprudential support that is truly needed.
8. Before saving, confirm that the validated version preserved the evidentiary anchors of the complete sentence and did not replace concrete `ID` or `Evento + sigla` references with generic proof formulas.

## Insertion pattern in the body
- Use the format from `formato-remissao.md` as the default rule.
- Prefer:
  - one short introductory sentence;
  - one aderent ementa `ipsis litteris`, with the full identification of the judgment in the same block;
  - the official link immediately below in a standalone line.
- Default introductory sentence:
  `Nesse sentido, ja decidiu o e. Tribunal de Justica do Estado do Rio de Janeiro:`
- For STJ or STF precedents, adapt only the court name in the introductory sentence.

## Style limits
- Keep jurisprudential insertions proportionate.
- In ordinary cases, prefer:
  - one TJRJ precedent for factual adherence; and
  - one STJ or STF precedent for uniformizing ratio, if really useful.
- Keep the dispositive free of citation blocks.
- Do not rewrite the entire sentence if only one paragraph needs calibration.
- Default rule: preserve every paragraph of the complete sentence unless a specific paragraph needs a jurisprudential insertion or correction.
- Do not replace a highly aderent ementa with a generic reference block unless the ementa is truly too long for the paragraph.
- If using ementa, transcribe the official text literally; if using Tema, tese, or sumula, reproduce the official wording literally.

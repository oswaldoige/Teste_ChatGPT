---
name: "tribunal-simulado-apelacao-tjrj"
description: "Use when reviewing a TJRJ civil decision under the perspective of a simulated appellate court. This is the GENERAL version that works for BOTH sentences and decisions (despachos/decisões interlocutórias). For SENTENCES specifically, prefer tribunal-simulado-sentenca-tjrj. For DESPACHOS/DECISÕES specifically, prefer tribunal-simulado-decisao-tjrj. The skill simulates a Desembargador revisor analyzing whether a decision should be upheld, partially reformed, or fully reformed, with STF/STJ/TJRJ jurisprudential support. Input: validated decision/sentence (.docx) and process PDF/JSON. Output: structured review in .docx format."
---

# Tribunal Simulado / Revisor de Apelação TJRJ (Versão Geral)

## When to use
- Use for general review tasks when not specified whether it's a sentence or decision.
- Can be used as fallback when专门的 skills are not available.
- For sentence-specific review, use `tribunal-simulado-sentenca-tjrj`.
- For decision-specific review, use `tribunal-simulado-decisao-tjrj`.

## Workflow
1. Read [roteiro-apelacao.md](references/roteiro-apelacao.md) at the start of the task.
2. Read [fontes-oficiais-apelacao.md](references/fontes-oficiais-apelacao.md) for source rules.
3. Locate the validated decision file (`.docx` with "validada" in the filename).
4. Read the complete process PDF for full context.
5. If available, read the probationary review (`revisao_probatoria/`) to integrate its findings.
6. Identify whether the object is a SENTENCE or DECISION.
7. Apply the appropriate analysis:
   - For sentences: use 5-part review structure
   - For decisions: use verification/correction structure
8. Search for real STF/STJ/TJRJ precedents.
9. Produce the structured output.
10. **IMPORTANT**: Output must be in `.docx` format.

## Output expectation
- Short, firm, and practical output
- Clear conclusion for the type of decision
- Jurisprudential validation with official links
- Corrections suggested when applicable

## Output Format

**IMPORTANT**: The final output must ALWAYS be in `.docx` format.

Generate:
1. Analysis in docx format for immediate presentation
2. Save to the folder defined by the user

## Do not use
- Do not use as replacement for sentence drafting skills.
- Do not use when user specifically wants sentence review (use specific skill).
- Do not use when user specifically wants decision review (use specific skill).
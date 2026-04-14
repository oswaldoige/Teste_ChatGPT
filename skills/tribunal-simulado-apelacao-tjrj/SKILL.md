---
name: "tribunal-simulado-apelacao-tjrj"
description: "Use when reviewing a TJRJ civil sentence under the perspective of a simulated appellate court. The skill simulates a Desembargador revisor analyzing whether a sentence should be upheld, partially reformed, or fully reformed, with STF/STJ/TJRJ jurisprudential support. Input: validated sentence (.docx) and optionally the triage JSON. Output: structured appellate vote with Result, Central Point, Jurisprudential Basis, and Objective Conclusion."
---

# Tribunal Simulado / Revisor de Apelação TJRJ

## When to use
- Use when the user wants to review a sentence already issued (arquivo `.docx` validado) under the perspective of an appellate court.
- Use when the task is to simulate a Desembargador revisor analyzing the legal correctness of a sentence.
- Use when the user provides a list of process numbers and wants each sentence reviewed for potential appeal grounds.

## Workflow
1. Read [roteiro-apelacao.md](references/roteiro-apelacao.md) at the start of the task.
2. Read [fontes-oficiais-apelacao.md](references/fontes-oficiais-apelacao.md) for source rules.
3. Locate the validated sentence file (`.docx` with "validada" in the filename) for the given process number.
4. Optionally read the triage JSON for full procedural context.
5. Analyze the sentence strictly under the appellate review scope defined in the roteiro.
6. Produce the structured vote following the four-part format: Resultado → Ponto Central → Fundamento Jurisprudencial → Conclusão Objetiva.
7. Search for real STF/STJ/TJRJ precedents. If no reliable precedent is found, state that explicitly.
8. Never invent process numbers, rapporteurs, themes, or súmulas.

## Output expectation
- Short, firm, and practical output following the four-part structure.
- Clear conclusion: uphold, partially reform, or fully reform.
- Precise identification of the error or correctness.
- Sufficient legal reasoning with pertinent precedents and links.
- Sober, technical, direct language — no academic digressions, no doctrine, no invented theses.
- Only STF, STJ, and TJRJ jurisprudence.

## Do not use
- Do not use for first-pass drafting of sentences, despachos, or decisões interlocutórias.
- Do not use as a replacement for `sentenca-civel-tjrj` or `revisor-base-tjrj`.
- Do not use when the user wants to rewrite or redraft the sentence rather than review it.

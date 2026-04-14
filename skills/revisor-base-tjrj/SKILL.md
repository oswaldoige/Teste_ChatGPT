---
name: "revisor-base-tjrj"
description: "Use when drafting or reviewing civil judicial acts for TJRJ from process dossies or JSON files, especially to apply the shared rules on CC/CPC/CDC, eproc versus PJe references, model lookup, PT-BR style, .docx output, and final validation across any procedural phase."
---

# Revisor Base TJRJ

## When to use
- Use alongside any phase-specific TJRJ skill for judicial drafting or review from JSON dossies.
- Use when the task needs the shared TJRJ rules before finalizing a despacho, decisao, sentenca, or cumprimento de sentenca.

## Workflow
1. Read [shared-rules.md](references/shared-rules.md) at the start of the task and, when model selection matters, also read [nucleo-operacional.md](references/nucleo-operacional.md).
2. Before any drafting, apply the mandatory strict-flow gate from `skills\fluxo-estrito-civel-tjrj\references\checklist.md`.
3. Identify the process system, the exact procedural phase, the last relevant judicial act, every supervening petition or incident, and any unresolved checkpoint that still conditions the next judicial step.
4. Before drafting, apply `$roteamento-modelos-tjrj` and search `modelos` first. After selecting the best canonical model, also check the matching `90_BLOCOS_REUTILIZAVEIS` folder whenever the family has a stable gabinete opening or burden-of-proof block. Only if no canonically aderent model exists there should the search escalate to `00_PRIORITARIOS_AUTOMACAO`, then to the specialized folders and the wider archive.
5. Draft in PT-BR judicial prose with minimal deviation from the selected base model and deliver the final version in `.docx`.
6. Run the final validation checklist from the reference file before saving.

## Do not use
- Do not use this as the only skill if the task clearly belongs to iniciais, tutela, saneador, sentenca, or cumprimento; pair it with the phase-specific skill.

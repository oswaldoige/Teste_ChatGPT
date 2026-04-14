---
name: "orquestrador-gabinete-tjrj"
description: "Use when the user wants a broader gabinete automation that coordinates intake, filtering, routing, and production around the judicial revisor core without changing or replacing it. Use to organize larger workflows, decide when to invoke the revisor core, preserve the core rules intact, and keep the main process-analysis automation isolated from satellite routines such as triage, queue organization, and production consolidation."
---

# Orquestrador Gabinete TJRJ

## When to use
- Use when the user asks for the broader gabinete automation, not just the core process reviewer.
- Use when the workflow needs orchestration before or after judicial drafting, such as intake, queue filtering, batch routing, or production consolidation.
- Use when the user wants a wider automation but expressly does not want to alter the existing `revisor-processual-tjrj` core.
- Do not use this skill as a substitute for the core drafting flow itself.

## Workflow
1. Read [contrato-core.md](references/contrato-core.md).
2. Read [fluxo-orquestracao.md](references/fluxo-orquestracao.md).
3. Identify which part of the requested workflow belongs to orchestration and which part belongs to the judicial revisor core.
4. Keep the orchestration layer outside the core; do not rewrite core rules, outputs, or model priorities.
5. When the task reaches the judicial-act stage, invoke the core revisor flow using:
   - `$revisor-base-tjrj`
   - the phase-specific skill that matches the produced act
   - the material-family skill that matches the dispute whenever it can already be identified
   - `$validacao-juris-sentenca-tjrj` whenever the produced act is a sentence
6. Resume orchestration only after the core finishes that judicial step.
7. Report results without collapsing the distinction between orchestration and the core.

## Output expectation
- Preserve the autonomy and integrity of the `revisor-processual-tjrj` core.
- Treat the core as a service layer for judicial drafting, not as something to be redefined.
- Use separate commands for the core and for the broader gabinete automation.
- Never import unrelated project rules into the core.

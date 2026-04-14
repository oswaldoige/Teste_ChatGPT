---
name: "roteamento-modelos-tjrj"
description: "Use when selecting TJRJ drafting models for tutela, saneador, or sentenca so the agent first searches the canonical operational nucleus and only falls back to the wider archive when necessary."
---

# Roteamento Modelos TJRJ

## When to use
- Use before searching models for a tutela, saneador, or sentenca in the TJRJ civil workflow.
- Use when the task needs a predictable search order instead of browsing the full model archive from the start.

## Workflow
1. Read [matriz-provimentos.md](references/matriz-provimentos.md).
2. Identify the provimento: `tutela`, `saneador`, or `sentenca`.
3. Identify the macrofamilia material: `consumidor`, `civel contratual`, or `Fazenda Publica`.
4. Search the matching folder inside `modelos`.
5. After choosing the best canonical model, consult the matching folder inside `90_BLOCOS_REUTILIZAVEIS` whenever the family has a stable gabinete block for opening, burden of proof, or dispositive cadence.
6. If no canonically aderent model exists there, fall back to `00_PRIORITARIOS_AUTOMACAO`, then to the specialized folder for the subject, and only after that to the wider archive.
7. When a recurring family still needs a special matrix, keep it as a refinement inside the chosen macrofamilia instead of restarting the search from the whole archive.

## Output expectation
- Reduce model-search noise.
- Prefer a small, stable set of canonical models.
- Escalate to the large archive only when the operational nucleus is genuinely insufficient.

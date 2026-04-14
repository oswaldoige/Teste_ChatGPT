---
name: "validacao-juris-sentenca-tjrj"
description: "Use when a TJRJ civil sentence is already drafted and needs a separate, post-draft jurisprudential validation layer based only on official TJRJ, STJ, and STF sources. Use to confirm or correct the reasoning, prefer recent precedents when possible, insert official ementas, temas, teses, or sumulas literally in the body of the sentence, keep the official link after each citation, and generate a third validated .docx version. Do not use for first-pass drafting, non-sentence acts, or when the user wants to keep the main revisor flow untouched."
---

# Validacao Juris Sentenca TJRJ

## When to use
- Use only after the sentence already exists, usually alongside `$revisor-base-tjrj`, `$sentenca-civel-tjrj`, and `$doc`.
- Use when the user wants a third sentence version validated by jurisprudence without altering the main automation flow.
- Do not use for despacho, decisao interlocutoria, saneador, cumprimento de sentenca, or the first drafting pass of the sentence.

## Workflow
1. Confirm there is already a drafted sentence and preserve the existing complete and concise `.docx` files.
2. Read [fluxo.md](references/fluxo.md).
3. Read [fontes-oficiais.md](references/fontes-oficiais.md).
4. Read [formato-remissao.md](references/formato-remissao.md).
5. Identify the central legal controversies actually decided in the sentence.
6. Search only official TJRJ, STJ, and STF sources, unless the user expressly authorizes another platform.
7. Prefer recent official precedents when they are materially equivalent in authority and factual fit.
8. If the most relevant precedent is older because it is a leading case, Tema, tese, ou ratio marcante, keep it only if useful and, when possible, pair it with a newer official reaffirmation.
9. Validate whether the current sentence is correct, partially correct, or needs adjustment.
10. Generate a third `.docx` version starting from the complete sentence as the base matrix, preserving its structure and wording wherever possible.
11. Insert the jurisprudential support in the body of the reasoning, not by default in a final annex.
12. Use the remissao format from the reference file as the default pattern for each precedent block.
13. After each ementa, tema, tese, or sumula inserted in the body, keep the official link to the judgment or official source immediately below it.

## Output expectation
- Preserve the dispositive structure and the gabinete style of the original sentence as much as possible.
- Preserve not only the outcome but also the base-model architecture of the sentence. The validation layer may calibrate or reinforce specific reasoning paragraphs, but it must not replace a strongly aderent family model with a new stylistic structure.
- The validated version should ordinarily read like the complete sentence plus jurisprudential additions, not like a separate redraft.
- Preserve the evidentiary anchors already individualized in the complete sentence. The validation layer must not genericize, suppress, or dilute explicit references to `ID` documents or `Evento + sigla` that support the decisive factual findings.
- Keep the dispositive clean; place ementas and references only in the reasoning.
- Prefer one or two strong precedents over a crowded string of citations.
- When an ementa is used, transcribe it `ipsis litteris` from the official source. Do not summarize, paraphrase, or rewrite the ementa text.
- When the support is a Tema, tese, or sumula, reproduce the official wording literally.
- Default to the formula `Nesse sentido, ja decidiu...` plus full precedent identification and the official link below it.
- Do not force citation where no genuinely useful official precedent was found.
- Deliver a third `.docx` with a stable and descriptive name, in addition to the existing complete and concise versions.

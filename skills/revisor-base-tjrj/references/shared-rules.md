# Shared Rules

## Core sources to open first
- `docs\arquitetura\CLAUDE.md`
- `docs\arquitetura\AUTOMACAO_REVISOR_PROCESSUAL.md`
- `modelos`
- `${GABINETE_RAIZ_2026}\AUTOMACAO_MODELOS\00_PRIORITARIOS_AUTOMACAO`

## Model-search order
1. `00_NUCLEO_OPERACIONAL`
2. `00_PRIORITARIOS_AUTOMACAO`
3. Specialized folder for the matter or chamber
4. Correlated folders
5. Reference PDFs when needed

Special case:
- For water and sewer cases from the 3o Nucleo de Justica 4.0 da Capital, prioritize `${GABINETE_RAIZ_2026}\AUTOMACAO_MODELOS\NUCLEO 4.0`.

Reference PDFs:
- `${GABINETE_RAIZ_2026}\AUTOMACAO_MODELOS\modelos_variados\98 - REFERENCIA - JTRAMOS.pdf`
- `${GABINETE_RAIZ_2026}\AUTOMACAO_MODELOS\modelos_variados\98 - REFERENCIA - MODELOS CONSECTARIOS TJRJ TEMA1368.pdf`

Internal reference:
- `${GABINETE_SKILLS}\revisor-base-tjrj\references\consectarios-civis-lei-14905.md`
- `${GABINETE_SKILLS}\revisor-base-tjrj\references\nucleo-operacional.md`

## Shared legal and drafting rules
- Strict-flow gate is mandatory. Before drafting any judicial act, close the following six internal answers: (1) system; (2) exact procedural phase and candidate act; (3) last relevant judicial act; (4) every supervening petition or incident after it; (5) unresolved procedural checkpoint, if any; and (6) exact base model path selected for drafting. If any of these answers is still uncertain, do not draft yet.
- Technical generation gate is also mandatory for outputs in `saida_docx`: the `.md` source must have a sidecar `.gate.json` file with the six strict-flow answers formally filled plus `preflight_confirmado = true` and `postflight_confirmado = true`. Without that sidecar, the local `make_docx.py` must refuse generation.
- No judicial act may be drafted before the exact gabinete model path is chosen. It is not enough to know the family or the matter; the automation must know which concrete base model is serving as the primary drafting matrix.
- After classifying the phase, run a second control question before drafting: `is this truly the next procedural step after the last relevant act and all later petitions?` If the answer is not clearly yes, reopen the dossier and reclassify the phase before writing.
- The dossier JSON is the only source of facts. Do not invent events, dates, parties, IDs, or procedural incidents.
- Never attribute to a party any statement, manifestation, allegation, factual assertion, request, waiver, consent, opposition, disinterest, admission, payment, compliance, refusal, knowledge, ignorance, recognition, or any other procedural or factual position unless that content is expressly supported by an identifiable item in the dossier.
- Do not infer or embellish what a party "said", "requested", "admitted", "opposed", "accepted", "waived", "recognized", or "demonstrated" unless the dossier expressly shows that position. When the file is silent, the draft must remain silent or use only an institutional or objective rationale that does not impute a statement to the party.
- If the dossier does not contain an express manifestation about conciliation, hearing, settlement, evidence, agreement, waiver, or similar procedural posture, draft the act without imputing that statement to the party. In particular, do not write that the party manifested disinterest in the art. 334 hearing unless the dossier expressly shows it.
- Operational isolation is mandatory. Ignore unrelated sidebar projects, topics, folders, or automations unless the user expressly directs otherwise for that specific run.
- Do not read from, write to, or take drafting guidance from unrelated projects such as `Download_Processos`, `Scalp_Smart`, or any folder outside the process/model/output paths expressly indicated for the revisor workflow.
- Identify the system before drafting:
  - `eproc/TJRJ`: use `Evento + sigla` when the reference matters.
  - `PJe`: use `ID` when the reference matters.
- In judicial reasoning, whenever a decisive factual statement is supported by an identifiable document, petition, hearing record, certificate, expert report, or exhibit, cite the corresponding `ID` or `Evento + sigla` in the sentence instead of using a generic formula such as `the evidentiary record shows`.
- Generic references to `the evidentiary record`, `the documents attached`, or equivalent are only acceptable for secondary or cumulative support. They are not acceptable when the reasoning depends on specific proof of acquisition, payment, possession, notice, compliance, refusal, damage, or any other decisive fact that can be individually identified in the dossier.
- When the proof is composite, individualize the main evidentiary anchors in the same sentence or in consecutive sentences. Example logic: contract/document `ID X`, conversations `ID Y`, hearing record `ID Z`, certificate `ID W`.
- When a party attributes a specific wording to a bill, invoice, screenshot, contract clause, notice, line item, or on-screen field, do not elevate that wording to an established documentary fact unless the underlying document itself clearly displays it. If the wording was used only by the party or by a prior ruling, attribute it to that source instead of presenting it as an independently verified feature of the document.
- In urgent-relief or follow-up rulings involving faturas, TOI, parcelamentos, multas, or equivalent charges, keep separate: (a) what the underlying bill objectively shows; (b) how a prior judicial act described the controversy; and (c) how the parties characterize the charge. Never collapse those three planes into a single asserted fact.
- In water-and-sewer cases with proven intimation of a tutela de restabelecimento and repeated later petitions reporting ongoing lack of supply, the first follow-up decision may reforcar the tutela with majoracao de multa and ordem subsidiaria de carro-pipa. If noncompliance persists after that renewed deadline and the dossier still lacks objective proof of regularization, prefer the second-step block with SISBAJUD arresto and autorizacao de contratacao particular de carro-pipa, instead of merely repeating generic warnings.
- When there is an adherent base model, keep the model as the primary drafting matrix. Preserve its sentence structure, connective style, punctuation flow, and cadence, changing only what the concrete case actually requires.
- Treat `modelos` as the default operational search root. The broader archive remains consultative and should only become the starting point when the user expressly asks for that broader search or when the operational nucleus is insufficient.
- After choosing the main model, consult the corresponding `90_BLOCOS_REUTILIZAVEIS` folder whenever the gabinete has a stable opening, burden-of-proof bridge, or dispositive cadence for that family.
- Before opening large volumes of models, classify the case by provimento (`tutela`, `saneador`, `sentenca`) and by macrofamilia (`consumidor`, `civel contratual`, `Fazenda Publica`).
- Do not paraphrase a suitable gabinete model just to "improve" style. Minimal adaptation is preferred over free rewriting when the model already fits the case.
- In highly repetitive sentence families with a very aderent model, the draft must mirror the model's macro-structure almost verbatim: opening formula, order of procedural history, transition to the reasoning, sequence of legal grounds, dispositive cadence, and closing lines. Replace facts, IDs, parties, dates, and outcome details as needed, but do not switch to a new prose architecture.
- When the selected model already contains the preferred gabinete voice for that family, avoid "cleaner" or "shorter" rewrites that erase the recognizable structure of the base model. Fidelity to the gabinete matrix prevails over stylistic simplification.
- In consumer-service disputes, if the dossier or a prior judicial ruling already recognizes the applicability of the CDC and the selected base model contains an express paragraph stating that the relationship is one of consumption, keep that paragraph in the reasoning. Do not leave the consumer nature only implicit, only in the report, or only in the dispositive.
- In the same scenario, also preserve the immediate legal consequences that the model ties to that classification when they remain pertinent in the concrete case, such as the identification of consumer/supplier positions, the duty of information, objective liability, or the inversion of the burden of proof already decided in the case.
- In jurisprudential support, prefer the most recent official precedents available when they are materially equivalent in authority and factual fit.
- If the most relevant precedent is older because it is the leading case, Tema, tese, or landmark ratio, do not discard it solely for age; instead, when possible, pair it with a more recent official application from TJRJ, STJ, or STF.
- In civil condemnation details, prefer the internal consectarios guide first. Use the external PDF as a complementary cross-check, not as the only source.
- In civil condemnation details, separate correction and mora in the dispositive, identify whether the case crosses `30/08/2024`, and avoid algebraic formulas when the cleaner reference to `art. 406, paragraph 1, of the Civil Code` is enough.
- In post-`30/08/2024` private-law cases, prefer the cleaner dispositive formula from the internal consectarios guide: `correcao monetaria pelo IPCA` plus `juros de mora pela taxa legal, na forma do art. 406, paragrafo 1o, do Codigo Civil`, with no extended explanation about CMN methodology in the dispositive unless a specific local model expressly requires more.
- In consumer sentences with multiple monetary chapters, prefer splitting the dispositive into separate items for: (a) declaratory/refaturamento relief; (b) nullity of parcelamento or ancillary contractual act; (c) repetition/restitution chapter with its own consectarios; and (d) moral-damages chapter with its own consectarios. Avoid mixing parcelamento nullity, restitution, and moral damages in a single long item when the family model allows cleaner segmentation.
- Always face the last relevant judicial act and every relevant petition after it.
- Always name known incidents expressly. Never hide them under generic language.
- In follow-up interlocutory acts, do not redecide matters already resolved by prior rulings merely because they appear in the procedural history. Tutela, gratuity, custas, citation, redistribution, and similar points should normally be mentioned only as background or science, unless there is a supervening request, alleged noncompliance, material error, express reconsideration request, or another concrete reason that truly reopens the issue.
- The corollary is equally mandatory: do not skip unresolved procedural checkpoints created by prior rulings. If an earlier decision ordered complementacao de custas, emenda da inicial, regularizacao de mandato, deposit, or another conditional act for the case to proceed, confirm from the dossier whether there was compliance, certification of noncompliance, or a later ruling on the point before drafting the next act. Do not impulsionar the merits or the ordinary contraditorio as though that checkpoint did not exist.
- In passive litisconsortium, individualize the procedural position of each defendant before drafting. Do not treat citação, comparecimento espontâneo, revelia, prazo, or contestação from one defendant as if they regularized the entire passive pole.
- In the first manifestation of the 3o Nucleo de Justica 4.0 after redistribution, use the gabinete standard opening block when supported by the dossier: science of the redistribution and of the relevant ruling from the origin court, science of pending habilitation/anotacao de patrono, and the standard `+Acordo` paragraph.
- In 3o Nucleo de Justica 4.0 water-and-sewer cases that already passed contestation and replica and still require evidentiary organization, prefer the gabinete's `EM - PROVAS - COM - SANEAMENTO` matrix from the Nucleo 4.0 model folder as the default base model for that procedural phase. Keep its short saneador cadence: opening under art. 357 CPC, treatment of the true preliminary issue, fixation of controverted points, burden-of-proof bridge when procedurally pertinent, and disciplined opening of the proof-specification phase.
- In 3o Nucleo de Justica 4.0 water-and-sewer cases, if the file already has contestation after redistribution and there is a later petition alleging compliance with a tutela previously granted by the origin court, do not jump to sentence and do not issue a generic despacho. The default next act is the Nucleo's replica-pattern decision: (a) science of the redistribution and of the relevant origin-court rulings; (b) science of the later petition alleging compliance, with anotacao de patrono when requested; (c) the standard `+Acordo` paragraph; (d) view to the author for replica to the contestation; (e) express determination that the author also address the alleged compliance with the tutela; and (f) simultaneous objective and justified specification of evidence by both parties.
- Before using the Nucleo 4.0 replica-pattern decision, confirm from the dossier whether the author has already filed a later petition that materially responds to the contestation, to the alleged compliance with tutela, or to the defense documents. If such manifestation already exists, do not reopen replica. Reclassify the phase to the next real step, usually saneamento com provas or, if the case is mature, sentence.
- A later petition by the author should be treated as replica when, in substance, it impugns the contestation, rebuts defense documents, discusses alleged compliance/noncompliance of tutela, or renews merits arguments after the defense. Do not insist on a formal label requirement if the procedural content is clearly that of replica.
- Postflight is also mandatory. Before saving the final artifact, reconfirm: (1) the chosen act still matches the real phase; (2) no later petition was ignored; (3) no point already decided was redecided without a new procedural trigger; (4) the selected model's macrostructure was in fact preserved; and (5) the `.docx` reopened without accent corruption.
- When a party requests anotacao de patrono, first verify from the dossier whether that lawyer is already cadastrated or whether prior publications already run in that name. If the patrono already appears as duly registered, do not issue a redundant new order of annotation; record that the request is prejudiced because the cadastro already exists.
- In judicial reasoning, do not use bullets, markdown headers, or serial numbering of paragraphs. The exception is some standardized initial orders that already use numbered items in the model.
- In sentences, do not write as if the court were newly granting inversion of the burden of proof under art. 6, VIII, CDC. That rule belongs to the procedural/instructional plane. At judgment stage, either: (a) record that a prior interlocutory ruling already addressed the point; or (b) state that a specific ruling on the request is unnecessary or prejudiced in light of the evidentiary record and the concrete burden allocation used in the case. Do not use formulas such as `I grant the inversion of the burden of proof` in the sentence unless merely reporting an earlier ruling.
- Final output must be in PT-BR and saved as `.docx`.
- Before delivery, reopen the generated `.docx` and confirm there is no mojibake or encoding corruption. Sequences such as `A??o`, `N?cleo`, `?gua`, `R?PLICA`, `consumidor ?`, `matr?cula`, or `3?o` are forbidden in the final artifact and require regeneration.
- When the draft contains a large amount of accented PT-BR text, prefer a UTF-8 source file plus later `.docx` conversion instead of relying exclusively on inline shell text.
- Sentences and complex interlocutory decisions require two versions: complete and concise.
- Whenever the produced act is a sentence, also run the jurisprudential validation layer from `validacao-juris-sentenca-tjrj` and generate a third `.docx` version validated with official TJRJ, STJ, and STF sources.

## Final validation checklist
- Confirm the exact phase of the case.
- Confirm the last relevant decision and all later events.
- Confirm the correct model family was used.
- Confirm the factual references use the correct system (`Evento + sigla` or `ID`).
- Confirm the text is in PT-BR with accents.
- Confirm the sentence did not defer inversion of the burden of proof as a new ruling at judgment stage.
- Confirm the reopened `.docx` does not contain mojibake markers or in-word question marks replacing Portuguese characters.
- Confirm the final artifact is `.docx`, not `.md`.

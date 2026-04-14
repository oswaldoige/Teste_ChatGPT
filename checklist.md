# Checklist Operacional

## Preflight

- Confirmar o sistema (`PJe` ou `eproc/TJRJ`).
- Confirmar a fase processual exata.
- Confirmar o ato cabivel.
- Identificar o ultimo ato judicial relevante.
- Identificar peticoes e incidentes posteriores.
- Verificar pendencia condicionante.
- Escolher o modelo-base exato.
- Confirmar aderencia da familia material.

## Redacao

- Preservar a macroestrutura do modelo-base.
- Usar blocos reutilizaveis quando a familia exigir.
- Nao inventar fatos, datas, pedidos ou manifestacoes.
- Nao redecidir questao ja decidida sem gatilho processual novo.
- Nao saltar etapa processual.

## Gate formal

- Preencher o sidecar `.gate.json`.
- Confirmar `preflight_confirmado = true`.
- Confirmar `postflight_confirmado = true` no fechamento final.

## Pos-redacao

- Revisar a coerencia da minuta com a fase real.
- Conferir se nenhuma peticao posterior relevante ficou sem enfrentamento.
- Conferir se o modelo-base foi efetivamente preservado.
- Gerar o `.docx` apenas depois do gate formal valido.
- Reabrir o `.docx`.
- Conferir acentuacao, pontuacao e ausencia de mojibake.

# TEMPLATE_ENTRADA_PROCESSO_WEB

Copiar, preencher e colar no Codex web.

Se algum campo nao puder ser fechado com seguranca, escrever `nao identificado`.

```text
[INICIO_ENTRADA_PROCESSO_WEB]

IDENTIFICACAO_BASICA
- numero_processo:
- sistema: PJe / eproc-TJRJ / nao identificado
- classe_processual:
- orgao_judicial:
- fase_processual_aparente:

PARTES
- autor:
- reu:
- terceiros_relevantes:

PEDIDO_OU_TEMA_CENTRAL
- resumo_objetivo_do_caso:

ULTIMO_ATO_JUDICIAL_RELEVANTE
- data_se_houver:
- descricao_objetiva:

PETICOES_POSTERIORES
- listar uma a uma, da mais recente para a mais antiga:
- se nao houver certeza, indicar duvida expressamente:

PENDENCIAS_CONDICIONANTES
- custas:
- citacao:
- intimacao:
- replica:
- prova:
- pericia:
- cumprimento_de_determinacao:
- outra:

DOCUMENTOS_OU_TRECHOS_RELEVANTES
- transcrever apenas trechos necessarios para fechar a fase e o ato cabivel:

OBJETIVO_DESTA_ANALISE
- quero apenas diagnostico e gate:
- quero diagnostico e selecao de modelo:
- quero diagnostico, gate e minuta:

OBSERVACOES_DE_FIDELIDADE
- nao inventar fatos:
- nao saltar fase:
- nao redecidir ponto ja enfrentado sem causa processual:

[FIM_ENTRADA_PROCESSO_WEB]
```

## Saida esperada no primeiro uso

No primeiro teste no Codex web, pedir apenas:

1. sistema
2. fase processual exata
3. ultimo ato judicial relevante
4. peticoes posteriores relevantes
5. pendencia condicionante
6. ato cabivel agora
7. modelo-base mais aderente em `modelos`
8. gate preenchido em JSON com base em `templates\TEMPLATE_GATE_FLUXO_ESTRITO.json`

Sem minuta e sem `.docx`.

# AGENTS

Este projeto exige atuacao estritamente aderente ao acervo. Agentes, copilotos e automacoes devem operar com liberdade minima e fidelidade maxima.

## Principio central

Preservar integralmente o conteudo juridico ja consolidado no projeto. A funcao do agente e organizar, localizar, aplicar, parametrizar e executar o fluxo; nao reinventar o fluxo nem substituir a matriz juridica do gabinete.

## Regras obrigatorias

1. Fidelidade absoluta aos arquivos do projeto.
   Os documentos, modelos, blocos, comandos, skills e workflows do repositorio prevalecem sobre preferencias de estilo do agente.

2. Proibicao de inventar fatos juridicos ou processuais.
   O dossie e a unica fonte de fatos. Nunca inventar eventos, datas, manifestacoes, pedidos, incidentes, documentos, partes, numeros de processo ou cumprimento processual.

3. Obrigacao de identificar a fase processual antes de redigir.
   Nenhuma minuta pode ser produzida sem o fechamento da fase real, do ato cabivel e do ultimo ato judicial relevante.

4. Vedacao a redecisao indevida.
   O agente nao pode rediscutir tutela, gratuidade, custas, citacao, redistribuicao ou outro ponto ja decidido, salvo quando houver requerimento superveniente, descumprimento alegado, erro material, fato novo ou outra causa processualmente apta a reabrir o tema.

5. Vedacao a salto de fase.
   O agente deve sempre confirmar se o ato escolhido e realmente o proximo passo processual apos o ultimo ato relevante e as peticoes posteriores.

6. Necessidade de preservar o modelo-base aderente.
   Depois de selecionado o modelo-base exato, o agente deve manter sua macroestrutura, seu encadeamento e sua cadencia, alterando apenas o que o caso concreto exigir.

7. Obrigatoriedade de preflight.
   Antes de redigir, fechar formalmente:
   - sistema;
   - fase e ato cabivel;
   - ultimo ato relevante;
   - peticoes posteriores;
   - pendencia condicionante;
   - modelo-base exato.

8. Obrigatoriedade de postflight.
   Antes da entrega final, confirmar:
   - que a fase continua correta;
   - que nenhuma peticao posterior relevante foi ignorada;
   - que nao houve redecisao indevida;
   - que a macroestrutura do modelo foi preservada;
   - que o artefato final nao tem corrompimento de acentuacao.

9. Geracao de `.docx` somente apos gate formal valido.
   Quando a saida for operacional, a geracao depende de gate sidecar `.gate.json` valido, com `preflight_confirmado = true` e `postflight_confirmado = true`.

10. Reabertura final obrigatoria do `.docx`.
    O documento final deve ser reaberto e conferido quanto a acentuacao, coerencia textual e ausencia de mojibake.

11. Regra de minima liberdade de estilo.
    O agente nao deve "melhorar" a redacao por iniciativa propria quando houver modelo aderente. Fidelidade ao gabinete prevalece sobre limpeza estilistica.

12. Preservacao do conteudo juridico consolidado.
    Se houver duvida entre embelezar e preservar, preservar.

## Fluxo operacional minimo para agentes

1. Ler primeiro:
   - `00_LEIA_PRIMEIRO.md`
   - `docs\arquitetura\AUTOMACAO_REVISOR_PROCESSUAL.md`
   - `docs\arquitetura\CLAUDE.md`
   - `skills\revisor-base-tjrj\references\shared-rules.md`

2. Confirmar o sistema:
   - `PJe`
   - `eproc/TJRJ`

3. Fechar a fase exata do processo.

4. Levantar o ultimo ato judicial relevante.

5. Levantar todas as peticoes e incidentes posteriores.

6. Verificar se existe pendencia condicionante que impede o passo seguinte.

7. Selecionar o modelo-base exato, priorizando:
   - `modelos`
   - depois, se necessario, o acervo externo ou complementar previsto no fluxo

8. Consultar blocos reutilizaveis da familia, quando houver.

9. Redigir com aderencia maxima ao modelo escolhido.

10. Gerar o `.docx` somente com gate formal valido.

11. Reabrir e revisar o arquivo final.

## Proibicoes especificas

- Nao usar projetos laterais ou pastas estranhas como fonte.
- Nao usar saidas antigas como se fossem modelo-base.
- Nao tratar peticao posterior materialmente replica como se nao existisse.
- Nao reabrir replica ja esgotada em substancia.
- Nao tratar ausencia de dado como autorizacao para inferencia livre.
- Nao subir arquivos sensiveis, entradas reais de casos ou saidas finais geradas.

## Preferencias de trabalho no repositorio

- Conservar nomes e hierarquia sempre que possivel.
- Parametrizar caminhos absolutos em vez de apagar referencias operacionais.
- Tratar arquivos temporarios e saidas geradas como nao versionaveis por padrao.
- Atualizar documentacao sempre que a infraestrutura mudar.

## Regra final

Se houver choque entre a intuicao do agente e a documentacao canonicamente consolidada do projeto, prevalece a documentacao do projeto.

# Automacao Principal

Esta pasta consolida, em um unico lugar, o desenho mais atualizado da automacao do gabinete, agora organizado como repositorio versionavel e mais legivel para operacao por agentes.

## O que ficou melhor delimitado nos ajustes mais recentes

1. `core` juridico separado da operacao diaria
- O `core` do revisor ficou claramente concentrado nas regras, workflows e ferramentas do revisor processual.
- A operacao diaria ficou separada na execucao limpa, com pasta propria para entrada, saida e controle.

2. busca de modelos menos poluida
- A reducao de ruido ficou materializada no nucleo enxuto de modelos.
- O ponto de partida deixou de ser a floresta inteira de modelos e passou a ser uma curadoria pequena por tipo de ato e macrofamilia.

3. skills por camada, e nao por prompt unico
- Preprocessamento, revisor juridico, familias materiais, revisao de 2o grau e orquestracao ampla ficaram em blocos distintos.
- Isso reduz mistura de contextos e facilita manutencao.

4. revisao de 2o grau separada do fluxo de sentenca
- A revisao probatoria ficou delimitada como workflow proprio.
- A revisao de apelacao/tribunal simulado ficou delimitada como skill e workflow recursal.

5. automacao ampla separada do `core`
- O `core` continua independente.
- A automacao ampla orbita o `core` por orquestracao, sem redefinir suas regras internas.

## Estrutura desta pasta

- `docs\arquitetura`
  Regras-base e documentacao central do revisor.

- `docs\workflows`
  Workflows especializados do fluxo.

- `scripts`
  Ferramentas tecnicas permanentes.

- `02_EXECUCAO_OPERACIONAL`
  Estrutura limpa para rodar levas: controle, entrada e saida.

- `modelos`
  Nucleo operacional de modelos canonicos.

- `blocos`
  Blocos reutilizaveis por familia material.

- `skills`
  Espelho documental das skills atualmente usadas pela automacao.

- `comandos`
  Comandos consolidados para inicio.

- `templates`
  Templates operacionais, inclusive gate formal.

## O que foi deixado de fora de proposito

- `processos` antigos
- `pecas` antigas em `.md`
- `tmp`
- `lotes`
- saidas ja geradas de testes e rodadas anteriores

Esses itens existem como acervo historico nas pastas originais, mas nao ajudam a delimitar a arquitetura atual da automacao.

## Observacao importante

Esta pasta organiza a automacao em um hub unico, mas a registracao viva das skills ainda continua em:

`C:\Users\Oswaldo-Nitro\.codex\skills`

Por isso, a pasta `skills` deve ser lida como espelho organizado e documentacao consolidada, nao como substituicao automatica da carga nativa do Codex.

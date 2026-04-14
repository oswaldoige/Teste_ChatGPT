# Mapa da Automacao Atual

## 1. Core juridico

Origem principal consolidada em:

- `docs\arquitetura`
- `docs\workflows`
- `scripts`

Conteudo central:
- `docs\arquitetura\CLAUDE.md`
- `docs\arquitetura\AUTOMACAO_REVISOR_PROCESSUAL.md`
- `docs\arquitetura\ARQUITETURA_AUTOMACAO_AMPLA.md`
- `docs\arquitetura\AUTOMACAO_AMPLA_GABINETE.md`
- `scripts\make_docx.py`
- `scripts\summarize_triage.py`
- `docs\workflows\revisao-probatoria.md`
- `docs\workflows\revisao-apelacao.md`

Funcao:
- ler `json`
- escolher o ato
- buscar modelos
- redigir minutas
- gerar `.docx`
- revisar sentencas em 2o grau quando o fluxo pedir

## 2. Operacao limpa

Origem consolidada em:

`02_EXECUCAO_OPERACIONAL`

Funcao:
- receber a leva da rodada
- guardar o comando de inicio
- separar entrada de `json` e saida de `.docx`
- evitar mistura com testes e arquivos temporarios
- manter como destino fisico preferencial dos `.docx` a pasta local `C:\Users\Oswaldo-Nitro\Documents\AUTOMACAO_PRINCIPAL_LOCAL\saida_docx`, deixando o OneDrive apenas como espelho opcional

## 3. Modelos enxutos

Origem consolidada em:

`modelos`

Funcao:
- ser o primeiro ponto de busca de modelos
- reduzir ruido
- organizar por:
  - tutela
  - saneador
  - sentenca
  - blocos reutilizaveis
- e por macrofamilia:
  - consumidor
  - civel contratual
  - Fazenda Publica

## 4. Skills espelhadas

Origem consolidada em:

`skills`

Funcao:
- concentrar o mapa real das skills hoje usadas pela automacao
- separar:
  - preprocessing
  - core juridico
  - roteamento/familia
  - 2o grau
  - orquestracao ampla

## 5. Delimitacao que guiou esta consolidacao

Foi mantido:
- o que hoje eh estrutura
- o que reflete os ajustes mais recentes
- o que reduz ambiguidade operacional

Foi omitido:
- acervo historico de saida
- arquivos temporarios
- rodadas antigas
- rascunhos antigos em `.md`

## 6. Regra pratica de leitura

Se a pergunta for "qual eh a automacao hoje?", a ordem correta para ler esta pasta eh:

1. `00_LEIA_PRIMEIRO.md`
2. `docs\arquitetura`
3. `docs\workflows`
4. `scripts`
5. `02_EXECUCAO_OPERACIONAL`
6. `modelos`
7. `blocos`
8. `skills`
9. `comandos`

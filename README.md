# AUTOMACAO_PRINCIPAL

Repositorio operacional da automacao principal do gabinete para leitura de dossies, classificacao da fase processual, selecao de modelo-base aderente e geracao controlada de minutas em `.docx`, com gate formal de fluxo estrito.

O objetivo deste repositorio e preservar e versionar a infraestrutura da automacao sem reinventar a logica juridica ja consolidada no acervo. O conteudo juridico-material continua ancorado nas regras, workflows, skills e modelos ja existentes no projeto.

## Visao geral do projeto

O fluxo observado no acervo hoje se apoia em seis pilares:

1. `docs\arquitetura`
   Contem a documentacao central do revisor processual e da arquitetura consolidada.
2. `docs\workflows`
   Reunem os workflows especializados do fluxo.
3. `scripts`
   Reunem as ferramentas tecnicas permanentes do projeto.
4. `02_EXECUCAO_OPERACIONAL`
   Isola a operacao diaria em entrada, controle e saida.
5. `modelos` e `blocos`
   Reunem o nucleo operacional de modelos canonicos e os blocos reutilizaveis.
6. `skills`
   Mantem o espelho documental das skills usadas pela automacao.

Os comandos-base foram concentrados em `comandos`.

## Logica do fluxo principal

O fluxo real do projeto, conforme a documentacao consolidada e os arquivos operacionais encontrados, pode ser resumido assim:

1. Receber um ou mais dossies `.json`.
2. Aplicar o fechamento do gate de fluxo estrito antes de qualquer redacao.
3. Identificar o sistema, a fase processual exata, o ultimo ato relevante, as peticoes posteriores e eventual pendencia condicionante.
4. Selecionar o modelo-base exato, priorizando `modelos`.
5. Redigir a minuta com fidelidade maxima ao modelo-base aderente e aos blocos reutilizaveis da familia.
6. Validar preflight e postflight.
7. Gerar o `.docx` por meio do script `make_docx.py`, somente apos gate formal valido.
8. Reabrir o arquivo final para conferenciar acentuacao, coerencia e ausencia de corrompimento de encoding.

## Estrutura atual de pastas

```text
AUTOMACAO_PRINCIPAL/
  00_LEIA_PRIMEIRO.md
  02_EXECUCAO_OPERACIONAL/
    controle/
    entrada_json/
    revisao_probatoria/
    saida_docx/
  blocos/
  comandos/
  docs/
    arquitetura/
    workflows/
  entrada_exemplos/
  modelos/
  saida_docx/
  scripts/
  skills/
  templates/
```

Pontos de referencia importantes:

- Regras centrais: `docs\arquitetura\AUTOMACAO_REVISOR_PROCESSUAL.md`
- Comando-base estrito: `comandos\COMANDO_PADRAO_CIVEL_ESTRITO.txt`
- Gate formal: `templates\TEMPLATE_GATE_FLUXO_ESTRITO.json`
- Geracao de `.docx`: `scripts\make_docx.py`
- Sumario de triagem: `scripts\summarize_triage.py`

## Como preparar o ambiente

O projeto depende de Python e das bibliotecas listadas em `requirements.txt`, em especial:

- `python-docx`
- `pdfplumber`
- `pytesseract`
- `pdf2image`

A parametrizacao principal dos scripts permanentes ja foi feita. Ainda assim, a orientacao segura e:

1. Criar um ambiente virtual local.
2. Instalar as dependencias Python exigidas pelos scripts efetivamente usados.
3. Conferir a disponibilidade local do `Tesseract OCR` e do `Poppler`, quando houver uso do pipeline PDF -> JSON.
4. Evitar usar o OneDrive como destino principal de arquivos finais quando houver pasta local fisica preferencial configurada.

## Como rodar

O acionamento operacional do revisor parte dos comandos consolidados em:

- `comandos\COMANDO_CORE.txt`
- `comandos\COMANDO_PADRAO_CIVEL.txt`
- `comandos\COMANDO_PADRAO_CIVEL_ESTRITO.txt`
- `02_EXECUCAO_OPERACIONAL\controle\COMANDO_OFICIAL.txt`

Uso pratico observado:

1. Separar a rodada em `02_EXECUCAO_OPERACIONAL\entrada_json`.
2. Iniciar a execucao com o comando-base apropriado.
3. Fechar o gate estrito antes da minuta.
4. Produzir a minuta fonte.
5. Gerar o `.docx` apenas depois da validacao formal.

## Como gerar o gate

O gate formal usa como base:

`templates\TEMPLATE_GATE_FLUXO_ESTRITO.json`

Campos nucleares observados no template:

- `sistema`
- `fase_e_ato_cabivel`
- `ultimo_ato_relevante`
- `peticoes_posteriores`
- `pendencia_condicionante`
- `modelo_base_path`
- `preflight_confirmado`
- `postflight_confirmado`

Sem esse fechamento, a geracao de `.docx` para a saida operacional deve ser recusada.

## Como gerar o .docx

O script principal de geracao identificado no acervo e:

`scripts\make_docx.py`

Comportamento relevante observado:

- exige gate sidecar `.gate.json` quando a saida for para `saida_docx`;
- valida sinais de corrompimento de acentuacao;
- grava o arquivo final em formato `.docx`.

Antes de usar o script em outra maquina, revise os caminhos absolutos ainda existentes no projeto. Essa parametrizacao sera tratada na fase tecnica do preparo para GitHub.

## Quais arquivos sao entrada

Entradas operacionais principais:

- dossies `.json` em `02_EXECUCAO_OPERACIONAL\entrada_json`
- minuta fonte correspondente ao provimento
- gate sidecar `.gate.json`

Entradas auxiliares:

- modelos canonicos em `modelos`
- blocos reutilizaveis em `blocos`
- regras e skills espelhadas em `docs\arquitetura`, `docs\workflows` e `skills`

## Quais arquivos sao saida

Saidas finais:

- `.docx` gerados em `saida_docx`

Saidas intermediarias e artefatos de rodada:

- gates gerados
- minutas intermediarias em `.md` ou `.txt`
- arquivos temporarios em `controle\temp` e `tmp`

Esses artefatos intermediarios nao devem ser tratados como acervo canonicamente versionado.

## Cuidados para nao quebrar o fluxo

- Nao inventar fatos juridicos nem reescrever regras consolidadas por estilo.
- Nao redigir antes de identificar a fase processual real.
- Nao gerar `.docx` sem gate formal valido.
- Nao alterar a macroestrutura de modelos canonicos sem necessidade concreta.
- Nao confundir modelos canonicos com saidas geradas de rodadas anteriores.
- Nao subir ao repositorio dados reais de processos, saidas finais de casos ou artefatos temporarios.
- Nao depender de caminhos absolutos de uma unica maquina; prefira parametrizacao.
- Reabrir sempre o `.docx` final para conferenciar acentuacao e coerencia.

## Fontes canonicamente mais relevantes

- `00_LEIA_PRIMEIRO.md`
- `docs\arquitetura\AUTOMACAO_REVISOR_PROCESSUAL.md`
- `docs\arquitetura\CLAUDE.md`
- `skills\revisor-base-tjrj\references\shared-rules.md`
- `docs\arquitetura\MAPA_AUTOMACAO_ATUAL.md`

## Estado do repositorio

Este repositorio esta sendo preparado para versionamento no GitHub. Durante essa transicao, a prioridade e preservar o fluxo real do acervo, limpar o versionamento e documentar os pontos de entrada, sem alterar a logica juridica/material consolidada.

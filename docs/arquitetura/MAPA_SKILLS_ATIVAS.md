# Mapa das Skills Ativas

Total espelhado nesta pasta: `19` skills.

## Preprocessamento

- `download-pje-tjrj`
  Baixa PDFs de processos no PJe.

- `download-eproc-tjrj`
  Baixa PDFs de processos no eproc.

- `pdf-json-triagem-tjrj`
  Converte PDFs em `.triagem.json`.

- `preprocessamento-processos-tjrj`
  Encadeia download + conversao antes do revisor.

## Core juridico

- `revisor-base-tjrj`
  Regras transversais do revisor, rastreabilidade, PT-BR, `.docx` e validacao final.

- `analise-iniciais-tjrj`
  Atos iniciais.

- `tutela-urgencia-tjrj`
  Tutelas, liminares, reconsideracoes e descumprimento.

- `saneador-tjrj`
  Decisoes saneadoras.

- `sentenca-civel-tjrj`
  Sentencas civeis.

- `validacao-juris-sentenca-tjrj`
  Terceira versao da sentenca com jurisprudencia oficial.

- `cumprimento-sentenca-tjrj`
  Fase de cumprimento e execucao.

- `registro-padroes-sentenca-tjrj`
  Cataloga hipoteses recorrentes e consolida novas matrizes de sentenca no nucleo operacional.

## Roteamento e familias

- `roteamento-modelos-tjrj`
  Prioriza o nucleo operacional reduzido de modelos.

- `familia-consumidor-tjrj`
  Mantem a arquitetura consumerista.

- `agua-esgoto-reiteracao-tjrj`
  Aciona a matriz padrao para sentencas de agua e esgoto com nova cobranca excessiva na mesma unidade ja litigada antes.

- `familia-civel-contratual-tjrj`
  Mantem a arquitetura civel contratual.

- `familia-fazenda-publica-tjrj`
  Mantem a arquitetura de Fazenda Publica.

## Segundo grau

- `tribunal-simulado-apelacao-tjrj`
  Simula revisao de apelacao com base oficial de STF, STJ e TJRJ.

Observacao:
- a revisao probatoria, hoje, esta delimitada como workflow e nao como skill separada.

## Camada ampla

- `orquestrador-gabinete-tjrj`
  Coordena a automacao ampla sem substituir o `core`.

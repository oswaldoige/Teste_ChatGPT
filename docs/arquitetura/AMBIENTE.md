# AMBIENTE DE EXECUCAO

Este documento define como a automacao resolve caminhos operacionais e o que muda
quando ela roda fora da maquina do gabinete. Ele nao altera nenhuma regra juridica
do `core`. Trata apenas de infraestrutura.

## Por que existe

A documentacao canonica do projeto foi escrita para a maquina local, com caminhos
absolutos do OneDrive do Tribunal. Esses caminhos continuam sendo a referencia
operacional correta, mas nao existem quando a automacao roda na nuvem, pelo
GitHub. Em vez de apagar as referencias, elas foram parametrizadas, conforme a
preferencia ja registrada em `AGENTS.md`.

## Variaveis operacionais

- `${GABINETE_RAIZ_2026}`
  Raiz do acervo de trabalho de 2026. Local: a pasta `2026` do OneDrive do
  Tribunal. Dela descendem `AUTOMACAO_MODELOS`, a curadoria reduzida em
  `00_PRIORITARIOS_AUTOMACAO`, o `NUCLEO 4.0`, `modelos_variados` e `2a_civel`.

- `${GABINETE_SKILLS}`
  Registracao viva das skills. Local: a pasta de skills do Codex. No repositorio,
  a pasta `skills` e o espelho documental correspondente.

- `${GABINETE_SAIDA}`
  Destino das minutas `.docx` geradas.

## Resolucao

`scripts/ambiente.py` resolve cada variavel nesta ordem:

1. variavel de ambiente de mesmo nome;
2. chave correspondente em `config/ambiente.json`, quando o arquivo existir;
3. valor padrao do ambiente detectado.

A deteccao do ambiente e feita pela existencia real do acervo do OneDrive, e nao
pelo sistema operacional. Outra maquina Windows, sem o acervo sincronizado, e
tratada como ambiente sem acervo.

Para conferir a resolucao vigente:

```
python scripts/ambiente.py
```

## Diferenca material entre os dois ambientes

Na maquina do gabinete o acervo amplo esta disponivel, e a busca de modelo segue
integralmente o fluxo do `core`: curadoria reduzida primeiro, depois as pastas
especializadas, depois o acervo correlato.

Na nuvem o acervo amplo nao existe. O unico material disponivel e o nucleo curado
versionado em `modelos`, com os blocos reutilizaveis em `blocos`. Isso tem duas
consequencias de observancia obrigatoria:

1. A etapa de busca ampla nao pode ser simulada. Se nenhum modelo canonico do
   nucleo for aderente ao ato, a limitacao deve ser declarada na entrega, e nao
   suprida por redacao autoral do agente. A regra 6 do `AGENTS.md`, de preservacao
   do modelo-base, nao admite substituicao por parafrase quando o modelo apenas
   nao esta ao alcance.

2. Atos cujo modelo-base nao esteja no nucleo curado devem ser redigidos na
   maquina local, ou o modelo correspondente deve ser previamente incorporado ao
   nucleo. O despacho inicial de procedimento comum e o exemplo mais frequente:
   seu modelo-base vive na curadoria reduzida, fora do repositorio.

## Indice de modelos

`scripts/indexar_modelos.py` varre as raizes disponiveis no ambiente e grava
`config/indice_modelos.json`, com nome, pasta tematica, caminho e data de cada
modelo. O indice nao e versionado, por conter caminhos da maquina local, e deve
ser regerado quando o acervo mudar.

A busca ordena por aderencia ao termo e, em empate, pela data de modificacao,
atendendo a preferencia pelos modelos mais recentes. O objetivo e permitir a
leitura de um unico modelo-base por minuta, em vez do carregamento do acervo.

## Dados sensiveis

O ambiente de nuvem executa em container efemero e o repositorio e remoto. Nada
de entrada real de caso deve ser versionado: dossies, PDFs de autos e minutas
geradas continuam cobertos pelo `.gitignore` e permanecem fora do repositorio.

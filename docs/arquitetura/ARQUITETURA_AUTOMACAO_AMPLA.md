# Arquitetura da Automacao Ampla

Objetivo: subir um degrau na automacao sem alterar nem sobrepor a automacao atual do revisor processual, que permanece como nucleo estavel (`core`).

## Regra de Ouro

- A automacao atual do `revisor-processual-tjrj` continua sendo o `core`.
- A futura automacao ampla deve orbitar esse `core`, e nao substitui-lo.
- Qualquer ampliacao deve ocorrer por camada externa de orquestracao.
- O comando do `core` continua valido e independente.
- O comando da automacao ampla sera separado.

## Arquitetura Proposta

### 1. Core estavel

Componente:
- `revisor-processual-tjrj`

Responsabilidade:
- ler dossies JSON;
- buscar modelos;
- escolher o ato processual adequado;
- redigir despachos, decisoes e sentencas;
- gerar `.docx`;
- nas sentencas, gerar versao completa, versao concisa e versao validada jurisprudencialmente.

Regra:
- esse `core` nao deve ser redefinido pela automacao ampla;
- ajustes nele so ocorrem por determinacao expressa do usuario.

### 2. Automacao ampla futura

Componente sugerido:
- `orquestrador-gabinete-tjrj`

Responsabilidade:
- coordenar etapas anteriores e posteriores ao `core`;
- decidir quando acionar o revisor processual;
- agregar outras rotinas sem contaminar o fluxo do revisor.

Exemplos de uso futuro:
- triagem macro de novos arquivos;
- separacao por materia, gabinete ou fila;
- disparo do `core` apenas nos processos aptos;
- consolidacao de relatorios de producao;
- validacoes administrativas externas ao texto do provimento.

Regra:
- a automacao ampla pode chamar o `core`, mas nao pode reescrever sua identidade, suas regras-base ou sua saida obrigatoria.

### 3. Automacoes satelites opcionais

Componente:
- automacoes auxiliares independentes, quando necessario

Exemplos:
- download de processos;
- organizacao de fila;
- consolidacao de planilhas;
- classificacao previa de acervo.

Regra:
- automacoes satelites nao entram como fonte de redacao do `core`, salvo autorizacao expressa.

## Contrato entre a automacao ampla e o core

Quando a automacao ampla usar o `revisor-processual-tjrj`, ela deve apenas:
- informar a pasta ou os arquivos que devem ser analisados;
- informar filtros ou prioridades legitimas;
- receber de volta os provimentos gerados.

Ela nao deve:
- trocar os modelos-base do `core` sem comando expresso;
- alterar a logica juridica do `core`;
- mudar a nomenclatura essencial das pecas;
- mudar a regra de saida de sentencas;
- suprimir a terceira versao validada das sentencas;
- misturar instrucoes de outros projetos no fluxo do revisor.

## Comandos separados

### Comando do core

```text
Executar automacao revisor. Use apenas as skills do revisor-processual-tjrj, ignore qualquer outra automacao/projeto, analise somente os arquivos .json da pasta que eu indicar, busque modelos em C:\Users\Oswaldo-Nitro\OneDrive - Tribunal de Justica do Estado do Rio de Janeiro\2026\AUTOMACAO_MODELOS e gere os provimentos finais em .docx.
```

### Comando reservado para a automacao ampla

```text
Executar automacao ampla do gabinete. Use apenas a camada orquestradora da automacao ampla, preserve integralmente o core revisor-processual-tjrj, acione o core somente nas etapas de analise processual e elaboracao de minutas, e nao altere suas regras internas sem minha autorizacao expressa.
```

## Regra de implementacao futura

- a automacao ampla deve nascer em arquivo, skill e comando proprios;
- o `core` nao deve ser renomeado nem absorvido por ela;
- toda nova logica ampla deve ser adicionada fora do `revisor-processual-tjrj`;
- se houver conflito entre a automacao ampla e o `core`, prevalece o `core` ate nova decisao expressa do usuario.

## Estado atual

- `core`: implementado e em uso;
- automacao ampla: implementada como skill separada `orquestrador-gabinete-tjrj`, sem absorver nem redefinir o `core`.

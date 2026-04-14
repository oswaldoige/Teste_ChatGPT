# Contrato com o Core

## Core protegido

O `revisor-processual-tjrj` e o nucleo juridico estavel.

O orquestrador pode:
- identificar filas, lotes e escopo;
- separar arquivos ou grupos de processos;
- decidir quando acionar o `core`;
- consolidar resultados e organizar a producao.

O orquestrador nao pode:
- mudar a logica juridica do `core`;
- trocar a biblioteca de modelos do `core` sem ordem expressa;
- alterar o padrao de saida do `core`;
- suprimir a versao validada das sentencas;
- misturar regras de outros projetos no fluxo do revisor.

## Regra de acionamento do core

Quando a atividade exigir provimento jurisdicional:
- acionar o `core`;
- manter o comando judicial dentro do fluxo do `revisor-processual-tjrj`;
- voltar ao orquestrador apenas depois da entrega do ato.

## Separacao de identidade

- `orquestrador-gabinete-tjrj` = camada ampla
- `revisor-processual-tjrj` = nucleo juridico

Uma camada nao substitui a outra.

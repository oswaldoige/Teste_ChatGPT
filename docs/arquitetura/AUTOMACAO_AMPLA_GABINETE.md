# Automacao Ampla do Gabinete

Este arquivo registra a camada ampla, separada do `core` do revisor processual.

## Estado atual

- `revisor-processual-tjrj`: nucleo estavel, em producao
- `orquestrador-gabinete-tjrj`: camada ampla implementada como skill separada

## Regra principal

A automacao ampla existe para coordenar o trabalho em volta do `core`.

Ela nao substitui:
- a analise juridica do `core`
- a busca de modelos do `core`
- a logica processual do `core`
- a saida obrigatoria do `core`

## Skill da camada ampla

Skill:
- `${GABINETE_SKILLS}\orquestrador-gabinete-tjrj`

## Comando oficial da automacao ampla

```text
Executar automacao ampla do gabinete. Use apenas $orquestrador-gabinete-tjrj como camada orquestradora, preserve integralmente o core revisor-processual-tjrj, acione o core somente nas etapas de analise processual e elaboracao de minutas, use os arquivos .json da pasta que eu indicar e nao altere as regras internas do core sem minha autorizacao expressa.
```

## Comando oficial do core

```text
Executar automacao revisor. Use apenas as skills do revisor-processual-tjrj, ignore qualquer outra automacao/projeto, analise somente os arquivos .json da pasta que eu indicar, busque modelos em ${GABINETE_ACERVO} e gere os provimentos finais em .docx.
```

## Regra de convivencia

- automacao ampla e `core` coexistem;
- a automacao ampla pode chamar o `core`;
- o `core` nao depende da automacao ampla para funcionar;
- se houver conflito, prevalece o `core`, salvo ordem expressa do usuario.

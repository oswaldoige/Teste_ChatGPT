# Fluxo de Orquestracao

## Passo 1 - Definir escopo

Antes de agir, identificar se o pedido e:
- apenas revisor processual;
- apenas tarefa satelite;
- fluxo amplo misto.

## Passo 2 - Separar etapas

Separar o trabalho em:
- etapa de preparacao
- etapa de analise/minuta judicial
- etapa posterior de consolidacao

Somente a etapa de analise/minuta judicial pertence ao `core`.

## Passo 3 - Acionar a skill correta

### Se o ato final for judicial

Usar:
- `$revisor-base-tjrj`
- `$analise-iniciais-tjrj`, `$tutela-urgencia-tjrj`, `$saneador-tjrj`, `$sentenca-civel-tjrj` ou `$cumprimento-sentenca-tjrj`, conforme a fase
- `$validacao-juris-sentenca-tjrj` quando houver sentenca

### Se a etapa for satelite

Executar fora do `core`, sem contaminar a redacao das pecas.

## Passo 4 - Consolidar

Depois da etapa judicial:
- reunir arquivos gerados;
- conferir faltantes;
- devolver o status do lote ou da fila.

## Regra de seguranca

Se houver duvida entre ampliar o `core` ou resolver por orquestracao externa, escolher sempre a orquestracao externa.

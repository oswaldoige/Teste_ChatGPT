---
name: nucleo4-replica-agua-esgoto-tjrj
description: Use when a 3o Nucleo de Justica 4.0 water-and-sewer case already has contestation after redistribution and a later petition alleging cumprimento da tutela, so the next act must follow the approved replica-pattern decision of the Nucleo instead of a generic despacho, premature saneador, or sentence.
---

# Nucleo4 Replica Agua Esgoto TJRJ

## Quando usar

- Quando o processo do 3o Nucleo 4.0 ja tiver contestacao apos a redistribuicao.
- Quando houver peticao posterior da re alegando cumprimento da tutela deferida na origem.
- Quando ainda nao houver replica da parte autora ou quando a fase correta ainda for completar esse contraditorio.

## O que esta skill faz

- Puxa o padrao aprovado de decisao de replica do Nucleo 4.0.
- Evita salto indevido para sentenca, saneador ou despacho generico.
- Obriga a manter a sequencia operacional do gabinete: redistribuicao, decisoes da origem, anotacao de patrono, `+Acordo`, replica, manifestacao sobre cumprimento da tutela e especificacao de provas.
- Obriga a tratar as decisoes anteriores apenas como ciencia e contexto, sem redecidir tutela, custas, citacao, redistribuicao ou outros pontos ja resolvidos, salvo se houver erro, fato superveniente, novo pedido ou necessidade concreta de reconsideracao.
- Obriga tambem a verificar se alguma decisao anterior deixou pendencia procedimental autonoma ainda nao resolvida, como complementacao de custas sob o art. 290 do CPC, antes de abrir simples replica como se o feito estivesse regularizado.

## Fluxo curto

1. Aplicar `$revisor-base-tjrj`.
2. Confirmar que o processo e do 3o Nucleo 4.0 e que a materia e agua/esgoto.
3. Verificar se ja existe contestacao apos a redistribuicao e se ha peticao posterior alegando cumprimento da tutela.
4. Ler o roteiro curto desta skill e o bloco reutilizavel correspondente.
5. Redigir a decisao no padrao aprovado, com numeracao enxuta e linguagem do nucleo.
6. So apos a replica e a especificacao de provas reavaliar se o caso segue para saneador ou sentenca.

## Fontes obrigatorias desta skill

- Roteiro:
  `skills\nucleo4-replica-agua-esgoto-tjrj\references\roteiro.md`
- Bloco reutilizavel:
  `blocos\01_CONSUMIDOR\BLOCO 06 - DECISAO - NUCLEO 4.0 - REPLICA POS CONTESTACAO E ALEGACAO DE CUMPRIMENTO TUTELA.txt`

## Guardrails

- Nao substituir essa decisao por despacho generico de impulso.
- Nao pular direto para saneador enquanto ainda faltar replica da autora sobre a contestacao e sobre o alegado cumprimento da tutela.
- Nao omitir o bloco `+Acordo` quando a estrutura do Nucleo o comportar.
- Nao esquecer de enfrentar pedido de anotacao de patrono quando houver.
- Nao redecidir, por simples repeticao narrativa, questoes ja enfrentadas em decisoes anteriores. Quando o ponto ja estiver resolvido e nao houver reabertura concreta, a redacao deve apenas registrar ciencia do ato anterior e seguir para o verdadeiro impulso pendente.
- Nao ignorar pendencia procedimental expressamente aberta por decisao anterior. Se houver ordem de complementacao de custas, emenda, regularizacao ou providencia condicionante sem comprovacao clara de cumprimento no dossie, a minuta deve enfrentar esse ponto antes de impulsionar a fase seguinte.

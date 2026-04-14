---
name: nucleo4-saneamento-provas-tjrj
description: Use when a 3o Nucleo de Justica 4.0 water-and-sewer case already has contestation and replica and the correct next act is a short saneador opening the evidentiary phase, preferably on the approved `EM - PROVAS - COM - SANEAMENTO` matrix.
---

# Nucleo4 Saneamento Provas TJRJ

## Quando usar

- Quando o processo do 3o Nucleo 4.0 ja tiver contestacao e replica.
- Quando o contraditorio minimo ja estiver formado, mas ainda nao for caso de sentenca.
- Quando a fase correta for organizar a prova e fixar os pontos controvertidos.

## O que esta skill faz

- Puxa o modelo aprovado `EM - PROVAS - COM - SANEAMENTO` como matriz principal.
- Mantem o saneador curto e fiel ao estilo do Nucleo 4.0.
- Obriga a resolver a preliminar real, fixar pontos controvertidos concretos e abrir a fase de provas com disciplina.
- Evita despacho generico, pseudo-saneador prolixo e repeticao desnecessaria de comandos ja decididos.
- Obriga a verificar se pedido de anotacao de patrono ja esta satisfeito no sistema, para nao determinar nova anotacao inutil.

## Fluxo curto

1. Aplicar `$revisor-base-tjrj`.
2. Confirmar que o processo e do 3o Nucleo 4.0 e que a materia e agua/esgoto.
3. Confirmar que contestacao e replica ja existem.
4. Abrir o roteiro desta skill e o modelo `EM - PROVAS - COM - SANEAMENTO`.
5. Redigir saneador curto no ritmo do paradigma.
6. Gerar as versoes completa e concisa em `.docx`.

## Fontes obrigatorias desta skill

- Roteiro:
  `skills\nucleo4-saneamento-provas-tjrj\references\roteiro.md`
- Modelo-base:
  localizar em `C:\Users\Oswaldo-Nitro\OneDrive - Tribunal de Justica do Estado do Rio de Janeiro\2026\AUTOMACAO_MODELOS` o arquivo `90 - EXEMPLO - EM - PROVAS - COM - SANEAMENTO.docx`, priorizando a pasta `NÚCLEO 4.0`

## Guardrails

- Nao usar esse fluxo se ainda faltar replica.
- Nao alongar o saneador com relatorio ou fundamentacao fora do paradigma.
- Nao redecidir tutela, custas, gratuidade ou redistribuicao sem fato novo.
- Nao mandar anotar patrono se ele ja estiver devidamente cadastrado.

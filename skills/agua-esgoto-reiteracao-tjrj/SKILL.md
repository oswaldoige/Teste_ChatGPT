---
name: agua-esgoto-reiteracao-tjrj
description: Use when a TJRJ consumer sentence concerns new excessive water or sewer bills in the same unit already litigated before, especially with historical-average refaturamento, generic defense from the concessionaire, possible parcelamento compulsorio, service cut, repetition of overpayment, and moral damages.
---

# Agua Esgoto Reiteracao TJRJ

## Quando usar

- Quando o processo tratar de novas contas excessivas de agua/esgoto na mesma matricula ja discutida em demanda anterior.
- Quando a autora invocar processo preterito como reforco de recorrencia da anomalia, mas as competencias agora discutidas forem novas.
- Quando houver pedido de refaturamento pela media historica, repeticao do indebito e dano moral, com ou sem parcelamento compulsorio e corte indevido do servico.

## O que esta skill faz

- Puxa a matriz canonica dessa subfamilia antes da redacao.
- Obriga a manter a frase-pivo `A controversia central da lide reside...`.
- Obriga a tratar a sentenca anterior apenas como reforco contextual ou de recorrencia, sem transformar automaticamente suas premissas em coisa julgada sobre competencias novas.
- Obriga a trabalhar o onus concreto da concessionaria pelo artigo 373, II, do CPC, sem escrever como se a sentenca estivesse deferindo originariamente a inversao do onus da prova.
- Reaproveita o bloco estavel de fundamentacao quando a hipotese se repetir.
- Puxa tambem o bloco padrao de dispositivo e consectarios desta subfamilia quando o caso estiver integralmente no regime posterior a 30/08/2024.

## Fluxo curto

1. Ler o registro recorrente da familia consumidor.
2. Abrir o modelo canonico e os blocos reutilizaveis desta hipotese.
3. Verificar se o caso concreto tem apenas novas contas excessivas ou se tambem houve corte, religacao tardia e parcelamento compulsorio.
4. Redigir a sentenca com a mesma cadencia do paradigma aprovado, modulando apenas os fatos, as competencias impugnadas e os consectarios concretos.
5. Se a hipotese evoluir de forma estavel, acionar a skill `registro-padroes-sentenca-tjrj` para atualizar o registro e o modelo.

## Fontes obrigatorias desta skill

- Registro recorrente:
  `modelos\03_SENTENCA\01_CONSUMIDOR\REGISTRO_HIPOTESES_RECORRENTES_CONSUMIDOR.md`
- Modelo canonico:
  `modelos\03_SENTENCA\01_CONSUMIDOR\CANONICO 07 - SENTENCA - CONSUMIDOR - AGUA E ESGOTO - REITERACAO POS PROCESSO ANTERIOR.docx`
- Bloco reutilizavel de fundamentacao:
  `blocos\01_CONSUMIDOR\BLOCO 04 - SENTENCA - CONSUMIDOR - AGUA E ESGOTO - REITERACAO POS PROCESSO ANTERIOR.txt`
- Bloco de dispositivo e consectarios:
  `blocos\01_CONSUMIDOR\BLOCO 05 - DISPOSITIVO - CONSUMIDOR - AGUA E ESGOTO - POS LEI 14905.txt`

## Guardrails

- Nao reescrever a arquitetura da sentenca do zero se o caso couber nessa subfamilia.
- Nao escrever que a sentenca esta deferindo inversao do onus da prova.
- Nao confundir a recorrencia do problema com extensao automatica da coisa julgada material do processo anterior.
- Se houver corte indevido do fornecimento, tratar o dano moral dentro da logica de servico essencial e desvio produtivo, sem cair em redacao generica.
- Preferir dispositivo segmentado: refaturamento, nulidade do parcelamento, repeticao do indebito e dano moral em itens proprios, com consectarios autonomos e formula enxuta do art. 406, paragrafo 1o, do Codigo Civil.

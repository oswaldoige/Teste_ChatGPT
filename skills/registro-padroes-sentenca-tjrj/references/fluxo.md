# Fluxo De Registro De Padroes

## Quando registrar

- Quando o usuario aprovar uma nova matriz de sentenca e pedir reaproveitamento futuro.
- Quando a controversia de um novo processo for materialmente semelhante a uma familia recorrente, mas ainda nao houver registro proprio no nucleo operacional.
- Quando um modelo canonico existente deixar de ser suficiente porque surgiu subfamilia repetitiva com fatos e dispositivo distintivos.

## Onde gravar

- Skill:
  `skills\registro-padroes-sentenca-tjrj`
- Registro recorrente da familia consumidor:
  `modelos\03_SENTENCA\01_CONSUMIDOR\REGISTRO_HIPOTESES_RECORRENTES_CONSUMIDOR.md`
- Modelos canonicos:
  `modelos\03_SENTENCA`
- Blocos reutilizaveis:
  `blocos`

## Arvore de decisao

1. Ha modelo canonico ja aderente?
   - Sim: reutilizar o modelo e, no maximo, atualizar o registro com nova observacao.
   - Nao: ir para 2.
2. A diferenca esta apenas em um paragrafo estavel de fundamentacao ou dispositivo?
   - Sim: criar ou atualizar bloco reutilizavel.
   - Nao: ir para 3.
3. A nova hipotese tem alta chance de repeticao ou foi expressamente sinalizada pelo usuario como padrao?
   - Sim: criar nova entrada no registro e novo modelo canonico.
   - Nao: apenas anotar no registro como variacao contextual de hipotese ja existente.

## Regra de qualidade

- Nao criar modelo novo por mera troca de nomes, datas ou pequenos ajustes de consequencias.
- Nao apagar modelo antigo sem substituicao clara.
- Nao registrar hipotese sem dizer, objetivamente, do que ela trata.
- Sempre vincular a hipotese a pelo menos um processo-exemplo ou paradigma aprovado.

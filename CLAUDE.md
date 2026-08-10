# CLAUDE.md

Ponto de carga do projeto. Este arquivo nao redefine o `core` do revisor
processual: ele apenas garante que o `core` seja efetivamente carregado e resolve
o ambiente de execucao. Em caso de conflito, prevalece a documentacao canonica.

## Leitura obrigatoria antes de qualquer minuta

1. `00_LEIA_PRIMEIRO.md`
2. `AGENTS.md`
3. `docs/arquitetura/CLAUDE.md` - persona, regras e checagens do `core`
4. `docs/arquitetura/AMBIENTE.md` - resolucao de caminhos e limites do ambiente
5. `skills/revisor-base-tjrj/references/shared-rules.md`

A pasta `skills` e o espelho documental das skills do gabinete. Ela nao e
carregada automaticamente: a skill pertinente ao ato deve ser lida sob demanda,
a partir do `SKILL.md` da pasta correspondente.

## Ambiente

Caminhos operacionais aparecem na documentacao como `${GABINETE_RAIZ_2026}`,
`${GABINETE_SKILLS}` e `${GABINETE_SAIDA}`. Antes de buscar modelo, resolver o
ambiente com `python scripts/ambiente.py`.

Quando o acervo amplo estiver indisponivel, o nucleo curado em `modelos` e o
unico ponto de partida, e a ausencia de modelo-base aderente deve ser declarada
na entrega. Nao suprir modelo ausente com redacao autoral.

## Preferencias registradas do magistrado

1. Entregar as minutas de todas as opcoes tecnicamente viaveis, e nao perguntar
   qual adotar. A analise pode indicar qual e a mais correta, mas as pecas de
   cada caminho devem vir prontas na mesma entrega.

2. Adaptar sempre ao acervo de modelos do gabinete, preferindo os mais recentes.
   O formato do ato segue o modelo-base, inclusive quanto a estrutura: despachos
   iniciais padronizados usam itens numerados, sem relatorio e sem bloco de
   assinatura.

3. Nao designar a audiencia do art. 334 do CPC nos despachos iniciais quando o
   modelo-base aplicar a dispensa pela plataforma `+Acordo` do TJRJ.

## Carga de dossie

O dossie e a unica fonte de fatos. Na nuvem ele precisa ser fornecido na propria
sessao, em `.json`, e nao pode ser versionado. Nao ha extracao automatica de PDF
dos autos neste ambiente.

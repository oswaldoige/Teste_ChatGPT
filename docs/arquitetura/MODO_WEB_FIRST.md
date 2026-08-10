# MODO_WEB_FIRST

Este documento adapta o projeto para uso prioritario no Codex web quando o ambiente de trabalho nao permite Codex App e o navegador nao aceita upload operacional de `JSON` ou `PDF`.

## Premissa

O repositiorio continua sendo a fonte de regras, modelos, blocos, skills e trilhos operacionais.

O que muda no modo web-first nao e a logica juridica. O que muda e a forma de entrada do caso.

## Nova porta de entrada

Em vez de depender de anexo `JSON` ou `PDF`, o caso entra por um destes meios:

1. texto colado na conversa;
2. conteudo estruturado em `.md` ou `.txt`;
3. arquivo anonimizado versionado em `entrada_exemplos`.

## Fluxo recomendado no Codex web

1. Mandar o agente ler:
   - `README.md`
   - `AGENTS.md`
   - `00_LEIA_PRIMEIRO.md`
   - `docs\arquitetura\AUTOMACAO_REVISOR_PROCESSUAL.md`

2. Colar a entrada estruturada baseada em `entrada_exemplos\TEMPLATE_ENTRADA_PROCESSO_WEB.md`.

3. Pedir somente:
   - sistema;
   - fase processual;
   - ultimo ato relevante;
   - peticoes posteriores;
   - pendencia condicionante;
   - ato cabivel;
   - modelo-base aderente;
   - gate formal.

4. Validar o gate antes de pedir qualquer minuta.

5. So depois pedir redacao.

## O que nao fazer no modo web-first

- Nao depender de upload de `JSON` pelo seletor do navegador.
- Nao depender de upload de `PDF` se a interface nao aceitar.
- Nao subir processo real ao GitHub apenas para viabilizar leitura pelo navegador.
- Nao pular direto para a minuta sem fechar a fase.

## Vantagem pratica

Esse modo permite usar o projeto no trabalho mesmo quando:

- o navegador limita anexos;
- o Codex App nao e permitido;
- o ambiente local nao expoe os arquivos do processo ao agente.

## Limite do modo web-first

Se o caso depender de leitura massiva de autos, OCR, extracao automatica ou dezenas de pecas extensas, o modo web-first nao substitui integralmente o fluxo local. Ele e um modo operacional de analise guiada por entrada estruturada.

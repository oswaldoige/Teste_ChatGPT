# Entrada Para Uso Web

Esta pasta existe para apoiar o uso do projeto no Codex web, quando o navegador nao aceita `JSON` ou `PDF` como anexo operacional.

## Objetivo

No modo web, a porta de entrada mais segura e confiavel passa a ser texto estruturado colado na conversa ou arquivo `.md`/`.txt` sanitizado.

## Regra de seguranca

- Nao subir processo real ao repositorio sem anonimizar.
- Nao commitar dados sensiveis, documentos pessoais, dados medicos ou pecas integrais identificaveis.
- Para teste no GitHub, usar somente exemplo anonimizado ou sintetico.

## Arquivos desta pasta

- `TEMPLATE_ENTRADA_PROCESSO_WEB.md`
  Modelo-base para colar no Codex web.

## Uso recomendado

1. Abrir `TEMPLATE_ENTRADA_PROCESSO_WEB.md`.
2. Preencher os campos com os dados do processo.
3. Colar o conteudo na conversa do Codex web.
4. Usar o comando-base `comandos\COMANDO_WEB_ANALISE_ESTRITA.txt`.

## Quando usar esta pasta

- Quando o Codex web nao aceitar upload de `JSON`.
- Quando o navegador nao aceitar `PDF`.
- Quando o processo puder ser resumido ou transcrito em blocos essenciais.
- Quando for necessario testar o fluxo do projeto no ambiente do trabalho sem Codex App.

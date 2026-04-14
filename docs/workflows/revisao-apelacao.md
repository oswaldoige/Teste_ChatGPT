---
description: Executa revisão simulada de apelação (Tribunal Simulado TJRJ) sobre a sentença final escolhida para o processo
---

# Revisão de Apelação - Tribunal Simulado TJRJ

## Pré-requisitos
- O usuário deve indicar os números dos processos e, se possível, o arquivo da sentença final que deve servir de base para a revisão.
- Os arquivos precisam estar acessíveis no workspace, em `saida_docx/` ou pasta equivalente.
- Se existir revisão probatória prévia em `revisao_probatoria/`, ela deve ser incorporada como insumo obrigatório.

## Etapas

1. **Ler a skill** - Abrir e ler `C:\Users\Oswaldo-Nitro\.codex\skills\tribunal-simulado-apelacao-tjrj\SKILL.md` para carregar as instruções do tribunal simulado.

2. **Ler as referências** - Abrir e ler os dois arquivos de referência:
   - `C:\Users\Oswaldo-Nitro\.codex\skills\tribunal-simulado-apelacao-tjrj\references\roteiro-apelacao.md`
   - `C:\Users\Oswaldo-Nitro\.codex\skills\tribunal-simulado-apelacao-tjrj\references\fontes-oficiais-apelacao.md`

3. **Receber a lista de processos** - O usuário fornece os números dos processos e, quando houver mais de uma versão da sentença, identifica expressamente qual arquivo final deve ser revisado.

4. **Localizar os arquivos** - Para cada processo:
   - se o usuário indicar o arquivo final nominalmente, ele prevalece como entrada da revisão;
   - se o usuário não indicar o arquivo, localizar primeiro a versão final mais aderente ao processo na pasta de saída;
   - somente na ausência de outra indicação segura usar, como fallback, o `.docx` que contenha `validada` no nome;
   - localizar também o JSON/PDF correspondente da leva para leitura do contexto completo.

5. **Extrair o texto da sentença** - Usar `python-docx` ou leitura equivalente para extrair o texto completo da sentença escolhida, preservando a distinção entre a versão final e versões intermediárias.

6. **Buscar o contexto processual** - Ler o JSON de triagem correspondente e, quando disponível, o PDF do processo, para conferir a base probatória, os atos supervenientes e a coerência da sentença revisada.

7. **Integrar a revisão probatória** - Se existir arquivo em `revisao_probatoria/[numero]_revisao_probatoria.docx` ou `.txt`, incorporar seus achados antes de fechar a conclusão recursal.

8. **Analisar cada sentença** - Aplicar rigorosamente o roteiro de apelação:
   - verificar `error in procedendo`, `error in judicando`, omissões, contradições internas e consectários;
   - pesquisar jurisprudência real somente em STF, STJ e TJRJ;
   - usar links oficiais dos julgados ou das páginas de precedentes;
   - não inventar precedentes nem revisar versão diversa da sentença final escolhida.

9. **Produzir o voto** - Gerar o voto estruturado em 5 seções:
   - **1. Resultado** - Negar provimento / Dar parcial provimento / Dar provimento
   - **2. Ponto Central** - 2 a 5 parágrafos explicando o acerto ou erro
   - **3. Fundamento Jurisprudencial** - Precedentes com links oficiais
   - **4. Conclusão Objetiva** - Frase de voto
   - **5. Redação Sugerida** - Trecho original + trecho corrigido, obrigatória quando houver reforma

10. **Salvar o voto** - Salvar o resultado final como `[numero-processo]_revisao_apelacao.docx`, preferencialmente na pasta de saída indicada pelo usuário. Arquivo `.txt` pode existir apenas como rascunho interno, nunca como entrega final.

11. **Repetir** para cada processo da lista.

## Observações
- Quando o usuário indicar expressamente qual arquivo é a sentença final, essa indicação deve prevalecer sobre heurísticas baseadas no nome `validada`.
- Nunca alterar os arquivos originais das sentenças.
- Se não localizar precedente confiável, declarar isso expressamente.
- Se a sentença estiver correta, dizer isso sem criar problema artificial.
- A entrega final desta revisão deve ser em `.docx`.

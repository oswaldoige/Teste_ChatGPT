# Pipeline

## Sequencia correta
1. Receber a lista de processos.
2. Separar a rodada por sistema:
   - `PJe`
   - `eproc`
3. Rodar o download dos PDFs no sistema correto.
4. Rodar a conversao de `PDF -> .triagem.json`.
5. Validar se os JSONs trazem:
   - o texto integral extraido do PDF; e
   - o campo `provas` preenchido sempre que houver documentos probatorios relevantes.
6. So depois disso iniciar o revisor judicial.

## Formato minimo recomendado da lista
- Rodada homogenea:
  - `.txt` com um numero de processo por linha.
- Rodada mista:
  - `.csv` com colunas `numero_processo` e `sistema`.

## Estrutura de saida recomendada
- `downloads_pje`
- `downloads_eproc`
- `json_pje` ou JSONs na propria pasta de download
- `json_eproc` ou JSONs na propria pasta de download

## Handoff para o revisor
- Quando os JSONs estiverem prontos, o handoff para a automacao judicial deve voltar ao comando isolado do revisor.
- Nao misturar OCR, Selenium ou downloads dentro das skills de analise e minuta.
- O revisor deve receber JSONs ricos em prova documental; a etapa de conversao nao pode descartar anexos, faturas, laudos, extratos, comprovantes ou outros documentos de suporte.

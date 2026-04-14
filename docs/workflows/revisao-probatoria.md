---
description: Executa revisão probatória focada no acervo de prova antes da revisão de apelação do tribunal simulado
---

# Revisão Probatória - Tribunal Simulado TJRJ

## Pré-requisitos
- O usuário deve indicar o processo ou a leva a ser analisada.
- O JSON de triagem e, quando disponível, o PDF do processo precisam estar acessíveis no workspace.
- A revisão deve ficar limitada ao material efetivamente constante dos autos.

## Etapas

1. **Localizar os arquivos-base** - Encontrar o JSON de triagem do processo e, se houver, o PDF correspondente na pasta da leva.

2. **Ler o contexto processual essencial** - Identificar:
   - petição inicial e documentos centrais do autor;
   - contestação e documentos do réu;
   - réplica;
   - decisões de saneamento;
   - requerimentos de prova;
   - audiência de instrução e julgamento, se realizada;
   - eventual encerramento da fase probatória.

3. **Mapear o acervo de prova** - Registrar, com referência processual adequada, quais provas documentais, testemunhais, periciais ou orais efetivamente existem e quais teses cada uma sustenta.

4. **Avaliar o peso do conjunto probatório** - Apontar:
   - quais fatos constitutivos têm suporte documental suficiente;
   - quais fatos impeditivos, modificativos ou extintivos ficaram sem comprovação robusta;
   - se houve desistência, preclusão ou ausência de produção de prova relevante;
   - se a sentença valorizou corretamente o ônus da prova.

5. **Fechar a conclusão probatória** - Indicar, de forma objetiva, se o acervo:
   - sustenta a conclusão da sentença;
   - revela fragilidade específica;
   - ou exige cautela em eventual revisão recursal.

6. **Salvar o resultado** - Salvar como `[numero-processo]_revisao_probatoria.docx` na pasta `revisao_probatoria/`. Arquivo `.txt` pode existir apenas como rascunho interno.

## Observações
- A revisão probatória não substitui a revisão de apelação; ela funciona como insumo obrigatório da etapa recursal quando disponível.
- Não inventar lacunas nem afirmar inexistência de prova sem conferir o dossiê.
- A entrega final deve ser em `.docx`.

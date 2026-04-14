# Execução Limpa do Revisor

Esta pasta foi criada para isolar a operação cotidiana da automação do revisor, sem misturar:
- testes de calibração;
- arquivos temporários;
- versões intermediárias;
- ou outras automações do gabinete.

## Estrutura
- `entrada_json`
  Coloque aqui, se desejar, apenas os `.json` da rodada que será executada.
- `saida_docx`
  Pode continuar existindo como pasta de saída organizada da rodada dentro do OneDrive, mas não deve mais ser tratada como destino único confiável.
- `controle`
  Contém o nome sugerido do novo tópico e o comando oficial para iniciar a automação.

## Uso recomendado
1. Abra um novo tópico no projeto do revisor.
2. Dê ao tópico o nome indicado em `controle\TOPICO_SUGERIDO.txt`, se houver.
3. Cole a mensagem inicial oficial da rodada.
4. Se quiser trabalhar por leva fechada, copie os `.json` da rodada para `entrada_json`.
5. Mantenha o `core` da automação exatamente como está, sem adaptações locais nesta pasta.

## Saída física preferencial
Em razão de instabilidades de sincronização do OneDrive, a gravação dos provimentos finais deve priorizar a pasta local do notebook:

`C:\Users\Oswaldo-Nitro\Documents\AUTOMACAO_PRINCIPAL_LOCAL\saida_docx`

Essa pasta local deve ser considerada a cópia principal da rodada.

## Observação
Esta pasta melhora a organização e reduz ruído humano, mas não substitui a proteção principal da automação, que continua sendo:
- o comando isolado;
- as skills separadas;
- e as regras do `revisor-processual-tjrj`.

O `OneDrive` pode continuar sendo usado apenas como espelho posterior, quando conveniente.

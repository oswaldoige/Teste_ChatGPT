# Gate Fluxo Estrito

Para qualquer geracao de `.docx` na pasta:

`saida_docx`

o `make_docx.py` agora exige um arquivo sidecar JSON com o mesmo nome-base do `.md` de entrada:

- exemplo de entrada: `minuta.md`
- gate obrigatorio: `minuta.gate.json`

Campos obrigatorios:
- `sistema`
- `fase_e_ato_cabivel`
- `ultimo_ato_relevante`
- `peticoes_posteriores`
- `pendencia_condicionante`
- `modelo_base_path`
- `preflight_confirmado = true`
- `postflight_confirmado = true`

Sem esse gate, o `.docx` nao sera gerado.

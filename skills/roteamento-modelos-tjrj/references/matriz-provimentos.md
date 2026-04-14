# Matriz de Roteamento

## Canonical root
- `modelos`

## Search matrix
- `tutela` + `consumidor`
  `00_NUCLEO_OPERACIONAL\01_TUTELA\01_CONSUMIDOR`
- `tutela` + `civel contratual`
  `00_NUCLEO_OPERACIONAL\01_TUTELA\02_CIVEL_CONTRATUAL`
- `tutela` + `Fazenda Publica`
  `00_NUCLEO_OPERACIONAL\01_TUTELA\03_FAZENDA_PUBLICA`
- `saneador` + `consumidor`
  `00_NUCLEO_OPERACIONAL\02_SANEADOR\01_CONSUMIDOR`
- `saneador` + `civel contratual`
  `00_NUCLEO_OPERACIONAL\02_SANEADOR\02_CIVEL_CONTRATUAL`
- `saneador` + `Fazenda Publica`
  `00_NUCLEO_OPERACIONAL\02_SANEADOR\03_FAZENDA_PUBLICA`
- `sentenca` + `consumidor`
  `00_NUCLEO_OPERACIONAL\03_SENTENCA\01_CONSUMIDOR`
- `sentenca` + `civel contratual`
  `00_NUCLEO_OPERACIONAL\03_SENTENCA\02_CIVEL_CONTRATUAL`
- `sentenca` + `Fazenda Publica`
  `00_NUCLEO_OPERACIONAL\03_SENTENCA\03_FAZENDA_PUBLICA`

## Fallback order
1. `00_NUCLEO_OPERACIONAL`
2. `00_PRIORITARIOS_AUTOMACAO`
3. Specialized folder for the matter or chamber
4. Correlated archive folders
5. Reference PDFs when they are really needed

## Curatorship rule
- Keep the operational nucleus curated and authoritative, but not artificially tiny.
- In recurring families, allow 3 to 6 canonical models when that is what preserves the gabinete's standard structure.
- Push small wording variations into `90_BLOCOS_REUTILIZAVEIS`.
- After selecting the canonical model, consult the matching `90_BLOCOS_REUTILIZAVEIS` folder whenever a stable opening or burden-of-proof block exists.
- Do not create a fresh standalone model when the difference can be solved by swapping one reasoning block or dispositive block.

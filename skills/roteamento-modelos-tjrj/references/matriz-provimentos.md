# Matriz de Roteamento

## Canonical root
- `modelos`

Paths are relative to the canonical root. The nucleus folders live directly under
`modelos`; there is no `00_NUCLEO_OPERACIONAL` level inside the repository, which
is the layout of the wide archive, not of the curated nucleus.

## Search matrix
- `despacho inicial` + `rito comum`
  `00_DESPACHO_INICIAL\01_RITO_COMUM`
- `despacho inicial` + `Fazenda Publica`
  `00_DESPACHO_INICIAL\02_FAZENDA_PUBLICA`
- `despacho inicial` + `execucao extrajudicial`
  `00_DESPACHO_INICIAL\03_EXECUCAO_EXTRAJUDICIAL`
- `tutela` + `consumidor`
  `01_TUTELA\01_CONSUMIDOR`
- `tutela` + `civel contratual`
  `01_TUTELA\02_CIVEL_CONTRATUAL`
- `tutela` + `Fazenda Publica`
  `01_TUTELA\03_FAZENDA_PUBLICA`
- `saneador` + `consumidor`
  `02_SANEADOR\01_CONSUMIDOR`
- `saneador` + `civel contratual`
  `02_SANEADOR\02_CIVEL_CONTRATUAL`
- `saneador` + `Fazenda Publica`
  `02_SANEADOR\03_FAZENDA_PUBLICA`
- `sentenca` + `consumidor`
  `03_SENTENCA\01_CONSUMIDOR`
- `sentenca` + `civel contratual`
  `03_SENTENCA\02_CIVEL_CONTRATUAL`
- `sentenca` + `Fazenda Publica`
  `03_SENTENCA\03_FAZENDA_PUBLICA`

The opening act routes by rite, not by subject matter: the same consumer or
contractual dispute takes the same `01_RITO_COMUM` model.

## Fallback order
1. The curated nucleus in `modelos`
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
- In `00_DESPACHO_INICIAL`, do not schedule the art. 334 hearing when the model
  applies the dispensation through the TJRJ `+Acordo` platform. In the rito comum
  model that is the third wording of the base file, and it is the default.

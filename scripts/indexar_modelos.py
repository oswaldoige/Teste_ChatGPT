"""Indexacao e busca do acervo de modelos do gabinete.

O acervo amplo tem centenas de arquivos e nao cabe em leitura integral. Este
modulo produz um indice leve, com caminho, pasta tematica e data de modificacao
de cada modelo, e permite localizar o modelo-base aderente sem varrer o acervo
inteiro a cada minuta.

A preferencia registrada do magistrado e pelos modelos mais recentes. A busca,
por isso, ordena por aderencia textual e, em empate, pela data de modificacao,
da mais nova para a mais antiga.

Uso:

    python scripts/indexar_modelos.py                      # indexa o acervo
    python scripts/indexar_modelos.py --buscar "despacho inicial"
    python scripts/indexar_modelos.py --buscar "gratuidade" --limite 5

O indice e gravado em `config/indice_modelos.json`, que nao e versionado por
conter caminhos da maquina local.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import ambiente

INDICE = ambiente.RAIZ_REPO / "config" / "indice_modelos.json"

EXTENSOES = {".docx", ".doc", ".txt", ".md", ".pdf", ".rtf"}

# Ruido de sincronizacao do OneDrive e de saidas antigas que nao servem como
# modelo-base. A regra 2 do AGENTS.md veda usar saida gerada como modelo.
IGNORAR = re.compile(
    r"(^~\$)|(\.tmp)|(conflicted copy)|(copia em conflito)",
    re.IGNORECASE,
)


def normalizar(texto: str) -> str:
    """Remove acentuacao e caixa, para busca tolerante."""
    sem_acento = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join(c for c in sem_acento if not unicodedata.combining(c))
    return sem_acento.lower()


def raizes_de_busca() -> list[Path]:
    """Devolve as raizes a indexar, conforme o ambiente detectado.

    Na maquina do gabinete, o acervo amplo `AUTOMACAO_MODELOS`. Sem ele, apenas
    o nucleo curado versionado no repositorio, que e o unico ponto de partida
    legitimo quando o acervo nao esta ao alcance.
    """
    raizes = list(ambiente.acervos())
    nucleo = ambiente.RAIZ_REPO / "modelos"
    if nucleo.is_dir():
        raizes.append(nucleo)
    return raizes


def indexar() -> dict:
    """Varre as raizes disponiveis e monta o indice de modelos."""
    itens = []
    raizes = raizes_de_busca()

    for raiz in raizes:
        for caminho in raiz.rglob("*"):
            if not caminho.is_file():
                continue
            if caminho.suffix.lower() not in EXTENSOES:
                continue
            if IGNORAR.search(caminho.name):
                continue
            try:
                stat = caminho.stat()
            except OSError:
                continue
            itens.append(
                {
                    "nome": caminho.stem,
                    "caminho": str(caminho),
                    "pasta": str(caminho.parent.relative_to(raiz)) or ".",
                    "raiz": str(raiz),
                    "extensao": caminho.suffix.lower(),
                    "modificado_em": datetime.fromtimestamp(
                        stat.st_mtime, tz=timezone.utc
                    ).isoformat(),
                    "bytes": stat.st_size,
                }
            )

    itens.sort(key=lambda i: i["modificado_em"], reverse=True)
    return {
        "gerado_em": datetime.now(tz=timezone.utc).isoformat(),
        "ambiente": "local" if ambiente.ambiente_local() else "nuvem",
        "raizes": [str(r) for r in raizes],
        "total": len(itens),
        "modelos": itens,
    }


def carregar_indice() -> dict:
    if not INDICE.is_file():
        raise SystemExit(
            "Indice inexistente. Rode antes: python scripts/indexar_modelos.py"
        )
    return json.loads(INDICE.read_text(encoding="utf-8"))


def pontuar(item: dict, termos: list[str]) -> int:
    """Pontua a aderencia do modelo aos termos buscados.

    O nome do arquivo pesa mais que a pasta, porque no acervo do gabinete o nome
    e que identifica o ato ("DESPACHO INICIAL COMUM - AUD 334"), enquanto a pasta
    identifica apenas a macrofamilia.
    """
    nome = normalizar(item["nome"])
    pasta = normalizar(item["pasta"])
    pontos = 0
    for termo in termos:
        if termo in nome:
            pontos += 10
        if termo in pasta:
            pontos += 3
    return pontos


def buscar(consulta: str, limite: int) -> list[dict]:
    indice = carregar_indice()
    termos = [normalizar(t) for t in consulta.split() if t.strip()]
    if not termos:
        return []

    pontuados = []
    for item in indice["modelos"]:
        pontos = pontuar(item, termos)
        if pontos:
            pontuados.append((pontos, item["modificado_em"], item))

    # Aderencia primeiro; em empate, o mais recente, conforme a preferencia
    # registrada do magistrado.
    pontuados.sort(key=lambda t: (t[0], t[1]), reverse=True)
    return [item for _, _, item in pontuados[:limite]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--buscar", metavar="TERMOS", help="busca no indice ja gerado")
    parser.add_argument("--limite", type=int, default=10, help="resultados da busca")
    args = parser.parse_args()

    if args.buscar:
        achados = buscar(args.buscar, args.limite)
        if not achados:
            print("Nenhum modelo aderente aos termos informados.")
            print("Declarar a ausencia de modelo-base na entrega; nao suprir por")
            print("redacao autoral.")
            return 1
        for i, item in enumerate(achados, 1):
            data = item["modificado_em"][:10]
            print(f"{i:2}. [{data}] {item['nome']}")
            print(f"    {item['pasta']}")
            print(f"    {item['caminho']}")
        return 0

    indice = indexar()
    INDICE.parent.mkdir(parents=True, exist_ok=True)
    INDICE.write_text(
        json.dumps(indice, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Ambiente: {indice['ambiente']}")
    for raiz in indice["raizes"]:
        print(f"  raiz indexada: {raiz}")
    print(f"\n{indice['total']} modelos indexados em {INDICE}")
    if indice["ambiente"] == "nuvem":
        print(
            "\nAcervo amplo ausente. Indexado apenas o nucleo curado do"
            "\nrepositorio. Rode novamente na maquina do gabinete para"
            "\nalcancar AUTOMACAO_MODELOS."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

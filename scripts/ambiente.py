"""Resolucao de caminhos operacionais do gabinete.

Este modulo existe porque a documentacao canonica do projeto foi escrita para a
maquina local e passou a ser usada tambem em execucao na nuvem. Em vez de apagar
as referencias operacionais, os caminhos absolutos foram parametrizados como
`${GABINETE_RAIZ_2026}`, `${GABINETE_SKILLS}` e `${GABINETE_SAIDA}`, e este
modulo resolve cada um deles conforme o ambiente em que a automacao esta rodando.

Ordem de precedencia de cada variavel:

1. variavel de ambiente de mesmo nome;
2. chave correspondente em `config/ambiente.json`, quando o arquivo existir;
3. valor padrao do ambiente detectado.

Uso em linha de comando:

    python scripts/ambiente.py            # relatorio legivel
    python scripts/ambiente.py --json     # saida estruturada
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parent.parent
CONFIG_LOCAL = RAIZ_REPO / "config" / "ambiente.json"

RAIZ_2026_LOCAL = (
    r"C:\Users\Oswaldo-Nitro\OneDrive - Tribunal de Justica do Estado do Rio de Janeiro\2026"
)
SKILLS_LOCAL = r"C:\Users\Oswaldo-Nitro\.codex\skills"
SAIDA_LOCAL = r"C:\Users\Oswaldo-Nitro\Documents\AUTOMACAO_PRINCIPAL_LOCAL\saida_docx"

VARIAVEIS = ("GABINETE_RAIZ_2026", "GABINETE_SKILLS", "GABINETE_SAIDA")

PADRAO_VARIAVEL = re.compile(r"\$\{(GABINETE_[A-Z0-9_]+)\}")


def ambiente_local() -> bool:
    """Indica se a automacao esta rodando na maquina do gabinete.

    O criterio e a existencia real do acervo do OneDrive. Rodar em Windows nao
    basta: outra maquina Windows sem o acervo sincronizado deve ser tratada como
    ambiente sem acervo, e nao como ambiente local completo.
    """
    return Path(RAIZ_2026_LOCAL).is_dir()


def _config_local() -> dict:
    if not CONFIG_LOCAL.is_file():
        return {}
    try:
        dados = json.loads(CONFIG_LOCAL.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return dados if isinstance(dados, dict) else {}


def _padroes() -> dict:
    if ambiente_local():
        return {
            "GABINETE_RAIZ_2026": RAIZ_2026_LOCAL,
            "GABINETE_SKILLS": SKILLS_LOCAL,
            "GABINETE_SAIDA": SAIDA_LOCAL,
        }
    return {
        # Na nuvem o acervo completo do OneDrive nao existe. O nucleo curado de
        # modelos versionado no repositorio e o unico ponto de partida possivel.
        "GABINETE_RAIZ_2026": str(RAIZ_REPO),
        "GABINETE_SKILLS": str(RAIZ_REPO / "skills"),
        "GABINETE_SAIDA": str(RAIZ_REPO / "02_EXECUCAO_OPERACIONAL" / "saida_docx"),
    }


def caminhos() -> dict:
    """Devolve o valor resolvido de cada variavel operacional."""
    config = _config_local()
    padroes = _padroes()
    return {
        nome: os.environ.get(nome) or config.get(nome) or padroes[nome]
        for nome in VARIAVEIS
    }


def resolver(texto: str) -> str:
    """Substitui `${GABINETE_*}` pelos caminhos resolvidos do ambiente atual."""
    valores = caminhos()
    return PADRAO_VARIAVEL.sub(lambda m: valores.get(m.group(1), m.group(0)), texto)


def acervo_completo_disponivel() -> bool:
    """Indica se o acervo amplo `AUTOMACAO_MODELOS` esta acessivel."""
    return (Path(caminhos()["GABINETE_RAIZ_2026"]) / "AUTOMACAO_MODELOS").is_dir()


def relatorio() -> dict:
    valores = caminhos()
    return {
        "ambiente": "local" if ambiente_local() else "nuvem",
        "acervo_completo_disponivel": acervo_completo_disponivel(),
        "nucleo_curado": str(RAIZ_REPO / "modelos"),
        "caminhos": valores,
    }


def main(argv: list[str]) -> int:
    dados = relatorio()
    if "--json" in argv:
        print(json.dumps(dados, ensure_ascii=False, indent=2))
        return 0

    print(f"Ambiente detectado: {dados['ambiente']}")
    for nome, valor in dados["caminhos"].items():
        print(f"  {nome} = {valor}")
    if dados["acervo_completo_disponivel"]:
        print("\nAcervo AUTOMACAO_MODELOS disponivel. Busca ampla liberada.")
    else:
        print(
            "\nAcervo AUTOMACAO_MODELOS indisponivel neste ambiente."
            "\nUsar apenas o nucleo curado em `modelos` e registrar a limitacao"
            "\nna entrega, quando nenhum modelo canonico for aderente ao caso."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

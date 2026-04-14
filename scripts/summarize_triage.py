from __future__ import annotations

import json
import pathlib
import re
import sys
from typing import Iterable


PROCESS_RE = re.compile(r"\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b")


def clean(text: str) -> str:
    return " ".join(text.replace("\u00a0", " ").split())


def pick(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.IGNORECASE)
    return clean(match.group(1)) if match else ""


def render_case(path: pathlib.Path) -> str:
    obj = json.loads(path.read_text(encoding="utf-8"))
    segments = obj.get("texto_completo_segmentado") or []
    texts = [seg.get("texto", "") for seg in segments]
    joined = "\n".join(texts)
    head = "\n".join(texts[:8])

    proc = pick(r"PROCESSO N[ºO]\s*([0-9.\-]+)", joined)
    if not proc:
        match = PROCESS_RE.search(joined)
        proc = match.group(0) if match else ""

    classe = pick(r"Classe da a[cç][aã]o:\s*(.+?)\s+Compet[êe]ncia", joined)
    competencia = pick(r"Compet[êe]ncia\s+([A-Za-zÀ-ÿ ]+?)\s+Data de autua", joined)
    localizador = pick(r"Localizador\(es\):\s*(.+?)\s+Ajuda localizadores", head)
    assunto = pick(r"Assuntos?\s+Código\s+Descri[cç][aã]o\s+Principal\s+([^\n]+)", joined)
    valor = pick(r"Valor da causa:\s*R\$\s*([0-9.,]+)", joined)
    tutela = "sim" if re.search(r"tutela de urg[êe]ncia|tutela antecipada|liminar", head, re.I) else "não"
    autor = clean(str((obj.get("partes") or {}).get("autor") or ""))
    reu = clean(str((obj.get("partes") or {}).get("reu") or ""))
    ato = clean(str(((obj.get("ato_sugerido") or {}).get("tipo")) or ""))

    first_events: list[str] = []
    for text in texts[:30]:
        for ev, sig in re.findall(r"Evento\s+(\d+),\s*([A-Z0-9]+)", text):
            tag = f"{ev}/{sig}"
            if tag not in first_events:
                first_events.append(tag)
            if len(first_events) >= 8:
                break
        if len(first_events) >= 8:
            break

    return " | ".join(
        [
            proc or path.name,
            f"classe={classe or '?'}",
            f"competência={competencia or '?'}",
            f"localizador={localizador or '?'}",
            f"assunto={assunto or '?'}",
            f"valor={valor or '?'}",
            f"tutela={tutela}",
            f"autor={autor or '?'}",
            f"réu={reu or '?'}",
            f"ato_sugerido={ato or '?'}",
            f"eventos={','.join(first_events) if first_events else '?'}",
        ]
    )


def iter_paths(argv: Iterable[str]) -> list[pathlib.Path]:
    paths: list[pathlib.Path] = []
    for raw in argv:
        path = pathlib.Path(raw)
        if path.is_dir():
            paths.extend(sorted(path.glob("*.json")))
        else:
            paths.append(path)
    return paths


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: summarize_triage.py <json-or-dir> [...]", file=sys.stderr)
        return 2

    for path in iter_paths(sys.argv[1:]):
        print(render_case(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import argparse
import json
import logging
import os
import re
from datetime import datetime
from pathlib import Path

import pdfplumber
import pytesseract
from pdf2image import convert_from_path

PROVA_PADROES = [
    r"\bprova[s]?\b",
    r"\bdocumento[s]?\b",
    r"\banexo[s]?\b",
    r"\bfatura[s]?\b",
    r"\bconta[s]?\b",
    r"\bextrato[s]?\b",
    r"\bcomprovante[s]?\b",
    r"\bnota fiscal\b",
    r"\bboleto[s]?\b",
    r"\brecibo[s]?\b",
    r"\blaudo[s]?\b",
    r"\brelatorio[s]?\b",
    r"\breceita[s]?\b",
    r"\bexame[s]?\b",
    r"\bfoto[s]?\b",
    r"\bimagem[s]?\b",
    r"\bboletim de ocorrencia\b",
    r"\bcertidao\b",
    r"\bdeclaracao\b",
    r"\bcontrato\b",
    r"\bprocuracao\b",
    r"\bmandado\b",
    r"\boficio\b",
    r"\bvideo\b",
    r"\baudio\b",
]

DEFAULT_TESSERACT = os.getenv("AUTOMACAO_TESSERACT") or os.getenv("TESSERACT_CMD") or r"C:\Program Files\Tesseract-OCR\tesseract.exe"
DEFAULT_POPPLER = os.getenv("AUTOMACAO_POPPLER") or os.getenv("POPPLER_PATH") or r"C:\Program Files\poppler\Library\bin"


def build_logger(target_dir: Path):
    logger = logging.getLogger(f"pdf-json-triagem-{target_dir}")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    file_handler = logging.FileHandler(target_dir / "pipeline.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def detectar_tipo_pdf(caminho_pdf: Path, min_chars_por_pagina: int, limiar_nativo: float):
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            total_paginas = len(pdf.pages)
            if total_paginas == 0:
                return "digitalizado"

            paginas_com_texto = 0
            for pagina in pdf.pages:
                texto = pagina.extract_text() or ""
                if len(texto.strip()) >= min_chars_por_pagina:
                    paginas_com_texto += 1

            proporcao = paginas_com_texto / total_paginas
            return "nativo" if proporcao >= limiar_nativo else "digitalizado"
    except Exception:
        return "digitalizado"


def extrair_texto_nativo(caminho_pdf: Path):
    paginas_texto = []
    num_paginas = 0
    with pdfplumber.open(caminho_pdf) as pdf:
        num_paginas = len(pdf.pages)
        for i, pagina in enumerate(pdf.pages, 1):
            texto = pagina.extract_text() or ""
            if texto.strip():
                paginas_texto.append(f"[Pagina {i}]\n{texto.strip()}")
    return "\n\n".join(paginas_texto), num_paginas


def extrair_texto_ocr(caminho_pdf: Path, poppler_path: str, logger):
    paginas_texto = []
    imagens = convert_from_path(str(caminho_pdf), dpi=300, poppler_path=poppler_path)
    num_paginas = len(imagens)
    for i, imagem in enumerate(imagens, 1):
        logger.info(f"  OCR pagina {i}/{num_paginas}...")
        texto = pytesseract.image_to_string(imagem, lang="por")
        if texto.strip():
            paginas_texto.append(f"[Pagina {i}]\n{texto.strip()}")
    return "\n\n".join(paginas_texto), num_paginas


def extrair_texto(caminho_pdf: Path, poppler_path: str, min_chars_por_pagina: int, limiar_nativo: float, logger):
    tipo = detectar_tipo_pdf(caminho_pdf, min_chars_por_pagina=min_chars_por_pagina, limiar_nativo=limiar_nativo)
    logger.info(f"  Tipo detectado: {tipo}")

    if tipo == "nativo":
        texto, num_paginas = extrair_texto_nativo(caminho_pdf)
        if len(texto.strip()) < 100:
            logger.warning("  Extracao nativa insuficiente. Tentando OCR como fallback...")
            texto, num_paginas = extrair_texto_ocr(caminho_pdf, poppler_path=poppler_path, logger=logger)
            tipo = "digitalizado (fallback OCR)"
    else:
        texto, num_paginas = extrair_texto_ocr(caminho_pdf, poppler_path=poppler_path, logger=logger)

    return {
        "texto": texto,
        "tipo": tipo,
        "num_paginas": num_paginas,
        "chars_extraidos": len(texto),
    }


def segmentar_texto(texto: str):
    padroes_divisao = [
        r"\[Pagina \d+\]",
        r"(?:peticao inicial|contestacao|replica|impugnacao|embargos|recurso|apelacao|agravo|sentenca|decisao|despacho|laudo|declaracao|requerimento|memoriais|alegacoes finais)",
    ]
    padrao_combinado = "|".join(padroes_divisao)
    partes = re.split(f"({padrao_combinado})", texto, flags=re.IGNORECASE)

    segmentos = []
    id_contador = 1
    buffer = ""
    rotulo_atual = "Inicio dos autos"

    for parte in partes:
        if re.match(padrao_combinado, parte, re.IGNORECASE):
            if buffer.strip():
                segmentos.append(
                    {
                        "id": id_contador,
                        "rotulo": rotulo_atual,
                        "texto": buffer.strip()[:5000],
                    }
                )
                id_contador += 1
            rotulo_atual = parte.strip()
            buffer = ""
        else:
            buffer += parte

    if buffer.strip():
        segmentos.append(
            {
                "id": id_contador,
                "rotulo": rotulo_atual,
                "texto": buffer.strip()[:5000],
            }
        )

    return segmentos


def mapear_provas(segmentos: list[dict]):
    provas = []
    padrao = re.compile("|".join(PROVA_PADROES), flags=re.IGNORECASE)

    for segmento in segmentos:
        universo = f"{segmento['rotulo']}\n{segmento['texto']}"
        if not padrao.search(universo):
            continue

        trecho = re.sub(r"\s+", " ", segmento["texto"]).strip()[:1200]
        provas.append(
            {
                "id_segmento": segmento["id"],
                "rotulo": segmento["rotulo"],
                "trecho": trecho,
            }
        )

    return provas


def montar_json_triagem(caminho_pdf: Path, extracao: dict, segmentos: list[dict], provas: list[dict]):
    return {
        "metadados": {
            "arquivo_origem": caminho_pdf.name,
            "data_processamento": datetime.now().isoformat(),
            "tipo_extracao": extracao["tipo"],
            "num_paginas": extracao["num_paginas"],
            "chars_extraidos": extracao["chars_extraidos"],
        },
        "texto_completo_segmentado": segmentos,
        "partes": {"autor": "", "reu": "", "terceiros": []},
        "objeto_litigioso": "",
        "pedidos": [],
        "fatos_relevantes": [],
        "provas": provas,
        "decisoes_anteriores": [],
        "pontos_controvertidos": [],
        "ato_sugerido": {"tipo": "", "justificativa": ""},
        "observacoes": "",
    }


def processar_pdf(caminho_pdf: Path, poppler_path: str, min_chars_por_pagina: int, limiar_nativo: float, logger):
    caminho_json = caminho_pdf.with_suffix(".triagem.json")
    if caminho_json.exists():
        logger.info(f"  JSON ja existe, pulando: {caminho_json.name}")
        return True

    logger.info("=" * 60)
    logger.info(f"Processando: {caminho_pdf.name}")
    extracao = extrair_texto(
        caminho_pdf,
        poppler_path=poppler_path,
        min_chars_por_pagina=min_chars_por_pagina,
        limiar_nativo=limiar_nativo,
        logger=logger,
    )
    if not extracao["texto"].strip():
        logger.warning(f"  Nenhum texto extraido de {caminho_pdf.name}.")
        return False

    segmentos = segmentar_texto(extracao["texto"])
    provas = mapear_provas(segmentos)
    dados_json = montar_json_triagem(caminho_pdf, extracao, segmentos, provas)
    caminho_json.write_text(json.dumps(dados_json, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info(f"  JSON salvo: {caminho_json.name}")
    logger.info(f"  Provas mapeadas: {len(provas)}")
    return True


def build_parser():
    parser = argparse.ArgumentParser(description="Converte PDFs de processos em arquivos .triagem.json.")
    parser.add_argument("--pasta", required=True, help="Pasta que contem os PDFs.")
    parser.add_argument("--tesseract", default=DEFAULT_TESSERACT, help="Caminho do executavel do Tesseract.")
    parser.add_argument("--poppler", default=DEFAULT_POPPLER, help="Caminho do Poppler.")
    parser.add_argument("--min-chars", type=int, default=50, help="Minimo de caracteres por pagina para considerar PDF nativo.")
    parser.add_argument("--limiar-nativo", type=float, default=0.4, help="Proporcao minima de paginas com texto para classificar como PDF nativo.")
    return parser


def main():
    args = build_parser().parse_args()
    pasta = Path(args.pasta).resolve()
    pasta.mkdir(parents=True, exist_ok=True)

    pytesseract.pytesseract.tesseract_cmd = args.tesseract
    logger = build_logger(pasta)

    pdfs = sorted(pasta.glob("*.pdf"))
    if not pdfs:
        logger.info("Nenhum PDF encontrado na pasta.")
        return

    sucesso = 0
    falha = 0
    for caminho_pdf in pdfs:
        try:
            ok = processar_pdf(
                caminho_pdf,
                poppler_path=args.poppler,
                min_chars_por_pagina=args.min_chars,
                limiar_nativo=args.limiar_nativo,
                logger=logger,
            )
            sucesso += int(ok)
            falha += int(not ok)
        except Exception as exc:
            logger.error(f"Erro ao processar {caminho_pdf.name}: {exc}", exc_info=True)
            falha += 1

    logger.info("=" * 60)
    logger.info(f"Pipeline concluido: {sucesso} OK | {falha} com falha")


if __name__ == "__main__":
    main()

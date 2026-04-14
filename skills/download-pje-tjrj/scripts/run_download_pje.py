import argparse
import csv
import importlib.util
import os
import sys
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime
from pathlib import Path


LEGACY_PJE_SCRIPT = Path(r"C:\download.py")


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for stream in self.streams:
            stream.write(data)
            stream.flush()
        return len(data)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def resolve_pje_script(cli_value: str | None) -> Path:
    chosen = cli_value or os.getenv("AUTOMACAO_PJE_SCRIPT") or str(LEGACY_PJE_SCRIPT)
    script_path = Path(chosen).expanduser().resolve()
    if not script_path.exists():
        raise FileNotFoundError(
            "Script base do PJe nao encontrado. "
            "Informe --script ou defina AUTOMACAO_PJE_SCRIPT."
        )
    return script_path


def load_pje_module(script_path: Path):
    spec = importlib.util.spec_from_file_location("pje_download_module", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def read_process_list(path: Path):
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames:
                raise ValueError("CSV sem cabecalho.")
            process_column = None
            for field in reader.fieldnames:
                if "process" in field.lower() or "numero" in field.lower():
                    process_column = field
                    break
            if not process_column:
                process_column = reader.fieldnames[0]
            return [
                (row[process_column] or "").replace("\ufeff", "").strip()
                for row in reader
                if (row.get(process_column) or "").replace("\ufeff", "").strip()
            ]

    return [
        line.replace("\ufeff", "").strip()
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.replace("\ufeff", "").strip()
    ]


def build_parser():
    parser = argparse.ArgumentParser(description="Wrapper para download de processos no PJe.")
    parser.add_argument(
        "--script",
        help="Caminho do script base de download do PJe. Se omitido, usa AUTOMACAO_PJE_SCRIPT ou o caminho legado.",
    )
    parser.add_argument("--processos-file", required=True, help="TXT ou CSV com a lista de processos.")
    parser.add_argument("--downloads", required=True, help="Pasta de saida dos PDFs.")
    parser.add_argument("--intervalo", type=int, default=5, help="Intervalo entre processos.")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout padrao do navegador.")
    parser.add_argument("--sem-pausa-final", action="store_true", help="Fecha sem aguardar ENTER no final.")
    return parser


def main():
    args = build_parser().parse_args()
    script_path = resolve_pje_script(args.script)
    processos = read_process_list(Path(args.processos_file))
    if not processos:
        raise ValueError("Nenhum processo valido foi encontrado na lista.")

    downloads_dir = Path(args.downloads).resolve()
    downloads_dir.mkdir(parents=True, exist_ok=True)
    log_path = downloads_dir / f"download_pje_execucao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    module = load_pje_module(script_path)
    automacao = module.PJEAutomation(download_path=str(downloads_dir), timeout=args.timeout)

    with log_path.open("w", encoding="utf-8") as log_file:
        tee = Tee(sys.stdout, log_file)
        with redirect_stdout(tee), redirect_stderr(tee):
            print(f"Log de execucao: {log_path}")
            print(f"Script base do PJe: {script_path}")
            try:
                automacao.configurar_navegador()
                automacao.abrir_pje()
                automacao.aguardar_login()
                automacao.processar_lista(processos, intervalo=args.intervalo)
            finally:
                if not args.sem_pausa_final:
                    try:
                        input("\nPressione ENTER para fechar o navegador e finalizar...")
                    except EOFError:
                        pass
                automacao.fechar()


if __name__ == "__main__":
    main()

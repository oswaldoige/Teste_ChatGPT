import argparse
import csv
import importlib.util
import os
import sys
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime
from pathlib import Path


LEGACY_EPROC_SCRIPT = Path(r"C:\download_eproc.py")


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


def resolve_eproc_script(cli_value: str | None) -> Path:
    chosen = cli_value or os.getenv("AUTOMACAO_EPROC_SCRIPT") or str(LEGACY_EPROC_SCRIPT)
    script_path = Path(chosen).expanduser().resolve()
    if not script_path.exists():
        raise FileNotFoundError(
            "Script base do eproc nao encontrado. "
            "Informe --script ou defina AUTOMACAO_EPROC_SCRIPT."
        )
    return script_path


def load_eproc_module(script_path: Path):
    spec = importlib.util.spec_from_file_location("eproc_download_module", script_path)
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
            return [row[process_column].strip() for row in reader if (row.get(process_column) or "").strip()]

    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def build_parser():
    parser = argparse.ArgumentParser(description="Wrapper para download de processos no eproc.")
    parser.add_argument(
        "--script",
        help="Caminho do script base de download do eproc. Se omitido, usa AUTOMACAO_EPROC_SCRIPT ou o caminho legado.",
    )
    parser.add_argument("--processos-file", required=True, help="TXT ou CSV com a lista de processos.")
    parser.add_argument("--downloads", required=True, help="Pasta de saida dos PDFs.")
    parser.add_argument("--logs", required=True, help="Pasta de logs e screenshots de debug.")
    parser.add_argument("--intervalo", type=int, default=5, help="Intervalo entre processos.")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout padrao do navegador.")
    parser.add_argument("--espera-geracao", type=int, default=150, help="Espera maxima pela geracao do arquivo.")
    parser.add_argument("--timeout-download", type=int, default=180, help="Espera maxima pelo download.")
    parser.add_argument("--sem-pausa-final", action="store_true", help="Fecha sem aguardar ENTER no final.")
    return parser


def main():
    args = build_parser().parse_args()
    script_path = resolve_eproc_script(args.script)
    processos = read_process_list(Path(args.processos_file))
    if not processos:
        raise ValueError("Nenhum processo valido foi encontrado na lista.")

    downloads_dir = Path(args.downloads).resolve()
    logs_dir = Path(args.logs).resolve()
    downloads_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = logs_dir / f"download_eproc_execucao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    module = load_eproc_module(script_path)
    automacao = module.EprocAutomation(
        download_path=str(downloads_dir),
        log_dir=str(logs_dir),
        timeout=args.timeout,
        generation_timeout=args.espera_geracao,
        download_timeout=args.timeout_download,
    )

    pendentes, pulados = automacao.split_pending_processes(processos)
    for numero_processo, arquivos_existentes in pulados:
        automacao.register_skipped_process(numero_processo, arquivos_existentes)

    with log_path.open("w", encoding="utf-8") as log_file:
        tee = Tee(sys.stdout, log_file)
        with redirect_stdout(tee), redirect_stderr(tee):
            print(f"Log de execucao: {log_path}")
            print(f"Script base do eproc: {script_path}")
            try:
                if not pendentes:
                    automacao.exibir_relatorio(total_lista=len(processos))
                    return

                automacao.configurar_navegador()
                automacao.abrir_eproc()
                automacao.aguardar_login()
                automacao.processar_lista(pendentes, intervalo=args.intervalo, total_lista=len(processos))
            finally:
                if not args.sem_pausa_final:
                    try:
                        input("\nPressione ENTER para fechar o navegador e finalizar...")
                    except EOFError:
                        pass
                automacao.fechar()


if __name__ == "__main__":
    main()

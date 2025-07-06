# modules/file_cleaner.py
import os
import shutil
from pathlib import Path
from .constants import PATHS_TO_CLEAN
from .logging import log_message
from colorama import Fore, Style

def clean_files() -> bool:
    success = False
    log_message("\n[*] Procurando arquivos de avaliação...")

    for directory in PATHS_TO_CLEAN:
        path = Path(directory)
        if not path.exists():
            continue

        log_message(f"[*] Limpando diretório: {path}")

        try:
            target_files = [
                "PermanentUserId", "PermanentDeviceId", "*.key",
                "*.license", "bl", "crl"
            ]

            for pattern in target_files:
                for file in path.glob(f"**/{pattern}"):
                    try:
                        if file.is_file():
                            file.unlink()
                            log_message(f"  - Removido: {file}")
                            success = True
                        elif file.is_dir():
                            shutil.rmtree(file)
                            log_message(f"  - Removido diretório: {file}")
                            success = True
                    except Exception as e:
                        log_message(f"  {Fore.YELLOW}[!] Erro ao remover {file}: {e}{Style.RESET_ALL}")

            android_studio_path = Path(os.environ["LOCALAPPDATA"]) / "Google" / "AndroidStudio*"
            for as_dir in android_studio_path.parent.glob(android_studio_path.name):
                try:
                    shutil.rmtree(as_dir)
                    log_message(f"  - Removido cache do Android Studio: {as_dir}")
                    success = True
                except Exception as e:
                    log_message(f"  {Fore.YELLOW}[!] Erro ao remover {as_dir}: {e}{Style.RESET_ALL}")

        except Exception as e:
            log_message(f"{Fore.RED}[×] Erro ao limpar {path}: {e}{Style.RESET_ALL}")

    return success
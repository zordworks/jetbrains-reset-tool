# modules/registry_cleaner.py
import winreg
from .constants import REG_KEYS
from .logging import log_message
from colorama import Fore, Style

def clean_registry() -> bool:
    success = False
    log_message("\n[*] Procurando chaves de registro...")

    for key in REG_KEYS:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_READ) as k:
                log_message(f"[*] Encontrada chave: HKEY_CURRENT_USER\\{key}")

            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key)
                log_message(f"  - Chave removida: HKEY_CURRENT_USER\\{key}")
                success = True
            except PermissionError:
                log_message(f"  {Fore.YELLOW}[!] Permissão negada para deletar chave{Style.RESET_ALL}")
            except Exception as e:
                log_message(f"  {Fore.YELLOW}[!] Erro ao deletar chave: {e}{Style.RESET_ALL}")

        except FileNotFoundError:
            continue

    return success
# modules/process_utils.py
import psutil
import time
from .constants import PRODUCTS
from .logging import log_message
from colorama import Fore, Style

def check_processes() -> list:
    running_processes = []
    for process in PRODUCTS:
        try:
            for proc in psutil.process_iter(['name']):
                if proc.info['name'].lower() == process.lower():
                    running_processes.append(process)
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return running_processes

def close_processes(processes: list) -> bool:
    if not processes:
        return True

    log_message(f"{Fore.YELLOW}[!] Processos rodando: {', '.join(processes)}{Style.RESET_ALL}")

    try:
        for proc in psutil.process_iter():
            if proc.name().lower() in [p.lower() for p in processes]:
                proc.kill()

        time.sleep(2)
        return True
    except Exception as e:
        log_message(f"{Fore.RED}[×] Erro ao fechar processos: {e}{Style.RESET_ALL}")
        return False
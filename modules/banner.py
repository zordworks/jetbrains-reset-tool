# modules/banner.py
import os
import time
from colorama import Fore, Style
import pyfiglet

from modules.constants import VERSION


def show_banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = pyfiglet.figlet_format("DarkWorks", font="slant")
    print(Fore.RED + banner + Style.RESET_ALL)
    animate_text(f"▓▓▓ Reset de Trial JetBrains v{VERSION} ▓▓▓", Fore.CYAN)
    print(Fore.YELLOW + "by DarkWorks Team - " + Fore.RED + "❤" + Style.RESET_ALL)
    print("\n")

def animate_text(text: str, color=Fore.GREEN, delay=0.05):
    for char in text:
        print(f"{color}{char}{Style.RESET_ALL}", end="", flush=True)
        time.sleep(delay)
    print()

def show_error_banner(message: str):
    show_banner()
    print(f"\n{Fore.RED}[×] {message}{Style.RESET_ALL}")

def show_exit_banner():
    show_banner()
    animate_text("Obrigado por usar o DarkWorks Reset Tool!", Fore.CYAN)
    time.sleep(1)
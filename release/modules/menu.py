# modules/menu.py
from colorama import Fore, Style
from . import banner, process_utils, file_cleaner, registry_cleaner
from .constants import VERSION
from utils.animation import AnimationThread


def display_main_menu():
    banner.show_banner()
    print_menu_options()
    return get_user_choice()


def print_menu_options():
    print(f"{Fore.CYAN}╔════════════════════════════════════════╗")
    print(f"║          {Fore.MAGENTA}MENU PRINCIPAL{Fore.CYAN}                ║")
    print(f"╠════════════════════════════════════════╣")
    print(f"║ {Fore.YELLOW}1{Fore.CYAN}. Resetar trial dos produtos JetBrains  ║")
    print(f"║ {Fore.YELLOW}2{Fore.CYAN}. Verificar processos JetBrains          ║")
    print(f"║ {Fore.YELLOW}3{Fore.CYAN}. Limpar apenas arquivos                ║")
    print(f"║ {Fore.YELLOW}4{Fore.CYAN}. Limpar apenas registro                ║")
    print(f"║ {Fore.YELLOW}5{Fore.CYAN}. Sobre este programa                   ║")
    print(f"║ {Fore.YELLOW}0{Fore.CYAN}. Sair                                  ║")
    print(f"╚════════════════════════════════════════╝{Style.RESET_ALL}")


def get_user_choice():
    try:
        choice = input(f"\n{Fore.GREEN}► {Fore.YELLOW}Escolha uma opção:{Style.RESET_ALL} ")
        return int(choice)
    except ValueError:
        return -1


def handle_full_reset():
    banner.show_banner()
    processes = process_utils.check_processes()

    if processes and not process_utils.close_processes(processes):
        input(f"\n{Fore.RED}Não foi possível fechar os processos. Tente manualmente.{Style.RESET_ALL}")
        return

    create_restore_point()

    animation = AnimationThread()
    animation.start()

    success_files = file_cleaner.clean_files()
    success_registry = registry_cleaner.clean_registry()

    animation.stop()

    if success_files or success_registry:
        banner.log_message(f"\n{Fore.GREEN}[✓] Reset concluído com sucesso!{Style.RESET_ALL}")
        banner.log_message(f"{Fore.YELLOW}Você pode agora reiniciar seus aplicativos JetBrains.{Style.RESET_ALL}")
    else:
        banner.log_message(f"\n{Fore.YELLOW}[!] Nenhum dado do JetBrains foi encontrado.{Style.RESET_ALL}")

    input(f"\n{Fore.GREEN}Pressione Enter para continuar...{Style.RESET_ALL}")


def show_about():
    banner.show_banner()
    print_about_info()
    input(f"\n{Fore.GREEN}Pressione Enter para voltar...{Style.RESET_ALL}")


def print_about_info():
    print(f"{Fore.CYAN}╔════════════════════════════════════════╗")
    print(f"║          {Fore.MAGENTA}SOBRE ESTE PROGRAMA{Fore.CYAN}            ║")
    print(f"╠════════════════════════════════════════╣")
    print(f"║ {Fore.YELLOW}Versão:{Fore.CYAN} {VERSION}                          ║")
    print(f"║ {Fore.YELLOW}Desenvolvedor:{Fore.CYAN} DarkWorks Team             ║")
    print(f"║                                        ║")
    print(f"║ {Fore.YELLOW}Descrição:{Fore.CYAN}                                ║")
    print(f"║ Este programa reinicia o período de    ║")
    print(f"║ avaliação dos produtos JetBrains.      ║")
    print(f"║                                        ║")
    print(f"║ {Fore.RED}Aviso:{Fore.CYAN} Use apenas para fins educacionais!   ║")
    print(f"╚════════════════════════════════════════╝{Style.RESET_ALL}")


def create_restore_point():
    # Implementação da criação de ponto de restauração
    pass


def handle_process_check():
    banner.show_banner()
    processes = process_utils.check_processes()
    display_process_results(processes)
    input(f"\n{Fore.GREEN}Pressione Enter para continuar...{Style.RESET_ALL}")


def display_process_results(processes):
    if processes:
        print(f"\n{Fore.RED}Processos JetBrains em execução:{Style.RESET_ALL}")
        for p in processes:
            print(f" - {p}")
    else:
        print(f"\n{Fore.GREEN}Nenhum processo JetBrains está em execução.{Style.RESET_ALL}")


def handle_file_clean():
    banner.show_banner()
    success = file_cleaner.clean_files()
    display_clean_result(success, "arquivos de avaliação")
    input(f"\n{Fore.GREEN}Pressione Enter para continuar...{Style.RESET_ALL}")


def handle_registry_clean():
    banner.show_banner()
    success = registry_cleaner.clean_registry()
    display_clean_result(success, "chaves de registro")
    input(f"\n{Fore.GREEN}Pressione Enter para continuar...{Style.RESET_ALL}")


def display_clean_result(success, item_type):
    if success:
        print(f"\n{Fore.GREEN}[✓] {item_type.capitalize()} removidos!{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}[!] Nenhum {item_type} encontrado.{Style.RESET_ALL}")
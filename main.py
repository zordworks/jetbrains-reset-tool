# main.py - Arquivo principal que orquestra a execução
from modules import (
    banner,
    admin_check,
    logging,
    process_utils,
    file_cleaner,
    registry_cleaner,
    menu,
    constants
)
import sys


def main():
    try:
        if not admin_check.verify_admin():
            banner.show_error_banner("Este programa requer privilégios de administrador!")
            return

        while True:
            choice = menu.display_main_menu()

            if choice == 1:  # Reset completo
                menu.handle_full_reset()
            elif choice == 2:  # Verificar processos
                menu.handle_process_check()
            elif choice == 3:  # Limpar arquivos
                menu.handle_file_clean()
            elif choice == 4:  # Limpar registro
                menu.handle_registry_clean()
            elif choice == 5:  # Sobre
                menu.show_about()
            elif choice == 0:  # Sair
                banner.show_exit_banner()
                break
            else:
                banner.show_error_banner("Opção inválida! Tente novamente.")

    except KeyboardInterrupt:
        banner.show_error_banner("Programa interrompido pelo usuário.")
        sys.exit(0)
    except Exception as e:
        banner.show_error_banner(f"Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
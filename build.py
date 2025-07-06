# build.py
import os
import sys
import subprocess
import platform
import shutil
import importlib.util
from pathlib import Path

# Configurações do projeto
APP_NAME = "JetBrainsTrialReset"
MAIN_SCRIPT = "main.py"
VERSION = "3.0.0"
ICON_PATH = "logo.ico" if os.path.exists("logo.ico") else None
ADDITIONAL_DATA = []

# Dependências necessárias
REQUIREMENTS = [
    'colorama',
    'pyfiglet',
    'psutil',
    'pyinstaller>=5.0',
    'tqdm'
]


def is_tool_installed(name):
    try:
        importlib.util.find_spec(name)
        return True
    except ImportError:
        return False


def verify_project_structure():
    required_dirs = ['modules', 'utils']
    missing = [d for d in required_dirs if not os.path.isdir(d)]
    if missing:
        print(f"\n❌ Diretórios necessários não encontrados: {', '.join(missing)}")
        sys.exit(1)

    if not os.path.exists(MAIN_SCRIPT):
        print(f"\n❌ Arquivo principal '{MAIN_SCRIPT}' não encontrado!")
        sys.exit(1)


def install_dependencies():
    print("\n[1/4] 🛠️ Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        for package in REQUIREMENTS:
            if not is_tool_installed(package.split('>=')[0] if '>=' in package else package):
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        sys.exit(1)


def clean_build_dirs():
    print("\n[2/4] 🧹 Limpando builds anteriores...")
    for item in ['build', 'dist', f'{APP_NAME}.spec']:
        try:
            if os.path.isdir(item):
                shutil.rmtree(item, ignore_errors=True)
            elif os.path.exists(item):
                os.remove(item)
        except Exception as e:
            print(f"⚠️ Não foi possível remover {item}: {e}")


def build_executable():
    print("\n[3/4] 🔨 Compilando aplicativo...")

    try:
        import PyInstaller
        import pyfiglet

        # Configura os argumentos do PyInstaller
        pyinstaller_cmd = [
            sys.executable,
            '-m',
            'PyInstaller',
            '--name', APP_NAME,
            '--onefile',
            '--clean',
            '--noconfirm',
            '--paths', 'modules',
            '--paths', 'utils',
            '--add-data', f'{os.path.dirname(pyfiglet.__file__)}{os.pathsep}pyfiglet',
            '--hidden-import', 'pyfiglet.fonts',
            '--hidden-import', 'importlib.resources',
            '--collect-data', 'pyfiglet',
            '--additional-hooks-dir', '.'
        ]

        if platform.system() == 'Windows':
            pyinstaller_cmd.extend([
                '--windowed',
                '--version-file', 'version_info.txt' if os.path.exists('version_info.txt') else ''
            ])

        if ICON_PATH and os.path.exists(ICON_PATH):
            pyinstaller_cmd.extend(['--icon', ICON_PATH])

        pyinstaller_cmd.append(MAIN_SCRIPT)

        print("Executando:", ' '.join([arg for arg in pyinstaller_cmd if arg]))
        subprocess.check_call([arg for arg in pyinstaller_cmd if arg])

    except Exception as e:
        print(f"\n❌ Erro durante a compilação: {e}")
        print("Tente executar como administrador ou desative o antivírus temporariamente")
        sys.exit(1)


def finalize_build():
    print("\n[4/4] ✨ Finalizando build...")
    executable_name = f"{APP_NAME}.exe" if platform.system() == 'Windows' else APP_NAME
    src_path = os.path.join('dist', executable_name)

    if os.path.exists(src_path):
        try:
            if os.path.exists(executable_name):
                os.remove(executable_name)
            shutil.move(src_path, executable_name)
            print(f"\n✅ Build completo! Executável criado: {executable_name}")
            print(f"📦 Tamanho: {os.path.getsize(executable_name) / 1024 / 1024:.2f} MB")
        except Exception as e:
            print(f"\n⚠️ Erro ao mover executável: {e}")
    else:
        print("\n⚠️ Executável não foi gerado corretamente")


if __name__ == '__main__':
    try:
        print(f"🚀 Iniciando build do {APP_NAME} v{VERSION}")
        verify_project_structure()
        install_dependencies()
        clean_build_dirs()
        build_executable()
        finalize_build()
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        sys.exit(1)
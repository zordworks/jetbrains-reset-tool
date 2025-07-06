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
PORTABLE_DIR = "release"

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
    for item in ['build', 'dist', f'{APP_NAME}.spec', PORTABLE_DIR]:
        try:
            if os.path.isdir(item):
                shutil.rmtree(item, ignore_errors=True)
            elif os.path.exists(item):
                os.remove(item)
        except Exception as e:
            print(f"⚠️ Não foi possível remover {item}: {e}")


def create_version_info():
    """Cria arquivo de informações de versão para Windows"""
    if platform.system() == 'Windows':
        version_file = os.path.join(PORTABLE_DIR, 'version_info.txt')
        if not os.path.exists(version_file):
            print("\nℹ️ Criando version_info.txt para Windows...")
            try:
                version_parts = VERSION.split('.')
                while len(version_parts) < 3:
                    version_parts.append('0')

                major, minor, patch = version_parts[:3]

                content = f"""# UTF-8
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({major}, {minor}, {patch}, 0),
    prodvers=({major}, {minor}, {patch}, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          '040904B0',
          [StringStruct('CompanyName', 'DarkWorks'),
          StringStruct('FileDescription', 'JetBrains Trial Reset Tool'),
          StringStruct('FileVersion', '{VERSION}'),
          StringStruct('InternalName', '{APP_NAME}'),
          StringStruct('LegalCopyright', 'Copyright © DarkWorks Team'),
          StringStruct('OriginalFilename', '{APP_NAME}.exe'),
          StringStruct('ProductName', 'JetBrains Trial Reset'),
          StringStruct('ProductVersion', '{VERSION}')])
      ]),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)"""
                os.makedirs(PORTABLE_DIR, exist_ok=True)
                with open(version_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            except Exception as e:
                print(f"⚠️ Não foi possível criar version_info.txt: {e}")


def build_portable():
    print("\n[3/4] 🔨 Criando versão portable...")

    try:
        # Cria diretório portable
        os.makedirs(PORTABLE_DIR, exist_ok=True)

        # Copia arquivos necessários
        shutil.copytree('modules', os.path.join(PORTABLE_DIR, 'modules'))
        shutil.copytree('utils', os.path.join(PORTABLE_DIR, 'utils'))
        shutil.copy(MAIN_SCRIPT, PORTABLE_DIR)

        if ICON_PATH and os.path.exists(ICON_PATH):
            shutil.copy(ICON_PATH, PORTABLE_DIR)

        # Cria o launcher.exe com PyInstaller mantendo os metadados
        import PyInstaller.__main__

        pyinstaller_args = [
            '--name', 'launcher',
            '--onefile',
            '--clean',
            '--noconfirm',
            '--paths', 'modules',
            '--paths', 'utils',
            '--add-data', f'{os.path.dirname(importlib.util.find_spec("pyfiglet").origin)}{os.pathsep}pyfiglet',
            '--hidden-import', 'pyfiglet.fonts',
            '--hidden-import', 'importlib.resources',
            '--collect-data', 'pyfiglet',
            '--additional-hooks-dir', '.',
            '--version-file', os.path.join(PORTABLE_DIR, 'version_info.txt') if os.path.exists(
                os.path.join(PORTABLE_DIR, 'version_info.txt')) else '',
            '--icon', ICON_PATH if ICON_PATH and os.path.exists(ICON_PATH) else '',
            os.path.join(PORTABLE_DIR, MAIN_SCRIPT)
        ]

        # Filtra argumentos vazios
        pyinstaller_args = [arg for arg in pyinstaller_args if arg]

        print("Compilando launcher.exe com os metadados...")
        PyInstaller.__main__.run(pyinstaller_args)

        # Move o launcher.exe para a pasta portable
        if os.path.exists(os.path.join('dist', 'launcher.exe')):
            shutil.move(os.path.join('dist', 'launcher.exe'), os.path.join(PORTABLE_DIR, 'launcher.exe'))
            print("\n✅ Launcher criado com sucesso!")
        else:
            print("\n⚠️ Launcher não foi gerado corretamente")

    except Exception as e:
        print(f"\n❌ Erro ao criar versão portable: {e}")
        sys.exit(1)


def finalize_build():
    print("\n[4/4] 📦 Finalizando versão portable...")

    try:
        # Cria arquivo ZIP com a versão portable
        shutil.make_archive(f"{APP_NAME}_Portable_v{VERSION}", 'zip', PORTABLE_DIR)
        print(f"\n✅ Versão portable criada em: {APP_NAME}_Portable_v{VERSION}.zip")

        # Mostra informações do arquivo
        zip_path = f"{APP_NAME}_Portable_v{VERSION}.zip"
        if os.path.exists(zip_path):
            size_mb = os.path.getsize(zip_path) / (1024 * 1024)
            print(f"📦 Tamanho: {size_mb:.2f} MB")
            print(f"📂 Local: {os.path.abspath(zip_path)}")
    except Exception as e:
        print(f"\n⚠️ Erro ao empacotar versão portable: {e}")


if __name__ == '__main__':
    try:
        print(f"🚀 Iniciando build portable do {APP_NAME} v{VERSION}")
        verify_project_structure()
        install_dependencies()
        clean_build_dirs()
        create_version_info()
        build_portable()
        finalize_build()
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        sys.exit(1)
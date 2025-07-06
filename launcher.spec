# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

datas = [('C:\\Users\\arthu\\PycharmProjects\\jetbrains_reset_tool\\.venv\\Lib\\site-packages\\pyfiglet', 'pyfiglet')]
datas += collect_data_files('pyfiglet')


a = Analysis(
    ['compilado\\main.py'],
    pathex=['modules', 'utils'],
    binaries=[],
    datas=datas,
    hiddenimports=['pyfiglet.fonts', 'importlib.resources'],
    hookspath=['.'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='compilado\\version_info.txt',
    icon=['logo.ico'],
)

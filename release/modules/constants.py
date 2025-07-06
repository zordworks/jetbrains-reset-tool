# modules/constants.py
import os
from pathlib import Path

VERSION = "3.0"
LOG_FILE = os.path.join(os.environ["TEMP"], "jetbrains_reset_log.txt")

PRODUCTS = [
    "idea64.exe", "pycharm64.exe", "webstorm64.exe", "phpstorm64.exe",
    "rider64.exe", "datagrip64.exe", "clion64.exe", "goland64.exe", "rubymine64.exe",
    "idea.exe", "pycharm.exe", "webstorm.exe", "phpstorm.exe", "rider.exe",
    "datagrip.exe", "clion.exe", "goland.exe", "rubymine.exe"
]

PATHS_TO_CLEAN = [
    os.path.join(os.environ["APPDATA"], "JetBrains"),
    os.path.join(os.environ["LOCALAPPDATA"], "JetBrains"),
    os.path.join(os.environ["USERPROFILE"], ".JetBrains"),
    os.path.join(os.environ["USERPROFILE"], ".IntelliJIdea"),
    os.path.join(os.environ["USERPROFILE"], ".PyCharm")
]

REG_KEYS = [
    r"Software\JavaSoft",
    r"Software\JetBrains",
    r"Software\Google\AndroidStudio"
]
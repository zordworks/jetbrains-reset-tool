# modules/logging.py
from datetime import datetime
from colorama import Fore, Style
from .constants import LOG_FILE

def log_message(message: str, log_file=LOG_FILE):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(message)
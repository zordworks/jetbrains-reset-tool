# utils/animation.py
import threading
import time
from colorama import Fore

class AnimationThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def run(self):
        spinner = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        i = 0
        while self.running:
            print(f"\r{Fore.YELLOW}{spinner[i]} {Fore.RESET}", end="")
            i = (i + 1) % len(spinner)
            time.sleep(0.1)

    def stop(self):
        self.running = False
        time.sleep(0.2)
        print("\r", end="")
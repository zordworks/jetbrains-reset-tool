# modules/admin_check.py
import ctypes

def verify_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
import winreg
import sys


RUN_KEY = r"Software\Microsoft\Windows\CurrentVersion\Run"
APP_NAME = "BrightnessControl"


def is_autostart_enabled():
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            RUN_KEY,
            0,
            winreg.KEY_READ
        ) as key:
            winreg.QueryValueEx(key, APP_NAME)
            return True
        
    except FileNotFoundError:
        return False
    

def enable_autostart():
    app_path = sys.executable

    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        RUN_KEY,
        0,
        winreg.KEY_SET_VALUE
    ) as key:
        winreg.SetValueEx(
            key,
            APP_NAME,
            0,
            winreg.REG_SZ,
            app_path
        )


def disable_autostart():
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            RUN_KEY,
            0,
            winreg.KEY_SET_VALUE
        ) as key:
            winreg.DeleteValue(key, APP_NAME)

    except FileNotFoundError:
        pass
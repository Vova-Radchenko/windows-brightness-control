import pystray
import sys
import threading
from PIL import Image
from pathlib import Path
from app.hotkeys import reload_hotkeys
from app.autostart import (
    enable_autostart,
    disable_autostart,
    is_autostart_enabled
)


def create_icon_image():
    icon_path = get_resourse_path("assets/brightness.ico")

    return Image.open(icon_path)


def on_exit(icon, item):
    icon.stop()


def start_tray():
    icon = pystray.Icon(
        "Brightness Control",
        create_icon_image(),
        "Brightness Control",
        menu=pystray.Menu(
            pystray.MenuItem(
                "Brightness Control",
                None,
                enabled=False
            ),

            pystray.Menu.SEPARATOR,

            pystray.MenuItem(
                "Start with Windows",
                on_toggle_autostart,
                checked=lambda item: is_autostart_enabled()
            ),

            pystray.MenuItem(
                "Settings",
                on_open_settings
            ),

            pystray.MenuItem(
                "Reload Settings",
                on_reload_settings
            ),

            pystray.MenuItem(
                "Exit",
                on_exit
            )
        )
    )

    icon.run()


def on_reload_settings(icon, item):
    reload_hotkeys()


def on_toggle_autostart(icon, item):
    if is_autostart_enabled():
        disable_autostart()
        print("Autostart disabled")
    else:
        enable_autostart()
        print("Autostart enabled")

    icon.update_menu()


def get_resourse_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path.cwd()

    return base_path / relative_path


def on_open_settings(icon, item):
    from app.settings_window import open_settings_window

    settings_thread = threading.Thread(
        target=open_settings_window,
        daemon=True
    )

    settings_thread.start()
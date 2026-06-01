import pystray
from PIL import Image, ImageDraw
from app.hotkeys import reload_hotkeys
from app.autostart import (
    enable_autostart,
    disable_autostart,
    is_autostart_enabled
)


def create_icon_image():
    image = Image.new("RGB", (64, 64), "black")
    draw = ImageDraw.Draw(image)

    draw.ellipse((16, 16, 48, 48), fill="white")

    return image


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
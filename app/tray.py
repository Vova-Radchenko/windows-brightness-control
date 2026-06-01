import pystray
from PIL import Image, ImageDraw
from app.hotkeys import reload_hotkeys


def create_icon_image():
    image = Image.new("RGB", (64, 64), "black")
    draw = ImageDraw.Draw(image)

    draw.ellipse((16, 16, 48, 48), fill="white")

    return image


def on_exit(icon):
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


def on_reload_settings(icon):
    reload_hotkeys()
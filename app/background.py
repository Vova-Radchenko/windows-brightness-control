import threading

from app.hotkeys import register_hotkeys
from app.overlay import start_overlay_loop
from app.tray import start_tray


def start_background():
    print("Brightness Control is running in background mode")
    print("Press Ctrl+C to stop")

    overlay_thread = threading.Thread(
        target=start_overlay_loop,
        daemon=True
    )

    overlay_thread.start()

    register_hotkeys()

    start_tray()
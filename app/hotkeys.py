import keyboard
from app.overlay import show_overlay
from app.brightness_service import (
    decrease_brightness,
    increase_brightness
)
from app.settings_service import get_brightness_step


def register_hotkeys():
    keyboard.add_hotkey(
        "ctrl+alt+up",
        lambda: show_overlay(
            increase_brightness(get_brightness_step())
        )
    )

    keyboard.add_hotkey(
        "ctrl+alt+down",
        lambda: show_overlay(
            decrease_brightness(get_brightness_step())
        )
    )

    print("Hotkeys registered")
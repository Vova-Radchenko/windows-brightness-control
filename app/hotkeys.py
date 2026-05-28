import keyboard
from app.overlay import show_overlay

from app.brightness_service import (
    decrease_brightness,
    increase_brightness
)
from app.constants import BRIGHTNESS_STEP


def register_hotkeys():
    keyboard.add_hotkey(
        "ctrl+alt+up",
        lambda: show_overlay(
            increase_brightness(BRIGHTNESS_STEP)
        )
    )

    keyboard.add_hotkey(
        "ctrl+alt+down",
        lambda: show_overlay(
            decrease_brightness(BRIGHTNESS_STEP)
        )
    )

    print("Hotkeys registered")
import keyboard
from app.overlay import show_overlay
from app.brightness_service import (
    decrease_brightness,
    increase_brightness
)
from app.settings_service import (
    get_brightness_step,
    get_increase_hotkey,
    get_decrease_hotkey,
    get_round_brightness_to_step
)


increase_hotkey = None
decrease_hotkey = None


def register_hotkeys():
    global increase_hotkey
    global decrease_hotkey

    increase_hotkey = keyboard.add_hotkey(
        get_increase_hotkey(),
        lambda: show_overlay(
            increase_brightness(
                get_brightness_step(),
                get_round_brightness_to_step()
            )
        )
    )

    decrease_hotkey = keyboard.add_hotkey(
        get_decrease_hotkey(),
        lambda: show_overlay(
            decrease_brightness(
                get_brightness_step(),
                get_round_brightness_to_step()
            )
        )
    )

    print("Hotkeys registered")


def unregister_hotkeys():
    global increase_hotkey
    global decrease_hotkey

    if increase_hotkey is not None:
        keyboard.remove_hotkey(increase_hotkey)
        increase_hotkey = None

    if decrease_hotkey is not None:
        keyboard.remove_hotkey(decrease_hotkey)
        decrease_hotkey = None


def reload_hotkeys():
    unregister_hotkeys()
    register_hotkeys()

    print("Hotkeys reloaded")
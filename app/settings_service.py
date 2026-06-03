import json
from pathlib import Path


SETTINGS_FILE = "settings.json"
DEFAULT_SETTINGS = {
    "brightness_step": 10,
    "hotkeys": {
        "increase": "ctrl+alt+up",
        "decrease": "ctrl+alt+down"
    }
}


def load_settings():
    if not Path(SETTINGS_FILE).exists():
        return DEFAULT_SETTINGS

    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)

    except json.JSONDecodeError:
        return DEFAULT_SETTINGS

    return settings


def get_brightness_step():
    settings = load_settings()

    return settings.get(
        "brightness_step",
        DEFAULT_SETTINGS["brightness_step"]
    )


def get_increase_hotkey():
    settings = load_settings()
    hotkeys = settings.get(
        "hotkeys",
        DEFAULT_SETTINGS["hotkeys"]
    )

    return hotkeys.get(
        "increase",
        DEFAULT_SETTINGS["hotkeys"]["increase"]
    )


def get_decrease_hotkey():
    settings = load_settings()
    hotkeys = settings.get(
        "hotkeys",
        DEFAULT_SETTINGS["hotkeys"]
    )

    return hotkeys.get(
        "decrease",
        DEFAULT_SETTINGS["hotkeys"]["decrease"]
    )


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)
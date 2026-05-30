import json


SETTINGS_FILE = "settings.json"


def load_settings():
    with open(SETTINGS_FILE, "r") as file:
        settings = json.load(file)

    return settings


def get_brightness_step():
    settings = load_settings()

    return settings["brightness_step"]


def get_increase_hotkey():
    settings = load_settings()

    return settings["hotkeys"]["increase"]


def get_decrease_hotkey():
    settings = load_settings()

    return settings["hotkeys"]["decrease"]
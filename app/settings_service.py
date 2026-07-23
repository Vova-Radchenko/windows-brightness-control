import json
import os
from copy import deepcopy
from pathlib import Path

APP_NAME = "BrightnessControl"

LOCAL_APP_DATA = os.getenv("LOCALAPPDATA")

if LOCAL_APP_DATA:
    SETTINGS_DIRECTORY = Path(LOCAL_APP_DATA) / APP_NAME
else:
    SETTINGS_DIRECTORY = Path.home() / f".{APP_NAME}"

SETTINGS_FILE = SETTINGS_DIRECTORY / "settings.json"

DEFAULT_SETTINGS = {
    "brightness_step": 10,
    "hotkeys": {
        "increase": "ctrl+alt+up",
        "decrease": "ctrl+alt+down"
    },
    "round_brightness_to_step": False
}


def load_settings():
    if not SETTINGS_FILE.exists():
        return deepcopy(DEFAULT_SETTINGS)

    try:
        with SETTINGS_FILE.open("r", encoding="utf-8") as file:
            settings = json.load(file)

    except (json.JSONDecodeError, OSError):
        return deepcopy(DEFAULT_SETTINGS)

    merged_settings = merge_default_settings(settings)

    if merged_settings != settings:
        save_settings(merged_settings)

    return merged_settings


def merge_default_settings(settings):
    merged = deepcopy(DEFAULT_SETTINGS)

    merged.update(settings)

    if "hotkeys" in settings:
        merged["hotkeys"].update(settings["hotkeys"])

    return merged


def get_brightness_step():
    settings = load_settings()

    return settings.get(
        "brightness_step",
        DEFAULT_SETTINGS["brightness_step"]
    )


def get_round_brightness_to_step():
    settings = load_settings()
    return settings["round_brightness_to_step"]


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
    SETTINGS_DIRECTORY.mkdir(parents=True, exist_ok=True)

    with SETTINGS_FILE.open("w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)
import os
import json
from pathlib import Path


def get_settings_path() -> Path:
    local_appdata = Path(os.getenv("LOCALAPPDATA"))
    settings_path = local_appdata / "Packages" / \
        "Microsoft.WindowsTerminal_8wekyb3d8bbwe" / "LocalState" / "settings.json"
    return settings_path if settings_path.exists() else None


def set_background_image(image_path: str):
    settings_path = get_settings_path()
    if not settings_path:
        return

    with open(settings_path, encoding="utf-8") as f:
        settings = json.load(f)

    profiles = settings.get("profiles", {})

    defaults = profiles.get("defaults", {})
    defaults["backgroundImage"] = image_path.replace("\\", "/")
    defaults["backgroundImageStretchMode"] = "uniformToFill"

    profiles["defaults"] = defaults
    settings["profiles"] = profiles

    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)


def remove_background_image():
    settings_path = get_settings_path()
    if not settings_path:
        return

    with open(settings_path, encoding="utf-8") as f:
        settings = json.load(f)

    profiles = settings.get("profiles", {})
    defaults = profiles.get("defaults", {})

    defaults.pop("backgroundImage", None)
    defaults.pop("backgroundImageOpacity", None)
    defaults.pop("backgroundImageStretchMode", None)

    profiles["defaults"] = defaults
    settings["profiles"] = profiles

    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

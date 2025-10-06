import os
import json
from pathlib import Path

def get_settings_path() -> Path:
    base_path = Path(os.getenv("LOCALAPPDATA"))
    return base_path / r"Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"

def set_background_image(image_path: str):
    settings_path = get_settings_path()

    with open(settings_path, encoding="utf-8") as f:
        settings = json.load(f)

    default_profile_guid = settings.get("defaultProfile")
    profiles = settings.get("profiles", {}).get("list", [])

    for profile in profiles:
        if profile.get("guid") == default_profile_guid:
            profile["backgroundImage"] = image_path.replace("\\", "/")  
            profile["backgroundImageOpacity"] = 0.7  
            profile["backgroundImageStretchMode"] = "uniformToFill" 
            break

    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)


def remove_background_image():
    settings_path = get_settings_path()

    with open(settings_path, encoding="utf-8") as f:
        settings = json.load(f)

    default_profile_guid = settings.get("defaultProfile")
    profiles = settings.get("profiles", {}).get("list", [])

    for profile in profiles:
        if profile.get("guid") == default_profile_guid:
            profile.pop("backgroundImage", None)
            profile.pop("backgroundImageOpacity", None)
            profile.pop("backgroundImageStretchMode", None)
            break

    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)


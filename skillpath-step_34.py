# === Stage 34: Add support for multiple local user profiles ===
# Project: SkillPath
import os
import json

PROFILES_DIR = "profiles"
DEFAULT_PROFILE = "default"

def get_profile_dir():
    os.makedirs(PROFILES_DIR, exist_ok=True)
    return PROFILES_DIR

def get_profile_path(profile_name):
    return os.path.join(get_profile_dir(), f"{profile_name}.json")

def get_profile_data(profile_name=None):
    if profile_name is None:
        profile_name = DEFAULT_PROFILE
    path = get_profile_path(profile_name)
    if not os.path.exists(path):
        data = {
            "name": profile_name,
            "goals": [],
            "practice_logs": [],
            "resources": [],
            "milestones": [],
        }
        save_profile_data(profile_name, data)
        return data
    with open(path, "r") as f:
        return json.load(f)

def save_profile_data(profile_name, data):
    path = get_profile_path(profile_name)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def list_profiles():
    profiles = []
    for name in os.listdir(get_profile_dir()):
        if name.endswith(".json"):
            profiles.append(name[:-5])
    return profiles

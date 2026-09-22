# === Stage 35: Add active user switching and user-specific records ===
# Project: SkillPath
import json
from pathlib import Path

SKILL_PATH = Path(__file__).parent
DATABASE = SKILL_PATH / "skillpath.db"


class UserStore:
    def __init__(self):
        with open(DATABASE, "w") as f:
            json.dump({}, f)

    def get_users(self):
        with open(DATABASE, "r") as f:
            return json.load(f)

    def save_users(self, users):
        with open(DATABASE, "w") as f:
            json.dump(users, f, indent=2)

    def add_user(self, name, goals=None, practice_logs=None):
        users = self.get_users()
        if name in users:
            print(f"User '{name}' already exists.")
            return
        user = {"name": name, "goals": goals or [], "practice_logs": practice_logs or []}
        users[name] = user
        self.save_users(users)
        print(f"Welcome, {name}! Your skill tracker is ready.")

    def switch_user(self, name):
        users = self.get_users()
        if name not in users:
            print(f"User '{name}' not found. Add them first.")
            return False
        self.current_user = name
        print(f"Switched to user: {name}")
        return True

    def get_current_user(self):
        users = self.get_users()
        if not hasattr(self, "current_user"):
            print("No active user. Switch to one first.")
            return None
        return users.get(self.current_user)

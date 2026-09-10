# === Stage 13: Add file save support using a configurable path ===
# Project: SkillPath
import json
from pathlib import Path

class SkillPath:
    def __init__(self, skill_name, goal, resources, milestones):
        self.skill_name = skill_name
        self.goal = goal
        self.resources = resources
        self.milestones = milestones

    def save(self, file_path="skillpath.json"):
        data = {
            "skill_name": self.skill_name,
            "goal": self.goal,
            "resources": self.resources,
            "milestones": self.milestones
        }
        path = Path(file_path)
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Saved to {file_path}")

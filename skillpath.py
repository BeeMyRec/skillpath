# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: SkillPath
import json
from datetime import datetime, timedelta

class SkillPathApp:
    def __init__(self):
        self.goals = []
        self.practice_logs = []
        self.resources = []
        self.milestones = []
        self._load_demo()

    def _load_demo(self):
        demo = [
            {"goal": "Learn Python basics", "progress": 75, "created": "2025-01-15"},
            {"goal": "Master data structures", "progress": 30, "created": "2025-02-01"},
            {"goal": "Build web apps", "progress": 10, "created": "2025-03-10"},
        ]
        for g in demo:
            self.goals.append({**g, "id": len(self.goals) + 1})
        demo_logs = [
            {"goal": "Learn Python basics", "hours": 2.5, "date": "2025-01-16"},
            {"goal": "Learn Python basics", "hours": 3.0, "date": "2025-01-20"},
            {"goal": "Master data structures", "hours": 1.5, "date": "2025-02-05"},
        ]
        for l in demo_logs:
            self.practice_logs.append({**l, "id": len(self.practice_logs) + 1})
        demo_resources = [
            {"title": "Python for Beginners", "url": "https://example.com/py101", "type": "tutorial"},
            {"title": "Data Structures Handbook", "url": "https://example.com/dsh", "type": "book"},
        ]
        for r in demo_resources:
            self.resources.append({**r, "id": len(self.resources) + 1})
        demo_milestones = [
            {"goal": "Learn Python basics", "description": "Completed intro chapters", "date": "2025-01-25"},
        ]
        for m in demo_milestones:
            self.milestones.append({**m, "id": len(self.milestones) + 1})

    def get_summary(self):
        return {
            "goals": len(self.goals),
            "practice_hours": sum(l["hours"] for l in self.practice_logs),
            "resources": len(self.resources),
            "milestones": len(self.milestones),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    def save_state(self, path="skillpath_state.json"):
        state = {
            "goals": self.goals,
            "practice_logs": self.practice_logs,
            "resources": self.resources,
            "milestones": self.milestones,
        }
        with open(path, "w") as f:
            json.dump(state, f, indent=2)

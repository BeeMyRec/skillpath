# === Stage 11: Add JSON export for the current application state ===
# Project: SkillPath
import json

def export_state():
    state = {
        "goals": list(GOALS.values()),
        "practice_logs": list(PRACTICE_LOGS.values()),
        "resources": list(RESOURCES.values()),
        "milestones": list(MILESTONES.values()),
    }
    return json.dumps(state, indent=2)

if __name__ == "__main__":
    print(export_state())

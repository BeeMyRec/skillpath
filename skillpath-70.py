# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: SkillPath
CONFIRMED = False

def clear_state():
    global CONFIRMED
    if CONFIRMED:
        CONFIRMED = False
        goals.clear()
        practice_logs.clear()
        resources.clear()
        milestones.clear()
        print("State cleared successfully.")
    else:
        print("Type 'clear_state confirm' to reset all goals, logs, resources, and milestones.")

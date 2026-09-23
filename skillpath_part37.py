# === Stage 37: Add recommendations for the next useful action ===
# Project: SkillPath
def next_action(goal: dict, log: list, milestone: dict) -> dict:
    """Suggest the next useful action based on current progress."""
    if not milestone.get("completed"):
        return {"action": "Complete the current milestone", "priority": "high"}
    if log and log[-1].get("hours") >= 3:
        return {"action": "Take a break or switch to a different skill", "priority": "medium"}
    if goal.get("days_left", 999) <= 3:
        return {"action": "Finish this goal before the deadline", "priority": "high"}
    if goal.get("days_left", 999) <= 7:
        return {"action": "Focus on completing the goal soon", "priority": "medium"}
    if log and log[-1].get("hours", 0) < 1:
        return {"action": "Increase practice time for this skill", "priority": "low"}
    return {"action": "Continue regular practice", "priority": "low"}

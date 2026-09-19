# === Stage 27: Add monthly summary calculations ===
# Project: SkillPath
def monthly_summary(goals, logs):
    """Return a dict with goals completed, hours practiced, and streak days."""
    month = logs[-1]["month"] if logs else "N/A"
    completed = sum(1 for g in goals if g["completed"] and g["month"] == month)
    hours = sum(log["hours"] for log in logs if log["month"] == month)
    days = sorted(set(log["date"] for log in logs if log["month"] == month))
    streak = 0
    for i in range(len(days) - 1, -1, -1):
        if (days[i] - days[i - 1]).days == 1:
            streak += 1
        else:
            break
    return {"month": month, "completed": completed, "hours": hours, "streak": streak}

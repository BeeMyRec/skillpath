# === Stage 26: Add weekly summary calculations ===
# Project: SkillPath
def weekly_summary(logs, goals):
    today = datetime.date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    week_logs = [l for l in logs if week_start <= l["date"] <= week_end]
    total_minutes = sum(l.get("duration", 0) for l in week_logs)
    active_days = len(set(l["date"] for l in week_logs))
    goal_progress = {
        g["name"]: sum(1 for l in week_logs if l.get("goal_id") == g["id"])
        for g in goals
    }
    summary = {
        "week_start": week_start,
        "week_end": week_end,
        "active_days": active_days,
        "total_minutes": total_minutes,
        "goal_progress": goal_progress,
    }
    return summary

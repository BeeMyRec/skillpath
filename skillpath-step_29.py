# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: SkillPath
from datetime import datetime, timedelta

def upcoming_goals(goals, days_ahead=30):
    """Return goals due within the next N days, sorted by due date."""
    now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    deadline = now + timedelta(days=days_ahead)
    return [
        g for g in goals
        if g.get("deadline") and g["deadline"].replace(hour=0, minute=0, second=0, microsecond=0) <= deadline
    ]

def upcoming_practice_logs(logs, days_ahead=7):
    """Return practice logs scheduled within the next N days."""
    now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    deadline = now + timedelta(days=days_ahead)
    return [
        log for log in logs
        if log.get("scheduled_date") and log["scheduled_date"].replace(hour=0, minute=0, second=0, microsecond=0) <= deadline
    ]

def upcoming_milestones(milestones, days_ahead=30):
    """Return milestones due within the next N days."""
    now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    deadline = now + timedelta(days=days_ahead)
    return [
        m for m in milestones
        if m.get("target_date") and m["target_date"].replace(hour=0, minute=0, second=0, microsecond=0) <= deadline
    ]

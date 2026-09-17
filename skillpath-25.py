# === Stage 25: Add daily summary calculations ===
# Project: SkillPath
def daily_summary(records):
    if not records:
        return {"total_practice": 0, "total_streak": 0, "avg_practice": 0, "last_practice": None}
    
    total_practice = sum(r.get("practice_minutes", 0) for r in records)
    last_practice = max((r.get("date") for r in records if r.get("date")), default=None)
    days = sorted(set(r.get("date") for r in records if r.get("date")))
    streak = 0
    for i in range(len(days) - 1, -1, -1):
        if (days[i] - timedelta(days=1)).date() in days:
            streak += 1
        else:
            break
    avg_practice = total_practice / len(records) if records else 0
    return {"total_practice": total_practice, "total_streak": streak, "avg_practice": avg_practice, "last_practice": last_practice}

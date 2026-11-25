# === Stage 66: Add export of a short status dashboard ===
# Project: SkillPath
def export_status_dashboard(data):
    goals = data.get("goals", [])
    logs = data.get("practice_logs", [])
    milestones = data.get("milestones", [])
    total_hours = sum(log.get("hours", 0) for log in logs)
    completed_goals = sum(1 for g in goals if g.get("completed"))
    total_goals = len(goals) or 1
    completed_milestones = sum(1 for m in milestones if m.get("completed"))
    total_milestones = len(milestones) or 1
    today = data.get("today", "N/A")
    lines = [
        "SKILLPATH STATUS DASHBOARD",
        "=========================",
        f"Date: {today}",
        f"Goals completed: {completed_goals}/{total_goals}",
        f"Milestones reached: {completed_milestones}/{total_milestones}",
        f"Total practice hours: {total_hours:.1f}",
        "",
        "GOALS",
        "-----",
    ]
    for g in goals:
        name = g.get("name", "Untitled")
        status = "DONE" if g.get("completed") else "ONGOING"
        progress = g.get("progress", 0)
        lines.append(f"- [{status}] {name} ({progress}%)")
    lines.append("")
    lines.append("MILESTONES")
    lines.append("----------")
    for m in milestones:
        name = m.get("name", "Untitled")
        status = "REACHED" if m.get("completed") else "PENDING"
        lines.append(f"- [{status}] {name}")
    lines.append("")
    lines.append("RECENT PRACTICE")
    lines.append("---------------")
    for log in logs[-5:]:
        subject = log.get("subject", "General")
        hours = log.get("hours", 0)
        date = log.get("date", "N/A")
        lines.append(f"- {subject}: {hours}h on {date}")
    return "\n".join(lines)

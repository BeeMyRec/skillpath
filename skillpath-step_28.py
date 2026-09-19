# === Stage 28: Add overdue item detection based on due dates ===
# Project: SkillPath
def detect_overdue(items, today=None):
    """Return list of item dicts whose due_date is past, sorted earliest first."""
    if today is None:
        today = datetime.date.today()
    overdue = []
    for item in items:
        due = item.get("due_date", item.get("due"))
        if due and isinstance(due, datetime.date) and due < today:
            overdue.append({
                "title": item.get("title", item.get("name", "")),
                "due_date": due,
                "days_overdue": (today - due).days,
                "priority": item.get("priority", "medium"),
            })
    overdue.sort(key=lambda x: x["due_date"])
    return overdue

# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: SkillPath
def generate_changelog(activity_log, max_entries=10):
    """Generate a compact changelog from the activity log."""
    entries = activity_log.get("entries", [])
    if not entries:
        return "No activity recorded yet."
    lines = ["SkillPath Changelog"]
    for entry in entries[-max_entries:]:
        date = entry.get("date", "Unknown")
        action = entry.get("action", "unknown")
        detail = entry.get("detail", "")
        if detail:
            lines.append(f"- {date}: {action} - {detail}")
        else:
            lines.append(f"- {date}: {action}")
    return "\n".join(lines)

def load_activity_log(path="activity_log.json"):
    """Load the activity log from a JSON file."""
    import json
    if not os.path.exists(path):
        return {"entries": []}
    with open(path, "r") as f:
        return json.load(f)

def save_activity_log(data, path="activity_log.json"):
    """Save the activity log to a JSON file."""
    import json
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def add_activity_entry(path="activity_log.json", date=None, action=None, detail=None):
    """Add a new entry to the activity log."""
    import json
    if date is None:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
    log = load_activity_log(path)
    log.setdefault("entries", []).append({
        "date": date,
        "action": action,
        "detail": detail,
    })
    save_activity_log(log, path)
    return log

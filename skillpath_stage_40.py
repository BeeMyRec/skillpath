# === Stage 40: Add plain text report export ===
# Project: SkillPath
def export_report(data, path):
    """Write a plain text report of goals, logs, resources, and milestones."""
    lines = []
    lines.append("SkillPath Report")
    lines.append("=" * 20)
    lines.append("")
    goals = data.get("goals", [])
    logs = data.get("logs", [])
    resources = data.get("resources", [])
    milestones = data.get("milestones", [])
    lines.append("GOALS")
    for g in goals:
        lines.append(f"- {g.get('title', 'Untitled')} ({g.get('status', 'active')})")
    lines.append("")
    lines.append("PRACTICE LOGS")
    for l in logs:
        lines.append(f"- {l.get('date', '')}: {l.get('note', '')}")
    lines.append("")
    lines.append("RESOURCES")
    for r in resources:
        lines.append(f"- {r.get('title', '')} ({r.get('type', '')})")
    lines.append("")
    lines.append("MILESTONES")
    for m in milestones:
        lines.append(f"- {m.get('title', '')} ({m.get('date', '')})")
    lines.append("")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    return path

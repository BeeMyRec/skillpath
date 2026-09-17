# === Stage 24: Add grouped summaries by category or status ===
# Project: SkillPath
def grouped_summaries(data, group_by):
    """Group entries by a key and return a compact summary dict.
    data: list of dicts, e.g. practice_logs
    group_by: field name to group by (str)
    """
    groups = {}
    for entry in data:
        key = entry[group_by]
        groups.setdefault(key, []).append(entry)
    summary = {}
    for key, items in groups.items():
        summary[key] = {
            "count": len(items),
            "avg_minutes": round(sum(e.get("minutes", 0) for e in items) / len(items), 1)
            if items else 0,
            "total_minutes": sum(e.get("minutes", 0) for e in items),
            "latest_date": max((e.get("date", "") for e in items), default=""),
        }
    return summary

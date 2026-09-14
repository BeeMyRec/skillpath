# === Stage 20: Add duplicate detection for newly created records ===
# Project: SkillPath
def find_duplicates(records, field):
    """Identify records with duplicate values in the specified field."""
    seen = {}
    for record in records:
        key = record.get(field)
        if key is not None:
            if key in seen:
                seen[key].append(record)
            else:
                seen[key] = [record]
    return {k: v for k, v in seen.items() if len(v) > 1}

# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: SkillPath
def filter_entries(entries, **kwargs):
    """Filter skill entries by status, category, owner, or tag."""
    for key, value in kwargs.items():
        if value is not None:
            entries = [e for e in entries if getattr(e, key, '').lower() == value.lower()]
    return entries

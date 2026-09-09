# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: SkillPath
def sort_records(records, sort_key='title'):
    """Sort a list of record dicts by a chosen key.

    Supported keys: title, date, priority, last_updated.
    Keys are case-insensitive and accept 'title', 'date',
    'priority', or 'last_updated'.
    """
    key_map = {
        'title': 'title',
        'date': 'date',
        'priority': 'priority',
        'last_updated': 'last_updated',
    }
    key = key_map.get(sort_key.lower().replace(' ', '_'))
    if key is None:
        raise ValueError(f"Unknown sort key: {sort_key!r}")
    return sorted(records, key=lambda r: r.get(key, ''))

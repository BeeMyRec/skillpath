# === Stage 45: Add restore from backup with validation ===
# Project: SkillPath
def restore_from_backup(path, validate=True):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Backup file not found: {path}")
    with open(path, 'r') as f:
        backup = json.load(f)
    if not isinstance(backup, dict):
        raise ValueError("Invalid backup structure")
    if validate:
        for key in ['goals', 'logs', 'resources', 'milestones']:
            if key not in backup:
                raise ValueError(f"Missing required field: {key}")
        if not isinstance(backup['goals'], list) or not isinstance(backup['logs'], list):
            raise ValueError("Goals and logs must be lists")
    for section, data in backup.items():
        existing = globals().get(section, [])
        if isinstance(data, list):
            globals()[section] = existing + data
        else:
            globals()[section] = data
    return globals()

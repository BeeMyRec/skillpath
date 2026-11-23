# === Stage 64: Add validation for relationship references ===
# Project: SkillPath
def validate_relationships(records):
    ids = {r['id'] for r in records}
    for rel in records:
        ref = rel.get('goal_id') or rel.get('resource_id')
        if ref is not None and ref not in ids:
            raise ValueError(f"Unknown reference {ref} in relationship {rel['id']}")
    return True

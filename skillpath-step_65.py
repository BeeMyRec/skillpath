# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: SkillPath
def merge_imports(existing, to_add):
    existing = list(existing or [])
    to_add = [i.strip() for i in to_add if i.strip()]
    merged = []
    added = set()
    for imp in existing:
        if imp in added:
            continue
        merged.append(imp)
        for alias in to_add:
            if alias.startswith(imp + " as ") or alias.startswith(imp + "."):
                merged.append(alias)
                added.add(alias)
    for alias in to_add:
        if alias not in added:
            merged.append(alias)
            added.add(alias)
    return merged

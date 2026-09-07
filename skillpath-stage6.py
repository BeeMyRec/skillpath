# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: SkillPath
def delete_item(item_id, confirm=False):
    if not confirm:
        raise ValueError("A confirmation flag is required for deletion. Call delete_item(item_id, confirm=True).")
    for key, entry in _items.items():
        if entry['id'] == item_id:
            del _items[key]
            return entry
    raise KeyError(f"No item with id {item_id} found.")

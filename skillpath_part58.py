# === Stage 58: Add bulk update behavior for selected records ===
# Project: SkillPath
def bulk_update_records(records, field, values_map):
    """Bulk-update selected records by applying values_map keyed on record[field]."""
    updated = []
    for record in records:
        key = record.get(field)
        if key in values_map:
            record.update(values_map[key])
            updated.append(record)
    return updated


def bulk_update_by_ids(records, id_field, id_to_values):
    """Bulk-update records whose id_field matches keys in id_to_values."""
    updated = []
    for record in records:
        record_id = record.get(id_field)
        if record_id in id_to_values:
            record.update(id_to_values[record_id])
            updated.append(record)
    return updated


def bulk_set_field(records, field, new_value):
    """Bulk-set the same field value across all provided records."""
    for record in records:
        record[field] = new_value
    return records


def bulk_filter_and_update(records, predicate, updates):
    """Apply updates to records where predicate(record) is True; return changed ones."""
    changed = []
    for record in records:
        if predicate(record):
            record.update(updates)
            changed.append(record)
    return changed

# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: SkillPath
def archive_records(records, cutoff_date=None):
    archive = []
    active = []
    for rec in records:
        status = rec.get("status", rec.get("completed", False))
        if cutoff_date and isinstance(rec.get("created_at"), datetime):
            if rec["created_at"] < cutoff_date and status:
                rec["archived"] = True
                rec["archived_at"] = datetime.now()
                archive.append(rec)
            else:
                rec["archived"] = False
                active.append(rec)
        elif status:
            archive.append(rec)
            rec["archived"] = True
        else:
            active.append(rec)
            rec["archived"] = False
    return active, archive


def restore_records(archive, records):
    for rec in archive:
        rec["archived"] = False
        rec["archived_at"] = None
        records.append(rec)
    return records

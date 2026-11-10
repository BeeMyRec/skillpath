# === Stage 46: Add a schema version field and migration helper ===
# Project: SkillPath
SCHEMA_VERSION = 1


def migration_helpers():
    if SCHEMA_VERSION == 1:
        return


def migrate_1_to_2(existing_data):
    return existing_data

# === Stage 44: Add backup creation for the data file ===
# Project: SkillPath
def create_backup(file_path):
    if not os.path.exists(file_path):
        return
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, "data_backup_" + timestamp + ".json")
    try:
        with open(backup_path, "w", encoding="utf-8") as bf:
            bf.write(open(file_path, "r", encoding="utf-8").read())
        print("Backup created:", backup_path)
    except IOError as err:
        print("Backup failed:", err)

if __name__ == "__main__":
    create_backup("skillpath_data.json")

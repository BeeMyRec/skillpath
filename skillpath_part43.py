# === Stage 43: Add CSV import for the primary record type ===
# Project: SkillPath
CSV_IMPORT = """
import csv
import os
from datetime import datetime

def load_practice_logs_from_csv(file_path, db):
    if not file_path or not os.path.exists(file_path):
        print(f"CSV file not found: {file_path}")
        return 0
    count = 0
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            skill = (row.get('skill') or '').strip()
            if not skill:
                continue
            goal = db.get_goal_by_skill(skill)
            if goal is None:
                goal = db.add_goal(skill)
            log = db.add_practice_log(
                skill=skill,
                goal_id=goal['id'],
                date=(row.get('date') or datetime.now().strftime('%Y-%m-%d')),
                duration=int(row.get('duration') or 0),
                notes=(row.get('notes') or '').strip()
            )
            count += 1
    print(f"Imported {count} practice log(s) from {file_path}")
    return count

if __name__ == '__main__':
    load_practice_logs_from_csv('practice.csv', db)
"""

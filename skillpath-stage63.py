# === Stage 63: Add relationships between records where useful ===
# Project: SkillPath
def link_records(db, goal_id=None, log_id=None, resource_id=None, milestone_id=None):
    if goal_id is not None and log_id is not None:
        cursor.execute("INSERT INTO goal_logs (goal_id, log_id) VALUES (?, ?)", (goal_id, log_id))
    if goal_id is not None and resource_id is not None:
        cursor.execute("INSERT INTO goal_resources (goal_id, resource_id) VALUES (?, ?)", (goal_id, resource_id))
    if goal_id is not None and milestone_id is not None:
        cursor.execute("INSERT INTO goal_milestones (goal_id, milestone_id) VALUES (?, ?)", (goal_id, milestone_id))
    if log_id is not None and resource_id is not None:
        cursor.execute("INSERT INTO log_resources (log_id, resource_id) VALUES (?, ?)", (log_id, resource_id))
    if milestone_id is not None and resource_id is not None:
        cursor.execute("INSERT INTO milestone_resources (milestone_id, resource_id) VALUES (?, ?)", (milestone_id, resource_id))
    db.commit()

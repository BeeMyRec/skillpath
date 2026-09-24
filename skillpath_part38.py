# === Stage 38: Add data integrity checks for broken references ===
# Project: SkillPath
def check_integrity(data):
    errors = []
    for goal in data.get("goals", []):
        if goal.get("status") not in ("active", "completed", "abandoned"):
            errors.append(f"Goal '{goal.get('name')}' has invalid status: {goal.get('status')}")
        for resource in goal.get("resources", []):
            res_id = resource.get("id")
            if res_id and res_id not in [r["id"] for r in data.get("resources", [])]:
                errors.append(f"Goal '{goal.get('name')}' references non-existent resource: {res_id}")
        for milestone in goal.get("milestones", []):
            m_id = milestone.get("id")
            if m_id and m_id not in [m["id"] for m in data.get("milestones", [])]:
                errors.append(f"Goal '{goal.get('name')}' references non-existent milestone: {m_id}")
    for log in data.get("logs", []):
        if log.get("goal_id") and log["goal_id"] not in [g["id"] for g in data.get("goals", [])]:
            errors.append(f"Log references non-existent goal: {log.get('goal_id')}")
    for resource in data.get("resources", []):
        if resource.get("goal_id") and resource["goal_id"] not in [g["id"] for g in data.get("goals", [])]:
            errors.append(f"Resource references non-existent goal: {resource.get('goal_id')}")
    return errors

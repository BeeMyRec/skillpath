# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: SkillPath
def update_goal(goal_id, updates):
    goals = load_goals()
    if goal_id not in goals:
        raise ValueError(f"Goal {goal_id} not found")
    goal = goals[goal_id]
    for key, value in updates.items():
        if key == "title":
            goal["title"] = value
        elif key == "description":
            goal["description"] = value
        elif key == "target_date":
            goal["target_date"] = value
        elif key == "status":
            goal["status"] = value
        elif key == "priority":
            goal["priority"] = value
        else:
            raise KeyError(f"Unknown goal field: {key}")
    goals[goal_id] = goal
    save_goals(goals)

def update_log(log_id, updates):
    logs = load_logs()
    if log_id not in logs:
        raise ValueError(f"Log {log_id} not found")
    log = logs[log_id]
    for key, value in updates.items():
        if key in ("duration_minutes", "date", "notes"):
            log[key] = value
        elif key == "status":
            log["status"] = value
        else:
            raise KeyError(f"Unknown log field: {key}")
    logs[log_id] = log
    save_logs(logs)

def update_resource(resource_id, updates):
    resources = load_resources()
    if resource_id not in resources:
        raise ValueError(f"Resource {resource_id} not found")
    resource = resources[resource_id]
    for key, value in updates.items():
        if key in ("title", "url", "description", "tags"):
            resource[key] = value
        else:
            raise KeyError(f"Unknown resource field: {key}")
    resources[resource_id] = resource
    save_resources(resources)

def update_milestone(milestone_id, updates):
    milestones = load_milestones()
    if milestone_id not in milestones:
        raise ValueError(f"Milestone {milestone_id} not found")
    milestone = milestones[milestone_id]
    for key, value in updates.items():
        if key in ("title", "description", "date_achieved"):
            milestone[key] = value
        else:
            raise KeyError(f"Unknown milestone field: {key}")
    milestones[milestone_id] = milestone
    save_milestones(milestones)

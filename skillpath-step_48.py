# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: SkillPath
def create_goal(name, category, target):
    goal = {"id": None, "name": name, "category": category, "target": target}
    next_id = _next_goal_id(goals)
    goal["id"] = next_id
    goals.append(goal)
    return goal

def create_practice_log(goal_id, activity, minutes):
    if not isinstance(minutes, (int, float)) or minutes < 0:
        raise ValueError("minutes must be a non-negative number")
    log = {"id": None, "goal_id": goal_id, "activity": activity, "minutes": minutes}
    next_id = _next_log_id(logs)
    log["id"] = next_id
    logs.append(log)
    return log

def create_resource(title, url, category):
    resource = {"id": None, "title": title, "url": url, "category": category}
    next_id = _next_resource_id(resources)
    resource["id"] = next_id
    resources.append(resource)
    return resource

def create_milestone(goal_id, title, date):
    if not isinstance(date, str):
        raise TypeError("date must be a string")
    milestone = {"id": None, "goal_id": goal_id, "title": title, "date": date}
    next_id = _next_milestone_id(milestones)
    milestone["id"] = next_id
    milestones.append(milestone)
    return milestone

def find_goal_by_id(goal_id):
    for goal in goals:
        if goal["id"] == goal_id:
            return goal
    return None

def validate_goal(goal):
    if not isinstance(goal, dict):
        raise TypeError("goal must be a dictionary")
    if not goal.get("name") or not goal["name"].strip():
        raise ValueError("goal name must not be empty")
    if not goal.get("category"):
        raise ValueError("goal category must not be empty")
    if not goal.get("target"):
        raise ValueError("goal target must not be empty")
    return True

def validate_practice_log(log):
    if not isinstance(log, dict):
        raise TypeError("practice log must be a dictionary")
    if not log.get("goal_id"):
        raise ValueError("practice log goal_id must not be empty")
    if not log.get("activity") or not log["activity"].strip():
        raise ValueError("practice log activity must not be empty")
    if not isinstance(log.get("minutes"), (int, float)) or log["minutes"] < 0:
        raise ValueError("practice log minutes must be a non-negative number")
    return True

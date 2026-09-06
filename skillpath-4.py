# === Stage 4: Implement create operations for the primary records ===
# Project: SkillPath
def create_goal(goal_dict):
    """Create a new Goal record."""
    goals = []
    with open("data/goals.json", "w") as f:
        json.dump(goals, f, indent=2)
    goals.append(goal_dict)
    with open("data/goals.json", "w") as f:
        json.dump(goals, f, indent=2)
    return goal_dict

def create_practice_log(log_dict):
    """Create a new PracticeLog record."""
    logs = []
    with open("data/practice_logs.json", "w") as f:
        json.dump(logs, f, indent=2)
    logs.append(log_dict)
    with open("data/practice_logs.json", "w") as f:
        json.dump(logs, f, indent=2)
    return log_dict

def create_resource(resource_dict):
    """Create a new Resource record."""
    resources = []
    with open("data/resources.json", "w") as f:
        json.dump(resources, f, indent=2)
    resources.append(resource_dict)
    with open("data/resources.json", "w") as f:
        json.dump(resources, f, indent=2)
    return resource_dict

def create_milestone(milestone_dict):
    """Create a new Milestone record."""
    milestones = []
    with open("data/milestones.json", "w") as f:
        json.dump(milestones, f, indent=2)
    milestones.append(milestone_dict)
    with open("data/milestones.json", "w") as f:
        json.dump(milestones, f, indent=2)
    return milestone_dict

# === Stage 67: Add a function that returns key project metrics ===
# Project: SkillPath
def get_project_metrics(goals, practice_logs, milestones, resources):
    total_goals = len(goals)
    completed_goals = sum(1 for g in goals if g.get("completed", False))
    goal_completion_rate = (completed_goals / total_goals) if total_goals else 0.0

    total_logs = len(practice_logs)
    total_hours = sum(float(log.get("hours", 0)) for log in practice_logs)
    total_sessions = sum(1 for log in practice_logs if log.get("hours", 0) > 0)
    avg_hours_per_session = (total_hours / total_sessions) if total_sessions else 0.0

    total_milestones = len(milestones)
    completed_milestones = sum(1 for m in milestones if m.get("completed", False))
    milestone_completion_rate = (completed_milestones / total_milestones) if total_milestones else 0.0

    total_resources = len(resources)
    total_resource_hours = sum(float(r.get("hours", 0)) for r in resources)

    return {
        "total_goals": total_goals,
        "completed_goals": completed_goals,
        "goal_completion_rate": round(goal_completion_rate, 2),
        "total_sessions": total_sessions,
        "total_hours": round(total_hours, 1),
        "avg_hours_per_session": round(avg_hours_per_session, 2),
        "total_milestones": total_milestones,
        "completed_milestones": completed_milestones,
        "milestone_completion_rate": round(milestone_completion_rate, 2),
        "total_resources": total_resources,
        "total_resource_hours": round(total_resource_hours, 1),
    }

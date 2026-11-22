# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: SkillPath
def recommend_focus(goals):
    scores = {}
    for goal in goals:
        if not goal.get("active"):
            scores[goal["name"]] = 0
            continue
        base = goal.get("priority", 3)
        streak = goal.get("streak", 0)
        progress = goal.get("progress", 0)
        total = goal.get("total", 1)
        score = base * 1.2 + streak * 0.5 + (progress / total) * 0.3
        scores[goal["name"]] = round(score, 2)
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)

def suggest_milestones(goal, progress, total):
    if not goal.get("active") or progress >= total:
        return []
    steps = 5
    size = max(1, round((total - progress) / steps))
    return [size * i for i in range(1, min(steps, (total - progress) // size) + 1)]

def next_goal(goal):
    if goal.get("progress", 0) >= goal.get("total", 1):
        return "complete"
    return goal.get("name")

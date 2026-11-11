# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: SkillPath
def demo_scenario():
    goals = {"Python": {"streak": 12, "hours": 40}}
    resources = {"Python": ["Automate the Boring Stuff", "Python.org"]}
    milestones = {"Python": [{"date": "2024-01-01", "text": "Finished intro course"}]}
    logs = []
    logs.append({"skill": "Python", "hours": 2, "note": "List comprehensions"})
    logs.append({"skill": "Python", "hours": 3, "note": "Object oriented basics"})
    for log in logs:
        goals[log["skill"]]["hours"] += log["hours"]
        goals[log["skill"]]["streak"] += 1
        print("Logged", log["hours"], "hours of", log["skill"], "-", log["note"])
    for skill, data in goals.items():
        print("Skill:", skill, "Total hours:", data["hours"], "Streak:", data["streak"], "days")
        for res in resources.get(skill, []):
            print("  Resource:", res)
        for m in milestones.get(skill, []):
            print("  Milestone:", m["date"], "-", m["text"])
    print("Demo complete")

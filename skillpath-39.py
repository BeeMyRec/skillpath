# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: SkillPath
def repair_data(data):
    repaired = []
    for item in data:
        if isinstance(item, dict):
            if "goal" not in item:
                item["goal"] = "General Skill"
            if "status" not in item:
                item["status"] = "in_progress"
            if "completed" not in item:
                item["completed"] = False
            if item.get("status") not in ("in_progress", "completed", "paused"):
                item["status"] = "in_progress"
            if not isinstance(item.get("progress", 0), (int, float)):
                item["progress"] = 0
            if not (0 <= item["progress"] <= 100):
                item["progress"] = 100 if item["progress"] > 100 else 0
            if item["completed"] and item["progress"] < 100:
                item["progress"] = 100
            if not item["completed"] and item["progress"] >= 100:
                item["status"] = "completed"
        else:
            item = {"goal": "General Skill", "status": "in_progress", "completed": False, "progress": 0}
        repaired.append(item)
    return repaired

# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: SkillPath
def add_tag(skill, tag):
    if tag not in skill.tags:
        skill.tags.append(tag)

def remove_tag(skill, tag):
    if tag in skill.tags:
        skill.tags.remove(tag)

def tag_summary(tag):
    matching = [s for s in SKILL_PATH.skills if tag in s.tags]
    return {"total": len(matching), "avg_hours": sum(s.hours / 100 for s in matching) if matching else 0}

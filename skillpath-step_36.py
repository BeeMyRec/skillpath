# === Stage 36: Add templates for quickly creating common records ===
# Project: SkillPath
TEMPLATE_GOAL = """
goal = Goal(
    title="{title}",
    description="{description}",
    category="{category}",
    target_date="{target_date}",
    status="not_started",
)
"""
TEMPLATE_LOG = """
log = Log(
    date="{date}",
    duration_minutes={duration_minutes},
    activity="{activity}",
    notes="{notes}",
    goal_id={goal_id},
)
"""
TEMPLATE_RESOURCE = """
resource = Resource(
    title="{title}",
    url="{url}",
    category="{category}",
    tags=[{tags}],
)
"""
TEMPLATE_MILESTONE = """
milestone = Milestone(
    title="{title}",
    goal_id={goal_id},
    achieved_date="{achieved_date}",
    reflection="{reflection}",
)
"""

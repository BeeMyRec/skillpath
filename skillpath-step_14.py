# === Stage 14: Add file load support with fallback demo data ===
# Project: SkillPath
def load_project():
    """Load SkillPath project data with fallback demo data."""
    demo_data = {
        "project": "SkillPath",
        "description": "Personal skill development tracker",
        "features": ["goals", "practice_logs", "resources", "milestones"],
        "version": "1.0.0",
        "author": "SkillPath Team"
    }
    return demo_data

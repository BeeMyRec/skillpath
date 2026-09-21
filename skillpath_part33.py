# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: SkillPath
SETTINGS = {
    "language": "en",
    "theme": "light",
    "notifications": True,
    "daily_reminder_time": "09:00",
    "weekly_review_day": "Sunday",
    "weekly_review_time": "18:00",
    "max_goals_per_day": 5,
    "log_retention_days": 365,
    "auto_sync_interval_seconds": 300,
    "enable_analytics": True,
    "default_practice_duration_minutes": 30,
    "language_options": ["en", "es", "fr", "de", "ja"],
    "theme_options": ["light", "dark", "auto"],
    "valid_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
}

def get_setting(key):
    return SETTINGS.get(key, None)

def set_setting(key, value):
    if key not in SETTINGS:
        raise ValueError(f"Unknown setting: {key}")
    SETTINGS[key] = value
    return SETTINGS[key]

def update_settings(**kwargs):
    for key, value in kwargs.items():
        set_setting(key, value)
    return SETTINGS

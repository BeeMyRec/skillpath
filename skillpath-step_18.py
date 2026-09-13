# === Stage 18: Add an activity log with timestamps and action names ===
# Project: SkillPath
class ActivityLog:
    def __init__(self):
        self._log = []

    def record(self, action_name, skill_name, timestamp=None):
        from datetime import datetime
        ts = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {"timestamp": ts, "action": action_name, "skill": skill_name}
        self._log.append(entry)
        return entry

    def get_log(self):
        return list(self._log)

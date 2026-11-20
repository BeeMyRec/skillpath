# === Stage 60: Add saved views for frequently used filters ===
# Project: SkillPath
class SavedView:
    def __init__(self, name, filters):
        self.name = name
        self.filters = filters

    def to_dict(self):
        return {"name": self.name, "filters": self.filters}

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["filters"])


class SavedViewStore:
    def __init__(self):
        self.views = {}

    def add(self, name, filters):
        if name in self.views:
            raise ValueError(f"View '{name}' already exists")
        self.views[name] = SavedView(name, filters)
        return self.views[name]

    def remove(self, name):
        return self.views.pop(name, None)

    def list(self):
        return list(self.views.values())

    def apply(self, name, log_records):
        saved = self.views.get(name)
        if not saved:
            return log_records
        filtered = []
        for record in log_records:
            if saved.filters.get("skill") and record["skill"] != saved.filters["skill"]:
                continue
            if saved.filters.get("status") and record["status"] != saved.filters["status"]:
                continue
            if saved.filters.get("min_minutes") and record["minutes"] < saved.filters["min_minutes"]:
                continue
            filtered.append(record)
        return filtered

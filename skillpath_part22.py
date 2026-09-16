# === Stage 22: Add favorite records and quick favorite listing ===
# Project: SkillPath
class FavoriteRecord:
    def __init__(self, skill_name, level):
        self.skill_name = skill_name
        self.level = level

    def display(self):
        return f"Favorite: {self.skill_name} (Level: {self.level})"

    def __repr__(self):
        return f"FavoriteRecord({self.skill_name}, {self.level})"

def list_favorites(favorites):
    if not favorites:
        return "No favorites yet!"
    lines = [f"Your Favorites:\n"]
    for fav in favorites:
        lines.append(f"  - {fav.display()}")
    return "\n".join(lines)

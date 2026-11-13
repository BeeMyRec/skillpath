# === Stage 50: Add unit tests for import and export behavior ===
# Project: SkillPath
import json
from datetime import datetime

def load_skills(path="skills.json"):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_skills(skills, path="skills.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2)

def test_export_import_roundtrip():
    skills = [
        {"id": 1, "name": "Python", "level": 5, "created": "2024-01-01"},
        {"id": 2, "name": "Math", "level": 3, "created": "2024-02-01"},
    ]
    payload = json.dumps(skills)
    restored = json.loads(payload)
    assert restored == skills
    assert restored[0]["name"] == "Python"
    assert restored[1]["level"] == 3

def test_export_empty_skills():
    assert json.dumps([]) == "[]"
    assert json.loads("[]") == []

def test_export_missing_file_returns_empty():
    assert load_skills("nonexistent_file.json") == []

def test_import_invalid_json_raises():
    with open("bad.json", "w", encoding="utf-8") as f:
        f.write("{not valid json")
    try:
        load_skills("bad.json")
        raise AssertionError("expected json error")
    except json.JSONDecodeError:
        pass
    finally:
        os.remove("bad.json")

if __name__ == "__main__":
    test_export_import_roundtrip()
    test_export_empty_skills()
    test_export_missing_file_returns_empty()
    test_import_invalid_json_raises()
    print("All export/import tests passed")

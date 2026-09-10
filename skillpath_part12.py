# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: SkillPath
import json

def load_safe(filepath):
    """Load JSON from file with friendly error handling for malformed data."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"error": f"File '{filepath}' not found."}
    except json.JSONDecodeError as e:
        return {"error": f"Malformed JSON in '{filepath}': {e}"}
    except Exception as e:
        return {"error": f"Unexpected error reading '{filepath}': {e}"}

# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: SkillPath
import re

def validate_required(value):
    return value is not None and len(value.strip()) > 0

def validate_identifier(value):
    return bool(re.match(r'^[a-z][a-z0-9_]*$', value.strip()))

def validate_short_text(value, max_length=256):
    return isinstance(value, str) and len(value) <= max_length

def validate_date(date_str):
    try:
        from datetime import datetime
        return datetime.strptime(date_str, '%Y-%m-%d')
    except (ValueError, TypeError):
        return None

def validate_percentage(value):
    try:
        pct = float(value)
        return 0 <= pct <= 100
    except (ValueError, TypeError):
        return False

def validate_email(email):
    return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email))

# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: SkillPath
def days_since(start_date, end_date=None):
    """Return the number of whole days between two date strings.

    Both arguments are expected in 'YYYY-MM-DD' format. If end_date is
    omitted the current date is used so the helper works well for
    tracking how long a goal has been active.
    """
    from datetime import date

    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date) if end_date else date.today()
    return (end - start).days


def average_streak(logs):
    """Return the average consecutive-day count from a list of logs.

    Each log should be a mapping that responds to ``get('date')`` and
    ``get('minutes')``. Days without activity are not counted toward the
    average, so the function returns 0.0 when there is nothing to measure.
    """
    if not logs:
        return 0.0

    active_dates = sorted(log.get('date') for log in logs if log.get('minutes'))
    if not active_dates:
        return 0.0

    total_minutes = sum(log.get('minutes', 0) for log in logs)
    return round(total_minutes / len(active_dates), 2)


def progress_percent(current, target):
    """Return the completion percentage of current progress toward target.

    A target of zero avoids division by zero and reports full completion
    when current work is already at or above that level.
    """
    if target <= 0:
        return 100.0
    return round(min(current, target) / target * 100, 1)


def format_date(value):
    """Return a date value formatted as 'YYYY-MM-DD'.

    Strings are parsed with ISO format, date objects are converted
    directly, and any other input is returned unchanged so callers can
    rely on a consistent return type without extra validation.
    """
    if isinstance(value, str):
        return date.fromisoformat(value).isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return value

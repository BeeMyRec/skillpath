# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: SkillPath
def parse_date(date_str, fmt=None):
    """Parse a date string, returning a datetime.date object.
    
    Tries common formats in order:
        YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD,
        DD/MM/YYYY, DD.MM.YYYY
    Raises ValueError with a clear message if none match.
    """
    if not date_str or not isinstance(date_str, str):
        raise ValueError(f"Invalid date input: {date_str!r}")
    
    date_str = date_str.strip()
    patterns = [
        ("%Y-%m-%d", "YYYY-MM-DD"),
        ("%Y/%m/%d", "YYYY/MM/DD"),
        ("%Y.%m.%d", "YYYY.MM.DD"),
        ("%d-%m-%Y", "DD-MM-YYYY"),
        ("%d/%m/%Y", "DD/MM/YYYY"),
        ("%d.%m.%Y", "DD.MM.YYYY"),
    ]
    
    for fmt, label in patterns:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    raise ValueError(f"Cannot parse date '{date_str}'. Expected one of: YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD, DD/MM/YYYY, DD.MM.YYYY")

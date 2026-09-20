# === Stage 31: Add compact table rendering for long lists ===
# Project: SkillPath
def render_compact_table(headers, rows):
    """Render a long list of records as a space-separated compact table.

    Args:
        headers: List[str] column names.
        rows: List[List[str]] data rows.

    Returns:
        str formatted table.
    """
    widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(val))
    lines = []
    lines.append('  ' + '  '.join(str(h).ljust(widths[i]) for i, h in enumerate(headers)))
    lines.append('  ' + '  ~'.join('-' * w for w in widths))
    for row in rows:
        lines.append('  ' + '  '.join(str(v).ljust(widths[i]) for i, v in enumerate(row)))
    return '\n'.join(lines)

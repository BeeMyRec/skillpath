# === Stage 32: Add pagination helpers for long console output ===
# Project: SkillPath
def paginate(lines, page_size=12):
    """Yield chunks of lines for console paging."""
    for i in range(0, len(lines), page_size):
        yield lines[i:i + page_size]

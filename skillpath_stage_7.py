# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: SkillPath
def fmt_status(status: str) -> str:
    colors = {"active": "green", "completed": "cyan", "overdue": "red", "on_hold": "yellow"}
    return f"\033[{colors.get(status, 'white')}\033[0m{status.upper()}\033[0m"

def fmt_goal(g: dict) -> str:
    return f"{fmt_status(g.get('status', 'unknown'))}  {g.get('title', '')}"

def fmt_log(entry: dict) -> str:
    return f"[{entry.get('date', '')}] {entry.get('duration', '')}m: {entry.get('note', '')}"

def fmt_milestone(m: dict) -> str:
    return f"★ {m.get('title', '')} — {m.get('date', '')}"

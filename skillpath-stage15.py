# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: SkillPath
def dispatch(cmd, args):
    cmd = cmd.strip().lower()
    if cmd == "":
        return None
    commands = {
        "add": "add_goal",
        "log": "log_practice",
        "show": "show_goals",
        "help": "show_help",
        "quit": "quit",
    }
    action = commands.get(cmd.split()[0])
    if action is None:
        return f"Unknown command: {cmd.split()[0]}"
    if action == "show_help":
        return "Available commands:\n  add <goal>    Add a new goal\n  log <goal> <mins>  Log practice\n  show          Show all goals\n  help          Show this help\n  quit          Exit"
    return action, args

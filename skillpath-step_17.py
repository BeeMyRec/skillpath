# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: SkillPath
import os

DRY_RUN = False

def dry_run_mode():
    global DRY_RUN
    DRY_RUN = True

def confirm_action(action):
    if not DRY_RUN:
        print(f"Action '{action}' will be executed. Type 'y' to confirm: ", end="")
        response = input()
        if response.lower() != 'y':
            print("Action cancelled.")
            return False
    return True

def log_action(action):
    if DRY_RUN:
        print(f"[DRY RUN] {action}")
    else:
        print(f"[EXECUTED] {action}")

def save_file(path, content):
    if confirm_action(f"Save {path}"):
        if DRY_RUN:
            log_action(f"Would save {path} with {len(content)} bytes")
            return False
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)
        log_action(f"Saved {path}")
        return True
    return False

# === Stage 53: Add command help text and usage examples ===
# Project: SkillPath
HELP = {
    "skillpath": "SkillPath - personal skill development tracker",
    "usage": "python skillpath.py <command> [options]",
    "commands": {
        "add-goal": "Add a new skill goal",
        "log": "Record a practice session",
        "resources": "List or add learning resources",
        "milestones": "View or track milestones",
        "help": "Show this help message",
    },
    "examples": [
        "python skillpath.py add-goal --skill 'Python' --level 'Beginner'",
        "python skillpath.py log --skill 'Python' --minutes 45 --notes 'List comprehension'",
        "python skillpath.py resources --add 'Automate the Boring Stuff' --url 'https://example.com'",
        "python skillpath.py milestones --skill 'Python' --add 'Finish chapter 5' --date '2025-01-15'",
        "python skillpath.py help",
    ],
}


def show_help():
    print("=" * 40)
    print(HELP["skillpath"])
    print("=" * 40)
    print(HELP["usage"])
    print("Available commands:")
    for command, description in HELP["commands"].items():
        print(f"  {command:<15} {description}")
    print("Example commands:")
    for example in HELP["examples"]:
        print(f"  $ {example}")
    print("=" * 40)


if __name__ == "__main__":
    show_help()

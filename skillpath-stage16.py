# === Stage 16: Add argparse support for the most common commands ===
# Project: SkillPath
import argparse

def main():
    parser = argparse.ArgumentParser(description="SkillPath - Personal Skill Development Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("status", help="Show current progress")
    subparsers.add_parser("new-goal", help="Create a new practice goal")
    subparsers.add_parser("log", help="Add a practice session log")
    subparsers.add_parser("resources", help="List learning resources")
    subparsers.add_parser("milestones", help="View milestones and achievements")

    args = parser.parse_args()
    print(f"Command: {args.command}")

if __name__ == "__main__":
    main()

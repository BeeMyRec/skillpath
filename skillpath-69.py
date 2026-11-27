# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: SkillPath
def reset_demo_data(db):
    db.execute("DELETE FROM milestones")
    db.execute("DELETE FROM resources")
    db.execute("DELETE FROM practice_logs")
    db.execute("DELETE FROM goals")
    goals = [
        (1, "Python Basics", "Learn Python fundamentals", 4, "2024-01-01"),
        (2, "Python Basics", "Complete all exercises", 8, "2024-01-15"),
        (3, "Python Basics", "Build a small project", 12, "2024-02-01"),
    ]
    db.executemany("INSERT INTO goals VALUES (?, ?, ?, ?, ?)", goals)
    resources = [
        (1, "Python for Everybody", "https://www.py4e.com"),
        (2, "Automate the Boring Stuff", "https://automatetheboringstuff.com"),
    ]
    db.executemany("INSERT INTO resources VALUES (?, ?, ?)", resources)
    logs = [
        (1, 1, "2024-01-05", "Completed variables and data types", 60),
        (2, 1, "2024-01-06", "Practiced loops and conditionals", 90),
    ]
    db.executemany("INSERT INTO practice_logs VALUES (?, ?, ?, ?, ?)", logs)
    db.commit()

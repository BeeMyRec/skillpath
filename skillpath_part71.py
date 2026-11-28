# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: SkillPath
def seed_demo_data(store):
    store['goals'] = [
        {'id': 'goal_demo_1', 'title': 'Learn Python basics', 'level': 2, 'tags': ['python']},
        {'id': 'goal_demo_2', 'title': 'Build a Flask app', 'level': 1, 'tags': ['flask']},
    ]
    store['resources'] = [
        {'id': 'res_demo_1', 'title': 'Python for Everybody', 'url': 'https://www.py4e.com', 'tags': ['python']},
        {'id': 'res_demo_2', 'title': 'Flask Documentation', 'url': 'https://flask.palletsprojects.com', 'tags': ['flask']},
    ]
    store['milestones'] = [
        {'id': 'ms_demo_1', 'goal_id': 'goal_demo_1', 'title': 'Finished Python course', 'completed': True},
        {'id': 'ms_demo_2', 'goal_id': 'goal_demo_2', 'title': 'Deployed first app', 'completed': False},
    ]
    rng = random.Random(42)
    store['practice_logs'] = []
    for i in range(5):
        goal = store['goals'][i % len(store['goals'])]
        store['practice_logs'].append({
            'id': 'log_demo_%d' % (i + 1),
            'goal_id': goal['id'],
            'title': goal['title'],
            'duration_minutes': rng.randint(15, 120),
            'notes': 'Sample practice session %d' % (i + 1),
            'created_at': '2024-01-%02d' % (i + 1),
        })

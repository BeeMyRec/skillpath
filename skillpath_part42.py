# === Stage 42: Add CSV export without external dependencies ===
# Project: SkillPath
def export_csv(path, goals=None, logs=None, resources=None, milestones=None):
    with open(path, 'w', newline='') as f:
        if goals:
            w = csv.DictWriter(f, fieldnames=['name', 'skill', 'target', 'progress', 'created'])
            w.writeheader()
            for g in goals:
                w.writerow({'name': g['name'], 'skill': g['skill'], 'target': g['target'], 'progress': g['progress'], 'created': g['created']})
        if logs:
            w = csv.DictWriter(f, fieldnames=['date', 'skill', 'activity', 'minutes', 'notes'])
            w.writeheader()
            for l in logs:
                w.writerow({'date': l['date'], 'skill': l['skill'], 'activity': l['activity'], 'minutes': l['minutes'], 'notes': l['notes']})
        if resources:
            w = csv.DictWriter(f, fieldnames=['skill', 'title', 'url', 'notes'])
            w.writeheader()
            for r in resources:
                w.writerow({'skill': r['skill'], 'title': r['title'], 'url': r['url'], 'notes': r['notes']})
        if milestones:
            w = csv.DictWriter(f, fieldnames=['skill', 'milestone', 'date', 'completed'])
            w.writeheader()
            for m in milestones:
                w.writerow({'skill': m['skill'], 'milestone': m['milestone'], 'date': m['date'], 'completed': m['completed']})

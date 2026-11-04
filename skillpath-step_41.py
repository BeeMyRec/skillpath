# === Stage 41: Add plain text import for a simple line-based format ===
# Project: SkillPath
def load_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        for raw in f:
            line = raw.rstrip('\n')
            if not line.strip():
                continue
            yield line

def parse_kv(lines, sep='='):
    result = {}
    for line in lines:
        if sep in line:
            key, value = line.split(sep, 1)
            result[key.strip()] = value.strip()
    return result

def load_goals(path):
    goals = []
    for line in load_lines(path):
        if line.startswith('#'):
            continue
        if ':' in line:
            name, detail = line.split(':', 1)
            goals.append({'name': name.strip(), 'detail': detail.strip()})
        else:
            goals.append({'name': line.strip(), 'detail': ''})
    return goals

def save_lines(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

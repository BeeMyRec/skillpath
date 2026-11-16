# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: SkillPath
ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_black": "\033[40m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
}

COLOR = False
FORCE_COLOR = os.environ.get("SKILLPATH_FORCE_COLOR") == "1"
if FORCE_COLOR:
    COLOR = True

def col(text, color):
    if not COLOR or not color:
        return text
    return ANSI[color] + text + ANSI["reset"]

def success(text):
    return col(text, "green")

def warn(text):
    return col(text, "yellow")

def error(text):
    return col(text, "red")

def header(text):
    return col(" " + text + " ", "cyan") + ANSI["bold"] + col(text, "white") + ANSI["reset"]

def dim(text):
    return col(text, "dim")

def enable_color():
    global COLOR
    COLOR = FORCE_COLOR

def disable_color():
    global COLOR
    COLOR = False

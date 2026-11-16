# === Stage 55: Add a setting to disable colorized output ===
# Project: SkillPath
NO_COLOR = os.environ.get("NO_COLOR") is not None
USE_COLOR = getattr(sys.stdout, "isatty", lambda: False)() and not NO_COLOR


def colorize(text, color=None):
    if not USE_COLOR:
        return text
    table = {"reset": "\033[0m", "bold": "\033[1m", "red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m", "blue": "\033[34m", "cyan": "\033[36m"}
    code = ""
    if color:
        code += table.get(color, "")
    code += table["reset"]
    return f"{code}{text}{code}"


def print_header(title):
    if USE_COLOR:
        print(colorize(f"  {title}  ", "cyan"))
    else:
        print(f"  {title}  ")


def print_success(text):
    if USE_COLOR:
        print(colorize(f"  [OK] {text}", "green"))
    else:
        print(f"  [OK] {text}")


def print_warning(text):
    if USE_COLOR:
        print(colorize(f"  [!] {text}", "yellow"))
    else:
        print(f"  [!] {text}")


def print_error(text):
    if USE_COLOR:
        print(colorize(f"  [X] {text}", "red"))
    else:
        print(f"  [X] {text}")


def print_info(text):
    if USE_COLOR:
        print(colorize(f"  {text}", "blue"))
    else:
        print(f"  {text}")


def print_divider():
    if USE_COLOR:
        print(colorize("-" * 40, "cyan"))
    else:
        print("-" * 40)

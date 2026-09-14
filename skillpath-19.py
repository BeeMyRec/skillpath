# === Stage 19: Add undo support for the last simple mutation ===
# Project: SkillPath
import json
from datetime import datetime

def undo_last_mutation(data, undo_stack, max_undo=10):
    """Undo the last mutation to a SkillPath data structure.

    Args:
        data: The current state of the SkillPath data (dict).
        undo_stack: A list of previous states of the data.
        max_undo: Maximum number of states to keep in the undo stack.

    Returns:
        A tuple (new_data, new_undo_stack).
    """
    if len(undo_stack) >= max_undo:
        undo_stack.pop(0)
    undo_stack.append(data)
    return data, undo_stack

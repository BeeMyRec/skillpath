# === Stage 56: Add compact error classes for domain failures ===
# Project: SkillPath
class SkillPathError(Exception):
    """Base class for all SkillPath domain errors."""
    pass


class GoalNotFoundError(SkillPathError):
    def __init__(self, goal_id):
        self.goal_id = goal_id
        super().__init__(f"Goal '{goal_id}' not found.")


class PracticeLogValidationError(SkillPathError):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Invalid practice log field '{field}': {message}")


class MilestoneNotFoundError(SkillPathError):
    def __init__(self, milestone_id):
        self.milestone_id = milestone_id
        super().__init__(f"Milestone '{milestone_id}' not found.")


class ResourceNotFoundError(SkillPathError):
    def __init__(self, resource_id):
        self.resource_id = resource_id
        super().__init__(f"Resource '{resource_id}' not found.")


class ProgressConflictError(SkillPathError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

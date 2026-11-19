# === Stage 57: Add structured result objects for command handlers ===
# Project: SkillPath
class SkillPathResult:
    def __init__(self, success=True, message="OK"):
        self.success = success
        self.message = message
        self.data = None
        self.errors = []

    def set_data(self, data):
        self.data = data
        return self

    def set_errors(self, errors):
        self.errors = errors
        self.success = False
        return self

    def message(self):
        if self.errors:
            return "; ".join(self.errors)
        return self.message

    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "errors": self.errors,
        }

    def __repr__(self):
        return f"SkillPathResult(success={self.success}, message={self.message!r})"


def result(message="OK"):
    return SkillPathResult(message=message)


def result_ok(data=None):
    return SkillPathResult(success=True, message="OK").set_data(data)


def result_error(message, *errors):
    return SkillPathResult(success=False, message=message).set_errors(list(errors))

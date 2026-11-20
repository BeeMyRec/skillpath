# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: SkillPath
def bulk_delete(self, predicate, confirm=True):
    remaining = []
    for item in self._items:
        if not predicate(item):
            remaining.append(item)
    if confirm and len(self._items) - len(remaining) > 0:
        self._confirm = True
        while not self._confirm:
            print("Delete the following items?")
            for item in self._items:
                if predicate(item):
                    print(" -", item)
            response = input("Type 'yes' to confirm: ").strip().lower()
            if response == "yes":
                self._confirm = True
            else:
                self._confirm = False
                return
    self._items = remaining

# === Stage 61: Add performance timing for core list and search operations ===
# Project: SkillPath
import time

def _timeit(func, *args, repeats=3):
    best = float('inf')
    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        best = min(best, time.perf_counter() - start)
    return best * 1000

def time_list_operations(items, predicate=None):
    insert = _timeit(lambda: items.insert(0, None), items)
    append = _timeit(lambda: items.append(None), items)
    pop = _timeit(lambda: items.pop(), items)
    find = _timeit(lambda: next((i for i, v in enumerate(items) if predicate and predicate(v)), -1), items) if predicate else _timeit(lambda: items.index(None), items)
    return {"insert": insert, "append": append, "pop": pop, "search": find}

def time_search_operations(items, predicate=None):
    linear = _timeit(lambda: next((i for i, v in enumerate(items) if predicate and predicate(v)), -1), items) if predicate else _timeit(lambda: items.index(None), items)
    binary = _timeit(lambda: _binary_search(items, predicate), items) if predicate else _timeit(lambda: _binary_search_sorted(items), items)
    return {"linear": linear, "binary": binary}

def _binary_search(items, predicate):
    lo, hi = 0, len(items)
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(items[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo if lo < len(items) and predicate(items[lo]) else -1

def _binary_search_sorted(items):
    lo, hi = 0, len(items)
    while lo < hi:
        mid = (lo + hi) // 2
        if items[mid] < items[-1]:
            lo = mid + 1
        else:
            hi = mid
    return lo

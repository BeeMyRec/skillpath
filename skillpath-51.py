# === Stage 51: Add unit tests for search and filter behavior ===
# Project: SkillPath
def test_search_by_name_is_case_insensitive():
    tracker = SkillPathTracker()
    tracker.add_goal("Python", "Master basics")
    tracker.add_goal("Guitar", "Learn chords")
    assert len(tracker.search("python")) == 1
    assert len(tracker.search("PYTHON")) == 1
    assert tracker.search("python") == tracker.search("Python")


def test_search_by_description_matches():
    tracker = SkillPathTracker()
    tracker.add_goal("Math", "Practice calculus")
    assert len(tracker.search("calculus")) == 1
    assert tracker.search("calculus") == [tracker.get_goal("Math")]


def test_search_no_match_returns_empty_list():
    tracker = SkillPathTracker()
    tracker.add_goal("Python", "Master basics")
    assert tracker.search("cooking") == []


def test_filter_by_status_active_only():
    tracker = SkillPathTracker()
    tracker.add_goal("Python", "Master basics")
    tracker.add_goal("Guitar", "Learn chords")
    tracker.mark_active("Guitar")
    tracker.mark_active("Python")
    tracker.mark_complete("Guitar")
    active = tracker.filter_by_status("active")
    assert len(active) == 1
    assert active[0].name == "Python"


def test_filter_by_status_all_includes_completed():
    tracker = SkillPathTracker()
    tracker.add_goal("Python", "Master basics")
    tracker.mark_active("Python")
    tracker.mark_complete("Python")
    all_goals = tracker.filter_by_status("all")
    assert len(all_goals) == 1
    assert all_goals[0].name == "Python"

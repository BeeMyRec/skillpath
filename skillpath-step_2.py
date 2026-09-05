# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: SkillPath
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime


@dataclass
class Goal:
    title: str
    description: str = ""
    target_date: date = field(default_factory=date.today)
    is_active: bool = True
    progress: float = 0.0  # 0..1


@dataclass
class PracticeLog:
    date: date
    duration_minutes: int
    notes: str = ""
    goal_id: str = ""


@dataclass
class Resource:
    title: str
    url: str
    category: str = "general"
    added_date: date = field(default_factory=date.today)


@dataclass
class Milestone:
    title: str
    date: date
    goal_id: str = ""
    description: str = ""

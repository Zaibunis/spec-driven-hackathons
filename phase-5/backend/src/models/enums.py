from enum import Enum


class PriorityEnum(str, Enum):
    """
    Enum for task priority levels.
    """
    low = "low"
    medium = "medium"
    high = "high"


class RecurrencePatternEnum(str, Enum):
    """
    Enum for recurrence patterns.
    """
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    custom = "custom"
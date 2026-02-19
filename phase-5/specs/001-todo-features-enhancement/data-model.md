# Data Model: Phase V Part A – Intermediate & Advanced Features

**Feature**: 001-todo-features-enhancement  
**Date**: 2026-02-15  
**Status**: Completed

## 1. Extended Task Entity

### 1.1 Task Model
```python
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class RecurrencePatternEnum(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    custom = "custom"

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(..., max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    user_id: str = Field(..., foreign_key="user.id")  # Existing field
    
    # NEW: Priority (default: medium)
    priority: PriorityEnum = Field(default=PriorityEnum.medium)
    
    # NEW: Tags (max 5 per task)
    tags_str: Optional[str] = Field(default=None, max_length=255)  # Serialized as comma-separated string
    
    # NEW: Due Date
    due_date: Optional[datetime] = Field(default=None)
    
    # NEW: Recurrence
    recurrence_pattern: Optional[RecurrencePatternEnum] = Field(default=None)
    recurrence_interval: Optional[int] = Field(default=None)  # For custom patterns
    recurrence_end_date: Optional[datetime] = Field(default=None)
    parent_task_id: Optional[int] = Field(default=None, foreign_key="task.id")  # For recurring tasks
    
    # NEW: Reminder
    reminder_offset_minutes: Optional[int] = Field(default=None)  # Minutes before due date
    
    # Existing relationships
    user: "User" = Relationship(back_populates="tasks")
    sub_tasks: List["Task"] = Relationship(back_populates="parent_task")
    parent_task: Optional["Task"] = Relationship(back_populates="sub_tasks")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

### 1.2 Helper Methods for Tags
```python
from typing import List

def get_tags(self) -> List[str]:
    """Get deserialized tags list"""
    if self.tags_str:
        return [tag.strip() for tag in self.tags_str.split(',') if tag.strip()]
    return []

def set_tags(self, tags: List[str]) -> None:
    """Set serialized tags string (max 5)"""
    if len(tags) > 5:
        raise ValueError("Maximum 5 tags per task")
    self.tags_str = ','.join(tags[:5])
```

### 1.3 Task Event Model
```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskEvent(BaseModel):
    task_id: int
    user_id: str
    event_type: str  # 'created', 'updated', 'completed', 'deleted', 'reminder_triggered'
    timestamp: datetime
    payload: Optional[dict] = None  # Additional data depending on event type
```

### 1.4 Reminder Model
```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Reminder(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    task_id: int = Field(..., foreign_key="task.id")
    user_id: str = Field(..., foreign_key="user.id")
    scheduled_time: datetime
    triggered: bool = Field(default=False)
    snoozed_until: Optional[datetime] = Field(default=None)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

## 2. Validation Rules

### 2.1 Task Validation
- Priority must be one of: low, medium, high (default: medium)
- Tags must be 5 or fewer per task
- Due date cannot be in the past (configurable)
- Recurrence end date must be after start date
- Reminder offset must be positive if set

### 2.2 Recurrence Validation
- Parent task must exist for recurring tasks
- Recurrence pattern must be valid enum value
- Custom interval must be positive if pattern is custom
- Max 10 future instances for recurring tasks

## 3. Indexes for Performance

### 3.1 Required Indexes
```sql
-- For filtering by priority
CREATE INDEX idx_task_priority ON task(priority);

-- For filtering by tags (GIN index for array-like operations)
CREATE INDEX idx_task_tags ON task USING gin(tags_str);

-- For filtering by due date
CREATE INDEX idx_task_due_date ON task(due_date);

-- For filtering by user and due date (common combination)
CREATE INDEX idx_task_user_due_date ON task(user_id, due_date);

-- For filtering by user and priority (common combination)
CREATE INDEX idx_task_user_priority ON task(user_id, priority);

-- For filtering by user and tags (common combination)
CREATE INDEX idx_task_user_tags ON task(user_id, tags_str);
```

### 3.2 Composite Indexes for Sorting
```sql
-- For sorting by due date and priority
CREATE INDEX idx_task_sort_due_priority ON task(due_date, priority DESC);

-- For sorting by creation date
CREATE INDEX idx_task_created_at ON task(created_at DESC);
```

## 4. State Transitions

### 4.1 Task State Transitions
```
CREATED -> ACTIVE (default)
ACTIVE -> COMPLETED (when task is marked complete)
COMPLETED -> ACTIVE (when task is unmarked)
ACTIVE -> DELETED (when task is deleted)
```

### 4.2 Recurring Task Lifecycle
```
PARENT_TASK_CREATED -> WAITING_FOR_NEXT_INSTANCE
WAITING_FOR_NEXT_INSTANCE -> NEW_INSTANCE_CREATED (based on recurrence pattern)
NEW_INSTANCE_CREATED -> ACTIVE
ACTIVE -> COMPLETED -> TRIGGER_RECURRING_LOGIC
TRIGGER_RECURRING_LOGIC -> CREATE_NEXT_INSTANCE_OR_END
```

### 4.3 Reminder Lifecycle
```
TASK_WITH_DUE_DATE_CREATED -> SCHEDULE_REMINDER
SCHEDULE_REMINDER -> WAITING_FOR_REMINDER_TIME
WAITING_FOR_REMINDER_TIME -> REMINDER_TRIGGERED (at scheduled time)
REMINDER_TRIGGERED -> DELIVER_TO_USER
DELIVER_TO_USER -> MARK_AS_TRIGGERED
```
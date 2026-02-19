# API Contracts: Phase V Part A – Intermediate & Advanced Features

## 1. Task Management Extensions

### 1.1 Update Task with Priority
```
PUT /api/tasks/{task_id}
{
  "priority": "high" | "medium" | "low"
}
```
- Updates the priority of an existing task
- Priority defaults to "medium" if not specified during creation
- Returns updated task object

### 1.2 Update Task with Tags
```
PUT /api/tasks/{task_id}
{
  "tags": ["tag1", "tag2", "tag3"]
}
```
- Updates tags for a task (max 5 tags)
- Returns updated task object or error if more than 5 tags provided

### 1.3 Update Task with Due Date
```
PUT /api/tasks/{task_id}
{
  "due_date": "2026-02-20T10:00:00Z",
  "reminder_offset_minutes": 60
}
```
- Sets due date and optional reminder offset for a task
- Reminder offset specifies minutes before due date to trigger reminder
- Returns updated task object

### 1.4 Create Recurring Task
```
POST /api/tasks/
{
  "title": "Water plants",
  "description": "Water the office plants",
  "recurrence_pattern": "weekly",
  "recurrence_interval": 1,
  "recurrence_start_date": "2026-02-15T00:00:00Z",
  "recurrence_end_date": "2026-12-31T23:59:59Z"
}
```
- Creates a recurring task with specified pattern
- recurrence_pattern: "daily", "weekly", "monthly", "custom"
- recurrence_interval: number of units between occurrences (for custom pattern)
- Returns created task object with recurrence details

## 2. Search, Filter, Sort Endpoints

### 2.1 Search Tasks
```
GET /api/tasks/search?q={query}&user_id={user_id}
```
- Full-text search across task titles and descriptions
- Returns paginated list of matching tasks
- Query parameters:
  - q: search query string
  - user_id: user identifier
  - page: page number (default 1)
  - limit: results per page (default 20)

### 2.2 Filter Tasks
```
GET /api/tasks/filter?user_id={user_id}&priority={priority}&tags={tags}&due_date_from={date}&due_date_to={date}&has_due_date={bool}
```
- Filter tasks by multiple criteria
- Query parameters:
  - user_id: user identifier
  - priority: "low", "medium", "high" (optional)
  - tags: comma-separated list of tags (optional)
  - due_date_from: earliest due date (optional)
  - due_date_to: latest due date (optional)
  - has_due_date: boolean to filter tasks with/without due dates (optional)
- Returns filtered list of tasks

### 2.3 Sort Tasks
```
GET /api/tasks/sort?user_id={user_id}&sort_by={field}&order={asc|desc}
```
- Sort tasks by specified field
- Query parameters:
  - user_id: user identifier
  - sort_by: "due_date", "priority", "created_at", "title" (default: created_at)
  - order: "asc" or "desc" (default: desc)
- Returns sorted list of tasks

## 3. Reminder Management

### 3.1 Snooze Reminder
```
POST /api/reminders/{reminder_id}/snooze
{
  "snooze_duration_minutes": 30
}
```
- Snoozes a reminder for the specified duration
- Returns updated reminder object with new scheduled time

### 3.2 Dismiss Reminder
```
DELETE /api/reminders/{reminder_id}
```
- Dismisses a reminder
- Returns success status

## 4. Event Notifications

### 4.1 Task Event Stream
```
GET /api/events/stream?user_id={user_id}
```
- Server-sent events stream for real-time task updates
- Events include: task created, updated, completed, deleted, reminder triggered
- Requires user authentication

## 5. Response Format

### 5.1 Success Response
```json
{
  "success": true,
  "data": { /* response data */ },
  "message": "Operation completed successfully"
}
```

### 5.2 Error Response
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Descriptive error message",
    "details": { /* additional error details */ }
  }
}
```

## 6. Common Error Codes

- `INVALID_INPUT`: Provided data doesn't meet validation requirements
- `RESOURCE_NOT_FOUND`: Requested resource doesn't exist
- `UNAUTHORIZED`: User doesn't have permission for the requested operation
- `VALIDATION_ERROR`: Input validation failed (e.g., too many tags)
- `RECURRING_TASK_LIMIT_EXCEEDED`: Creating more than 10 future instances for recurring task
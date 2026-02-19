---

description: "Task list template for feature implementation"
---

# Tasks: Phase V Part A – Intermediate & Advanced Features

**Input**: Design documents from `/specs/001-todo-features-enhancement/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in backend/src/
- [ ] T002 Initialize Python 3.11 project with FastAPI, SQLModel, Dapr SDK, Pydantic dependencies
- [ ] T003 [P] Configure linting and formatting tools for Python backend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T004 Setup database schema and migrations framework with extended Task model
- [ ] T005 [P] Configure Dapr components for PostgreSQL state store, Kafka/Redpanda pub/sub
- [ ] T006 [P] Setup API routing and middleware structure extending existing backend
- [ ] T007 Create base models/entities that all stories depend on (extended Task model)
- [ ] T008 Configure error handling and logging infrastructure for new features
- [ ] T009 Setup environment configuration management for Dapr integration

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Priority Setting for Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to assign priority levels (low, medium, high) to tasks with medium as default

**Independent Test**: Can be fully tested by creating tasks with different priority levels and verifying they display and sort correctly in the chat interface.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Contract test for priority update endpoint in backend/tests/contract/test_priority.py
- [ ] T011 [P] [US1] Integration test for priority assignment in backend/tests/integration/test_priority.py

### Implementation for User Story 1

- [ ] T012 [P] [US1] Create PriorityEnum in backend/src/models/enums.py
- [ ] T013 [US1] Update Task model with priority field in backend/src/models/task.py
- [ ] T014 [US1] Implement PriorityService in backend/src/services/priority_service.py
- [ ] T015 [US1] Implement PUT /api/tasks/{task_id} endpoint for priority updates in backend/src/api/task_routes.py
- [ ] T016 [US1] Add validation for priority assignment (default to medium)
- [ ] T017 [US1] Add logging for priority operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Tagging Tasks (Priority: P1)

**Goal**: Allow users to tag tasks with free-text labels (max 5 per task) for categorization

**Independent Test**: Can be fully tested by creating tasks with tags and verifying they can be filtered and searched by tags.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Contract test for tag update endpoint in backend/tests/contract/test_tags.py
- [ ] T019 [P] [US2] Integration test for tag assignment and validation in backend/tests/integration/test_tags.py

### Implementation for User Story 2

- [ ] T020 [P] [US2] Update Task model with tags field in backend/src/models/task.py
- [ ] T021 [US2] Implement TagService with validation (max 5 tags) in backend/src/services/tag_service.py
- [ ] T022 [US2] Implement PUT /api/tasks/{task_id} endpoint for tag updates in backend/src/api/task_routes.py
- [ ] T023 [US2] Add helper methods for tag serialization/deserialization in backend/src/models/task.py
- [ ] T024 [US2] Add validation for tag count limits

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Search, Filter, Sort (Priority: P2)

**Goal**: Enable users to search, filter, and sort tasks based on various criteria

**Independent Test**: Can be fully tested by creating multiple tasks with different properties and verifying search, filter, and sort functions work correctly.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US3] Contract test for search endpoint in backend/tests/contract/test_search.py
- [ ] T026 [P] [US3] Contract test for filter endpoint in backend/tests/contract/test_filter.py
- [ ] T027 [P] [US3] Contract test for sort endpoint in backend/tests/contract/test_sort.py

### Implementation for User Story 3

- [ ] T028 [P] [US3] Create SearchService in backend/src/services/search_service.py
- [ ] T029 [US3] Create FilterService in backend/src/services/filter_service.py
- [ ] T030 [US3] Create SortService in backend/src/services/sort_service.py
- [ ] T031 [US3] Implement GET /api/tasks/search endpoint in backend/src/api/task_routes.py
- [ ] T032 [US3] Implement GET /api/tasks/filter endpoint in backend/src/api/task_routes.py
- [ ] T033 [US3] Implement GET /api/tasks/sort endpoint in backend/src/api/task_routes.py
- [ ] T034 [US3] Add database indexes for efficient search/filter/sort operations in backend/src/database/indexes.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Recurring Tasks (Priority: P3)

**Goal**: Enable users to create recurring tasks with various patterns that auto-generate new instances

**Independent Test**: Can be fully tested by creating recurring tasks with different patterns and verifying new instances are created appropriately.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T035 [P] [US4] Contract test for recurring task creation endpoint in backend/tests/contract/test_recurring.py
- [ ] T036 [P] [US4] Integration test for recurring task lifecycle in backend/tests/integration/test_recurring.py

### Implementation for User Story 4

- [ ] T037 [P] [US4] Create RecurrencePatternEnum in backend/src/models/enums.py
- [ ] T038 [US4] Update Task model with recurrence fields in backend/src/models/task.py
- [ ] T039 [US4] Implement RecurringTaskService in backend/src/services/recurring_task_service.py
- [ ] T040 [US4] Implement POST /api/tasks/ endpoint for recurring task creation in backend/src/api/task_routes.py
- [ ] T041 [US4] Create event handler for recurring task generation in backend/src/events/recurring_handler.py
- [ ] T042 [US4] Configure Dapr Pub/Sub for recurring task events in backend/config/dapr_components/pubsub.yaml
- [ ] T043 [US4] Implement task completion logic that triggers next instance creation

**Checkpoint**: At this point, all user stories should now be independently functional

---

## Phase 7: User Story 5 - Due Dates & Reminders (Priority: P3)

**Goal**: Enable users to set due dates and receive reminders for tasks

**Independent Test**: Can be fully tested by setting due dates and reminders and verifying they trigger appropriately.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T044 [P] [US5] Contract test for due date/reminder creation endpoint in backend/tests/contract/test_reminders.py
- [ ] T045 [P] [US5] Contract test for snooze/dismiss endpoints in backend/tests/contract/test_reminder_actions.py

### Implementation for User Story 5

- [ ] T046 [P] [US5] Create Reminder model in backend/src/models/reminder.py
- [ ] T047 [US5] Update Task model with due date and reminder fields in backend/src/models/task.py
- [ ] T048 [US5] Implement ReminderService in backend/src/services/reminder_service.py
- [ ] T049 [US5] Implement PUT /api/tasks/{task_id} endpoint for due date/reminder updates in backend/src/api/task_routes.py
- [ ] T050 [US5] Implement POST /api/reminders/{reminder_id}/snooze endpoint in backend/src/api/reminder_routes.py
- [ ] T051 [US5] Implement DELETE /api/reminders/{reminder_id} endpoint in backend/src/api/reminder_routes.py
- [ ] T052 [US5] Create event handler for reminder delivery in backend/src/events/reminder_handler.py
- [ ] T053 [US5] Configure Dapr Jobs API for exact-time reminder delivery in backend/config/dapr_components/jobs.yaml

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T054 [P] Documentation updates in backend/docs/
- [ ] T055 Code cleanup and refactoring
- [ ] T056 Performance optimization across all stories
- [ ] T057 [P] Additional unit tests (if requested) in backend/tests/unit/
- [ ] T058 Security hardening
- [ ] T059 [P] Run quickstart.md validation in backend/validation/

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for priority update endpoint in backend/tests/contract/test_priority.py"
Task: "Integration test for priority assignment in backend/tests/integration/test_priority.py"

# Launch all models for User Story 1 together:
Task: "Create PriorityEnum in backend/src/models/enums.py"
Task: "Update Task model with priority field in backend/src/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
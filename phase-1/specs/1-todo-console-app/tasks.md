---
description: "Task list for Phase I In-Memory Python Todo Console Application"
---

# Tasks: Phase I – In-Memory Python Todo Console Application

**Input**: Design documents from `/specs/1-todo-console-app/`
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

- [x] T001 Create project structure per implementation plan
- [x] T002 Initialize Python 3.13+ project with pyproject.toml for UV package management
- [x] T003 [P] Create src/todo_app/ directory structure with __init__.py files
- [x] T004 [P] Create tests/ directory structure with __init__.py files
- [x] T005 Create README.md and CLAUDE.md files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create Task model in src/todo_app/models/task.py
- [x] T007 Create TaskService in src/todo_app/services/task_service.py
- [x] T008 Create in-memory storage mechanism in src/todo_app/services/task_service.py
- [x] T009 Implement sequential ID assignment in src/todo_app/services/task_service.py
- [x] T010 Create ConsoleInterface in src/todo_app/cli/console_interface.py
- [x] T011 Set up main application entry point in src/todo_app/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and Manage Tasks (Priority: P1) 🎯 MVP

**Goal**: Implement the core functionality to add, view, update, delete, and mark tasks as complete/incomplete

**Independent Test**: The application can be fully tested by adding tasks, viewing the list, updating tasks, deleting tasks, and marking them complete/incomplete. This delivers the complete value of a basic todo application.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T012 [P] [US1] Unit test for Task model in tests/unit/test_task.py
- [x] T013 [P] [US1] Unit test for TaskService add_task method in tests/unit/test_task_service.py
- [x] T014 [P] [US1] Unit test for TaskService get_all_tasks method in tests/unit/test_task_service.py
- [x] T015 [P] [US1] Unit test for TaskService update_task method in tests/unit/test_task_service.py
- [x] T016 [P] [US1] Unit test for TaskService delete_task method in tests/unit/test_task_service.py
- [x] T017 [P] [US1] Unit test for TaskService mark_complete/incomplete methods in tests/unit/test_task_service.py

### Implementation for User Story 1

- [x] T018 [US1] Implement Task model with ID, title, description, and completion status in src/todo_app/models/task.py
- [x] T019 [US1] Implement add_task method in src/todo_app/services/task_service.py
- [x] T020 [US1] Implement get_all_tasks method in src/todo_app/services/task_service.py
- [x] T021 [US1] Implement update_task method in src/todo_app/services/task_service.py
- [x] T022 [US1] Implement delete_task method in src/todo_app/services/task_service.py
- [x] T023 [US1] Implement mark_task_complete method in src/todo_app/services/task_service.py
- [x] T024 [US1] Implement mark_task_incomplete method in src/todo_app/services/task_service.py
- [x] T025 [US1] Add validation for empty titles in src/todo_app/services/task_service.py
- [x] T026 [US1] Add ID validation for operations in src/todo_app/services/task_service.py
- [x] T027 [US1] Implement view tasks display in src/todo_app/cli/console_interface.py
- [x] T028 [US1] Implement add task interface in src/todo_app/cli/console_interface.py
- [x] T029 [US1] Implement update task interface in src/todo_app/cli/console_interface.py
- [x] T030 [US1] Implement delete task interface in src/todo_app/cli/console_interface.py
- [x] T031 [US1] Implement mark complete/incomplete interface in src/todo_app/cli/console_interface.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Console Interaction (Priority: P2)

**Goal**: Implement menu-driven console interface with numbered options for all operations

**Independent Test**: Users can navigate the console menu system and execute all basic operations without requiring a GUI, providing the core value of a console-based todo app.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T032 [P] [US2] Integration test for menu navigation in tests/integration/test_console_flow.py
- [x] T033 [P] [US2] Test for console input handling in tests/unit/test_console_interface.py

### Implementation for User Story 2

- [x] T034 [US2] Implement main menu display in src/todo_app/cli/console_interface.py
- [x] T035 [US2] Implement menu option selection in src/todo_app/cli/console_interface.py
- [x] T036 [US2] Implement user input validation in src/todo_app/cli/console_interface.py
- [x] T037 [US2] Integrate menu system with main application in src/todo_app/main.py
- [x] T038 [US2] Add console formatting and user feedback in src/todo_app/cli/console_interface.py
- [x] T039 [US2] Add error handling for user input in src/todo_app/cli/console_interface.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - In-Memory Data Persistence (Priority: P3)

**Goal**: Ensure task data persists in memory during the application session

**Independent Test**: The application maintains task data in memory during the current session, allowing users to perform multiple operations on tasks.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T040 [P] [US3] Test for data persistence across operations in tests/integration/test_data_persistence.py

### Implementation for User Story 3

- [x] T041 [US3] Implement proper in-memory storage with Python lists/dicts in src/todo_app/services/task_service.py
- [x] T042 [US3] Ensure ID gaps are preserved after deletion in src/todo_app/services/task_service.py
- [x] T043 [US3] Add memory management for large task lists in src/todo_app/services/task_service.py
- [x] T044 [US3] Add session lifecycle management in src/todo_app/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Edge Cases and Error Handling

**Goal**: Handle all specified edge cases and provide appropriate error messages

**Independent Test**: Application properly handles invalid operations and provides helpful error messages.

- [x] T045 [P] Handle invalid task ID for update operations in src/todo_app/services/task_service.py
- [x] T046 [P] Handle invalid task ID for delete operations in src/todo_app/services/task_service.py
- [x] T047 [P] Handle invalid task ID for mark complete/incomplete operations in src/todo_app/services/task_service.py
- [x] T048 [P] Handle empty task list when viewing in src/todo_app/cli/console_interface.py
- [x] T049 [P] Handle empty task list when operating on tasks in src/todo_app/cli/console_interface.py
- [x] T050 [P] Add appropriate error messages for all invalid operations in src/todo_app/cli/console_interface.py

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T051 [P] Update README.md with usage instructions
- [x] T052 [P] Add proper formatting for checkbox-style status indicators in src/todo_app/cli/console_interface.py
- [x] T053 [P] Add validation for sequential numeric IDs starting from 1 in src/todo_app/services/task_service.py
- [x] T054 [P] Add validation for empty descriptions being allowed in src/todo_app/services/task_service.py
- [x] T055 [P] Add integration tests for complete user flow in tests/integration/test_console_flow.py
- [x] T056 [P] Code cleanup and refactoring across all modules
- [x] T057 [P] Documentation updates in docstrings across all modules
- [x] T058 Run quickstart.md validation

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

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
Task: "Unit test for Task model in tests/unit/test_task.py"
Task: "Unit test for TaskService add_task method in tests/unit/test_task_service.py"

# Launch all models for User Story 1 together:
Task: "Implement Task model with ID, title, description, and completion status in src/todo_app/models/task.py"
Task: "Implement add_task method in src/todo_app/services/task_service.py"
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
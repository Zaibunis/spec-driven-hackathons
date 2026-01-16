# Research: Phase I – In-Memory Python Todo Console Application

**Feature**: 1-todo-console-app
**Date**: 2025-12-22

## Decision Log

### 1. Python Version Selection
**Decision**: Use Python 3.13+
**Rationale**: The specification explicitly requires Python 3.13+, which provides the latest language features and performance improvements. This aligns with the project's constraint to use UV + Python 3.13+.
**Alternatives considered**: Python 3.11, Python 3.12 - but the spec requires 3.13+

### 2. Storage Approach
**Decision**: In-memory data structures using Python lists and dictionaries
**Rationale**: The specification explicitly requires "storage must be purely in-memory" with no external database. Python's built-in data structures provide efficient in-memory storage suitable for the application's constraints.
**Alternatives considered**: SQLite in-memory mode, external databases (rejected per spec)

### 3. CLI Framework
**Decision**: Built-in Python input/output with custom menu system
**Rationale**: The application requires a simple menu-driven interface with numbered options. Python's built-in input() and print() functions are sufficient for this basic console application without adding external dependencies.
**Alternatives considered**: argparse, click, typer (rejected as unnecessary complexity for this simple interface)

### 4. Project Structure
**Decision**: Modular Python package with separation of concerns
**Rationale**: Organizing the code into models, services, and CLI components follows clean architecture principles and makes the code more maintainable and testable.
**Alternatives considered**: Single file application (rejected as it would not be maintainable)

### 5. Testing Framework
**Decision**: pytest
**Rationale**: pytest is the most popular and feature-rich testing framework for Python. It provides excellent support for fixtures, parameterized tests, and has good integration with most development tools.
**Alternatives considered**: unittest (built-in), nose (pytest is more modern and feature-rich)

### 6. Dependency Management
**Decision**: UV package manager with pyproject.toml
**Rationale**: The specification mentions using UV, which is a fast Python package installer and resolver. Using pyproject.toml follows modern Python packaging standards.
**Alternatives considered**: pip + requirements.txt (UV is specified in requirements)

### 7. Task ID Management
**Decision**: Sequential numeric IDs starting from 1
**Rationale**: As clarified in the spec, sequential numeric IDs are intuitive for console applications and easy for users to reference.
**Alternatives considered**: UUIDs, custom strings (rejected as more complex for console use)

### 8. Status Display Format
**Decision**: Checkbox-style indicators [ ] and [x]
**Rationale**: As clarified in the spec, checkbox-style indicators are intuitive and commonly used in console applications.
**Alternatives considered**: Text labels, symbols (decided per spec clarification)
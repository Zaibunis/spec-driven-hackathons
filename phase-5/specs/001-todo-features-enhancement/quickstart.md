# Quickstart Guide: Phase V Part A – Intermediate & Advanced Features

**Feature**: 001-todo-features-enhancement  
**Date**: 2026-02-15  
**Status**: Draft

## Overview
This quickstart guide provides instructions for validating the new features implemented in Phase V Part A: priorities, tags, search/filter/sort, recurring tasks, and due date reminders.

## Prerequisites
- Running Phase IV Todo Chatbot with Dapr sidecar
- Access to the chat interface
- Valid user authentication token

## New Feature Validation Steps

### 1. Priority Setting
1. Create a new task: "Add priority test task"
2. Set priority: "Set priority to high for task 'Add priority test task'"
3. Verify: Check that the task shows as high priority in the list
4. Default test: Create a task without specifying priority and verify it defaults to medium

### 2. Tagging
1. Create a task: "Add tagging test task"
2. Add tags: "Add tags #work #urgent to task 'Add tagging test task'"
3. Verify: Check that the task shows the assigned tags
4. Limit test: Try adding more than 5 tags and verify the system rejects extras
5. Filter test: Ask to show tasks with "#work" tag and verify only matching tasks appear

### 3. Search, Filter, Sort
1. Create multiple tasks with different properties (priorities, tags, due dates)
2. Search test: "Find tasks containing 'test'" and verify relevant results
3. Filter test: "Show only high priority tasks" and verify filtering works
4. Sort test: "Sort tasks by due date" and verify chronological ordering

### 4. Recurring Tasks
1. Create a recurring task: "Create recurring task 'Water plants' weekly"
2. Verify: Check that the task is marked as recurring
3. Completion test: Complete the recurring task and verify a new instance is created
4. End date test: Create a recurring task with an end date and verify it stops after that date

### 5. Due Dates & Reminders
1. Create a task with due date: "Create task 'Meeting prep' due tomorrow at 9am"
2. Set reminder: "Remind me 1 hour before 'Meeting prep' is due"
3. Verify: Check that the due date and reminder are set correctly
4. Overdue test: View tasks with past due dates and verify they show as overdue

### 6. Combined Features
1. Create a task with multiple features: "Create high priority #work task 'Weekly report' due Friday with weekly recurrence and 1-day reminder"
2. Verify: Check that all features are applied correctly to the task

## Expected Outcomes
- All new features work through the existing chat interface
- Natural language commands are properly parsed
- No regression in existing Phase IV functionality
- Response times remain under 500ms
- User data remains isolated and secure

## Troubleshooting
- If natural language commands aren't recognized, try more explicit phrasing
- If recurring tasks don't generate new instances, check Dapr Pub/Sub connectivity
- If reminders don't trigger, verify Dapr Jobs API configuration
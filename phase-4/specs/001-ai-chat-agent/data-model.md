# Data Model: AI Chat Agent & Integration

**Feature**: AI Chat Agent & Integration
**Date**: 2026-01-20
**Branch**: 001-ai-chat-agent

## Overview

This document defines the data models required for the AI-powered chatbot for natural language todo management. The models follow SQLModel patterns and maintain user data isolation as required by the constitution.

## Entity: Conversation

**Description**: Represents a user's chat session with the AI agent, containing metadata and context

**Fields**:
- `id`: UUID (Primary Key) - Unique identifier for the conversation
- `user_id`: UUID (Foreign Key) - Reference to the owning user
- `title`: String (optional) - Auto-generated title based on conversation content
- `created_at`: DateTime - Timestamp when conversation was initiated
- `updated_at`: DateTime - Timestamp of last activity
- `is_active`: Boolean - Whether the conversation is currently active

**Relationships**:
- One-to-many with Message entity (one conversation has many messages)
- Many-to-one with User entity (many conversations belong to one user)

**Validation**:
- `user_id` must reference an existing user
- `created_at` must be before `updated_at`

## Entity: Message

**Description**: Individual user or AI messages within a conversation, including content, timestamp, and sender type

**Fields**:
- `id`: UUID (Primary Key) - Unique identifier for the message
- `conversation_id`: UUID (Foreign Key) - Reference to the parent conversation
- `sender_type`: Enum ['user', 'ai'] - Indicates if message is from user or AI
- `content`: Text - The actual message content
- `timestamp`: DateTime - When the message was sent
- `metadata`: JSON (optional) - Additional data for AI processing

**Relationships**:
- Many-to-one with Conversation entity (many messages belong to one conversation)
- One-to-one with User for user messages (AI messages don't have a user reference)

**Validation**:
- `conversation_id` must reference an existing conversation
- `sender_type` must be either 'user' or 'ai'
- `content` must not be empty

## Entity: User

**Description**: Registered user account with authentication tokens and associated data ownership

**Fields**:
- `id`: UUID (Primary Key) - Unique identifier for the user
- `email`: String - User's email address
- `name`: String (optional) - User's display name
- `created_at`: DateTime - When the user account was created
- `updated_at`: DateTime - Last update to user account

**Relationships**:
- One-to-many with Conversation entity (one user has many conversations)
- One-to-many with User Messages (one user has many messages they sent)

**Validation**:
- `email` must be a valid email format
- `email` must be unique across all users

## State Transitions

### Conversation States
- **Active**: Currently in progress, new messages can be added
- **Inactive**: No recent activity, but history preserved
- **Archived**: Long-term storage after extended inactivity

### Message States
- **Pending**: AI is processing the message
- **Processed**: AI has responded and message is saved
- **Errored**: Failed to process, requires handling

## Indexes

1. **Conversation Index**: `user_id` for efficient retrieval of user's conversations
2. **Message Index**: `conversation_id` and `timestamp` for chronological ordering
3. **User Index**: `email` for efficient lookup during authentication

## Constraints

1. **Data Isolation**: Foreign key constraints ensure messages and conversations can only reference the user's own records
2. **Referential Integrity**: Cascading deletes from User → Conversation → Message to maintain consistency
3. **Timestamp Consistency**: `updated_at` must always be >= `created_at` for all entities
4. **Content Validation**: Message content must be non-empty and within reasonable length limits
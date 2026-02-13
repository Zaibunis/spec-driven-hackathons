// T041: apiClient utility functions for conversation history

import apiClient from '../../lib/api-client';
import { Conversation, ChatMessage } from '../types/chatTypes';

const CONVERSATION_STORAGE_KEY = 'conversationHistory';

/**
 * Retrieves the conversation history for a given user.
 *
 * @param userId - The ID of the user.
 * @returns The user's conversation history, or null if not found.
 */
export function getConversationHistory(userId: string): Conversation | null {
  if (typeof window === 'undefined') return null;

  const storedHistory = localStorage.getItem(`${CONVERSATION_STORAGE_KEY}_${userId}`);
  if (storedHistory) {
    try {
      return JSON.parse(storedHistory);
    } catch (e) {
      console.error('Failed to parse conversation history:', e);
      return null;
    }
  }
  return null;
}

/**
 * Adds a message to the user's conversation history.
 *
 * @param userId - The ID of the user.
 * @param message - The message to add.
 */
export function addMessageToConversation(userId: string, message: ChatMessage): void {
  if (typeof window === 'undefined') return;

  const history = getConversationHistory(userId) || {
    id: `conv_${userId}`,
    userId,
    messages: [],
    createdAt: new Date(),
    updatedAt: new Date(),
  };

  history.messages.push(message);
  history.updatedAt = new Date();

  try {
    localStorage.setItem(`${CONVERSATION_STORAGE_KEY}_${userId}`, JSON.stringify(history));
  } catch (e) {
    console.error('Failed to save conversation history:', e);
  }
}

/**
 * Clears the conversation history for a given user.
 *
 * @param userId - The ID of the user.
 */
export function clearConversationHistory(userId: string): void {
  if (typeof window === 'undefined') return;

  localStorage.removeItem(`${CONVERSATION_STORAGE_KEY}_${userId}`);
}
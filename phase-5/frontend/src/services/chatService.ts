// T040: chatService for handling chat API calls

import apiClient from '../lib/api-client';

interface SendMessagePayload {
  message: string;
}

interface SendMessageResponse {
  success: boolean;
  assistantMessage: string;
  error?: {
    message: string;
  };
}

/**
 * Sends a user's message to the backend chat agent.
 *
 * @param userId - The ID of the user sending the message.
 * @param payload - The message payload.
 * @returns A promise that resolves to the server's response.
 */
export async function sendMessage(
  userId: string,
  payload: SendMessagePayload
): Promise<SendMessageResponse> {
  try {
    const response = await apiClient.post(
      `/chat/agent/${userId}`,
      payload
    );

    // Assuming the response has a `data` object with the assistant's reply
    if (response.data && response.data.assistantMessage) {
      return {
        success: true,
        assistantMessage: response.data.assistantMessage,
      };
    } else {
      return {
        success: false,
        assistantMessage: '',
        error: {
          message: 'Invalid response from server',
        },
      };
    }
  } catch (error: any) {
    const errorMessage =
      error.response?.data?.error?.message ||
      error.response?.data?.detail ||
      'An unexpected error occurred';
    
    return {
      success: false,
      assistantMessage: '',
      error: {
        message: errorMessage,
      },
    };
  }
}
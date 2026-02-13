import React, { useState, useEffect } from 'react';
import { ChatMessage } from '../types/chatTypes';
import { addMessageToConversation } from '../utils/apiClient';
import { GoogleGenerativeAI } from '@google/generative-ai';
import { ChatUI } from './ChatUI/page'; // Your custom ChatUI component

interface ChatKitWrapperProps {
  userId: string;
}

const ChatKitWrapper: React.FC<ChatKitWrapperProps> = ({ userId }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const geminiKey = process.env.NEXT_PUBLIC_GEMINI_API_KEY;

    if (!geminiKey) {
      setError('Missing NEXT_PUBLIC_GEMINI_API_KEY');
    }

    console.log('ChatKit initialized (Gemini mode, no JWT required)');
  }, []);

  const handleSendMessage = async (input: string) => {
    setIsLoading(true);
    setError(null);

    try {
      // 1️⃣ Add user message immediately
      const userMessage: ChatMessage = {
        id: crypto.randomUUID ? crypto.randomUUID() : Date.now().toString(),
        content: input,
        role: 'user',
        timestamp: new Date(),
        status: 'sending' as const,
      };

      setMessages(prev => [...prev, userMessage]);

      // 2️⃣ Send to Gemini
      const assistantText = await sendToGemini(input);

      // 3️⃣ Add assistant message
      const assistantMessage: ChatMessage = {
        id: crypto.randomUUID ? crypto.randomUUID() : Date.now().toString(),
        content: assistantText,
        role: 'assistant',
        timestamp: new Date(),
        status: 'confirmed' as const,
      };

      setMessages(prev =>
        prev.map(msg =>
          msg.id === userMessage.id ? { ...msg, status: 'confirmed' as const } : msg
        ).concat(assistantMessage)
      );

      // 4️⃣ Optionally store messages in history
      addMessageToConversation(userId, userMessage);
      addMessageToConversation(userId, assistantMessage);

    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error occurred');
      console.error('Error sending message to Gemini:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const sendToGemini = async (message: string) => {
    const apiKey = process.env.NEXT_PUBLIC_GEMINI_API_KEY;
    if (!apiKey) throw new Error('Missing NEXT_PUBLIC_GEMINI_API_KEY');

    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: 'gemini-2.5-flash' });

    const result = await model.generateContent(message);
    const response = await result.response;
    return response.text();
  };

  return (
    <div className="chat-container h-full flex flex-col">
      {error && (
        <div className="error-message bg-red-900/50 border border-red-700/50 text-red-200 p-3 m-4 rounded-lg">
          Error: {error}
        </div>
      )}

      <ChatUI
        messages={messages}
        onSend={handleSendMessage}
        disabled={isLoading || !!error}
        placeholder="Type your message..."
      />

      {isLoading && (
        <div className="loading-indicator bg-blue-900/30 border border-blue-700/30 text-blue-200 p-2 m-2 rounded-lg text-center text-sm">
          Assistant is thinking...
        </div>
      )}
    </div>
  );
};

export default ChatKitWrapper;

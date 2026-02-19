export interface Message {
  id: string;
  content: string;
  sender: 'user' | 'ai'; // 'user' for user messages, 'ai' for AI responses
  timestamp: Date;
}

export interface Conversation {
  id: string;
  title?: string;
  createdAt: Date;
  updatedAt: Date;
  isActive: boolean;
}
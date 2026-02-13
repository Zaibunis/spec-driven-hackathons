'use client';

import React, { useState, useRef, useEffect } from 'react';
import { ChatMessage } from '../../types/chatTypes';
import { Button } from '@/src/styling/ui/button';
import { Input } from '@/src/styling/ui/input';
import { Send } from 'lucide-react';
import { Avatar, AvatarFallback } from '@/src/styling/ui/avatar';
import ReactMarkdown from 'react-markdown';
import { cn } from '@/src/lib/utils';

interface ChatUIProps {
  messages: ChatMessage[];
  onSend: (input: string) => void;
  onTaskOperation?: () => void; // Callback when task operations are performed
  disabled?: boolean;
  placeholder?: string;
}

export const ChatUI: React.FC<ChatUIProps> = ({
  messages,
  onSend,
  onTaskOperation,
  disabled,
  placeholder,
}) => {
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = () => {
    if (!input.trim() || disabled) return;

    // Check if this is a task-related command to trigger the callback
    const lowerInput = input.toLowerCase();
    const isTaskRelated = [
      'create task', 'add task', 'new task', 'make task',
      'update task', 'edit task', 'change task', 'modify task',
      'delete task', 'remove task', 'cancel task',
      'complete task', 'finish task', 'done task', 'mark task',
      'get tasks', 'list tasks', 'show tasks', 'view tasks',
      'todo', 'to do', 'to-do'
    ].some(keyword => lowerInput.includes(keyword));

    if (isTaskRelated && onTaskOperation) {
      onTaskOperation();
    }

    onSend(input);
    setInput('');
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="flex flex-col h-full bg-transparent">
      {/* Message List */}
      <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-6">
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={cn(
              'flex items-start gap-3',
              msg.role === 'user' ? 'justify-end' : 'justify-start'
            )}
          >
            {/* Assistant Avatar */}
            {msg.role === 'assistant' && (
              <Avatar className="w-9 h-9 border border-gray-600 bg-gradient-to-br from-blue-600 to-purple-600">
                <AvatarFallback className="bg-gradient-to-br from-blue-600 to-purple-600 text-white text-sm font-medium">
                  AI
                </AvatarFallback>
              </Avatar>
            )}

            {/* Message Content */}
            <div
              className={cn(
                'p-4 rounded-2xl max-w-[85%] sm:max-w-[75%] shadow-sm',
                msg.role === 'user'
                  ? 'bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-br-none' // Enhanced gradient for user messages
                  : 'bg-gray-800/80 text-gray-100 rounded-bl-none border border-gray-700/50'
              )}
            >
              <ReactMarkdown
                components={{
                  p: ({ node, ...props }) => <p className="m-0 leading-relaxed mb-2 last:mb-0" {...props} />,
                  ul: ({ node, ...props }) => <ul className="list-disc list-inside mb-2 ml-2" {...props} />,
                  ol: ({ node, ...props }) => <ol className="list-decimal list-inside mb-2 ml-2" {...props} />,
                  li: ({ node, ...props }) => <li className="mb-1" {...props} />,
                  code: ({ node, ...props }) => <code className="bg-black/30 px-1.5 py-0.5 rounded text-sm font-mono" {...props} />,
                  pre: ({ node, ...props }) => <pre className="bg-black/40 p-3 rounded-lg overflow-x-auto my-2 text-sm" {...props} />,
                  strong: ({ node, ...props }) => <strong className="font-semibold" {...props} />,
                  em: ({ node, ...props }) => <em className="italic" {...props} />,
                  blockquote: ({ node, ...props }) => <blockquote className="border-l-2 border-blue-500 pl-3 italic text-gray-300" {...props} />,
                }}
              >
                {msg.content}
              </ReactMarkdown>
            </div>

            {/* User Avatar */}
            {msg.role === 'user' && (
              <Avatar className="w-9 h-9 border border-gray-600 bg-gray-700">
                <AvatarFallback className="bg-gray-700 text-white text-sm font-medium">U</AvatarFallback>
              </Avatar>
            )}
          </div>
        ))}

        {/* Thinking Indicator */}
        {disabled && messages.length > 0 && (
          <div className="flex items-start gap-3 justify-start">
            <Avatar className="w-9 h-9 border border-gray-600 bg-gradient-to-br from-blue-600 to-purple-600">
              <AvatarFallback className="bg-gradient-to-br from-blue-600 to-purple-600 text-white text-sm font-medium">
                AI
              </AvatarFallback>
            </Avatar>
            <div className="p-4 rounded-2xl max-w-[85%] sm:max-w-[75%] bg-gray-800/80 rounded-bl-none border border-gray-700/50">
              <div className="flex items-center space-x-2">
                <span className="h-2 w-2 bg-blue-400 rounded-full animate-pulse"></span>
                <span className="h-2 w-2 bg-purple-400 rounded-full animate-pulse delay-75"></span>
                <span className="h-2 w-2 bg-cyan-400 rounded-full animate-pulse delay-150"></span>
                <span className="ml-2 text-sm text-gray-400">AI is thinking...</span>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Enhanced Input Area */}
      <div className="shrink-0 p-4 bg-gray-900/50 border-t border-gray-700/50 backdrop-blur-sm">
        <div className="relative max-w-4xl mx-auto">
          <div className="relative flex items-center bg-gray-800/80 border border-gray-700/50 rounded-2xl px-1 py-1 shadow-lg focus-within:ring-2 focus-within:ring-blue-500/50 focus-within:border-blue-500/50 transition-all duration-200">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={placeholder || 'Type your message...'}
              disabled={disabled}
              className="flex-1 bg-transparent border-none focus-visible:ring-0 focus-visible:ring-offset-0 text-gray-200 h-12 px-4 rounded-xl"
            />
            <Button
              onClick={handleSend}
              disabled={disabled || !input.trim()}
              className="mx-1 rounded-xl px-4"
              size="md"
              variant={input.trim() ? "gradient" : "ghost"}
            >
              <Send className="w-4 h-4" />
              <span className="ml-2 hidden sm:inline">Send</span>
            </Button>
          </div>
          <p className="text-xs text-gray-500 mt-2 text-center">
            Press Enter to send, Shift+Enter for new line
          </p>
        </div>
      </div>
    </div>
  );
}
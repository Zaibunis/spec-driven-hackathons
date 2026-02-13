'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/src/context/AuthContext';
import ChatKitWrapper from './ChatInterface/ChatKitWrapper';
import { Button } from '@/src/styling/ui/button';
import { X } from 'lucide-react';

export function FloatingChat() {
  const { user, isAuthenticated, loading } = useAuth();
  const router = useRouter();
  const [isOpen, setIsOpen] = useState(false);
  const [hasCheckedAuth, setHasCheckedAuth] = useState(false);

  // Check authentication status when component mounts
  useEffect(() => {
    if (!loading && !isAuthenticated && hasCheckedAuth && isOpen) {
      setIsOpen(false);
      router.push('/signin');
    }
  }, [isAuthenticated, loading, router, hasCheckedAuth, isOpen]);

  const handleToggleChat = () => {
    if (loading) return;

    if (!isAuthenticated) {
      router.push('/signin');
      return;
    }

    setIsOpen(!isOpen);
    setHasCheckedAuth(true);
  };

  const handleClose = () => {
    setIsOpen(false);
  };

  // Close the chat if user becomes unauthenticated while chat is open
  useEffect(() => {
    if (isAuthenticated && isOpen) {
      // Chat stays open when authenticated
    } else if (!isAuthenticated && isOpen) {
      // Close chat if user becomes unauthenticated
      setIsOpen(false);
    }
  }, [isAuthenticated, isOpen]);

  return (
    <>
      {/* Chat Toggle Button */}
      <button
        onClick={handleToggleChat}
        className={`fixed bottom-6 right-6 w-14 h-14 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-xl hover:scale-105 transition-all z-50 ${
          isOpen ? 'hidden' : ''
        }`}
        title="Chat"
      >
        💬
      </button>

      {/* Floating Chat Window */}
      {isOpen && isAuthenticated && (
        <div className="fixed bottom-24 right-6 w-full max-w-md h-[70vh] max-h-[600px] bg-gray-900/90 backdrop-blur-xl rounded-2xl shadow-2xl border border-gray-700/50 z-50 flex flex-col overflow-hidden">
          {/* Chat Header */}
          <div className="flex items-center justify-between p-4 bg-gray-900/50 border-b border-gray-700/50">
            <h2 className="text-lg font-semibold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
              AI Chat Agent
            </h2>
            <Button
              onClick={handleClose}
              variant="ghost"
              size="sm"
              className="text-gray-400 hover:text-white hover:bg-gray-800/50"
            >
              <X className="w-5 h-5" />
            </Button>
          </div>

          {/* Chat Content */}
          <div className="flex-1 overflow-hidden">
            {user && <ChatKitWrapper userId={user.id} />}
          </div>
        </div>
      )}
    </>
  );
}
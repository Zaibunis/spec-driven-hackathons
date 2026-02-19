'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import ChatKitWrapper from '../../components/ChatInterface/ChatKitWrapper';
import LoadingStates from '../../components/ChatInterface/LoadingStates';
import { useAuth } from '../../context/AuthContext';
import { getConversationHistory } from '../../components/utils/apiClient';
import { Conversation } from '../../components/types/chatTypes';

export default function ChatPage() {
  const { user, isAuthenticated, loading } = useAuth();
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [conversation, setConversation] = useState<Conversation | null>(null);

  // Redirect to sign-in page if not authenticated
  useEffect(() => {
    if (!isAuthenticated && !loading) {
      router.push('/signin');
    }
  }, [isAuthenticated, loading, router]);

  useEffect(() => {
    if (isAuthenticated && user) {
      // Load conversation history if available
      const history = getConversationHistory(user.id);
      if (history) {
        setConversation(history);
      }
    }
  }, [isAuthenticated, user]);

  if (loading) {
    return <LoadingStates isLoading={true} error={null} />;
  }

  // Don't render anything if not authenticated, as redirect will happen
  if (!isAuthenticated) {
    return null;
  }

  if (error) {
    return <LoadingStates isLoading={false} error={error} />;
  }

  return (
    <div className="relative h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 flex flex-col overflow-hidden">
      {/* Animated background elements */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-900/20 via-transparent to-transparent" />
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-600/10 rounded-full blur-3xl animate-pulse" />
      <div className="absolute bottom-1/3 right-1/4 w-80 h-80 bg-purple-600/10 rounded-full blur-3xl animate-pulse delay-1000" />

      {/* Unified Chat Card */}
      <div className="relative z-10 w-full max-w-6xl mx-auto flex-1 flex flex-col bg-gray-900/30 backdrop-blur-xl rounded-3xl shadow-2xl border border-gray-700/50 m-4 sm:m-6 overflow-hidden">
        <header className="chat-header w-full p-4 sm:p-6 flex-shrink-0 border-b border-gray-700/50 bg-gray-900/20">
          <div className="max-w-4xl mx-auto">
            <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent text-center">
              AI Chat Agent
            </h1>
            <p className="text-gray-400 text-center text-sm mt-2">
              Manage your tasks through natural language
            </p>
          </div>
        </header>

        <main className="chat-main flex-1 flex flex-col w-full overflow-hidden min-h-0">
          <div className="h-full max-w-4xl mx-auto flex flex-col">
            {user && <ChatKitWrapper userId={user.id} />}
          </div>
        </main>
      </div>
    </div>
  );
}
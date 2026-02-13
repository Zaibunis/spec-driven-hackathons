'use client';

import { useRouter } from 'next/navigation';
import { useAuth } from '@/src/context/AuthContext';

export function ChatIcon() {
  const { isAuthenticated, loading } = useAuth();
  const router = useRouter();

  const handleClick = () => {
    if (loading) return;

    if (!isAuthenticated) {
      router.push('/signin'); // 🔐 redirect to sign in
      return;
    }

    // For the original ChatIcon, we'll still navigate to the full chat page
    router.push('/chat');
  };

  return (
    <button
      onClick={handleClick}
      className="fixed bottom-6 right-6 w-14 h-14 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-xl hover:scale-105 transition"
      title="Chat"
    >
      💬
    </button>
  );
}

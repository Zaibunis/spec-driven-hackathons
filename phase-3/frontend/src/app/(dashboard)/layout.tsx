'use client';

import React, { useState } from 'react';
import { Menu } from 'lucide-react';
import { Sidebar } from '@/src/components/Layout/Sidebar';
import { FloatingChat } from '@/src/components/FloatingChat';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="app-bg flex h-screen overflow-hidden">
      <Sidebar open={sidebarOpen} onClose={() => setSidebarOpen(false)} />

      <div className="flex-1 flex flex-col min-w-0">
        {/* Mobile top bar */}
        <header className="lg:hidden flex items-center gap-3 px-4 py-3 border-b border-gray-800/80 bg-gray-950/60 backdrop-blur-xl">
          <button
            onClick={() => setSidebarOpen(true)}
            className="p-2 -ml-2 text-gray-300 hover:text-white hover:bg-gray-800/60 rounded-lg transition-colors"
            aria-label="Open menu"
          >
            <Menu className="w-6 h-6" />
          </button>
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">✓</span>
            </div>
            <span className="font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
              TaskFlow Pro
            </span>
          </div>
        </header>

        <main className="flex-1 overflow-y-auto relative">
          {children}
          <FloatingChat />
        </main>
      </div>
    </div>
  );
}

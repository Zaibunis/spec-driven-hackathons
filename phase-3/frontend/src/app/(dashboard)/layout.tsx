import React from 'react';
import { Sidebar } from '@/src/components/Layout/Sidebar';
import { FloatingChat } from '@/src/components/FloatingChat';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <main className="flex-1 overflow-y-auto bg-transparent relative">
        {children}
        <FloatingChat />
      </main>
    </div>
  );
}
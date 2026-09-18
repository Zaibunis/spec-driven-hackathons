'use client';

import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { Button } from '@/src/styling/ui/button';
import {
  LogOut,
  LayoutDashboard,
  MessageSquare,
  X,
} from 'lucide-react';
import { Avatar, AvatarFallback } from '@/src/styling/ui/avatar';
import { cn } from '@/src/lib/utils';
import { useAuth } from '@/src/context/AuthContext';

const links = [
  { href: '/', label: 'AI Chat', icon: MessageSquare },
  { href: '/tasks', label: 'Tasks', icon: LayoutDashboard },
];

interface SidebarProps {
  open?: boolean;
  onClose?: () => void;
}

export function Sidebar({ open = false, onClose }: SidebarProps) {
  const pathname = usePathname();
  const router = useRouter();
  const { user, signOut } = useAuth();

  const displayName = user?.email?.split('@')[0] || 'Guest';
  const initial = (user?.email?.[0] || 'G').toUpperCase();

  const handleSignOut = async () => {
    try {
      await signOut();
    } finally {
      router.push('/signin');
    }
  };

  return (
    <>
      {/* Mobile backdrop */}
      {open && (
        <div
          className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm lg:hidden"
          onClick={onClose}
          aria-hidden="true"
        />
      )}

      <aside
        className={cn(
          // Mobile: fixed slide-in drawer; Desktop: static flex column
          'fixed inset-y-0 left-0 z-50 w-72 transform transition-transform duration-300 ease-in-out',
          'app-bg border-r border-gray-800/80 flex flex-col p-6',
          'lg:static lg:z-auto lg:translate-x-0',
          open ? 'translate-x-0' : '-translate-x-full'
        )}
      >
        {/* Brand */}
        <div className="flex items-center justify-between mb-10">
          <Link href="/" className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center shadow-lg shadow-blue-500/20">
              <span className="text-white font-bold text-lg">✓</span>
            </div>
            <h1 className="text-xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
              TaskFlow Pro
            </h1>
          </Link>
          <button
            onClick={onClose}
            className="p-2 text-gray-400 hover:text-white hover:bg-gray-800/60 rounded-lg lg:hidden"
            aria-label="Close menu"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Nav */}
        <nav className="flex-1 space-y-1.5">
          {links.map(({ href, label, icon: Icon }) => {
            const active = pathname === href;
            return (
              <Link key={href} href={href} onClick={onClose}>
                <span
                  className={cn(
                    'flex items-center p-3 rounded-xl transition-all duration-200 text-sm font-medium group',
                    active
                      ? 'bg-gradient-to-r from-blue-500/15 to-purple-500/15 text-white border border-blue-500/30 shadow-sm'
                      : 'text-gray-400 hover:text-white hover:bg-gray-800/50 border border-transparent'
                  )}
                >
                  <Icon
                    className={cn(
                      'w-5 h-5 mr-3 transition-colors',
                      active ? 'text-blue-400' : 'text-gray-500 group-hover:text-gray-300'
                    )}
                  />
                  {label}
                  {active && (
                    <span className="ml-auto w-1.5 h-1.5 rounded-full bg-blue-400" />
                  )}
                </span>
              </Link>
            );
          })}
        </nav>

        {/* User card */}
        <div className="mt-auto">
          <div className="surface-card rounded-2xl p-4">
            <div className="flex items-center">
              <Avatar className="w-10 h-10 border border-blue-500/30">
                <AvatarFallback className="bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold">
                  {initial}
                </AvatarFallback>
              </Avatar>
              <div className="ml-3 min-w-0">
                <p className="font-semibold text-gray-100 text-sm truncate">
                  {displayName}
                </p>
                <p className="text-xs text-gray-500 truncate">{user?.email || 'Not signed in'}</p>
              </div>
              <Button
                variant="ghost"
                size="sm"
                className="ml-auto text-gray-400 hover:text-red-400 hover:bg-red-500/10 shrink-0"
                onClick={handleSignOut}
                title="Sign out"
              >
                <LogOut className="w-4 h-4" />
              </Button>
            </div>
          </div>
        </div>
      </aside>
    </>
  );
}

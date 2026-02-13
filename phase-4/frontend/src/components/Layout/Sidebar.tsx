'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Button } from '@/src/styling/ui/button';
import {
  LogOut,
  LayoutDashboard,
  Settings,
  Sun,
  Moon,
} from 'lucide-react';
import { Avatar, AvatarFallback } from '@/src/styling/ui/avatar';
import { cn } from '@/src/lib/utils';

const links = [
  { href: '/tasks', label: 'Tasks', icon: LayoutDashboard },
];

export function Sidebar() {
  const pathname = usePathname();
  // Dummy user data - replace with actual user data from context
  const user = { name: 'Zainab Khan', email: 'zainab.khan@example.com' };

  // Dummy theme toggle - replace with actual theme logic
  const isDarkMode = true;
  const toggleTheme = () => console.log('Toggling theme');

  return (
    <aside className="w-72 bg-gray-50 dark:bg-gray-900/80 p-6 flex flex-col border-r border-gray-200 dark:border-gray-800">
      <div className="flex items-center space-x-3 mb-10">
        <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
          <span className="text-white font-bold text-lg">✓</span>
        </div>
        <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
          TaskFlow Pro
        </h1>
      </div>

      <nav className="flex-1 space-y-2">
        {links.map(({ href, label, icon: Icon }) => (
          <Link key={href} href={href}>
            <p
              className={cn(
                'flex items-center p-3 rounded-lg transition-colors text-base font-medium',
                pathname === href
                  ? 'bg-blue-500/10 text-blue-600 dark:text-blue-400'
                  : 'text-gray-500 dark:text-gray-400 hover:bg-gray-200/50 dark:hover:bg-gray-700/50'
              )}
            >
              <Icon className="w-6 h-6 mr-4" />
              {label}
            </p>
          </Link>
        ))}
      </nav>

      <div className="mt-auto">
        <div className="border-t border-gray-200 dark:border-gray-800 my-4"></div>

        <div className="flex items-center">
          <Avatar className="w-12 h-12">
            <AvatarFallback>{user.name.charAt(0)}</AvatarFallback>
          </Avatar>
          <div className="ml-4">
            <p className="font-semibold text-gray-800 dark:text-gray-200">{user.name}</p>
            <p className="text-sm text-gray-500 dark:text-gray-400">{user.email}</p>
          </div>
          <Button variant="ghost" size="sm" className="ml-auto">
            <LogOut className="w-5 h-5" />
          </Button>
        </div>
      </div>
    </aside>
  );
}
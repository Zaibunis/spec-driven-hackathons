'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useAuth } from '../../../lib/hooks/useAuth';
import { Task, CreateTaskData, UpdateTaskData } from '../../../lib/types';
import { TaskList } from '../../../components/tasks/task-list';
import { getApiBaseUrl } from '../../../lib/api-url';

const TasksPage = () => {
  const { user} = useAuth();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Reload tasks when the user changes OR when a chat-driven task change
  // is broadcast (dispatched by the chat UI after a successful MCP operation).
  useEffect(() => {
    if (user?.id) {
      loadTasks();
    }
  }, [user]);

  useEffect(() => {
    const onTasksChanged = () => {
      if (user?.id) loadTasks();
    };
    window.addEventListener('todo:tasks-changed', onTasksChanged);
    return () => window.removeEventListener('todo:tasks-changed', onTasksChanged);
  }, [user]);

  const loadTasks = async () => {
    try {
      setLoading(true);
      setError(null);

      const token = localStorage.getItem('access_token');
      if (!token) {
        setError('Not authenticated');
        return;
      }

      const apiUrl = getApiBaseUrl();
      const res = await fetch(`${apiUrl}/v1/tasks`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (res.status === 401) {
        setError('Session expired. Please sign in again.');
        return;
      }
      if (!res.ok) {
        setError(`Failed to load tasks (HTTP ${res.status})`);
        return;
      }

      const data = await res.json();
      // API returns either a bare array or { tasks: [...] }
      const rawTasks: any[] = Array.isArray(data) ? data : data.tasks || [];

      const mapped: Task[] = rawTasks.map((t) => ({
        id: String(t.id),
        title: t.title,
        description: t.description ?? t.details ?? undefined,
        completed: Boolean(t.is_completed ?? t.completed),
        userId: String(t.user_id ?? user!.id),
        createdAt: t.created_at ?? new Date().toISOString(),
        updatedAt: t.updated_at ?? t.created_at ?? new Date().toISOString(),
      }));

      setTasks(mapped);
    } catch (err) {
      setError('Failed to load tasks');
      console.error('Error loading tasks:', err);
    } finally {
      setLoading(false);
    }
  };

  const addTask = async (taskData: CreateTaskData) => {
    try {
      const token = localStorage.getItem('access_token');
      const apiUrl = getApiBaseUrl();
      const res = await fetch(`${apiUrl}/v1/tasks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ title: taskData.title, description: taskData.description }),
      });

      if (!res.ok) {
        setError(`Failed to add task (HTTP ${res.status})`);
        return;
      }

      await loadTasks();
    } catch (err) {
      setError('Failed to add task');
      console.error('Error adding task:', err);
    }
  };

  const updateTask = async (id: string, taskData: UpdateTaskData) => {
    try {
      const token = localStorage.getItem('access_token');
      const apiUrl = getApiBaseUrl();
      const res = await fetch(`${apiUrl}/v1/tasks/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          title: taskData.title,
          description: taskData.description,
        }),
      });

      if (!res.ok) {
        setError(`Failed to update task (HTTP ${res.status})`);
        return;
      }

      await loadTasks();
    } catch (err) {
      setError('Failed to update task');
      console.error('Error updating task:', err);
    }
  };

  const deleteTask = async (id: string) => {
    try {
      const token = localStorage.getItem('access_token');
      const apiUrl = getApiBaseUrl();
      const res = await fetch(`${apiUrl}/v1/tasks/${id}`, {
        method: 'DELETE',
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!res.ok) {
        setError(`Failed to delete task (HTTP ${res.status})`);
        return;
      }

      setTasks(prev => prev.filter(task => task.id !== id));
    } catch (err) {
      setError('Failed to delete task');
      console.error('Error deleting task:', err);
    }
  };

  const toggleTask = async (id: string, completed: boolean) => {
    try {
      const token = localStorage.getItem('access_token');
      const apiUrl = getApiBaseUrl();
      const res = await fetch(`${apiUrl}/v1/tasks/${id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ is_completed: completed }),
      });

      if (!res.ok) {
        setError(`Failed to toggle task (HTTP ${res.status})`);
        return;
      }

      setTasks(prev => prev.map(task =>
        task.id === id
          ? { ...task, completed, updatedAt: new Date().toISOString() }
          : task
      ));
    } catch (err) {
      setError('Failed to toggle task');
      console.error('Error toggling task:', err);
    }
  };


  if (!user) {
    return (
      <div className="flex items-center justify-center min-h-screen app-bg">
        <div className="text-center">
          <div className="w-16 h-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center mx-auto mb-4 shadow-lg shadow-blue-500/20">
            <span className="text-white font-bold text-2xl">✓</span>
          </div>
          <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent mb-2">
            TaskFlow Pro
          </h1>
          <p className="text-lg text-gray-300">Please sign in to view your tasks</p>
        </div>
      </div>
    );
  }

  const totalTasks = tasks.length;
  const completedTasks = tasks.filter(t => t.completed).length;
  const activeTasks = totalTasks - completedTasks;

  return (
    <div className="min-h-screen app-bg">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
            My Tasks
          </h1>
          <p className="text-gray-400 mt-1">
            Organize your workflow and boost productivity.
          </p>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-3 sm:gap-4 mb-8">
          <div className="surface-card rounded-2xl p-4 sm:p-5">
            <p className="text-xs sm:text-sm text-gray-400 mb-1">Total</p>
            <p className="text-2xl sm:text-3xl font-bold text-white">{totalTasks}</p>
          </div>
          <div className="surface-card rounded-2xl p-4 sm:p-5">
            <p className="text-xs sm:text-sm text-gray-400 mb-1">Active</p>
            <p className="text-2xl sm:text-3xl font-bold text-blue-400">{activeTasks}</p>
          </div>
          <div className="surface-card rounded-2xl p-4 sm:p-5">
            <p className="text-xs sm:text-sm text-gray-400 mb-1">Completed</p>
            <p className="text-2xl sm:text-3xl font-bold text-green-400">{completedTasks}</p>
          </div>
        </div>

        <TaskList
          tasks={tasks}
          loading={loading}
          error={error ?? undefined}
          onAddTask={addTask}
          onUpdateTask={updateTask}
          onDeleteTask={deleteTask}
          onToggleTask={toggleTask}
        />
      </div>
    </div>
  );
};

export default TasksPage;

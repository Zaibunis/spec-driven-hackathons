// T003: apiClient with Authorization header

import axios from 'axios';
import { getApiBaseUrl } from './api-url';

// Single source of truth: NEXT_PUBLIC_API_URL (inlined at build time) or the
// deployed backend fallback from api-url.ts. Never derive the API base from
// window.location.origin - the backend is a separate deployment, and
// self-origin requests produce 404s on Vercel.
const baseURL = getApiBaseUrl();

const apiClient = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
  // Enable credentials for cross-origin requests if needed
  withCredentials: false,
});

// Add a request interceptor to include the auth token
apiClient.interceptors.request.use(
  (config) => {
    // Check if localStorage is available (client-side)
    if (typeof window !== 'undefined') {
      const token = localStorage.getItem('access_token');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default apiClient;

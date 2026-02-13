// T003: apiClient with Authorization header

import axios from 'axios';

// Determine the base URL based on the environment
// Use a fallback for when environment variable is not set
let baseURL = process.env.NEXT_PUBLIC_API_URL || 'https://faria45678-chat-agent.hf.space';

// In production environments, ensure we're using the correct API URL
if (typeof window !== 'undefined') {
  // Client-side: determine API URL based on current origin
  if (process.env.NODE_ENV === 'production') {
    // If NEXT_PUBLIC_API_URL is not set, try to construct from current domain
    if (!process.env.NEXT_PUBLIC_API_URL || process.env.NEXT_PUBLIC_API_URL === 'https://faria45678-chat-agent.hf.space') {
      const currentOrigin = window.location.origin;
      // Assuming the API is hosted at the same domain under /api/v1
      baseURL = `${currentOrigin}/api/v1`;
    }
  }
}

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
  (error) => {
    return Promise.reject(error);
  }
);

// Add a response interceptor to handle common errors
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized access - maybe redirect to login
      if (typeof window !== 'undefined') {
        localStorage.removeItem('access_token');
        window.location.href = '/signin';
      }
    }
    return Promise.reject(error);
  }
);

export default apiClient;
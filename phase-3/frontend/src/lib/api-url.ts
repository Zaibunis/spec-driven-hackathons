// Shared API base URL with paste-safety.
// Handles two classic env-var paste mistakes:
//  1. Trailing whitespace (e.g. "https://api.example.com/ ") - .trim() removes it
//  2. Trailing slash (e.g. "https://api.example.com/") - regex strips it
// Without this, requests become ".../ /v1/tasks" (%20 + //) and the backend 404s.
//
// NOTE: NEXT_PUBLIC_ vars are inlined at BUILD time. If the env var is not set
// when Vercel builds, we fall back to the deployed backend URL - never to this
// frontend's own origin, because the API does not live there.
const FALLBACK_API_URL = 'https://hackathon-phase-4-eight.vercel.app';

export function getApiBaseUrl(): string {
  const raw = (process.env.NEXT_PUBLIC_API_URL || FALLBACK_API_URL).trim();
  return raw.replace(/\/+$/, '');
}

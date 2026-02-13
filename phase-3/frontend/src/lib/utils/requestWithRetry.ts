import { AxiosInstance, AxiosResponse } from 'axios';

/**
 * Retry helper for Axios requests
 * @param requestFn - function returning Axios request promise
 * @param retries - number of retry attempts
 * @param delayMs - delay between retries in ms
 */
export async function requestWithRetry<T>(
  requestFn: () => Promise<AxiosResponse<T>>,
  retries = 3,
  delayMs = 500
): Promise<AxiosResponse<T>> {
  let attempt = 0;

  while (attempt < retries) {
    try {
      return await requestFn();
    } catch (err) {
      attempt++;
      if (attempt >= retries) throw err; // no retries left, throw error
      await new Promise(res => setTimeout(res, delayMs)); // wait before retry
    }
  }

  // should never reach here
  throw new Error('requestWithRetry failed unexpectedly');
}

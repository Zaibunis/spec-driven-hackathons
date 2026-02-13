import apiClient from '../lib/api-client';
import { AxiosResponse } from 'axios';
import { requestWithRetry } from '../lib/utils/requestWithRetry';

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  message?: string;
  error?: {
    message: string;
    code: string;
    details?: Array<{ field: string; message: string }>;
  };
}

export abstract class BaseService {
  protected async get<T>(url: string): Promise<ApiResponse<T>> {
    try {
      const response = await requestWithRetry(() => apiClient.get<T>(url));
      return { success: true, data: response.data };
    } catch (error: any) {
      return this.handleError(error);
    }
  }

  protected async post<T>(url: string, data?: any): Promise<ApiResponse<T>> {
    try {
      const response = await requestWithRetry(() => apiClient.post<T>(url, data));
      return { success: true, data: response.data };
    } catch (error: any) {
      return this.handleError(error);
    }
  }

  protected async put<T>(url: string, data?: any): Promise<ApiResponse<T>> {
    try {
      const response = await requestWithRetry(() => apiClient.put<T>(url, data));
      return { success: true, data: response.data };
    } catch (error: any) {
      return this.handleError(error);
    }
  }

  protected async patch<T>(url: string, data?: any): Promise<ApiResponse<T>> {
    try {
      const response = await requestWithRetry(() => apiClient.patch<T>(url, data));
      return { success: true, data: response.data };
    } catch (error: any) {
      return this.handleError(error);
    }
  }

  protected async delete<T>(url: string): Promise<ApiResponse<T>> {
    try {
      const response = await requestWithRetry(() => apiClient.delete<T>(url));
      return { success: true, data: response.data };
    } catch (error: any) {
      return this.handleError(error);
    }
  }

  private handleError(error: any): ApiResponse<never> {
    console.error('API Error:', error);

    if (error.response) {
      const { status, data } = error.response;
      return {
        success: false,
        error: {
          message: data?.error?.message || data?.message || `Request failed with status ${status}`,
          code: data?.error?.code || `HTTP_${status}`,
          details: data?.error?.details || [],
        },
      };
    } else if (error.request) {
      return {
        success: false,
        error: {
          message: 'Network error: Unable to reach the server',
          code: 'NETWORK_ERROR',
        },
      };
    } else {
      return {
        success: false,
        error: {
          message: error.message || 'An unexpected error occurred',
          code: 'UNKNOWN_ERROR',
        },
      };
    }
  }
}

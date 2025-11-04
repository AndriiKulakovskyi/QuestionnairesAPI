// API client for communicating with the FastAPI backend

import {
  QuestionnaireListItem,
  QuestionnaireDetail,
  ScoreResponse,
  ValidationResponse,
  AnswersRequest,
} from '../types/questionnaire';

// In production (server-side), use localhost:8000
// In browser (client-side), requests go through Next.js rewrites
const API_BASE_URL = typeof window === 'undefined' 
  ? 'http://localhost:8000'  // Server-side: direct connection
  : '';  // Client-side: use relative URLs (handled by Next.js rewrites)

class APIError extends Error {
  constructor(
    message: string,
    public status: number,
    public data?: any
  ) {
    super(message);
    this.name = 'APIError';
  }
}

async function fetchAPI<T>(endpoint: string, options?: RequestInit, retries = 3): Promise<T> {
  const url = `${API_BASE_URL}${endpoint}`;
  
  // Debug logging
  if (typeof window !== 'undefined') {
    console.log(`[API Client] Fetching from: ${url}`);
  } else {
    console.log(`[API Client SSR] Fetching from: ${url}`);
  }
  
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const response = await fetch(url, {
        ...options,
        headers: {
          'Content-Type': 'application/json',
          ...options?.headers,
        },
        // Add timeout and cache settings
        cache: 'no-store',
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        console.error(`[API Client] Error response (attempt ${attempt}/${retries}):`, response.status, errorData);
        
        // Don't retry on 4xx errors (client errors)
        if (response.status >= 400 && response.status < 500) {
          throw new APIError(
            errorData.detail || `HTTP error ${response.status}`,
            response.status,
            errorData
          );
        }
        
        // Retry on 5xx errors
        if (attempt < retries) {
          await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
          continue;
        }
        
        throw new APIError(
          errorData.detail || `HTTP error ${response.status}`,
          response.status,
          errorData
        );
      }

      return await response.json();
    } catch (error) {
      if (error instanceof APIError) {
        throw error;
      }
      
      console.error(`[API Client] Fetch failed (attempt ${attempt}/${retries}):`, error);
      
      // Retry on network errors
      if (attempt < retries) {
        await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
        continue;
      }
      
      throw new APIError(
        `Failed to fetch from ${endpoint}: ${error instanceof Error ? error.message : 'Unknown error'}`,
        0
      );
    }
  }
  
  // This should never be reached, but TypeScript needs it
  throw new APIError(`Failed to fetch from ${endpoint} after ${retries} attempts`, 0);
}

/**
 * Fetch all available questionnaires by category
 */
export async function getQuestionnaireList(category: 'auto' | 'hetero'): Promise<QuestionnaireListItem[]> {
  return fetchAPI<QuestionnaireListItem[]>(`/api/${category}/questionnaires`);
}

/**
 * Fetch complete questionnaire structure by category and ID
 */
export async function getQuestionnaire(category: 'auto' | 'hetero', id: string): Promise<QuestionnaireDetail> {
  return fetchAPI<QuestionnaireDetail>(`/api/${category}/questionnaires/${encodeURIComponent(id)}`);
}

/**
 * Validate answers without calculating scores
 */
export async function validateAnswers(
  category: 'auto' | 'hetero',
  id: string,
  answers: Record<string, number | string>
): Promise<ValidationResponse> {
  return fetchAPI<ValidationResponse>(
    `/api/${category}/questionnaires/${encodeURIComponent(id)}/validate`,
    {
      method: 'POST',
      body: JSON.stringify({ answers }),
    }
  );
}

/**
 * Submit answers and calculate scores
 */
export async function submitAnswers(
  category: 'auto' | 'hetero',
  id: string,
  answers: Record<string, number | string>
): Promise<ScoreResponse> {
  return fetchAPI<ScoreResponse>(
    `/api/${category}/questionnaires/${encodeURIComponent(id)}/submit`,
    {
      method: 'POST',
      body: JSON.stringify({ answers }),
    }
  );
}

export { APIError };


// TypeScript types matching the backend API schemas

export interface QuestionnaireListItem {
  id: string;
  name: string;
  abbreviation: string;
  language: string;
  category: string;
  description?: string;
}

export interface QuestionnaireMetadata {
  id: string;
  name: string;
  abbreviation: string;
  language: string;
  version: string;
  reference_period?: string;
  description?: string;
  total_questions?: number;
  scoring_range?: number[];
  sources?: string[];
  [key: string]: any; // Allow additional fields
}

export interface QuestionOption {
  code: number | string;
  label: string;
  score?: number | null;
  [key: string]: any;
}

export interface Question {
  id: string;
  section_id?: string;
  text: string;
  type: string;
  required: boolean;
  options: QuestionOption[];
  constraints: {
    value_type?: string;
    min_value?: number;
    max_value?: number;
    allowed_values?: (number | string)[];
    [key: string]: any;
  };
  help?: string;
  [key: string]: any;
}

export interface Section {
  id: string;
  label: string;
  description: string;
  question_ids: string[];
  [key: string]: any;
}

export interface QuestionnaireDetail {
  metadata: QuestionnaireMetadata;
  sections: Section[];
  questions: Question[];
}

export interface AnswersRequest {
  answers: Record<string, number | string>;
}

export interface ValidationResponse {
  valid: boolean;
  errors: string[];
  warnings: string[];
}

export interface ScoreResponse {
  questionnaire_id: string;
  score_data: {
    total_score?: number;
    [key: string]: any; // Flexible structure for different questionnaires
  };
  validation?: ValidationResponse;
}

export interface ErrorResponse {
  detail: string;
  questionnaire_id?: string;
}


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
  gender_specific?: string;  // "F" or "M" for gender-specific questions
  display_if?: any;  // JSONLogic condition for visibility
  required_if?: any;  // JSONLogic condition for requirement
  [key: string]: any;
}

export interface Section {
  id: string;
  label: string;
  description: string;
  question_ids: string[];
  [key: string]: any;
}

export interface RespondentField {
  id: string;
  label: string;
  label_en?: string;
  type: string;
  required: boolean;
  purpose?: string;
  options?: {
    code: string;
    label: string;
    label_en?: string;
    triggers?: string;
  }[];
  validation?: {
    required_message?: string;
  };
}

export interface RespondentSchema {
  schema_version: string;
  description: string;
  fields: RespondentField[];
  notes?: string[];
}

export interface BranchingLogic {
  schema_version: string;
  type: string;
  rules: any[];
  context_variables?: any;
  fallback_behavior?: any;
  scoring_logic?: any;
}

export interface QuestionnaireDetail {
  metadata: QuestionnaireMetadata;
  sections: Section[];
  questions: Question[];
  respondent?: RespondentSchema;  // Optional demographics requirements
  logic?: BranchingLogic;  // Optional branching logic
}

export interface AnswersRequest {
  answers: Record<string, number | string>;
  demographics?: Record<string, string>;  // Optional demographics for branching logic
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


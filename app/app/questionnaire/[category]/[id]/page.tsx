'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { getQuestionnaire, submitAnswers } from '../../../lib/api';
import { QuestionnaireDetail, ScoreResponse, Question as QuestionType } from '../../../types/questionnaire';
import Question from '../../../components/Question';
import Results from '../../../components/Results';
import { shouldDisplayQuestion, isQuestionRequired } from '../../../lib/jsonlogic';

export default function QuestionnairePage() {
  const params = useParams();
  const router = useRouter();
  const category = params.category as 'auto' | 'hetero';
  const questionnaireId = params.id as string;

  const [questionnaire, setQuestionnaire] = useState<QuestionnaireDetail | null>(null);
  const [answers, setAnswers] = useState<Record<string, number | string>>({});
  const [demographics, setDemographics] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<ScoreResponse | null>(null);
  const [validationErrors, setValidationErrors] = useState<string[]>([]);

  // Validate category
  useEffect(() => {
    if (category && category !== 'auto' && category !== 'hetero') {
      setError('Invalid category. Must be "auto" or "hetero".');
      setLoading(false);
    }
  }, [category]);

  useEffect(() => {
    if (!questionnaireId || !category || (category !== 'auto' && category !== 'hetero')) return;

    async function loadQuestionnaire() {
      try {
        setLoading(true);
        setError(null);
        const data = await getQuestionnaire(category, questionnaireId);
        setQuestionnaire(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load questionnaire');
      } finally {
        setLoading(false);
      }
    }

    loadQuestionnaire();
  }, [questionnaireId, category]);

  const handleDemographicChange = (fieldId: string, value: string) => {
    setDemographics((prev) => ({
      ...prev,
      [fieldId]: value,
    }));
    // Clear validation errors when demographic changes
    setValidationErrors([]);
  };

  const handleAnswerChange = (questionId: string, value: number | string) => {
    setAnswers((prev) => ({
      ...prev,
      [questionId]: value,
    }));
    // Clear validation errors when user changes an answer
    setValidationErrors([]);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!questionnaire) return;

    // Check if demographics are required
    if (questionnaire.respondent && questionnaire.respondent.fields.length > 0) {
      const requiredDemoFields = questionnaire.respondent.fields.filter(f => f.required);
      const missingDemo = requiredDemoFields.filter(f => !demographics[f.id]);
      
      if (missingDemo.length > 0) {
        setValidationErrors([
          `Informations requises: ${missingDemo.map(f => f.label).join(', ')}`
        ]);
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }
    }

    // Filter visible questions based on demographics (if applicable)
    const visibleQuestions = questionnaire.questions.filter((q) =>
      shouldDisplayQuestion(q, demographics)
    );

    // Check if all required visible questions are answered
    const requiredQuestions = visibleQuestions.filter((q) =>
      isQuestionRequired(q, demographics)
    );
    const missingAnswers = requiredQuestions.filter((q) => !(q.id in answers));
    
    if (missingAnswers.length > 0) {
      setValidationErrors([
        `Veuillez répondre à toutes les questions requises. Manquantes: ${missingAnswers.map(q => q.id).join(', ')}`
      ]);
      // Scroll to top to show error
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }

    try {
      setSubmitting(true);
      setValidationErrors([]);
      // Submit with demographics if applicable
      const response = await submitAnswers(
        category,
        questionnaireId,
        answers,
        Object.keys(demographics).length > 0 ? demographics : undefined
      );
      setResult(response);
      // Scroll to top to show results
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (err) {
      setValidationErrors([
        err instanceof Error ? err.message : 'Failed to submit answers'
      ]);
      // Scroll to top to show error
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } finally {
      setSubmitting(false);
    }
  };

  const handleRestart = () => {
    setAnswers({});
    setResult(null);
    setValidationErrors([]);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const backLink = category === 'auto' ? '/auto-questionnaires' : '/hetero-questionnaires';
  const categoryLabel = category === 'auto' ? 'Auto Questionnaires' : 'Hetero Questionnaires';

  // Loading state
  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 flex items-center justify-center">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-gray-400 mb-4"></div>
          <p className="text-gray-400">Loading questionnaire...</p>
        </div>
      </div>
    );
  }

  // Error state
  if (error) {
    return (
      <div className="min-h-screen bg-gray-900">
        <div className="container mx-auto px-4 py-8 max-w-4xl">
          <div className="bg-red-900/20 border border-red-700 text-red-300 px-6 py-4 rounded-lg">
            <div className="flex items-center mb-2">
              <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
              </svg>
              <strong className="font-semibold">Error</strong>
            </div>
            <p>{error}</p>
          </div>
          <Link href={backLink} className="inline-block mt-6 px-6 py-3 bg-gray-700 hover:bg-gray-600 text-gray-100 font-medium rounded-lg transition-colors">
            Back to {categoryLabel}
          </Link>
        </div>
      </div>
    );
  }

  // No questionnaire data
  if (!questionnaire) {
    return null;
  }

  // Show results
  if (result) {
    return (
      <div className="min-h-screen bg-gray-900">
        <div className="container mx-auto px-4 py-8">
          <Results result={result} onRestart={handleRestart} />
        </div>
      </div>
    );
  }

  // Filter visible questions based on demographics
  const visibleQuestions = questionnaire.questions.filter((q) =>
    shouldDisplayQuestion(q, demographics)
  );

  // Show questionnaire form
  const answeredCount = Object.keys(answers).length;
  const visibleRequiredQuestions = visibleQuestions.filter((q) =>
    isQuestionRequired(q, demographics)
  );
  const totalRequired = visibleRequiredQuestions.length;
  const progress = totalRequired > 0 ? (answeredCount / totalRequired) * 100 : 0;

  return (
    <div className="min-h-screen bg-gray-900">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        {/* Header */}
        <div className="mb-8">
          <Link href={backLink} className="text-blue-400 hover:text-blue-300 text-sm mb-4 inline-flex items-center">
            <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
            </svg>
            Back to {categoryLabel}
          </Link>
          
          <h1 className="text-3xl font-bold text-gray-100 mt-4 mb-2">
            {questionnaire.metadata.name}
          </h1>
          
          <div className="flex flex-wrap gap-3 text-sm text-gray-400">
            <span className="px-3 py-1 bg-gray-800 rounded-full">
              {questionnaire.metadata.abbreviation}
            </span>
            <span className="px-3 py-1 bg-gray-800 rounded-full">
              {questionnaire.metadata.language}
            </span>
            <span className={`px-3 py-1 rounded-full ${
              category === 'auto' ? 'bg-blue-900/30 text-blue-300' : 'bg-green-900/30 text-green-300'
            }`}>
              {categoryLabel}
            </span>
            {questionnaire.metadata.reference_period && (
              <span className="px-3 py-1 bg-gray-800 rounded-full">
                Period: {questionnaire.metadata.reference_period}
              </span>
            )}
          </div>

          {questionnaire.metadata.description && (
            <p className="mt-4 text-gray-400">
              {questionnaire.metadata.description}
            </p>
          )}
        </div>

        {/* Progress Bar */}
        <div className="mb-8">
          <div className="flex justify-between text-sm text-gray-400 mb-2">
            <span>Progress</span>
            <span>{answeredCount} / {totalRequired} required questions</span>
          </div>
          <div className="w-full bg-gray-800 rounded-full h-2">
            <div
              className="bg-blue-600 h-2 rounded-full transition-all duration-300"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>

        {/* Validation Errors */}
        {validationErrors.length > 0 && (
          <div className="mb-6 bg-red-900/20 border border-red-700 text-red-300 px-6 py-4 rounded-lg">
            <div className="flex items-center mb-2">
              <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
              </svg>
              <strong className="font-semibold">Validation Errors</strong>
            </div>
            <ul className="list-disc list-inside space-y-1">
              {validationErrors.map((error, index) => (
                <li key={index}>{error}</li>
              ))}
            </ul>
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleSubmit}>
          {/* Demographics Toggle (if required) */}
          {questionnaire.respondent && questionnaire.respondent.fields && questionnaire.respondent.fields.length > 0 && (
            <div className="mb-8 p-6 bg-gray-800 border-2 border-blue-500 rounded-lg">
              {questionnaire.respondent.fields.map((field) => (
                <div key={field.id}>
                  <label className="block mb-4">
                    <div className="text-lg font-semibold text-gray-100 mb-2">
                      {field.label}
                      {field.required && <span className="text-red-400 ml-1">*</span>}
                    </div>
                    {field.purpose && (
                      <p className="text-sm text-gray-400 mb-4">{field.purpose}</p>
                    )}
                  </label>

                  {field.type === 'toggle' && field.options && field.options.length > 0 && (
                    <div className="flex gap-3">
                      {field.options.map((option) => (
                        <button
                          key={option.code}
                          type="button"
                          onClick={() => handleDemographicChange(field.id, option.code)}
                          className={`flex-1 px-6 py-4 rounded-lg border-2 font-medium transition-all ${
                            demographics[field.id] === option.code
                              ? 'border-blue-500 bg-blue-600 text-white shadow-lg'
                              : 'border-gray-600 bg-gray-750 text-gray-300 hover:border-gray-500 hover:bg-gray-700'
                          }`}
                        >
                          <div className="text-lg font-bold mb-1">{option.label}</div>
                          {option.triggers && (
                            <div className="text-xs opacity-80">{option.triggers}</div>
                          )}
                        </button>
                      ))}
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}

          {/* Sections and Questions */}
          {questionnaire.sections.map((section) => {
            // Filter section questions by visibility
            const sectionQuestions = visibleQuestions.filter(
              (q) => q.section_id === section.id
            );

            // Skip empty sections
            if (sectionQuestions.length === 0) {
              return null;
            }

            return (
              <div key={section.id} className="mb-10">
                <div className="mb-6">
                  <h2 className="text-2xl font-bold text-gray-100 mb-2">
                    {section.label}
                  </h2>
                  {section.description && (
                    <p className="text-gray-400">{section.description}</p>
                  )}
                </div>

                {sectionQuestions.map((question) => (
                  <Question
                    key={question.id}
                    question={question}
                    value={answers[question.id]}
                    onChange={handleAnswerChange}
                  />
                ))}
              </div>
            );
          })}

          {/* Submit Button */}
          <div className="sticky bottom-0 bg-gray-900 py-6 border-t border-gray-800">
            <button
              type="submit"
              disabled={submitting || answeredCount < totalRequired}
              className={`w-full px-6 py-4 font-semibold rounded-lg transition-all ${
                submitting || answeredCount < totalRequired
                  ? 'bg-gray-700 text-gray-500 cursor-not-allowed'
                  : 'bg-blue-600 hover:bg-blue-700 text-white shadow-lg hover:shadow-xl'
              }`}
            >
              {submitting ? (
                <span className="flex items-center justify-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Submitting...
                </span>
              ) : answeredCount < totalRequired ? (
                `Answer ${totalRequired - answeredCount} more required question${totalRequired - answeredCount !== 1 ? 's' : ''} to submit`
              ) : (
                'Submit Answers'
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}


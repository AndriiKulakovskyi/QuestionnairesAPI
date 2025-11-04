'use client';

import Link from 'next/link';
import { useState, useEffect } from 'react';
import { getQuestionnaireList } from '../lib/api';
import QuestionnaireCard from '../components/QuestionnaireCard';
import type { QuestionnaireListItem } from '../types/questionnaire';

export default function HeteroQuestionnairesPage() {
  const [questionnaires, setQuestionnaires] = useState<QuestionnaireListItem[]>([]);
  const [error, setError] = useState<string>('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const data = await getQuestionnaireList('hetero');
        setQuestionnaires(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load questionnaires');
      } finally {
        setLoading(false);
      }
    }
    
    fetchData();
  }, []);

  return (
    <div className="min-h-screen bg-gray-900">
      <div className="container mx-auto px-4 py-8 max-w-7xl">
        {/* Header */}
        <div className="mb-8">
          <Link href="/" className="text-blue-400 hover:text-blue-300 text-sm mb-4 inline-flex items-center">
            <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
            </svg>
            Back to home
          </Link>

          <div className="flex items-center mt-4 mb-3">
            <svg
              className="w-10 h-10 text-green-400 mr-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
              />
            </svg>
            <h1 className="text-4xl font-bold text-gray-100">
              Hetero Questionnaires
            </h1>
          </div>
          
          <p className="text-lg text-gray-400">
            Clinician-rated questionnaires for healthcare professionals to assess patient conditions.
          </p>
        </div>

        {/* Error State */}
        {error && (
          <div className="bg-red-900/20 border border-red-700 text-red-300 px-6 py-4 rounded-lg mb-6">
            <div className="flex items-center">
              <svg 
                className="w-5 h-5 mr-2" 
                fill="currentColor" 
                viewBox="0 0 20 20"
              >
                <path 
                  fillRule="evenodd" 
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" 
                  clipRule="evenodd" 
                />
              </svg>
              <div>
                <strong className="font-semibold">Error:</strong> {error}
              </div>
            </div>
            <p className="mt-2 text-sm text-gray-400">
              The API backend may be starting up. Please refresh the page in a moment.
            </p>
          </div>
        )}

        {/* Questionnaires Grid */}
        {questionnaires && questionnaires.length > 0 ? (
          <>
            <div className="mb-4 text-sm text-gray-500">
              Found {questionnaires.length} questionnaire{questionnaires.length !== 1 ? 's' : ''}
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {questionnaires.map((questionnaire) => (
                <QuestionnaireCard 
                  key={questionnaire.id} 
                  questionnaire={questionnaire}
                  category="hetero"
                />
              ))}
            </div>
          </>
        ) : loading && !error ? (
          <div className="text-center py-12">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-gray-400"></div>
            <p className="mt-4 text-gray-400">Loading questionnaires...</p>
          </div>
        ) : (
          <div className="text-center py-12 px-4">
            <div className="inline-block p-8 bg-gray-800 border border-gray-700 rounded-lg max-w-md">
              <svg
                className="w-16 h-16 text-gray-600 mx-auto mb-4"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
                />
              </svg>
              <h3 className="text-xl font-semibold text-gray-300 mb-2">
                No Questionnaires Available
              </h3>
              <p className="text-gray-500">
                Hetero questionnaires are currently being implemented.
                <br />
                Check back soon for updates.
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}


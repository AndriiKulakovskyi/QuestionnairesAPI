import { getQuestionnaireList } from './lib/api';
import QuestionnaireCard from './components/QuestionnaireCard';

export default async function Home() {
  let questionnaires;
  let error;

  try {
    questionnaires = await getQuestionnaireList();
  } catch (err) {
    error = err instanceof Error ? err.message : 'Failed to load questionnaires';
  }

  return (
    <div className="min-h-screen bg-gray-900">
      <div className="container mx-auto px-4 py-8 max-w-7xl">
        {/* Header */}
        <div className="mb-10">
          <h1 className="text-4xl font-bold text-gray-100 mb-3">
            Questionnaire Testing Platform
          </h1>
          <p className="text-lg text-gray-400">
            Select a questionnaire below to begin testing. All questionnaires are self-report instruments.
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
              Make sure the backend API is running at http://127.0.0.1:8000
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
                />
              ))}
            </div>
          </>
        ) : !error && (
          <div className="text-center py-12">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-gray-400"></div>
            <p className="mt-4 text-gray-400">Loading questionnaires...</p>
          </div>
        )}
      </div>
    </div>
  );
}

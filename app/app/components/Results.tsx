import Link from 'next/link';
import { ScoreResponse } from '../types/questionnaire';

interface ResultsProps {
  result: ScoreResponse;
  onRestart: () => void;
}

export default function Results({ result, onRestart }: ResultsProps) {
  const { score_data, validation } = result;

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-gray-800 border border-gray-700 rounded-lg shadow-lg p-8">
        {/* Header */}
        <div className="flex items-center mb-6">
          <svg
            className="w-12 h-12 text-green-500 mr-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <div>
            <h2 className="text-3xl font-bold text-gray-100">Results</h2>
            <p className="text-gray-400">Questionnaire completed successfully</p>
          </div>
        </div>

        {/* Score Section */}
        {score_data.total_score !== undefined && (
          <div className="mb-6 p-6 bg-gray-750 rounded-lg border border-gray-600">
            <div className="flex items-baseline justify-between mb-2">
              <h3 className="text-xl font-semibold text-gray-200">Total Score</h3>
              <span className="text-4xl font-bold text-blue-400">
                {score_data.total_score}
              </span>
            </div>
            {score_data.range && (
              <p className="text-sm text-gray-400">
                Range: {score_data.range[0]} - {score_data.range[1]}
              </p>
            )}
          </div>
        )}

        {/* Additional Score Data */}
        <div className="space-y-4 mb-6">
          {Object.entries(score_data).map(([key, value]) => {
            // Skip already displayed fields
            if (key === 'total_score' || key === 'range') return null;

            // Helper function to render a value
            const renderValue = (val: any): string => {
              if (val === null || val === undefined) return 'N/A';
              if (Array.isArray(val)) return val.join(', ');
              if (typeof val === 'object') return JSON.stringify(val);
              return String(val);
            };

            // Handle different value types
            if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
              // Check if this is a nested object structure (like subscales)
              const firstValue = Object.values(value)[0];
              const isNestedObjects = typeof firstValue === 'object' && firstValue !== null && !Array.isArray(firstValue);

              if (isNestedObjects) {
                // Handle 3-level nesting (e.g., subscales)
                return (
                  <div key={key} className="p-4 bg-gray-750 rounded-lg border border-gray-600">
                    <h4 className="text-sm font-semibold text-gray-300 uppercase tracking-wide mb-3">
                      {key.replace(/_/g, ' ')}
                    </h4>
                    <div className="space-y-3">
                      {Object.entries(value).map(([subKey, subValue]) => (
                        <div key={subKey} className="p-3 bg-gray-800 rounded border border-gray-700">
                          <h5 className="text-xs font-semibold text-gray-400 uppercase mb-2">
                            {typeof subValue === 'object' && subValue !== null && 'label' in subValue
                              ? (subValue as any).label
                              : subKey.replace(/_/g, ' ')}
                          </h5>
                          <div className="space-y-1">
                            {typeof subValue === 'object' && subValue !== null && (
                              Object.entries(subValue as Record<string, any>).map(([prop, propValue]) => {
                                // Skip 'name' and 'label' as they're used above
                                if (prop === 'name' || prop === 'label') return null;
                                return (
                                  <div key={prop} className="flex justify-between text-xs">
                                    <span className="text-gray-500">{prop.replace(/_/g, ' ')}:</span>
                                    <span className="text-gray-300">{renderValue(propValue)}</span>
                                  </div>
                                );
                              })
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                );
              }

              // Handle 2-level nesting (regular objects)
              return (
                <div key={key} className="p-4 bg-gray-750 rounded-lg border border-gray-600">
                  <h4 className="text-sm font-semibold text-gray-300 uppercase tracking-wide mb-2">
                    {key.replace(/_/g, ' ')}
                  </h4>
                  <div className="space-y-2">
                    {Object.entries(value).map(([subKey, subValue]) => (
                      <div key={subKey} className="flex justify-between text-sm">
                        <span className="text-gray-400">{subKey.replace(/_/g, ' ')}:</span>
                        <span className="text-gray-200 font-medium">{renderValue(subValue)}</span>
                      </div>
                    ))}
                  </div>
                </div>
              );
            }

            return (
              <div key={key} className="p-4 bg-gray-750 rounded-lg border border-gray-600">
                <h4 className="text-sm font-semibold text-gray-300 uppercase tracking-wide mb-2">
                  {key.replace(/_/g, ' ')}
                </h4>
                <p className="text-gray-200">{renderValue(value)}</p>
              </div>
            );
          })}
        </div>

        {/* Validation Warnings */}
        {validation && validation.warnings && validation.warnings.length > 0 && (
          <div className="mb-6 p-4 bg-yellow-900/20 border border-yellow-700 rounded-lg">
            <h4 className="text-sm font-semibold text-yellow-300 uppercase tracking-wide mb-2">
              Warnings
            </h4>
            <ul className="list-disc list-inside space-y-1">
              {validation.warnings.map((warning, index) => (
                <li key={index} className="text-yellow-200 text-sm">
                  {warning}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Actions */}
        <div className="flex flex-col sm:flex-row gap-4 mt-8">
          <button
            onClick={onRestart}
            className="flex-1 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors"
          >
            Retake Questionnaire
          </button>
          <Link
            href="/"
            className="flex-1 px-6 py-3 bg-gray-700 hover:bg-gray-600 text-gray-100 font-medium rounded-lg transition-colors text-center"
          >
            Back to Home
          </Link>
        </div>
      </div>
    </div>
  );
}


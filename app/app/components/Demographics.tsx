import { useState } from 'react';
import { RespondentSchema } from '../types/questionnaire';

interface DemographicsProps {
  schema: RespondentSchema;
  onComplete: (demographics: Record<string, string>) => void;
  onCancel?: () => void;
}

export default function Demographics({ schema, onComplete, onCancel }: DemographicsProps) {
  const [values, setValues] = useState<Record<string, string>>({});
  const [errors, setErrors] = useState<Record<string, string>>({});

  const handleChange = (fieldId: string, value: string) => {
    setValues((prev) => ({
      ...prev,
      [fieldId]: value,
    }));
    // Clear error for this field
    if (errors[fieldId]) {
      setErrors((prev) => {
        const newErrors = { ...prev };
        delete newErrors[fieldId];
        return newErrors;
      });
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // Validate required fields
    const newErrors: Record<string, string> = {};
    schema.fields.forEach((field) => {
      if (field.required && !values[field.id]) {
        newErrors[field.id] =
          field.validation?.required_message || `${field.label} is required`;
      }
    });

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    // Submit demographics
    onComplete(values);
  };

  return (
    <div className="max-w-2xl mx-auto">
      <div className="bg-gray-800 border border-gray-700 rounded-lg shadow-lg p-8">
        {/* Header */}
        <div className="mb-6">
          <div className="flex items-center mb-4">
            <svg
              className="w-10 h-10 text-blue-400 mr-3"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
              />
            </svg>
            <div>
              <h2 className="text-2xl font-bold text-gray-100">
                Demographic Information
              </h2>
              <p className="text-gray-400 text-sm mt-1">{schema.description}</p>
            </div>
          </div>

          {schema.notes && schema.notes.length > 0 && (
            <div className="bg-blue-900/20 border border-blue-700 rounded-lg p-4 mt-4">
              <div className="flex items-start">
                <svg
                  className="w-5 h-5 text-blue-400 mr-2 mt-0.5 flex-shrink-0"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    fillRule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                    clipRule="evenodd"
                  />
                </svg>
                <div className="text-sm text-blue-200">
                  <p className="font-semibold mb-1">Important Notes:</p>
                  <ul className="list-disc list-inside space-y-1">
                    {schema.notes.map((note, index) => (
                      <li key={index}>{note}</li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit}>
          <div className="space-y-6">
            {schema.fields.map((field) => (
              <div key={field.id}>
                <label className="block mb-2">
                  <div className="text-lg font-semibold text-gray-100 mb-3">
                    {field.label}
                    {field.required && <span className="text-red-400 ml-1">*</span>}
                  </div>
                  {field.purpose && (
                    <p className="text-sm text-gray-400 mb-3">{field.purpose}</p>
                  )}
                </label>

                {field.type === 'single_choice' && field.options && (
                  <div className="space-y-3">
                    {field.options.map((option) => (
                      <label
                        key={option.code}
                        className={`flex items-start p-4 rounded-lg border-2 cursor-pointer transition-all ${
                          values[field.id] === option.code
                            ? 'border-blue-500 bg-blue-900/20'
                            : 'border-gray-700 bg-gray-750 hover:border-gray-600'
                        }`}
                      >
                        <input
                          type="radio"
                          name={field.id}
                          value={option.code}
                          checked={values[field.id] === option.code}
                          onChange={(e) => handleChange(field.id, e.target.value)}
                          className="mt-1 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-600"
                        />
                        <div className="ml-3 flex-1">
                          <span className="text-gray-200 font-medium block">
                            {option.label}
                          </span>
                          {option.triggers && (
                            <span className="text-xs text-gray-500 mt-1 block">
                              {option.triggers}
                            </span>
                          )}
                        </div>
                      </label>
                    ))}
                  </div>
                )}

                {errors[field.id] && (
                  <p className="mt-2 text-sm text-red-400">{errors[field.id]}</p>
                )}
              </div>
            ))}
          </div>

          {/* Action Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 mt-8">
            <button
              type="submit"
              className="flex-1 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors"
            >
              Continue to Questionnaire
            </button>
            {onCancel && (
              <button
                type="button"
                onClick={onCancel}
                className="flex-1 px-6 py-3 bg-gray-700 hover:bg-gray-600 text-gray-100 font-medium rounded-lg transition-colors"
              >
                Cancel
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}


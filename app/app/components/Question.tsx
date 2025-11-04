import { Question as QuestionType } from '../types/questionnaire';

interface QuestionProps {
  question: QuestionType;
  value: number | string | undefined;
  onChange: (questionId: string, value: number | string) => void;
}

export default function Question({ question, value, onChange }: QuestionProps) {
  const handleChange = (newValue: number | string) => {
    onChange(question.id, newValue);
  };

  // Render based on question type
  if (question.type === 'integer') {
    const minValue = question.constraints.min_value ?? 0;
    const maxValue = question.constraints.max_value ?? 100;
    
    return (
      <div className="mb-8 p-6 bg-gray-800 border border-gray-700 rounded-lg">
        <label className="block mb-4">
          <div className="text-lg font-semibold text-gray-100 mb-2">
            {question.text}
            {question.required && <span className="text-red-400 ml-1">*</span>}
          </div>
          {question.help && (
            <p className="text-sm text-gray-400 mb-4">{question.help}</p>
          )}
          {(question as any).description && (
            <p className="text-sm text-gray-400 mb-4">{(question as any).description}</p>
          )}
          <div className="flex items-center gap-4 mt-4">
            <input
              type="number"
              min={minValue}
              max={maxValue}
              value={value ?? ''}
              onChange={(e) => {
                const val = e.target.value === '' ? '' : parseInt(e.target.value, 10);
                if (val === '' || (!isNaN(val as number) && val >= minValue && val <= maxValue)) {
                  handleChange(val as number);
                }
              }}
              className="w-24 px-4 py-2 bg-gray-750 border border-gray-600 rounded-lg text-gray-100 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none"
              placeholder={`${minValue}-${maxValue}`}
            />
            <span className="text-sm text-gray-400">
              Range: {minValue} - {maxValue}
            </span>
          </div>
        </label>
      </div>
    );
  }
  
  if (question.type === 'scale') {
    const scale = (question as any).scale || {};
    const minValue = scale.min_value ?? 0;
    const maxValue = scale.max_value ?? 10;
    const step = scale.step ?? 1;
    
    return (
      <div className="mb-8 p-6 bg-gray-800 border border-gray-700 rounded-lg">
        <label className="block">
          <div className="text-lg font-semibold text-gray-100 mb-2">
            {question.text}
            {question.required && <span className="text-red-400 ml-1">*</span>}
          </div>
          
          <div className="mt-6">
            {/* Min label */}
            <div className="text-sm text-gray-400 mb-2">{scale.min_label}</div>
            
            {/* Slider */}
            <input
              type="range"
              min={minValue}
              max={maxValue}
              step={step}
              value={value ?? minValue}
              onChange={(e) => handleChange(parseFloat(e.target.value))}
              className="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-blue-600"
            />
            
            {/* Max label */}
            <div className="text-sm text-gray-400 mt-2">{scale.max_label}</div>
            
            {/* Current value display */}
            <div className="mt-4 text-center">
              <span className="text-2xl font-bold text-blue-400">{value ?? minValue}</span>
              <span className="text-gray-500 ml-2">/ {maxValue}</span>
            </div>
            
            {scale.center_hint && (
              <div className="mt-2 text-center text-xs text-gray-500">{scale.center_hint}</div>
            )}
          </div>
        </label>
      </div>
    );
  }
  
  if (question.type === 'string') {
    const pattern = question.constraints.pattern;
    
    return (
      <div className="mb-8 p-6 bg-gray-800 border border-gray-700 rounded-lg">
        <label className="block">
          <div className="text-lg font-semibold text-gray-100 mb-2">
            {question.text}
            {question.required && <span className="text-red-400 ml-1">*</span>}
          </div>
          {question.help && (
            <p className="text-sm text-gray-400 mb-4">{question.help}</p>
          )}
          
          <input
            type="text"
            value={value ?? ''}
            onChange={(e) => handleChange(e.target.value)}
            pattern={pattern}
            className="w-full px-4 py-2 bg-gray-750 border border-gray-600 rounded-lg text-gray-100 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none"
            placeholder="Enter value"
          />
        </label>
      </div>
    );
  }
  
  if (question.type === 'time') {
    return (
      <div className="mb-8 p-6 bg-gray-800 border border-gray-700 rounded-lg">
        <label className="block">
          <div className="text-lg font-semibold text-gray-100 mb-2">
            {question.text}
            {question.required && <span className="text-red-400 ml-1">*</span>}
          </div>
          {question.help && (
            <p className="text-sm text-gray-400 mb-4">{question.help}</p>
          )}
          
          <input
            type="time"
            value={value ?? ''}
            onChange={(e) => handleChange(e.target.value)}
            className="px-4 py-2 bg-gray-750 border border-gray-600 rounded-lg text-gray-100 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none"
          />
        </label>
      </div>
    );
  }
  
  if (question.type === 'single_choice') {
    return (
      <div className="mb-8 p-6 bg-gray-800 border border-gray-700 rounded-lg">
        <label className="block mb-4">
          <div className="text-lg font-semibold text-gray-100 mb-2">
            {question.text}
            {question.required && <span className="text-red-400 ml-1">*</span>}
          </div>
          {question.help && (
            <p className="text-sm text-gray-400 mb-4">{question.help}</p>
          )}
        </label>
        
        <div className="space-y-3">
          {question.options.map((option) => (
            <label
              key={option.code}
              className={`flex items-start p-4 rounded-lg border-2 cursor-pointer transition-all ${
                value === option.code
                  ? 'border-blue-500 bg-blue-900/20'
                  : 'border-gray-700 bg-gray-750 hover:border-gray-600'
              }`}
            >
              <input
                type="radio"
                name={question.id}
                value={option.code}
                checked={value === option.code}
                onChange={() => handleChange(option.code)}
                className="mt-1 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-600"
              />
              <span className="ml-3 text-gray-200 flex-1">{option.label}</span>
              {option.score !== null && option.score !== undefined && (
                <span className="ml-2 text-xs text-gray-500 font-mono">
                  [{option.score}]
                </span>
              )}
            </label>
          ))}
        </div>
      </div>
    );
  }

  // Default fallback for unknown question types
  return (
    <div className="mb-6 p-4 bg-gray-800 border border-gray-700 rounded-lg">
      <p className="text-gray-400">
        Unsupported question type: {question.type}
      </p>
    </div>
  );
}


import Link from 'next/link';
import { QuestionnaireListItem } from '../types/questionnaire';

interface QuestionnaireCardProps {
  questionnaire: QuestionnaireListItem;
}

export default function QuestionnaireCard({ questionnaire }: QuestionnaireCardProps) {
  return (
    <Link href={`/questionnaire/${encodeURIComponent(questionnaire.id)}`}>
      <div className="block p-6 bg-gray-800 border border-gray-700 rounded-lg shadow-md hover:bg-gray-750 hover:border-gray-600 transition-all duration-200 cursor-pointer h-full">
        <div className="flex items-start justify-between mb-3">
          <h3 className="text-xl font-bold text-gray-100 tracking-tight">
            {questionnaire.abbreviation}
          </h3>
          <span className="text-xs font-semibold px-2 py-1 bg-gray-700 text-gray-300 rounded">
            {questionnaire.language}
          </span>
        </div>
        
        <h4 className="text-sm font-medium text-gray-300 mb-3 line-clamp-2">
          {questionnaire.name}
        </h4>
        
        {questionnaire.description && (
          <p className="text-sm text-gray-400 line-clamp-3">
            {questionnaire.description}
          </p>
        )}
        
        <div className="mt-4 flex items-center text-gray-500 text-sm">
          <svg 
            className="w-4 h-4 mr-1" 
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path 
              strokeLinecap="round" 
              strokeLinejoin="round" 
              strokeWidth={2} 
              d="M9 5l7 7-7 7" 
            />
          </svg>
          Start questionnaire
        </div>
      </div>
    </Link>
  );
}


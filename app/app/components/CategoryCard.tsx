import Link from 'next/link';

interface CategoryCardProps {
  title: string;
  description: string;
  href: string;
  icon: 'auto' | 'hetero';
  count?: number;
}

export default function CategoryCard({ title, description, href, icon, count }: CategoryCardProps) {
  return (
    <Link href={href}>
      <div className="block p-8 bg-gray-800 border-2 border-gray-700 rounded-xl shadow-lg hover:bg-gray-750 hover:border-blue-500 transition-all duration-300 cursor-pointer h-full group">
        <div className="flex items-start mb-4">
          {icon === 'auto' ? (
            <svg
              className="w-12 h-12 text-blue-400 group-hover:text-blue-300 transition-colors"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
              />
            </svg>
          ) : (
            <svg
              className="w-12 h-12 text-green-400 group-hover:text-green-300 transition-colors"
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
          )}
        </div>
        
        <h2 className="text-2xl font-bold text-gray-100 mb-3 group-hover:text-blue-300 transition-colors">
          {title}
        </h2>
        
        <p className="text-gray-400 mb-4 leading-relaxed">
          {description}
        </p>
        
        {count !== undefined && (
          <div className="inline-block px-3 py-1 bg-gray-700 text-gray-300 rounded-full text-sm font-medium mb-4">
            {count} questionnaire{count !== 1 ? 's' : ''}
          </div>
        )}
        
        <div className="flex items-center text-blue-400 font-medium group-hover:text-blue-300 transition-colors">
          <span>View questionnaires</span>
          <svg
            className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
          </svg>
        </div>
      </div>
    </Link>
  );
}


import CategoryCard from './components/CategoryCard';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-900">
      <div className="container mx-auto px-4 py-12 max-w-6xl">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold text-gray-100 mb-4">
            Questionnaire Testing Platform
          </h1>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Choose a category below to access and test psychiatric and clinical questionnaires
          </p>
        </div>

        {/* Category Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          <CategoryCard
            title="Auto Questionnaires"
            description="Self-report questionnaires completed independently by patients to assess their own symptoms and conditions."
            href="/auto-questionnaires"
            icon="auto"
          />
          
          <CategoryCard
            title="Hetero Questionnaires"
            description="Clinician-rated questionnaires completed by healthcare professionals based on patient assessment."
            href="/hetero-questionnaires"
            icon="hetero"
          />
        </div>

        {/* Info Section */}
        <div className="mt-16 text-center">
          <div className="inline-block p-6 bg-gray-800 border border-gray-700 rounded-lg">
            <h3 className="text-lg font-semibold text-gray-200 mb-2">
              Testing Environment
            </h3>
            <p className="text-gray-400 text-sm">
              This platform is designed for functional testing of questionnaire implementations.
              <br />
              All data is processed in real-time and not stored.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

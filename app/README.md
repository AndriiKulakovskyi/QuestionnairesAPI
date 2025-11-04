# Questionnaire Testing Platform

A Next.js frontend application for testing psychiatric and clinical questionnaires using the FastAPI backend.

## Features

- **Questionnaire List**: Browse all available auto-questionnaires
- **Dynamic Forms**: Render questionnaires dynamically based on backend structure
- **Real-time Validation**: Validate answers before submission
- **Score Calculation**: Display comprehensive results with interpretations
- **Responsive Design**: Works seamlessly on mobile, tablet, and desktop
- **Modern UI**: Gray-900 themed interface with Tailwind CSS

## Prerequisites

- Node.js 18+ or 20+
- Backend API running at `http://127.0.0.1:8000`

## Installation

```bash
# Install dependencies
npm install
```

## Running the Application

### Development Mode

```bash
npm run dev
```

The application will be available at `http://localhost:3000`

### Production Build

```bash
npm run build
npm start
```

## Environment Variables

Create a `.env.local` file (already configured):

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## Project Structure

```
app/
├── app/
│   ├── components/          # Reusable React components
│   │   ├── QuestionnaireCard.tsx
│   │   ├── Question.tsx
│   │   └── Results.tsx
│   ├── lib/                 # Utility functions
│   │   └── api.ts          # API client
│   ├── types/              # TypeScript type definitions
│   │   └── questionnaire.ts
│   ├── questionnaire/      # Dynamic questionnaire routes
│   │   └── [id]/
│   │       └── page.tsx
│   ├── globals.css         # Global styles
│   ├── layout.tsx          # Root layout
│   └── page.tsx            # Homepage
├── public/                 # Static assets
├── .env.local             # Environment variables
└── package.json           # Dependencies
```

## Usage

1. **Start the Backend API**: Make sure the FastAPI backend is running at `http://127.0.0.1:8000`
2. **Start the Frontend**: Run `npm run dev`
3. **Browse Questionnaires**: Visit `http://localhost:3000` to see all available questionnaires
4. **Take a Questionnaire**: Click on any questionnaire card to start
5. **Submit Answers**: Complete all required questions and submit
6. **View Results**: See your scores and clinical interpretations

## API Integration

The frontend communicates with the FastAPI backend using the following endpoints:

- `GET /api/auto/questionnaires` - List all questionnaires
- `GET /api/auto/questionnaires/{id}` - Get questionnaire details
- `POST /api/auto/questionnaires/{id}/validate` - Validate answers
- `POST /api/auto/questionnaires/{id}/submit` - Submit and score

## Technologies

- **Next.js 16** - React framework with App Router
- **React 19** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS 4** - Utility-first styling
- **Fetch API** - HTTP client

## Development

### Type Checking

```bash
npm run build
```

### Linting

```bash
npm run lint
```

## Notes

- The application uses Next.js App Router (not Pages Router)
- All questionnaire rendering is dynamic based on backend responses
- The app is configured for both light and dark modes (currently using dark gray-900 theme)
- Client-side rendering is used for the questionnaire page to handle form state

## Troubleshooting

### Cannot connect to API

Make sure the backend is running:
```bash
# In the parent directory
python run_api.py
```

### Port already in use

If port 3000 is in use, you can specify a different port:
```bash
npm run dev -- -p 3001
```

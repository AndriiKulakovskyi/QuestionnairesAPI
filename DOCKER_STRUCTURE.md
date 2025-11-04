# Docker Container Structure

## Directory Layout Inside Container

```
/app/
├── frontend/                    # Next.js Application
│   ├── package.json
│   ├── package-lock.json
│   ├── next.config.ts
│   ├── tsconfig.json
│   ├── .next/                   # Built Next.js app
│   ├── app/                     # Next.js app directory (pages/components)
│   │   ├── lib/
│   │   │   └── api.ts          # API client
│   │   ├── components/
│   │   ├── auto-questionnaires/
│   │   ├── hetero-questionnaires/
│   │   └── questionnaire/
│   └── public/                  # Static assets
│
├── questionnaires/              # Python questionnaire modules
│   ├── auto/
│   └── hetero/
├── api/                         # FastAPI application
│   ├── main.py
│   ├── routes/
│   ├── schemas.py
│   └── dependencies.py
├── run_api.py                   # Python startup script
├── pyproject.toml
└── poetry.lock

/etc/supervisor/conf.d/
└── supervisord.conf             # Supervisor configuration
```

## Process Management

### Supervisor manages two processes:

1. **Next.js (Frontend)**
   - Command: `npm start`
   - Working Directory: `/app/frontend`
   - Port: Uses `$PORT` from environment (10000 from Render)
   - Environment: `NODE_ENV=production`

2. **Python FastAPI (Backend)**
   - Command: `poetry run python run_api.py`
   - Working Directory: `/app`
   - Port: 8000 (internal)
   - Host: 0.0.0.0

## Port Routing

```
External (Render) → Port 10000
                    ↓
        Next.js Server (Port 10000)
                    ↓
        Rewrites /health, /api/*, /docs → http://localhost:8000
                    ↓
        Python FastAPI (Port 8000)
```

## Build Process

### Frontend Build (Lines 22-34)
1. Set WORKDIR to `/app/frontend`
2. Copy `package.json` and `package-lock.json`
3. Run `npm ci` (install all dependencies including dev)
4. Copy all Next.js source files
5. Run `npm run build` (build production Next.js)
6. Run `npm prune --production` (remove dev dependencies)

### Backend Setup (Lines 39-49)
1. Set WORKDIR to `/app`
2. Copy `pyproject.toml` and `poetry.lock`
3. Copy Python source directories
4. Configure Poetry (disable venv creation)
5. Run `poetry install --only=main` (production dependencies only)

## Verification Checklist

✅ Frontend correctly located at `/app/frontend`
✅ Backend correctly located at `/app`
✅ Supervisord runs Next.js from `/app/frontend`
✅ Supervisord runs Python from `/app`
✅ Next.js built with all dependencies
✅ Python installed with production dependencies
✅ Ports properly configured (10000 external, 8000 internal)
✅ API rewrites configured in next.config.ts
✅ Both processes log to stdout/stderr
✅ Both processes auto-restart on failure


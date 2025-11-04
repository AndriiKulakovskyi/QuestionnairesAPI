"""
Main FastAPI application for Questionnaires API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auto, hetero
from .dependencies import get_registry
from .schemas import HealthResponse, APIInfoResponse

# Initialize FastAPI app
app = FastAPI(
    title="Questionnaires API",
    description="""
    API for psychiatric and clinical questionnaires supporting both auto (self-report) 
    and hetero (clinician-rated) instruments.
    
    ## Categories
    
    * **Auto Questionnaires** - Self-report instruments completed by patients
    * **Hetero Questionnaires** - Clinician-rated instruments (coming soon)
    
    ## Features
    
    * List all available questionnaires
    * Retrieve complete questionnaire structures with questions and constraints
    * Validate answers before submission
    * Calculate scores and clinical interpretations
    * Full branching logic and constraint support
    """,
    version="1.0.0",
    contact={
        "name": "Questionnaires API",
        "url": "https://github.com/yourusername/QuestionnairesAPI",
    },
    license_info={
        "name": "MIT",
    },
)

# Configure CORS middleware - allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    auto.router, 
    prefix="/api/auto", 
    tags=["Auto Questionnaires (Self-Report)"]
)
app.include_router(
    hetero.router, 
    prefix="/api/hetero", 
    tags=["Hetero Questionnaires (Clinician-Rated)"]
)


@app.get(
    "/",
    response_model=APIInfoResponse,
    summary="API Information",
    description="Returns basic information about the API and available endpoints."
)
def root():
    """Root endpoint providing API information."""
    return APIInfoResponse(
        title="Questionnaires API",
        description="API for psychiatric and clinical questionnaires",
        version="1.0.0",
        endpoints={
            "auto_questionnaires": "/api/auto/questionnaires",
            "hetero_questionnaires": "/api/hetero/questionnaires",
            "health_check": "/health",
            "documentation": "/docs",
            "openapi_schema": "/openapi.json"
        }
    )


@app.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Returns the health status of the API and counts of available questionnaires."
)
def health_check():
    """Health check endpoint."""
    registry = get_registry()
    
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        questionnaires={
            "auto": len(registry.auto_questionnaires),
            "hetero": len(registry.hetero_questionnaires)
        }
    )


# Optional: Add startup and shutdown events
@app.on_event("startup")
async def startup_event():
    """Executed when the application starts."""
    registry = get_registry()
    print(f"🚀 Questionnaires API started")
    print(f"📋 Loaded {len(registry.auto_questionnaires)} auto questionnaires")
    print(f"📋 Loaded {len(registry.hetero_questionnaires)} hetero questionnaires")


@app.on_event("shutdown")
async def shutdown_event():
    """Executed when the application shuts down."""
    print("👋 Questionnaires API shutting down")


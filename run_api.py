#!/usr/bin/env python3
"""
Startup script for the Questionnaires API

This script runs the FastAPI application using Uvicorn with auto-reload enabled
for development purposes.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


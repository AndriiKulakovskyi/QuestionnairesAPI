#!/usr/bin/env python3
"""
Startup script for the Questionnaires API

This script can be used in two ways:
1. Run directly: python run_api.py
2. With uvicorn: uvicorn run_api:app --reload
"""

import uvicorn
from api.main import app

# Export app for uvicorn
__all__ = ["app"]

if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )


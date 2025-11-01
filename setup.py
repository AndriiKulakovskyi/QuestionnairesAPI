"""
Setup configuration for Fondation FondaMental Questionnaires Package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="fondamental-questionnaires",
    version="2.0.0",
    
    # Package info
    packages=find_packages(exclude=["tools", "*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.10",
    
    # Metadata
    author="Fondation FondaMental",
    author_email="contact@fondation-fondamental.org",
    description="Modern psychiatric questionnaire library with 151+ validated instruments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fondation-fondamental/questionnaires",
    
    # Classification
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    
    # Keywords for discovery
    keywords=[
        "psychiatry",
        "psychology", 
        "questionnaires",
        "mental-health",
        "assessment",
        "clinical-scales",
        "ymrs",
        "madrs",
        "panss",
        "bipolar",
        "schizophrenia",
        "depression",
        "autism"
    ],
    
    # No external dependencies - only Python stdlib!
    install_requires=[],
    
    # Optional dependencies for development/testing
    extras_require={
        "dev": [
            "pytest>=7.0",
            "mypy>=1.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
        "api": [
            "fastapi>=0.100.0",
            "uvicorn>=0.23.0",
        ],
    },
    
    # Include package data
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt"],
    },
    
    # Entry points for command-line tools (optional)
    entry_points={
        "console_scripts": [
            "questionnaires-list=api.service:main",  # Could add CLI later
        ],
    },
    
    # Project URLs
    project_urls={
        "Documentation": "https://github.com/fondation-fondamental/questionnaires/docs",
        "Source": "https://github.com/fondation-fondamental/questionnaires",
        "Bug Reports": "https://github.com/fondation-fondamental/questionnaires/issues",
    },
)

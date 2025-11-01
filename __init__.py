"""
Refactored Questionnaires Package
==================================

Modern, modular implementation of psychiatric questionnaires for Fondation FondaMental.

This package provides:
- Type-safe models for questions, answers, and responses
- Flexible scoring strategies for different scoring algorithms
- Comprehensive validation and interpretation
- API-ready structure for web services
- Registry and factory for questionnaire management

Version: 2.0.0
Author: Fondation FondaMental
"""

__version__ = "2.0.0"

# Import core models
from .core.models import (
    AnswerOption,
    Question,
    QuestionType,
    PathologyDomain,
    RespondentType,
    QuestionnaireResponse,
    ScoreResult,
    BaseQuestionnaire
)

# Import scoring utilities
from .core.scoring import (
    ScoringStrategy,
    SimpleSumStrategy,
    WeightedSumStrategy,
    SubscaleStrategy,
    GroupedMaxStrategy,
    PercentageStrategy,
    ThresholdInterpreter,
    InterpretationThreshold
)

# Import registry and factory
from .core.registry import (
    QuestionnaireRegistry,
    QuestionnaireFactory,
    questionnaire_registry,
    questionnaire_factory,
    register_questionnaire
)

# Import all questionnaires to trigger auto-registration
# This must come after registry imports
from . import questionnaires  # noqa: F401

__all__ = [
    # Models
    "AnswerOption",
    "Question",
    "QuestionType",
    "PathologyDomain",
    "RespondentType",
    "QuestionnaireResponse",
    "ScoreResult",
    "BaseQuestionnaire",
    
    # Scoring
    "ScoringStrategy",
    "SimpleSumStrategy",
    "WeightedSumStrategy",
    "SubscaleStrategy",
    "GroupedMaxStrategy",
    "PercentageStrategy",
    "ThresholdInterpreter",
    "InterpretationThreshold",
    
    # Registry
    "QuestionnaireRegistry",
    "QuestionnaireFactory",
    "questionnaire_registry",
    "questionnaire_factory",
    "register_questionnaire",
]

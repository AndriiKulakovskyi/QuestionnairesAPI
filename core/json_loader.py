"""Utility helpers for loading questionnaires from JSON definitions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import (
    AnswerOption,
    PathologyDomain,
    Question,
    QuestionType,
    RespondentType,
)
from .scoring import (
    NotImplementedStrategy,
    ScoringStrategy,
    SimpleSumStrategy,
    SubscaleStrategy,
    WeightedSumStrategy,
)


def _coerce_pathology(value: str) -> PathologyDomain:
    try:
        return PathologyDomain(value)
    except ValueError:
        return PathologyDomain[value.upper()]


def _coerce_respondent(value: str) -> RespondentType:
    try:
        return RespondentType(value)
    except ValueError:
        return RespondentType[value.upper()]


def _coerce_question_type(value: str) -> QuestionType:
    try:
        return QuestionType(value)
    except ValueError:
        return QuestionType[value.upper()]


def _build_answer_options(option_defs: List[Dict[str, Any]]) -> List[AnswerOption]:
    options: List[AnswerOption] = []
    for option in option_defs:
        options.append(
            AnswerOption(
                value=option["value"],
                label=option["label"],
                score=option.get("score"),
                conditional_trigger=option.get("conditional_trigger"),
            )
        )
    return options


def _build_questions(question_defs: List[Dict[str, Any]]) -> List[Question]:
    questions: List[Question] = []
    for question in question_defs:
        options = _build_answer_options(question["options"])
        questions.append(
            Question(
                id=question["id"],
                text=question["text"],
                options=options,
                question_type=_coerce_question_type(question.get("type", "single_choice")),
                required=question.get("required", True),
                reverse_scored=question.get("reverse_scored", False),
                conditional_on=question.get("conditional_on"),
                conditional_value=question.get("conditional_value"),
                group=question.get("group"),
                help_text=question.get("help_text"),
            )
        )
    return questions


def _build_scoring(scoring_def: Optional[Dict[str, Any]]) -> Optional[ScoringStrategy]:
    if not scoring_def:
        return SimpleSumStrategy()

    scoring_type = scoring_def.get("type", "simple_sum")
    if scoring_type == "simple_sum":
        return SimpleSumStrategy(scoring_def.get("missing_value_handling", "error"))
    if scoring_type == "weighted_sum":
        return WeightedSumStrategy(scoring_def.get("weights", {}))
    if scoring_type == "subscale":
        return SubscaleStrategy(
            scoring_def.get("subscales", {}),
            scoring_def.get("calculate_total", True),
        )
    if scoring_type == "not_implemented":
        reason = scoring_def.get("reason", "Scoring not implemented")
        return NotImplementedStrategy(reason)

    raise ValueError(f"Unsupported scoring strategy type: {scoring_type}")


def load_questionnaire_json(path: Path) -> Dict[str, Any]:
    """Load and parse a questionnaire JSON definition."""

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    questions = _build_questions(data.pop("questions"))
    scoring = _build_scoring(data.pop("scoring", None))

    metadata = {
        "code": data["code"],
        "name": data["name"],
        "description": data.get("description", ""),
        "pathology_domain": _coerce_pathology(data["pathology_domain"]),
        "respondent_type": _coerce_respondent(data["respondent_type"]),
        "questions": questions,
        "visit_types": data.get("visit_types", []),
        "estimated_duration_minutes": data.get("estimated_duration_minutes"),
        "version": data.get("version", "1.0"),
        "scoring_strategy": scoring,
    }

    return metadata


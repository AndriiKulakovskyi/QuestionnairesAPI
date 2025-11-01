"""EQ-5D-5L quality of life questionnaire backed by JSON data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..core.json_loader import load_questionnaire_json
from ..core.models import BaseQuestionnaire, QuestionnaireResponse, ScoreResult
from ..core.registry import register_questionnaire


DATA_FILE = Path(__file__).with_name("data").joinpath("eq_5d_5l.json")


@register_questionnaire("EQ_5D_5L")
@dataclass
class Eq5d5l(BaseQuestionnaire):
    """EQ-5D-5L questionnaire loaded from structured JSON."""

    def __init__(self):
        definition = load_questionnaire_json(DATA_FILE)
        scoring_strategy = definition.pop("scoring_strategy")

        super().__init__(**definition)
        self.scoring_strategy = scoring_strategy

    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Delegate to the configured scoring strategy (raises if unavailable)."""

        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")

        if not self.scoring_strategy:
            raise NotImplementedError("No scoring strategy configured for EQ-5D-5L")

        return self.scoring_strategy.calculate(responses, self.questions)

"""
ALDA - ALDA Questionnaire
=========================

6 items questionnaire

Source: Extracted from ebipolar application
Applications: ebipolar
Author: Fondation FondaMental
Version: 2.0.0
"""

from dataclasses import dataclass
from ..core.models import (
    BaseQuestionnaire,
    Question,
    AnswerOption,
    QuestionType,
    PathologyDomain,
    RespondentType,
    QuestionnaireResponse,
    ScoreResult
)
from ..core.scoring import SimpleSumStrategy
from ..core.registry import register_questionnaire


@register_questionnaire("ALDA")
@dataclass
class Alda(BaseQuestionnaire):
    """ALDA Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ALDA questionnaire with all 6 items."""
        
        questions_list = [
            Question(
                id='radhtml_alda_a',
                text="<b> critère A </b>",
                options=[
                    AnswerOption(value='0', label="Réponse complète, aucune récurrence mais le patient peut encore avoir des symptômes résiduels et récupération fonctionnelle totale", score=0),
                    AnswerOption(value='1', label="Très bonnes réponse, aucune récurrence mais le patient peut encore avoir des symptômes résiduels minimes (anxiété passagère, perturbation du sommeil, dysphorie, irritabilité) n'exigeant aucune intervention", score=1),
                    AnswerOption(value='2', label="Très bonne réponse. l'activité de la maladie réduite de plus de 90%", score=2),
                    AnswerOption(value='3', label="Bonne réponse. Réduction de l'activité de maladie de 80-90%", score=3),
                    AnswerOption(value='4', label="Bonne réponse. Réduction de l'activité de maladie de 65-80%", score=4),
                    AnswerOption(value='5', label="Bonne modérée. Réduction de l'activité de maladie de 50-56%", score=5),
                    AnswerOption(value='6', label="Amélioration modérée. Réduction de l'activité de maladie de 35-50%", score=6),
                    AnswerOption(value='7', label="Amélioration légère. Réduction de l'activité de maladie de 20-35%", score=7),
                    AnswerOption(value='8', label="Amélioration légère. Réduction de l'activité de maladie de 10-20%", score=8),
                    AnswerOption(value='9', label="Amélioration minime. Réduction de l'activité de maladie de 0-10%", score=9),
                    AnswerOption(value='10', label="Aucun changement, ni péjoration", score=10)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_alda_b1',
                text="<b>B1: nombre d'épisodes avant le traitement</b>",
                options=[
                    AnswerOption(value='a', label="4 épisodes ou plus", score=0),
                    AnswerOption(value='b', label="1. 2 ou 3 épisodes", score=1),
                    AnswerOption(value='c', label="1 épisode", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_alda_b2',
                text="<b>B2: Fréquence des épisodes avant le traitement.</b>",
                options=[
                    AnswerOption(value='a', label="Moyenne à élevée, incluant les cycles rapides", score=0),
                    AnswerOption(value='b', label="Faible, rémissions spontanées de 3 ans ou plus en moyenne", score=1),
                    AnswerOption(value='c', label="1 seul épisode, risque de récurrence ne peut être établi", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_alda_b3',
                text="<b>B3: Durée du traitement;</b>",
                options=[
                    AnswerOption(value='a', label="2 ans ou plus", score=0),
                    AnswerOption(value='b', label="1-2 ans", score=1),
                    AnswerOption(value='c', label="moins d'un an", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_alda_b4',
                text="<b>B4: Compliance durant la/les période(s) de stabilité</b>",
                options=[
                    AnswerOption(value='a', label="Excellente, documentée par des taux dans les limites thérapeutiques", score=0),
                    AnswerOption(value='b', label="Bonne, plus de 80% des taux dans les limites thérapeutiques", score=1),
                    AnswerOption(value='c', label="Pauvre, répétitivement hors traitements, moins de 80% des taux dans les limites thérapeutiques", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_alda_b5',
                text="<b>B5 Usage de médication additionnelle durant la phase de stabilité</b>",
                options=[
                    AnswerOption(value='a', label="Aucun hormis de rares somnifères (1 par semaine ou moins); pas d'autres stabilisateurs pour contrôler les symptômes thymiques", score=0),
                    AnswerOption(value='b', label="Antidépresseurs ou antipsychotiques à faible dose comme une sécurité, ou recours prolongé à des somnifères", score=1),
                    AnswerOption(value='c', label="Usage prolongé ou systématique d'un antidépresseur ou antipsychotique", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ALDA",
            name="ALDA Questionnaire",
            description="6 items questionnaire",
            pathology_domain=PathologyDomain.BIPOLAR,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ALDA score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

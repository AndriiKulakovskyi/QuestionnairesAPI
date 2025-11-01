"""
ALIMENTAIRE - ALIMENTAIRE Questionnaire
=======================================

21 items questionnaire

Source: Extracted from easperger application
Applications: easperger
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


@register_questionnaire("ALIMENTAIRE")
@dataclass
class Alimentaire(BaseQuestionnaire):
    """ALIMENTAIRE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ALIMENTAIRE questionnaire with all 21 items."""
        
        questions_list = [
            Question(
                id='al01',
                text="1. Actuellement, suivez-vous un régime alimentaire",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al0101',
                text="Ce régime vous a-t-il été prescrit par un(e) professionnel(le) de santé : médecin généraliste, médecin spécialiste (nutritionniste ou endocrinologue), diététicien(ne) ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al0102',
                text="Pour quelle raison suivez-vous ce régime ? (plusieurs réponses possibles)?",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al0103',
                text="Pour quelle raison suivez-vous ce régime ? (plusieurs réponses possibles)?",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5),
                    AnswerOption(value='g', label="7", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al03',
                text="3. Combien de sucre (blanc, brun, roux...) consommez-vous par jour (café, thé, yaourt...) ? (nombre de morceaux ou de cuillerées à café)",
                options=[
                    AnswerOption(value='a', label="Jamais ou rarement", score=0),
                    AnswerOption(value='b', label="1 ou 2", score=1),
                    AnswerOption(value='c', label="3 ou 4", score=2),
                    AnswerOption(value='d', label="5 ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al04',
                text="4. Combien de sucre allégé ou édulcorant (aspartame, stévia, sirop d’agave ...) consommez-vous par jour (café, thé, yaourt...) ? (nombre de morceaux, sucrettes ou de cuillerées à café)",
                options=[
                    AnswerOption(value='a', label="Jamais ou rarement", score=0),
                    AnswerOption(value='b', label="1 ou 2", score=1),
                    AnswerOption(value='c', label="3 ou 4", score=2),
                    AnswerOption(value='d', label="5 ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al05',
                text="5. Aimez-vous manger très salé ou resalez-vous vos plats avant de les avoir goûtés ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al06',
                text="6. Quel type de matière grasse utilisez-vous le plus souvent pour cuire les aliments ? (une seule réponse)",
                options=[
                    AnswerOption(value='a', label="Beurre", score=0),
                    AnswerOption(value='b', label="Beurre allégé", score=1),
                    AnswerOption(value='c', label="Huile", score=2),
                    AnswerOption(value='d', label="Margarine", score=3),
                    AnswerOption(value='e', label="Autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al0601',
                text="précisez quel type de margarine",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al0701',
                text="7. Quels types d’huile utilisez-vous le plus souvent pour l’assaisonnement ou la cuisson ? (deux réponses maximum)",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al08',
                text="8. Prenez-vous des compléments alimentaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al0801',
                text="combien de fois en prenez-vous par semaine ?",
                options=[
                    AnswerOption(value='a', label="1 fois", score=0),
                    AnswerOption(value='b', label="2 fois", score=1),
                    AnswerOption(value='c', label="3 fois", score=2),
                    AnswerOption(value='d', label="4 fois et plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al0802',
                text="précisez",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al09',
                text="9. Au cours de votre vie avez-vous déjà consommé des boissons alcoolisées (vins, apéritifs, bière..)?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al10',
                text="10. Habituellement, à quelle fréquence consommez-vous des boissons alcoolisées?",
                options=[
                    AnswerOption(value='a', label="1 à plusieurs fois par semaines", score=0),
                    AnswerOption(value='b', label="2 à 3 fois par mois", score=1),
                    AnswerOption(value='c', label="1 fois par mois ou moins", score=2),
                    AnswerOption(value='d', label="Jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al11',
                text="11. Au cours de la semaine dernière, avez-vous consommé du vin (rouge, blanc ou rosé)?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al12',
                text="12. Si oui, quelle quantité maximum par jour ?",
                options=[
                    AnswerOption(value='a', label="1 Verre", score=0),
                    AnswerOption(value='b', label="2 verres", score=1),
                    AnswerOption(value='c', label="3 verres", score=2),
                    AnswerOption(value='d', label="4 verres", score=3),
                    AnswerOption(value='e', label="5 verres", score=4),
                    AnswerOption(value='f', label="1 litre et plus", score=5),
                    AnswerOption(value='g', label="Ne sait pas", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al14',
                text="14. Au cours de la semaine dernière, avez-vous consommé de la bière ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al15',
                text="15. Si oui, quelle quantité maximum par jour ?",
                options=[
                    AnswerOption(value='a', label="1 demi", score=0),
                    AnswerOption(value='b', label="2 demi", score=1),
                    AnswerOption(value='c', label="3 demi", score=2),
                    AnswerOption(value='d', label="4 demi", score=3),
                    AnswerOption(value='e', label="5 demi", score=4),
                    AnswerOption(value='f', label="Ne sait pas", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al17',
                text="17. Au cours de la semaine dernière, avez-vous consommé un apéritif ou un digestif?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='al18',
                text="18. Si oui, quelle quantité maximum par jour ?",
                options=[
                    AnswerOption(value='a', label="1 verre", score=0),
                    AnswerOption(value='b', label="2 verres", score=1),
                    AnswerOption(value='c', label="3 verres", score=2),
                    AnswerOption(value='d', label="Ne sait pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ALIMENTAIRE",
            name="ALIMENTAIRE Questionnaire",
            description="21 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=10,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ALIMENTAIRE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

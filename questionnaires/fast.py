"""
FAST - FAST Questionnaire
=========================

21 items questionnaire

Source: Extracted from ecedr application
Applications: ecedr
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


@register_questionnaire("FAST")
@dataclass
class Fast(BaseQuestionnaire):
    """FAST Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize FAST questionnaire with all 21 items."""
        
        questions_list = [
            Question(
                id='fast1',
                text="1. Prendre des responsabilités au sein de la maison",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast10',
                text="10. Capacité à se concentrer devant un film, un livre..",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast11',
                text="11. Capacité au calcul mental",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast13',
                text="13. Capacité à se souvenir des noms récemment appris",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast14',
                text="14. Capacité à apprendre de nouvelles informations",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast15',
                text="15. Gérer votre propre argent",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast16',
                text="16. Dépenser façon équilibrée",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast17',
                text="17. Conserver des amitiés",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast18',
                text="18. Participer à des activités sociales",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast19',
                text="19. Avoir de bonnes relations avec vos proches",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast20',
                text="20. Habiter avec votre famille",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast21',
                text="21. Avoir des relations sexuelles satisfaisantes",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast22',
                text="22. Être capable de défendre vos intérêts",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast23',
                text="23. Faire de l’exercice ou pratiquer un sport",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast24',
                text="24. Avoir des loisirs",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast3',
                text="3. Faire les courses",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast5',
                text="5. Avoir un emploi rémunéré",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast6',
                text="6. Terminer les tâches le plus rapidement possible",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast7',
                text="7. Travailler dans le champ correspondant à votre formation",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast8',
                text="8. Recevoir le salaire que vous méritez",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fast9',
                text="9. Gérer correctement la somme de travail",
                options=[
                    AnswerOption(value='a', label="aucune difficulté", score=0),
                    AnswerOption(value='b', label="difficulté légère", score=1),
                    AnswerOption(value='c', label="difficulté modérée", score=2),
                    AnswerOption(value='d', label="difficulté sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="FAST",
            name="FAST Questionnaire",
            description="21 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.CLINICIAN_RATED,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=10,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute FAST score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

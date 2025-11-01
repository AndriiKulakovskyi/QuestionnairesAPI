"""
WURS - WURS Questionnaire
=========================

25 items questionnaire

Source: Extracted from eschizo application
Applications: eschizo
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


@register_questionnaire("WURS")
@dataclass
class Wurs(BaseQuestionnaire):
    """WURS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize WURS questionnaire with all 25 items."""
        
        questions_list = [
            Question(
                id='radhtml_wurs10',
                text="10.Des difficultés à me tenir aux choses, à mener mes projets jusqu’à la fin, à finir les choses commencées",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs11',
                text="11. Têtu(e),obstiné(e)",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs12',
                text="12.Triste ou cafardeux(se),déprimé(e),malheureux(se)",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs15',
                text="15. Désobéissant(e) envers mes parents,rebelle,effronté(e)",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs16',
                text="16. Mauvaise opinion de moi-même",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs17',
                text="17. Irritable",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs20',
                text="20. D’humeur changeante avec des hauts et des bas",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs21',
                text="21. En colère",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs24',
                text="24. Impulsif(ve).J’agissais sans réfléchir.",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs25',
                text="25. Tendance à être immature",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs26',
                text="26. Culpabilisé(e),plein(e) de regrets",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs27',
                text="27. Je pouvais perdre le contrôle de moi-même",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs28',
                text="28. Tendance à être ou à agir de façon irrationnelle",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs29',
                text="29. Impopulaire auprès des autres enfants. Je ne gardais pas longtemps mes amis ou je ne m’entendais pas avec les autres enfants",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs3',
                text="3. Des problèmes de concentration. J'étais facilement distrait(e)",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs4',
                text="4. Anxieux.Je me faisais du souci",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs40',
                text="40. Du mal à voir les choses du point de vue de quelqu’un d’autre",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs41',
                text="41. Des ennuis avec les autorités, des ennuis à l’école, convoqué(e) par le directeur",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs5',
                text="5. Nerveux.Je ne tenais pas en place",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs51',
                text="51. Dans l’ensemble un élève peu doué, apprenant lentement",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs56',
                text="56. Des difficultés en mathématiques ou avec les chiffres",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs59',
                text="59. En dessous de mon potentiel",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs6',
                text="6. Inattentif(ve),rêveur(se)",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs7',
                text="7. Facilement en colère,« soupe au lait »",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_wurs9',
                text="9. Des éclats d’humeur,des accès de colère",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="WURS",
            name="WURS Questionnaire",
            description="25 items questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=12,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute WURS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

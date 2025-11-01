"""
AUT_PSQI - AUT_PSQI Questionnaire
=================================

15 items questionnaire

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


@register_questionnaire("AUT_PSQI")
@dataclass
class AutPsqi(BaseQuestionnaire):
    """AUT_PSQI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_PSQI questionnaire with all 15 items."""
        
        questions_list = [
            Question(
                id='psqi10',
                text="10.Partagez vous votre lit ou votre logement avec quelqu’un ?",
                options=[
                    AnswerOption(value='a', label="Non, je ne partage ni mon lit ni mon logement avec quelqu’un", score=0),
                    AnswerOption(value='b', label="Oui, je partage mon logement avec une personne qui dort dans une autre chambre", score=1),
                    AnswerOption(value='c', label="Oui, avec une personne dans la même chambre, mais pas dans le même lit", score=2),
                    AnswerOption(value='d', label="Oui, avec une personne dans le même lit", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi11a',
                text="a. vous avez ronflé bruyamment",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi11b',
                text="b. vous avez fait de longues pauses entre les respirations en dormant",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi11c',
                text="c. vous avez eu des secousses ou des mouvements brusques des jambes en dormant",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi11d',
                text="d. vous avez eu de courtes périodes de désorientation ou de confusion en vous réveillant la nuit",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi11e',
                text="e. Autres types d’agitation pendant votre sommeil, merci de préciser",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi5c',
                text="c.Vous avez dû vous lever pour aller aux toilettes",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi5d',
                text="d.Vous avez eu du mal à respirer",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi5e',
                text="e. Vous avez toussé ou ronflé bruyamment",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi5f',
                text="f. Vous avez eu trop froid",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi5g',
                text="g. Vous avez eu trop chaud",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi5h',
                text="h. Vous avez fait des cauchemars",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi5i',
                text="i. Vous avez eu des douleurs",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi5j',
                text="j. Si vous avez eu des difficultés à dormir pour d’autres raisons, merci de les préciser",
                options=[
                    AnswerOption(value='a', label="Jamais au cours des 30 derniers jours", score=0),
                    AnswerOption(value='b', label="Moins d’une fois par semaine", score=1),
                    AnswerOption(value='c', label="Une ou deux fois par semaine", score=2),
                    AnswerOption(value='d', label="Trois fois par semaine ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psqi6',
                text="6.Comment qualifieriez-vous la qualité de votre sommeil en général au cours des 30 derniers jours ?",
                options=[
                    AnswerOption(value='a', label="Très bonne", score=0),
                    AnswerOption(value='b', label="Assez bonne", score=1),
                    AnswerOption(value='c', label="Assez mauvaise", score=2),
                    AnswerOption(value='d', label="Très mauvaise", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_PSQI",
            name="AUT_PSQI Questionnaire",
            description="15 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=7,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_PSQI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

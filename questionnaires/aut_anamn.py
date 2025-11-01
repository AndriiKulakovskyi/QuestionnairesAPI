"""
AUT_ANAMN - AUT_ANAMN Questionnaire
===================================

13 items questionnaire

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


@register_questionnaire("AUT_ANAMN")
@dataclass
class AutAnamn(BaseQuestionnaire):
    """AUT_ANAMN Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ANAMN questionnaire with all 13 items."""
        
        questions_list = [
            Question(
                id='antfamtb',
                text="Type de trouble",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5),
                    AnswerOption(value='g', label="7", score=6),
                    AnswerOption(value='h', label="8", score=7),
                    AnswerOption(value='i', label="9", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfam',
                text="Y-a-t-il des antécédents familiaux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='autretrb',
                text="Autre trouble neurodéveloppemental spécifié ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='genchang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hi',
                text="Handicap intellectuel ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuronsp',
                text="Trouble neurodéveloppemental non spécifié ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srel',
                text="Lien familial",
                options=[
                    AnswerOption(value='a', label="Père", score=0),
                    AnswerOption(value='b', label="Mère", score=1),
                    AnswerOption(value='c', label="Frère", score=2),
                    AnswerOption(value='d', label="Soeur", score=3),
                    AnswerOption(value='e', label="Fils", score=4),
                    AnswerOption(value='f', label="Fille", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdah',
                text="Déficit de l'Attention / Hyperactivité ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='top',
                text="Trouble oppositionnel avec provocation ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trbappr',
                text="Trouble spécifique des apprentissages ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trbcom',
                text="Trouble de la communication (Langage, phonation, fluidité verbale, communication sociale/pragmatique, non spécifié) ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trbmot',
                text="Troubles moteurs (Trouble développemental de la coordination, mouvements stéréotypés, Tics/syndrome Gilles de la Tourette) ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tsa',
                text="Trouble du Spectre de l'Autisme",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ANAMN",
            name="AUT_ANAMN Questionnaire",
            description="13 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_ANAMN score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

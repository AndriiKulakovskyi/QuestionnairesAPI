"""
AUT_C1EXPREL - AUT_C1EXPREL Questionnaire
=========================================

30 items questionnaire

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


@register_questionnaire("AUT_C1EXPREL")
@dataclass
class AutC1exprel(BaseQuestionnaire):
    """AUT_C1EXPREL Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1EXPREL questionnaire with all 30 items."""
        
        questions_list = [
            Question(
                id='aclacts',
                text="Acide lactique sang",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='acorgu',
                text="Acides organiques urine",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='acuriqs',
                text="Acide urique sang",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='acuriqu',
                text="Acide urique urine",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antelom',
                text="Analyse télomères",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='audiogr',
                text="Audiogramme",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='autrex',
                text="Autre",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='banqpre',
                text="Prélèvement sanguin",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='banqrpr',
                text="Reprélèvement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='banqsal',
                text="Prélèvement salivaire effectué",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='banqsan',
                text="Prélèvement sanguin effectué",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='caryoty',
                text="Caryotype",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdg',
                text="CDG",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chramis',
                text="Chromato acides aminés sanguins",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chramiu',
                text="Chromato acides aminés urinaires",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='creatiu',
                text="Créatine/guanidino acétate urine",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='eeg',
                text="EEG",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='exchang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='exwood',
                text="Examen à la lampe de Wood",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='eyetrack',
                text="Eye tracker",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fis15q1',
                text="FISH/MLPA 15q11-q13",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fis22q1',
                text="FISH/MLPA 22q11",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fis22qt',
                text="FISH/MLPA 22qter",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='frax',
                text="Fra-X",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='irmcer',
                text="IRM cérébrale",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mucpolu',
                text="Mucopolysaccharides urine",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pea',
                text="PEA",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='saicar',
                text="SAICAR/AICAR",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='scanced',
                text="Scanner cérébral",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spectpe',
                text="SPECT/PET/rCBF",
                options=[
                    AnswerOption(value='a', label="Résultat normal", score=0),
                    AnswerOption(value='b', label="Résultat anormal", score=1),
                    AnswerOption(value='c', label="Résultat non connu", score=2),
                    AnswerOption(value='d', label="Non fait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1EXPREL",
            name="AUT_C1EXPREL Questionnaire",
            description="30 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=15,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1EXPREL score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

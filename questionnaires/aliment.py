"""
ALIMENT - ALIMENT Questionnaire
===============================

18 items questionnaire

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


@register_questionnaire("ALIMENT")
@dataclass
class Aliment(BaseQuestionnaire):
    """ALIMENT Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ALIMENT questionnaire with all 18 items."""
        
        questions_list = [
            Question(
                id='aliment1',
                text="1/ Quelles quantité de pain blanc ou baguette consommez-vous par jour ? ",
                options=[
                    AnswerOption(value='a', label="0 gr", score=0),
                    AnswerOption(value='b', label="30 gr", score=1),
                    AnswerOption(value='c', label="45 gr", score=2),
                    AnswerOption(value='d', label="60 gr", score=3),
                    AnswerOption(value='e', label="75 gr", score=4),
                    AnswerOption(value='f', label="90 gr", score=5),
                    AnswerOption(value='g', label="120 gr", score=6),
                    AnswerOption(value='h', label="150 gr et plus", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment10',
                text="10/ Combien de portions de haricots verts consommez-vous par semaine ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1/2", score=1),
                    AnswerOption(value='c', label="1", score=2),
                    AnswerOption(value='d', label="1.5", score=3),
                    AnswerOption(value='e', label="2", score=4),
                    AnswerOption(value='f', label="2.5", score=5),
                    AnswerOption(value='g', label="3 et +", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment11',
                text="11/ Combien de portions de carottes cuites consommez-vous par semaine ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1/2", score=1),
                    AnswerOption(value='c', label="1", score=2),
                    AnswerOption(value='d', label="1.5", score=3),
                    AnswerOption(value='e', label="2", score=4),
                    AnswerOption(value='f', label="2.5", score=5),
                    AnswerOption(value='g', label="3 et +", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment14',
                text="14/ Combien d’oeufs consommez-vous par semaine ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5 ", score=5),
                    AnswerOption(value='g', label="6 et +", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment15',
                text="15/ Quelle quantité de poisson consommez-vous par semaine ?",
                options=[
                    AnswerOption(value='a', label="0 gr", score=0),
                    AnswerOption(value='b', label="50 gr", score=1),
                    AnswerOption(value='c', label="100 gr", score=2),
                    AnswerOption(value='d', label="150 gr", score=3),
                    AnswerOption(value='e', label="200 gr", score=4),
                    AnswerOption(value='f', label="300 gr", score=5),
                    AnswerOption(value='g', label="400 gr", score=6),
                    AnswerOption(value='h', label="500 gr et +", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment18',
                text="18/ Quelle quantité de boeuf consommez-vous par semaine ?",
                options=[
                    AnswerOption(value='a', label="0 gr", score=0),
                    AnswerOption(value='b', label="50 gr", score=1),
                    AnswerOption(value='c', label="100 gr", score=2),
                    AnswerOption(value='d', label="150 gr", score=3),
                    AnswerOption(value='e', label="200 gr", score=4),
                    AnswerOption(value='f', label="300 gr", score=5),
                    AnswerOption(value='g', label="400 gr", score=6),
                    AnswerOption(value='h', label="500 gr et +", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment19',
                text="19/ Quelle quantité de vin consommez-vous par semaine ?",
                options=[
                    AnswerOption(value='a', label="0 verre", score=0),
                    AnswerOption(value='b', label="1 verre", score=1),
                    AnswerOption(value='c', label="2 verres", score=2),
                    AnswerOption(value='d', label="3 verres", score=3),
                    AnswerOption(value='e', label="1 bouteille", score=4),
                    AnswerOption(value='f', label="2 bouteilles", score=5),
                    AnswerOption(value='g', label="3 bouteilles", score=6),
                    AnswerOption(value='h', label="4 bouteilles et +", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment2',
                text="2/ Quelle quantité de pains spéciaux consommez-vous par jour ?",
                options=[
                    AnswerOption(value='a', label="0 gr", score=0),
                    AnswerOption(value='b', label="30 gr", score=1),
                    AnswerOption(value='c', label="45 gr", score=2),
                    AnswerOption(value='d', label="60 gr", score=3),
                    AnswerOption(value='e', label="75 gr", score=4),
                    AnswerOption(value='f', label="90 gr", score=5),
                    AnswerOption(value='g', label="120 gr", score=6),
                    AnswerOption(value='h', label="150 gr et plus", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment20',
                text="20/ Combien de yaourts consommez-vous par semaine ?",
                options=[
                    AnswerOption(value='0', label="0", score=0),
                    AnswerOption(value='1', label="1", score=1),
                    AnswerOption(value='2', label="2", score=2),
                    AnswerOption(value='3', label="3", score=3),
                    AnswerOption(value='4', label="4", score=4),
                    AnswerOption(value='5', label="5 ", score=5),
                    AnswerOption(value='6', label="6", score=6),
                    AnswerOption(value='7', label="7", score=7),
                    AnswerOption(value='8', label="8", score=8),
                    AnswerOption(value='9', label="9", score=9),
                    AnswerOption(value='10', label="10", score=10),
                    AnswerOption(value='11', label="11 et +", score=11)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment21',
                text="21/ Quelle quantité de chocolat et/ou barres chocolatées consommez-vous par semaine ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="2 carrés", score=1),
                    AnswerOption(value='c', label="1 barre", score=2),
                    AnswerOption(value='d', label="2 barres", score=3),
                    AnswerOption(value='e', label="3 barres", score=4),
                    AnswerOption(value='f', label="1 tablette", score=5),
                    AnswerOption(value='g', label="2 tablettes et +", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment3',
                text="3/ Combien de tasses de lait consommez-vous par jour ? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1/2", score=1),
                    AnswerOption(value='c', label="1", score=2),
                    AnswerOption(value='d', label="2", score=3),
                    AnswerOption(value='e', label="3", score=4),
                    AnswerOption(value='f', label="4", score=5),
                    AnswerOption(value='g', label="5 et + ", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment4',
                text="4/ Combien de tasses de café consommez-vous par jour ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5 ", score=5),
                    AnswerOption(value='g', label="6", score=6),
                    AnswerOption(value='h', label="7", score=7),
                    AnswerOption(value='i', label="8", score=8),
                    AnswerOption(value='j', label="9 et +", score=9)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment5',
                text="5/ Combien de portions de fromage consommez-vous par jour ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1/4", score=1),
                    AnswerOption(value='c', label="1/2", score=2),
                    AnswerOption(value='d', label="1", score=3),
                    AnswerOption(value='e', label="2", score=4),
                    AnswerOption(value='f', label="3", score=5),
                    AnswerOption(value='g', label="4", score=6),
                    AnswerOption(value='h', label="5 et + ", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment6',
                text="Quelle quantité de fruits consommez-vous par jour ?",
                options=[
                    AnswerOption(value='0', label="0 gr", score=0),
                    AnswerOption(value='1', label="50 gr", score=1),
                    AnswerOption(value='2', label="100 gr", score=2),
                    AnswerOption(value='3', label="150 gr", score=3),
                    AnswerOption(value='4', label="200 gr", score=4),
                    AnswerOption(value='5', label="250 gr", score=5),
                    AnswerOption(value='6', label="300 gr", score=6),
                    AnswerOption(value='7', label="350 gr", score=7),
                    AnswerOption(value='8', label="400 gr", score=8),
                    AnswerOption(value='9', label="500 gr", score=9),
                    AnswerOption(value='10', label="600 gr et +", score=10)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment7',
                text="7/ Combien de cuillerées à soupe d’huile consommez-vous par jour ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1/4", score=1),
                    AnswerOption(value='c', label="1/2", score=2),
                    AnswerOption(value='d', label="1", score=3),
                    AnswerOption(value='e', label="2", score=4),
                    AnswerOption(value='f', label="3", score=5),
                    AnswerOption(value='g', label="4", score=6),
                    AnswerOption(value='h', label="5 et + ", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment8',
                text="8/ Combien de portions de beurre consommez-vous par jour ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1/4", score=1),
                    AnswerOption(value='c', label="1/2", score=2),
                    AnswerOption(value='d', label="1", score=3),
                    AnswerOption(value='e', label="1.5", score=4),
                    AnswerOption(value='f', label="2", score=5),
                    AnswerOption(value='g', label="3", score=6),
                    AnswerOption(value='h', label="4", score=7),
                    AnswerOption(value='i', label="5 et + ", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment9a',
                text="9a/ Combien de fois consommez-vous de la salade verte par semaine ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5 ", score=5),
                    AnswerOption(value='g', label="6", score=6),
                    AnswerOption(value='h', label="7", score=7),
                    AnswerOption(value='i', label="8", score=8),
                    AnswerOption(value='j', label="9 et +", score=9)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aliment9b',
                text="9b/ Combien de portions à chaque fois ?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1/2", score=1),
                    AnswerOption(value='c', label="1", score=2),
                    AnswerOption(value='d', label="1.5", score=3),
                    AnswerOption(value='e', label="2", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ALIMENT",
            name="ALIMENT Questionnaire",
            description="18 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=9,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ALIMENT score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

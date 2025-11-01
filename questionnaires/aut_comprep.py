"""
AUT_COMPREP - AUT_COMPREP Questionnaire
=======================================

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


@register_questionnaire("AUT_COMPREP")
@dataclass
class AutComprep(BaseQuestionnaire):
    """AUT_COMPREP Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_COMPREP questionnaire with all 30 items."""
        
        questions_list = [
            Question(
                id='compfreq',
                text="Fréquence",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="rarement", score=1),
                    AnswerOption(value='c', label="quelquefois", score=2),
                    AnswerOption(value='d', label="souvent", score=3),
                    AnswerOption(value='e', label="toujours", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='comprep',
                text="Comportements répétitifs",
                options=[
                    AnswerOption(value='a', label="tics", score=0),
                    AnswerOption(value='b', label="mouvements", score=1),
                    AnswerOption(value='c', label="bruits", score=2),
                    AnswerOption(value='d', label="compulsions", score=3),
                    AnswerOption(value='e', label="rituels", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='compsev',
                text="Sévérité ",
                options=[
                    AnswerOption(value='a', label="aucune", score=0),
                    AnswerOption(value='b', label="légère", score=1),
                    AnswerOption(value='c', label="modérée", score=2),
                    AnswerOption(value='d', label="sévère", score=3),
                    AnswerOption(value='e', label="extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rep2fre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rep2sev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rep3',
                text="Est-ce que vous ressentez une Anxiété Physique avant ou pendant la réalisation de vos comportements répétitifs ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rep3sym',
                text="Quels symptômes avez vous ?",
                options=[
                    AnswerOption(value='0', label="1", score=0),
                    AnswerOption(value='1', label="2", score=1),
                    AnswerOption(value='2', label="3", score=2),
                    AnswerOption(value='3', label="4", score=3),
                    AnswerOption(value='4', label="5", score=4),
                    AnswerOption(value='5', label="6", score=5),
                    AnswerOption(value='6', label="7", score=6),
                    AnswerOption(value='7', label="8", score=7),
                    AnswerOption(value='8', label="9", score=8),
                    AnswerOption(value='9', label="10", score=9),
                    AnswerOption(value='10', label="11", score=10),
                    AnswerOption(value='11', label="12", score=11),
                    AnswerOption(value='12', label="13", score=12)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rep4',
                text="Vos comportements répétitifs ne sont précédés par rien si ce n’est la sensation interne que vous avez « besoin de les faire ». ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rep4fre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rep4sev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa1',
                text="A.1. ‘Juste comme il faut’ visuel ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa1fre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa1sev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa2',
                text="A.2. ‘Juste comme il faut’ tactile",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa2fre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa2sev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa3',
                text="A.3. ‘Juste comme il faut’ auditif ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa3fre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa3sev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa4',
                text="A.4. ‘Juste comme il faut’",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa4fre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repa4sev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repbfre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repbsev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repc',
                text="Avez-vous une sensation interne d’incomplétude, d’insatisfaction, d’imperfection ; cette sensation subjective de malaise sera libérée lors de la réalisation de vos comportements répétitifs ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repcfre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repcsev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repd',
                text="Avez-vous d’autres sensations qui précèdent, déclenchent ou accompagnent vos comportements répétitifs ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repdfre',
                text="FREQUENCE",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Sévère", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repdsev',
                text="Sévèrité",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Modérée", score=2),
                    AnswerOption(value='d', label="Sévère", score=3),
                    AnswerOption(value='e', label="Extrême", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_COMPREP",
            name="AUT_COMPREP Questionnaire",
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
        """Compute AUT_COMPREP score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

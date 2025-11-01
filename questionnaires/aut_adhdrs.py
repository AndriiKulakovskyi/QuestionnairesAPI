"""
AUT_ADHDRS - AUT_ADHDRS Questionnaire
=====================================

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


@register_questionnaire("AUT_ADHDRS")
@dataclass
class AutAdhdrs(BaseQuestionnaire):
    """AUT_ADHDRS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ADHDRS questionnaire with all 15 items."""
        
        questions_list = [
            Question(
                id='adhdrs1',
                text="Souvent, votre enfant ne parvient pas à prêter attention aux détails, ou fait des fautes d’étourderie dans les devoirs scolaires, le travail ou d’autres activités",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs10',
                text="Votre enfant remue souvent les mains ou les pieds, ou se tortille sur son siège",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs11',
                text="Votre enfant se lève souvent en classe ou dans d’autres situations où il est supposé rester assis",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs12',
                text="Enfant, vous courriez ou grimpiez souvent partout, dans des situations où cela était inapproprié",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs13',
                text="Votre enfant a souvent du mal à se tenir tranquille dans les jeux ou les activités de loisir",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs14',
                text="Votre enfant est souvent 'sur la brèche' ou agit souvent comme s’il était 'monté sur ressorts'",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs15',
                text="Votre enfant parle souvent trop",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs16',
                text="Votre enfant laisse souvent échapper la réponse à une question qui n’est pas encore entièrement posée",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs17',
                text="Votre enfant a souvent du mal à attendre son tour",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs19',
                text="Certains de ces comportements étaient-ils présents avant l’âge de 7 ans ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs2',
                text="Votre enfant a souvent du mal à soutenir son attention au travail ou dans les jeux",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs3',
                text="Votre enfant semble souvent ne pas écouter quand on lui parle personnellement",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs5',
                text="Votre enfant a souvent du mal à organiser ses travaux ou ses activités",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs8',
                text="Souvent, votre enfant se laisse facilement distraire par des stimuli externes",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adhdrs9',
                text="Votre enfant a des oublis fréquents dans la vie quotidienne",
                options=[
                    AnswerOption(value='a', label="très souvent", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Rarement ou jamais", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ADHDRS",
            name="AUT_ADHDRS Questionnaire",
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
        """Compute AUT_ADHDRS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

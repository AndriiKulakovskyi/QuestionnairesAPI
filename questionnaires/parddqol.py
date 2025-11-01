"""
PARDDQOL - PARDDQOL Questionnaire
=================================

17 items questionnaire

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


@register_questionnaire("PARDDQOL")
@dataclass
class Parddqol(BaseQuestionnaire):
    """PARDDQOL Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize PARDDQOL questionnaire with all 17 items."""
        
        questions_list = [
            Question(
                id='pddqol01',
                text="1.Vous faites-vous du souci ?",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol02',
                text="2.Vous sentez-vous plus stressé(e) qu'à votre habitude ?",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol03',
                text="3.Perdez-vous plus facilement patience en général ?",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol04',
                text="4.Vous sentez-vous contrarié(e) ?",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol05',
                text="5.Cela affecte-il votre moral ?",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol06',
                text="6.La qualité de votre sommeil est-elle affecté(e) par un des aspects suivants : souci, stress, impatience, contrariété et perte de moral ? ",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol07',
                text="7.Consacrez-vous moins de temps aux autres membres de votre famille ? ",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol08',
                text="8.Limitez-vous vos sorties et loisirs ? ",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol09',
                text="9.Votre vie quotidienne est-elle perturbée par des changements de dernière minute ?",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol10',
                text="10.La qualité de votre travail, à l'extérieur ou à la maison est-elle perturbée ? ",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol11',
                text="11.Avez-vous des difficultés pour organiser votre emploi du temps ? ",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol12',
                text="12.Avez-vous des frais à votre charge ? ",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol13',
                text="13.Vous sentez-vous impuissant(e)s ou désarmé(e)s ? ",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol14',
                text="14.Les troubles de votre enfants ont-ils des répercussions sur votre propre santé ?",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol15',
                text="15.Les troubles de votre enfant sont-ils source de tension ou de dispute à l'intérieur de votre famille ? ",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Enormément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol16',
                text="16.Votre enfant vous réveille-t-il en raison de ses troubles ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="A chaque fois", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pddqol17',
                text="17.Du fait des troubles de votre enfant, diriez-vous que votre qualité de vie est :",
                options=[
                    AnswerOption(value='a', label="Inchangée", score=0),
                    AnswerOption(value='b', label="Un peu dégradée", score=1),
                    AnswerOption(value='c', label="Moyennement dégradée", score=2),
                    AnswerOption(value='d', label="Beaucoup dégradée", score=3),
                    AnswerOption(value='e', label="Enormément dégradée", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="PARDDQOL",
            name="PARDDQOL Questionnaire",
            description="17 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=8,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute PARDDQOL score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

"""
AUT_TDC - AUT_TDC Questionnaire
===============================

12 items questionnaire

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


@register_questionnaire("AUT_TDC")
@dataclass
class AutTdc(BaseQuestionnaire):
    """AUT_TDC Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_TDC questionnaire with all 12 items."""
        
        questions_list = [
            Question(
                id='tdc1',
                text="1. Votre enfant envoyait/envoie une balle de manière contrôlée et appropriée",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc10',
                text="10. Votre enfant découpait/découpe des images et des formes précisément et facilement. ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc11',
                text="11. Votre enfant était/est intéressé et aimait/aime participer aux activités sportives ou aux jeux qui requéraient/requièrent une bonne compétence motrice ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc13',
                text="13. Votre enfant était/est rapide et compétent pour ranger, s’habiller, mettre et lacer ses chaussures, … ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc15',
                text="15. Votre enfant ne semblait/semble pas fatigable facilement, ni vouté ou affalé sur sa chaise s’il doit rester assis pour un long moment. ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc3',
                text="3. Votre enfant frappait/frappe correctement une balle ou volant, avec une batte de baseball ou une raquette par exemple ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc4',
                text="4. Votre enfant sautait/saute facilement au dessus des obstacles dans un jardin ou une aire de jeu ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc5',
                text="5. Votre enfant courait/court aussi vite et de manière à peu près identique aux enfants de son âge et de même sexe. ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc6',
                text="6. Si votre enfant avait/a une activité motrice planifiée, il réussissait/réussit à utiliser son corps de manière organisée pour suivre son plan et réussir effectivement la tache  ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc7',
                text="7. Votre enfant  écrivait/écrit et dessinait/dessine suffisamment rapidement pour se maintenir au même rythme que le reste de la classe ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdc8',
                text="8. Les lettres, des nombres et des mots écrits par votre enfant étaient/sont lisibles, précises et appropriées ou, si votre enfant n’écrit pas il colorie et dessine de manière coordonnée des images que vous pouvez identifier. ",
                options=[
                    AnswerOption(value='a', label="Pas du tout comme les autres enfants", score=0),
                    AnswerOption(value='b', label="Un peu comme  les autres enfants", score=1),
                    AnswerOption(value='c', label="Presque comme les autres enfants", score=2),
                    AnswerOption(value='d', label="Quasiment comme les autres enfants", score=3),
                    AnswerOption(value='e', label="Tout à fait comme les autres enfants", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdcrel',
                text="Quelle relation avez-vous avec le patient ",
                options=[
                    AnswerOption(value='a', label="Père", score=0),
                    AnswerOption(value='b', label="Mère", score=1),
                    AnswerOption(value='c', label="Grands Parents", score=2),
                    AnswerOption(value='d', label="Tuteur", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_TDC",
            name="AUT_TDC Questionnaire",
            description="12 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_TDC score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

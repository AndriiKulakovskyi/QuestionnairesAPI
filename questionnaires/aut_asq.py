"""
AUT_ASQ - AUT_ASQ Questionnaire
===============================

31 items questionnaire

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


@register_questionnaire("AUT_ASQ")
@dataclass
class AutAsq(BaseQuestionnaire):
    """AUT_ASQ Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ASQ questionnaire with all 31 items."""
        
        questions_list = [
            Question(
                id='asq1',
                text="1.Globalement, je suis une personne qui a de la valeur",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq10',
                text="10.Si vous aviez une tâche à faire, vous la feriez sans vous préoccuper de savoir si cela pourrait blesser quelqu'un",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq11',
                text="11.Il est important pour moi que les autres m'aiment",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq12',
                text="12.Il est important pour moi d'éviter de faire des choses que les autres n'aimeraient pas",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq13',
                text="13.Je trouve difficile de prendre une décision sans savoir ce que pensent les autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq14',
                text="14.Mes relations avec les autres sont généralement peu profondes",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq15',
                text="15.Parfois je pense que je ne vaux rien",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq16',
                text="16.Je trouve difficile de faire confiance aux autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq17',
                text="17.Je trouve cela difficile de dépendre des autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq18',
                text="18.Je trouve que les autres ne se rapprochent pas de moi autant que je le voudrais",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq19',
                text="19.Je trouve qu'il est relativement facile de se rapprocher des autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq2',
                text="2.Je suis plus facile à connaître que la plupart des gens",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq20',
                text="20.C’est facile pour moi d'avoir confiance aux autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq21',
                text="21.Je me sens à l'aise avec l'idée de dépendre des autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq22',
                text="22.Je m'inquiète que les autres ne s'occupent pas autant de moi que je m'occupe d'eux",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq23',
                text="23.Je m’inquiète à l’idée que des gens veuillent trop se rapprocher de moi.",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq24',
                text="24.Je m'inquiète de ne pas être à la hauteur des autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq25',
                text="25.Je ne suis pas sûr de vouloir être proche des autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq26',
                text="26.Bien que je veux être proche des autres, cela me rend mal à l'aise",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq27',
                text="27.Je me demande pourquoi les gens veulent être en relation avec moi",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq28',
                text="28.Il est très important pour moi d'avoir une relation intime",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq29',
                text="29.Je m'inquiète beaucoup à propos de mes relations interpersonnelles",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq30',
                text="30.Je me demande comment je me débrouillerais sans avoir quelqu'un qui m'aime",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq34',
                text="34.Tout le monde a ses propres problèmes, donc je ne tracasse pas les gens avec les miens",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq37',
                text="37.Lorsque quelque chose me tracasse, les autres en sont généralement conscients et intéressés",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq38',
                text="38.J’ai confiance que les autres m'aiment et me respectent",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq40',
                text="40.Les autres me déçoivent souvent",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq5',
                text="5.Je préfère m'occuper de mes affaires et ne pas me mêler des relations entre les autres personnes de mon entourage",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq7',
                text="7.La valeur des gens devrait être jugée par leurs réussites",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq8',
                text="8.Réussir des choses est plus important que de bâtir des relations",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asq9',
                text="9.Exceller dans ce qu'on a à faire est plus important que de bien s'entendre avec les autres",
                options=[
                    AnswerOption(value='a', label="Totalement en désaccord", score=0),
                    AnswerOption(value='b', label="Fortement en désaccord", score=1),
                    AnswerOption(value='c', label="Faiblement en désaccord", score=2),
                    AnswerOption(value='d', label="Faiblement en accord", score=3),
                    AnswerOption(value='e', label="Fortement en accord", score=4),
                    AnswerOption(value='f', label="Totalement en accord", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ASQ",
            name="AUT_ASQ Questionnaire",
            description="31 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=15,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_ASQ score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

"""
CTQ - CTQ Questionnaire
=======================

28 items questionnaire

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


@register_questionnaire("CTQ")
@dataclass
class Ctq(BaseQuestionnaire):
    """CTQ Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CTQ questionnaire with all 28 items."""
        
        questions_list = [
            Question(
                id='ctq01',
                text="1. Il m'est arrivé de ne pas avoir assez à manger",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq02',
                text="2. Je savais qu'il y avait quelqu'un pour prendre soin de moi et me protéger.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq03',
                text="3. Des membres de ma famille me disaient que j'étais « stupide » ou « paresseux » ou « laid ». ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq04',
                text="4. Mes parents étaient trop saouls ou « pétés » pour s'occuper de la famille",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq05',
                text="5. Il y avait quelqu'un dans ma famille qui m'aidait à sentir que j'étais important ou particulier",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq06',
                text="6. Je devais porter des vêtements sales",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq07',
                text="7. Je me sentais aimé(e). ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq08',
                text="8. Je pensais que mes parents n'avaient pas souhaité ma naissance",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq09',
                text="9. J'ai été frappé(e) si fort par un membre de ma famille que j'ai dû consulter un docteur ou aller à l'hôpital",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq10',
                text="10. Je n'aurais rien voulu changer à ma famille",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq11',
                text="11. Un membre de ma famille m'a frappé(e) si fort que j'ai eu des bleus ou des marques",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq12',
                text="12. J'étais puni(e) au moyen d'une ceinture, d'un bâton, d'une corde ou de quelque autre objet dur",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq13',
                text="13. Les membres de ma famille étaient attentifs les uns aux autres",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq14',
                text="14. Les membres de ma famille me disaient des choses blessantes ou insultantes. ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq15',
                text="15. Je pense que j'ai été physiquement maltraité(e). ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq16',
                text="16. J'ai eu une enfance parfaite",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq17',
                text="17. J'ai été frappé(e) ou battu(e) si fort que quelqu'un l'a remarqué (par ex. un professeur, un voisin ou un docteur). ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq18',
                text="18. J'avais le sentiment que quelqu'un dans ma famille me détestait",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq19',
                text="19. Les membres de ma famille se sentaient proches les uns des autres. ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq20',
                text="20. Quelqu'un a essayé de me faire des attouchements sexuels ou de m'en faire faire",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq21',
                text="21. Quelqu'un a menacé de me blesser ou de raconter des mensonges à mon sujet si je ne faisais pas quelque chose de nature sexuelle avec lui. ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq22',
                text="22. J'avais la meilleure famille du monde. ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq23',
                text="23. Quelqu'un a essayé de me faire faire des actes sexuels ou de me faire regarder de tels actes",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq24',
                text="24. J'ai été victime d'abus sexuels. ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq25',
                text="25. Je pense que j'ai été maltraité affectivement.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq26',
                text="26. Il y avait quelqu'un pour m'emmener chez le docteur si j'en avais besoin",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq27',
                text="27. Je pense qu'on a abusé de moi sexuellement",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ctq28',
                text="28. Ma famille était une source de force et de soutien",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CTQ",
            name="CTQ Questionnaire",
            description="28 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=14,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute CTQ score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

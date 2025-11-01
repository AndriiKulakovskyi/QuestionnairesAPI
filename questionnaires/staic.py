"""
STAIC - STAIC Questionnaire
===========================

40 items questionnaire

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


@register_questionnaire("STAIC")
@dataclass
class Staic(BaseQuestionnaire):
    """STAIC Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize STAIC questionnaire with all 40 items."""
        
        questions_list = [
            Question(
                id='staic01',
                text="1. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très calme", score=0),
                    AnswerOption(value='b', label="calme", score=1),
                    AnswerOption(value='c', label="pas du tout calme", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic02',
                text="2. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très bouleversé-e", score=0),
                    AnswerOption(value='b', label="bouleversé-e", score=1),
                    AnswerOption(value='c', label="pas bouleversé-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic03',
                text="3. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très aimable", score=0),
                    AnswerOption(value='b', label="aimable", score=1),
                    AnswerOption(value='c', label="pas aimable", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic04',
                text="4. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très nerveux-se", score=0),
                    AnswerOption(value='b', label="nerveux-se", score=1),
                    AnswerOption(value='c', label="pas nerveux-se", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic05',
                text="5. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très agité-e", score=0),
                    AnswerOption(value='b', label="agité-e", score=1),
                    AnswerOption(value='c', label="pas agité-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic06',
                text="6. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très reposé-e", score=0),
                    AnswerOption(value='b', label="reposé-e", score=1),
                    AnswerOption(value='c', label="pas reposé-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic07',
                text="7. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="beaucoup de peur", score=0),
                    AnswerOption(value='b', label="un peu de peur", score=1),
                    AnswerOption(value='c', label="pas de peur", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic08',
                text="8. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très détendu-e", score=0),
                    AnswerOption(value='b', label="détendu-e", score=1),
                    AnswerOption(value='c', label="pas détendu-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic09',
                text="9. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très inquiet-ète", score=0),
                    AnswerOption(value='b', label="inquiet-ète", score=1),
                    AnswerOption(value='c', label="pas inquiet-ète", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic10',
                text="10. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très satisfait-e", score=0),
                    AnswerOption(value='b', label="satisfait-e", score=1),
                    AnswerOption(value='c', label="pas satisfait-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic11',
                text="11. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très effrayé-e", score=0),
                    AnswerOption(value='b', label="effrayé-e", score=1),
                    AnswerOption(value='c', label="pas effrayé-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic12',
                text="12. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très heureux-se", score=0),
                    AnswerOption(value='b', label="heureux-se", score=1),
                    AnswerOption(value='c', label="pas heureux-se", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic13',
                text="13. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très sûr-e", score=0),
                    AnswerOption(value='b', label="sûr-e", score=1),
                    AnswerOption(value='c', label="pas sûr-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic14',
                text="14. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très bien", score=0),
                    AnswerOption(value='b', label="bien", score=1),
                    AnswerOption(value='c', label="pas bien", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic15',
                text="15. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très troublé-e", score=0),
                    AnswerOption(value='b', label="troublé-e", score=1),
                    AnswerOption(value='c', label="pas troublé-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic16',
                text="16. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très tracassé-e", score=0),
                    AnswerOption(value='b', label="tracassé-e", score=1),
                    AnswerOption(value='c', label="pas tracassé-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic17',
                text="17. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très gentil-le", score=0),
                    AnswerOption(value='b', label="gentil-le", score=1),
                    AnswerOption(value='c', label="pas gentil-le", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic18',
                text="18. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très terrifié-e", score=0),
                    AnswerOption(value='b', label="terrifié-e", score=1),
                    AnswerOption(value='c', label="pas terrifié-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic19',
                text="19. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très mêlé-e", score=0),
                    AnswerOption(value='b', label="mêlé-e", score=1),
                    AnswerOption(value='c', label="pas mêlé-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic20',
                text="20. Je me sens ...",
                options=[
                    AnswerOption(value='a', label="très enjoué-e", score=0),
                    AnswerOption(value='b', label="enjoué-e", score=1),
                    AnswerOption(value='c', label="pas enjoué-e", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic21',
                text="1. Je suis préoccupé-e par l'idée de faire des erreurs",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic22',
                text="2. J'ai envie de pleurer",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic23',
                text="3. Je me sens malheureux-se",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic24',
                text="4. J'ai de la difficulté à prendre des décisions",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic25',
                text="5. Il est difficile pour moi de faire face à mes problèmes",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic26',
                text="6. Je m'inquiète trop",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic27',
                text="7. Je deviens bouleversé-e quand je suis à la maison",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic28',
                text="8. Je suis gêné-e",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic29',
                text="9. Je me sens troublé-e ",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic30',
                text="10. Des idées sans importance me passent par la tête et me tracassent",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic31',
                text="11. Je m'inquiète à propos de l'école",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic32',
                text="12. J'ai de la difficulté à décider quoi faire",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic33',
                text="13. Je remarque que mon coeur bat vite",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic34',
                text="14. J'ai peur et je n'en parle à personne",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic35',
                text="15. Je m'inquiète pour mes parents",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic36',
                text="16. Mes mains sont moites (mouillées)",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic37',
                text="17. Je m'inquiète à propos de choses",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic38',
                text="18. J'ai de la difficulté à m'endormir le soir",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic39',
                text="19. J'ai une sensation bizarre dans mon estomac",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staic40',
                text="20. Je m'inquiète à propos de ce que les autres pensent de moi ",
                options=[
                    AnswerOption(value='a', label="Presque jamais", score=0),
                    AnswerOption(value='b', label="Quelquefois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="STAIC",
            name="STAIC Questionnaire",
            description="40 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=20,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute STAIC score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

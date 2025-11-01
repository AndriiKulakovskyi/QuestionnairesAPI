"""
ERD - ERD Questionnaire
=======================

13 items questionnaire

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


@register_questionnaire("ERD")
@dataclass
class Erd(BaseQuestionnaire):
    """ERD Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ERD questionnaire with all 13 items."""
        
        questions_list = [
            Question(
                id='erd10',
                text="10. Fatigabilité ",
                options=[
                    AnswerOption(value='a', label="La fatigue n'est ni spontanément signalée, ni retrouvée à l'interrogatoire.", score=0),
                    AnswerOption(value='b', label="La fatigue n'est pas signalée spontanément mais peut être mise en évidence par l'interrogatoire.", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd11',
                text="11. Intérêt pour les activités habituelles ",
                options=[
                    AnswerOption(value='a', label="Le malade garde, malgré l'hospitalisation, ses intérêts habituels.", score=0),
                    AnswerOption(value='b', label="Le malade met la diminution d'un certain nombre de tâches pour lesquelles il avait de l'intérêt sur le compte de l'hospitalisation ou tout autre prétexte.", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd12',
                text="12. Perception par le malade de l'écoulement du temps présent  ",
                options=[
                    AnswerOption(value='a', label="Identique au vécu habituel.", score=0),
                    AnswerOption(value='b', label="Le temps présent passe lentement mais ceci tient à l'inactivité, l'hospitalisation...", score=1),
                    AnswerOption(value='c', label="Un écoulement plus lent du temps perçu existe mais n'est retrouvé que par un interrogatoire                précis.", score=2),
                    AnswerOption(value='d', label="Le malade signale spontanément ou facilement un écoulement ralenti du temps présent en réponse à une question directe.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd13',
                text="13. Mémoire ",
                options=[
                    AnswerOption(value='a', label="Le sujet affirme ne présenter aucun trouble mnésique, l'expérimentateur n'en retrouve pas à l'interrogatoire.", score=0),
                    AnswerOption(value='b', label="Une difficulté mnésique est évoquée par le malade mais difficile à objectiver.", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd14',
                text="14. Concentration ",
                options=[
                    AnswerOption(value='a', label="Faculté de concentration normale.", score=0),
                    AnswerOption(value='b', label="Le malade pense pouvoir se concentrer normalement, mais certaines tâches demandant un effort de concentration, semblent difficiles à réaliser.", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd15',
                text="Appréciation générale du ralentissement ",
                options=[
                    AnswerOption(value='a', label="Nul.", score=0),
                    AnswerOption(value='b', label="Doute.", score=1),
                    AnswerOption(value='c', label="Net.", score=2),
                    AnswerOption(value='d', label="Important.", score=3),
                    AnswerOption(value='e', label="Très grave.", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd2',
                text="2. Lenteur et rareté des mouvements : TRONC ",
                options=[
                    AnswerOption(value='a', label="Mouvements adaptés, normaux en amplitude, souplesse et rythme, le tronc est confortablement calé dans le fauteuil, les épaules dégagées.Attitude et mouvements sont en harmonie avec le discours", score=0),
                    AnswerOption(value='b', label="Il existe peut-être un léger \\", score=1),
                    AnswerOption(value='c', label="Un certain figeage est indiscutable", score=2),
                    AnswerOption(value='d', label="Ne mobilise que rarement ses membres, avec lenteur, d'un geste gauche et de faible amplitude ou encore les racines sont figées et seules les mains bougent. Tronc immobile, soit plaqué contre le dossier, soit les épaules tombantes", score=3),
                    AnswerOption(value='e', label="Refus de se lever du lit ou complètement figé dans le fauteuil. Aucun mouvement du tronc, aucune mobilité tête-tronc.", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd3',
                text="3. Lenteur et rareté des mouvements de la tête et du cou : MIMIQUE ",
                options=[
                    AnswerOption(value='a', label="La tête est mobile, son port est souple, le regard explore la pièce et fixe alternativement I'examinateur et d'autres centres d'intérêt de façon adaptée. Les mouvements de la bouche sont d'amplitude normale. ", score=0),
                    AnswerOption(value='b', label="Il existe peut-être une réduction de mobilité, difficile à affirmer.                                                     ", score=1),
                    AnswerOption(value='c', label="La réduction de la mobilité est indiscutable mais légère. Le regard souvent fixe est encore capable de mobilité, la mimique encore expressive est monotone.                                                                ", score=2),
                    AnswerOption(value='d', label="Le malade ne bouge pas la tête. Il n'explore pas la pièce, a le regard fixe le plus souvent vers le bas et regarde rarement l'examinateur. Il articule mal, ses lèvres sont peu mobiles, il ne sourit jamais, la mimique est figée. ", score=3),
                    AnswerOption(value='e', label="Faciès entièrement figé et douloureusement inexpressif.", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd4',
                text="4. Langage et DEBIT verbal ",
                options=[
                    AnswerOption(value='a', label="Débit supposé normal.", score=0),
                    AnswerOption(value='b', label="Ralentissement du langage à peine perceptible.", score=1),
                    AnswerOption(value='c', label="Ralentissement net mais gênant à peine la conversation.", score=2),
                    AnswerOption(value='d', label="Le sujet ne parle que s'il y est fortement incité.", score=3),
                    AnswerOption(value='e', label="Réponses stéréotypées.", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd6',
                text="6. Réponses brèves ",
                options=[
                    AnswerOption(value='a', label="Le sujet n'a pas de difficulté à faire des réponses d'une longueur adaptée.", score=0),
                    AnswerOption(value='b', label="Réponses semblant un peu brèves.", score=1),
                    AnswerOption(value='c', label="Réponses brèves mais ne gênant pas le cours de la conversation.", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd7',
                text="7. Variété des thèmes spontanément abordés : INITIATIVE IDEIQUE ",
                options=[
                    AnswerOption(value='a', label="Association d'idées facile. Thématique riche et variée.", score=0),
                    AnswerOption(value='b', label="Thèmes relativement riches et variés mais le patient a peut-être des difficultés à passer vite d'une idée à une autre.", score=1),
                    AnswerOption(value='c', label="Les thèmes nouveaux spontanément abordés sont rares et pauvres.", score=2),
                    AnswerOption(value='d', label="Les thèmes nouveaux sont absents spontanément, tendance à la rumination mentale.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd8',
                text="8. FLUIDITE idéique ",
                options=[
                    AnswerOption(value='a', label="Association d'idées facile.", score=0),
                    AnswerOption(value='b', label="Thèmes relativement riches et variés mais le patient a peut-être des difficultés à passer d'une idée à une autre.", score=1),
                    AnswerOption(value='c', label="Les thèmes nouveaux sont rares, peu variés.", score=2),
                    AnswerOption(value='d', label="Les thèmes nouveaux sont absents spontanément. Tendance à la rumination mentale.", score=3),
                    AnswerOption(value='e', label="Aucune élaboration, discours très pauvre.", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='erd9',
                text="9. Expérience subjective de rumination mentale ",
                options=[
                    AnswerOption(value='a', label="Sentiment qu'a le patient de penser librement sans gêne, comme auparavant.", score=0),
                    AnswerOption(value='b', label="Doute entre 0 et 2.", score=1),
                    AnswerOption(value='c', label="Impression du patient que ses pensées sont focalisées sur un à trois thèmes revenant sans cesse, gênant la vie courante envahissant son monde intérieur.", score=2),
                    AnswerOption(value='d', label="Le patient a le sentiment que ses pensées spontanées tendent à le ramener toujours à une seule et unique préoccupation douloureuse.", score=3),
                    AnswerOption(value='e', label="Le patient éprouve une incapacité totale à se dégager de sa rumination douloureuse.", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ERD",
            name="ERD Questionnaire",
            description="13 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ERD score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

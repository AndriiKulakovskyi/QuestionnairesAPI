"""
AUT_DUNN - AUT_DUNN Questionnaire
=================================

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


@register_questionnaire("AUT_DUNN")
@dataclass
class AutDunn(BaseQuestionnaire):
    """AUT_DUNN Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_DUNN questionnaire with all 31 items."""
        
        questions_list = [
            Question(
                id='completby',
                text="Complété par ",
                options=[
                    AnswerOption(value='a', label="Père", score=0),
                    AnswerOption(value='b', label="Mère", score=1),
                    AnswerOption(value='c', label="Autre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn10',
                text="10. Se limite à certaines textures ou certaines températures de nourriture ",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn11',
                text="11. Est difficile à satisfaire, particulièrement en ce qui concerne la texture des aliments",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn12',
                text="12. Devient anxieux ou se montre inquiet quand ses pieds quittent le sol",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn13',
                text="13. A peur de tomber ou a le vertige",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn15',
                text="15. Aime les bruits étranges / cherche à faire du bruit par plaisir.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn17',
                text="17. Devient trop excitable durant des activités impliquant du mouvement ",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn18',
                text="18. Touche les gens ou les objets",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn19',
                text="19.Ne semble pas remarquer quand son visage ou ses mains sont sales.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn2',
                text="2. Préfère porter des vêtements à manches longues quand il fait chaud ou à manches courtes quand il fait froid.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn20',
                text="20. Passe d'une activité à une autre, ce qui interfère avec son jeu.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn21',
                text="21. Laisse ses vêtements entortillés autour de son corps",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn22',
                text="22. Est troublé ou a du mal à fonctionner s'il y a beaucoup de bruit autour de lui.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn23',
                text="23. Semble ne pas entendre ce que vous dites (par ex. semble vous ignorer)..",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn25',
                text="25. A du mal à terminer des tâches quand la radio est allumée.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn26',
                text="26. Ne répond pas quand on l'appelle par son nom bien que son audition soit bonne",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn27',
                text="27. A des difficultés à fixer son attention",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn28',
                text="28. Semble avoir une faiblesse musculaire.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn29',
                text="29. Se fatigue facilement surtout quand il est debout ou quand il se tient dans une position particulière.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn3',
                text="3. Evite de marcher pieds nus, surtout dans le sable ou dans l’herbes",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn33',
                text="33. A une endurance limitées / se fatigue facilement.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn35',
                text="35. Se met les mains sur les oreilles pour se protéger du bruit.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn36',
                text="36. Est dérangé par des lumières fortes alors que les autres s'y sont adaptés.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn37',
                text="37. Observe toute personne qui se déplace dans la pièce.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn38',
                text="38. Se couvre ou plisse les yeux pour se protéger de la lumière",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn4',
                text="4. Réagit avec émotion ou de manière agressive lorsqu’on le touche",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn5',
                text="5. Evite les éclaboussures d'eau",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn6',
                text="6. A des difficultés à rester dans une file d’attente ou près des autres",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn7',
                text="7. Se frotte ou se gratte à l'endroit où il vient d’être touché.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn8',
                text="8. Evite certains goûts ou certaines odeurs de nourriture faisant typiquement partie des aliments pour enfants.",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dunn9',
                text="9. Ne mange que des aliments d'une certaine saveur",
                options=[
                    AnswerOption(value='a', label="Toujours", score=0),
                    AnswerOption(value='b', label="Fréquemment", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Rarement", score=3),
                    AnswerOption(value='e', label="Jamais", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_DUNN",
            name="AUT_DUNN Questionnaire",
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
        """Compute AUT_DUNN score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

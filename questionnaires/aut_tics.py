"""
AUT_TICS - AUT_TICS Questionnaire
=================================

47 items questionnaire

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


@register_questionnaire("AUT_TICS")
@dataclass
class AutTics(BaseQuestionnaire):
    """AUT_TICS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_TICS questionnaire with all 47 items."""
        
        questions_list = [
            Question(
                id='tic1',
                text="1. Cligner des yeux, loucher, mouvements rapides des yeux, rouler les yeux d’un côté, ou ouvrir les yeux largement très brièvement.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic10',
                text="10. Se passer la main dans les cheveux comme si on se peignait à la mode, ou toucher des objets ou les autres, se pincer, ou compter sur les doigts sans raison, ou avoir des tics d’écriture comme écrire plusieurs fois la même lettre ou le même mot, ou appuyer fortement sur son stylo en écrivant.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic11',
                text="11. Taper, sauter, se mettre à genoux, fléchir ou étendre une articulation ; secouer ou taper avec la pointe du pied ou avec le talon.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic12',
                text="12. Faire un pas puis reculer de deux pas, s’accroupir ou faire une flexion prononcée des genoux.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic13',
                text="13. Contracter l’'abdomen, contracter les fesses.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic14',
                text="14.Autres tics moteurs simple.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic15',
                text="15. Tics liés à des comportements compulsifs (toucher, taper, ramasser…)",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic16',
                text="16. Tics dépendant du stimulus.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic17',
                text="17. Gestes du doigt, de la main obscènes / impolis.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic18',
                text="18. Position inhabituelle.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic19',
                text="19. Se pencher sur soi-même.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic2',
                text="2. Faire des gestes des yeux, comme sembler surpris ou étonné, ou regarder brièvement d’un côté comme si on avait entendu un bruit.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic20',
                text="20. Tourner sur soi-même.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic21',
                text="21. Comportements soudains et impulsifs.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic22',
                text="22. Comportements qui peuvent blesser/mutiler les autres.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic23',
                text="23. Comportements automutilateurs.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic24',
                text="24. Autres types ou séquences de tics moteurs.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic25',
                text="25. Toux",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic26',
                text="26. S’éclaircir la voix",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic27',
                text="27. Renifler",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic28',
                text="28. Siffler",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic29',
                text="29. Faire des bruits d’oiseaux",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic3',
                text="3. Se mordre la langue, mâcher la lèvre, ou se lécher la lèvre, grincer des dents.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic30',
                text="30. Autres tics vocaux simples.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic31',
                text="31. Syllabes",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic32',
                text="32. Mots ou phrases impolis ou obscènes.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic33',
                text="33. Mots.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic36',
                text="36. Autres problèmes d’expression.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic37',
                text="37. Autres types ou séquences de tics vocaux ",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic4',
                text="4. Ecarter les narines comme si on sentait quelque chose, sourire, ou d’autres gestes impliquant la bouche, avoir des expressions bizarres ou tirer la langue.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic5',
                text="5. Toucher son épaule avec le menton ou tirer le menton vers le haut.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic6',
                text="6. Jeter la tête en arrière, comme si on avait des cheveux devant les yeux.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic7',
                text="7. Sursauts des épaules.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic8',
                text="8. Hausser les épaules comme pour dire ‘je ne sais pas’.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tic9',
                text="9. Fléchir ou étendre rapidement les bras, se mordre les ongles, tirer ses doigts en arrière, faire craquer les articulations.",
                options=[
                    AnswerOption(value='a', label="Jamais eu", score=0),
                    AnswerOption(value='b', label="Déjà eu", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticcons',
                text="Pendant la semaine dernière, est ce que vous avez eu une série de tics survenant en même temps ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticmul',
                text="Pendant la semaine dernière, est ce que vous avez eu des tics multiples distincts survenant en même temps ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticsem3',
                text="3. Pendant la semaine dernière, quelle était l’intensité de vos tics MOTEURS ?",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Intensité minimale", score=1),
                    AnswerOption(value='c', label="Intensité légère", score=2),
                    AnswerOption(value='d', label="Intensité modérée", score=3),
                    AnswerOption(value='e', label="Intensité marquée", score=4),
                    AnswerOption(value='f', label="Intensité sévère", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticsem4',
                text="4. Pendant la semaine dernière, quelle était l’intensité de vos tics VOCAUX ?",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Intensité minimale", score=1),
                    AnswerOption(value='c', label="Intensité légère", score=2),
                    AnswerOption(value='d', label="Intensité modérée", score=3),
                    AnswerOption(value='e', label="Intensité marquée", score=4),
                    AnswerOption(value='f', label="Intensité sévère", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticsem5_m',
                text="TICS MOTEURS",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Interrompt occasionnellement", score=1),
                    AnswerOption(value='c', label="Interrompt fréquemment", score=2),
                    AnswerOption(value='d', label="Perturbe occasionnellement", score=3),
                    AnswerOption(value='e', label="Perturbe fréquemment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticsem5_v',
                text="TICS VOCAUX",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Interrompt occasionnellement", score=1),
                    AnswerOption(value='c', label="Interrompt fréquemment", score=2),
                    AnswerOption(value='d', label="Perturbe occasionnellement", score=3),
                    AnswerOption(value='e', label="Perturbe fréquemment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticvie3',
                text="3. Pendant la période de tics la plus grave de toute votre vie, quelle était l’intensité de vos tics MOTEURS ?",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Intensité minimale", score=1),
                    AnswerOption(value='c', label="Intensité légère", score=2),
                    AnswerOption(value='d', label="Intensité modérée", score=3),
                    AnswerOption(value='e', label="Intensité marquée", score=4),
                    AnswerOption(value='f', label="Intensité sévère", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticvie4',
                text="4. Pendant la période de tics le plus grave de toute votre vie, quelle était l’intensité de vos tics VOCAUX ?",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Intensité minimale", score=1),
                    AnswerOption(value='c', label="Intensité légère", score=2),
                    AnswerOption(value='d', label="Intensité modérée", score=3),
                    AnswerOption(value='e', label="Intensité marquée", score=4),
                    AnswerOption(value='f', label="Intensité sévère", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticvie5_m',
                text="TICS MOTEURS",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Interrompt occasionnellement", score=1),
                    AnswerOption(value='c', label="Interrompt fréquemment", score=2),
                    AnswerOption(value='d', label="Perturbe occasionnellement", score=3),
                    AnswerOption(value='e', label="Perturbe fréquemment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ticvie5_v',
                text="TICS VOCAUX",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Interrompt occasionnellement", score=1),
                    AnswerOption(value='c', label="Interrompt fréquemment", score=2),
                    AnswerOption(value='d', label="Perturbe occasionnellement", score=3),
                    AnswerOption(value='e', label="Perturbe fréquemment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tourdiag',
                text="Est-ce que vous concernant, on a évoqué le diagnostic de Gilles de la Tourette ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tourtt',
                text="Est-ce que vous avez déjà reçu un traitement médicamenteux pour les tics et/ou le syndrome de Gilles de la Tourette ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_TICS",
            name="AUT_TICS Questionnaire",
            description="47 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=23,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_TICS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

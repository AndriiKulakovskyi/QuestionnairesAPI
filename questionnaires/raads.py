"""
RAADS - RAADS Questionnaire
===========================

80 items questionnaire

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


@register_questionnaire("RAADS")
@dataclass
class Raads(BaseQuestionnaire):
    """RAADS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize RAADS questionnaire with all 80 items."""
        
        questions_list = [
            Question(
                id='raads01',
                text="1. Je suis une personne compatissante",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads02',
                text="2. J'utilise souvent des mots et des phrases entendus dans des films ou à la télévision dans les conversations",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads03',
                text="3. Je suis souvent surpris lorsque les autres me disent que j'ai été impoli. ",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads04',
                text="4. Parfois je parle trop fort ou trop doucement, et je ne m'en aperçois pas. ",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads05',
                text="5. J'ai souvent des difficultés à savoir comment me comporter en société.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads06',
                text="6. Je peux « me mettre dans la peau de quelqu'un d'autre ».",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads07',
                text="7. J'ai du mal à comprendre le sens de certaines phrases comme « je tiens à toi comme à la prunelle de mes yeux ».",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads08',
                text="8. J'aime seulement parler aux gens qui partagent mes centres d'intérêts.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads09',
                text="9. Je fais plus attention aux détails qu'à l'idée générale.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads10',
                text="10. Je suis sensible à l'effet produit par un aliment d ans ma bouche.Ceci est plus important que son goût",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads11',
                text="11. Mes meilleurs amis ou ma famille me manquent quand nous sommes séparés depuis longtemps.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads12',
                text="12. Quelquefois je vexe les autres en disant ce que je pense, sans le faire exprès.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads13',
                text="13. J'aime seulement penser et parler des choses qui m'intéressent",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads14',
                text="14. Je préfère aller manger dans un restaurant tout seul plutôt qu'avec quelqu'un que je connais",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads15',
                text="15. Je n'arrive pas à imaginer comment ce serait d'être quelqu'un d'autre",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads16',
                text="16. On m'a déjà dit que j'étais maladroit ou que je manquais de coordination",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads17',
                text="17. Les autres me trouvent étrange ou différent",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads18',
                text="18. Je comprends lorsque des amis ont besoin d'être réconfortés",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads19',
                text="19. Je suis très sensible au contact de mes vêtementsorsquel je les touche. Leur texture est plus importante pour moi que leur look",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads20',
                text="20. J'aime copier la manière dont certaines personnes parlent et agissent. Cela m'aide à me sentir plus « normal ». ",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads21',
                text="21. Cela peut être très intimidant pour moi de parler à plus d'une personne en même temps.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads22',
                text="22. Je dois adopter un comportement « normal » pour plaire aux autres et pour qu'ils m'apprécient",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads23',
                text="23. Rencontrer de nouvelles personnes est habituellement facile pour moi.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads24',
                text="24. Je suis déstabilisé lorsque quelqu'un m'interromptalors que je parle de quelque chose qui m'intéresse beaucoup",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads25',
                text="25. Il m'est difficile de percevoir les sentiments des autres lors d'une conversation",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads26',
                text="26. J'aime avoir une conversation avec plusieurs personnes, par exemple lors d'un dîner, à l'école, ou au travail",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads27',
                text="27. Je prends les choses trop au premier degré, ainsi je passe à côté de ce que les gens essaient de dire",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads28',
                text="28. C'est très difficile pour moi de comprendre lorsque quelqu'un est gêné ou jaloux",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads29',
                text="29. Certaines textures ordinaires qui ne posent aucun problème aux autres sont pour moi insupportables lorsqu'elles sont au contact de ma peau.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads30',
                text="30. Je suis très contrarié lorsqu'on m'empêche de faire les choses à ma façon",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads31',
                text="31. Je n'ai jamais désiré ou eu besoin de ce que les autres personnes appellent une « relation intime ».",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads32',
                text="32. C'est difficile pour moi de commencer et d'arrêter une conversation. J'ai besoin d'aller jusqu'au bout de mon propos",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads33',
                text="33. Je parle avec un rythme de voix normal",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads34',
                text="34. Je peux sans transition être très sensible ou pas du tout sensible au même son, à la même couleur ou à la même texture",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads35',
                text="35. La phrase « je t'ai dans la peau » me met mal à l'aise",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads36',
                text="36. Quelquefois la sonorité d'un mot ou un bruit aigu peut me faire mal aux oreilles",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads37',
                text="37. On me considère comme une personne très compréhensive",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads38',
                text="38. Je ne peux pas m'identifier à un personnage dans un film, et je ne peux pas ressentir ce qu'il ressent.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads39',
                text="39. Je ne peux pas dire si quelqu'un est en train de me draguer",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads40',
                text="40. Je peux me représenter avec précision les détails qui m'intéressent.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads41',
                text="41. Je fais des listes de choses qui m'intéressent, même si elles n'ont pas d'utilité pratique (par exemple statistiques sportives, horaires de train, dates du calendrier, faits historiques et dates).\n	",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads42',
                text="42. Quand je me sens dépassé par des stimulations sensorielles, je dois m'isoler pour y échapper",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads43',
                text="43. J'aime parler de choses et d'autres avec mes amis",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads44',
                text="44. Je ne peux pas dire si quelqu'un est intéressé ou ennuyé par ce que je dis",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads45',
                text="45. Lorsque quelqu'un est en train de parler, il peut m'être très difficile de lire sur son visage, de comprendre les mouvements de ses mains ou de son corps",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads46',
                text="46. Je peux ressentir à différents moments la même chose très différemment (comme des vêtements ou la température).",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads47',
                text="47. Je me sens très à l'aise lors d'un rendez vous amoureux ou lorsque je me trouve en société.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads48',
                text="48. J'essaie d'être aussi aidant que possible lorsque les autres me parlent de leurs problèmes personnels.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads49',
                text="49. On m'a dit que j'avais une voix particulière (par exemple, plate, monotone, enfantine ou aigue).",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads50',
                text="50. Quelquefois une idée ou un sujet reste bloqué dans mon esprit et je dois en parler, même si cela n'intéresse personne",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads51',
                text="51. Je fais certaines choses avec mes mains de façon répétée (comme un battement d'ailes, faire tournoyer un bâton ou une ficelle, agiter des choses devant mes yeux).\n	",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads52',
                text="52. Je n'ai jamais été intéressé par ce que la plupart des gens que je connais considèrent comme intéressant",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads53',
                text="53. On me considère comme une personne compatissante",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads54',
                text="54. Pour m'entendre avec les autres, je suis un ensemble de règles spécifiques qui m'aide à paraître normale",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads55',
                text="55. C'est très difficile pour moi de travailler et d'évoluer dans un groupe",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads56',
                text="56. Lorsque je parle à quelqu'un, il m'est difficile de changer de sujet. Si l'autre personne le fait, je peux être bouleversé et confus.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads57',
                text="57. Quelquefois je dois couvrir mes oreilles pour  arrêter des bruits douloureux (comme un aspirateur ou des gens qui parlent de trop ou trop fort).",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads58',
                text="58. Je peux discuter et avoir des conversations superficielles",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads59',
                text="59. Quelquefois des choses qui devraient être douloureuses ne me font pas mal (par exemple, lorsque je me blesse ou lorsque je me brûle la main sur un poêle).\n	",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads60',
                text="60. Quand je parle à quelqu'un, j'ai des difficultés à savoir si c'est à mon tour de parler ou d'écouter",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads61',
                text="61. Je suis considéré comme un solitaire par ceux qui me connaissent le mieux",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads62',
                text="62. Je parle habituellement avec un ton de voix normal",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads63',
                text="63. J'aime que les choses se déroulent toujours de la même manière jour après jour, et même les petits changements dans mes routines me perturbent",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads64',
                text="64. Comment se faire des amis et s'intégrer socialement est un mystère pour moi",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads65',
                text="65. Cela me calme de tourner en rond ou de me balancer sur une chaise lorsque je me sens stressé",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads66',
                text="66. La phrase « il a le coeur sur la main » n'a pas de sens pour moi",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads67',
                text="67. Si je suis dans un endroit où il y a beaucoup d'odeurs, de matières à toucher, de bruits ou de lumières intenses, je me sens anxieux ou effrayé",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads68',
                text="68. Je sais faire la différence lorsque quelqu'un dit une chose mais veut en dire une autre",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads69',
                text="69. J'aime être seul autant que possible",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads70',
                text="70. Je garde mes pensées empilées dans ma mémoire comme dans un classeur, et je prends celles dont j'ai besoin en sélectionnant dans la pile (ou par une méthode similaire).\n	",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads71',
                text="71. Le même son peut paraître quelquefois très fort ou très doux alors que je sais qu'il n'a pas changé.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads72',
                text="72. J'aime passer du temps à manger et parler avec ma famille et mes amis",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads73',
                text="73. Je ne supporte pas les choses que je n'aime pas (comme des odeurs, des matières, des sons ou des couleurs).",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads74',
                text="74. Je n'aime pas être tenu ou étreint",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads75',
                text="75. Lorsque je vais quelque part, je dois suivre un parcours familier sinon je peux devenir très confus et perturbé",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads76',
                text="76. C'est difficile de comprendre ce que les autres personnes attendent de moi",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads77',
                text="77. J'aime avoir des amis proches.",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads78',
                text="78. On me dit que je donne trop de détails",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads79',
                text="79. On me dit souvent que je pose des questions embarrassantes",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='raads80',
                text="80. J'ai tendance à souligner les erreurs des autres",
                options=[
                    AnswerOption(value='a', label="Vrai maintenant et quand j'avais moins de 16 ans", score=0),
                    AnswerOption(value='b', label="Vrai seulement maintenant", score=1),
                    AnswerOption(value='c', label="Vrai seulement quand j'avais moins de 16 ans", score=2),
                    AnswerOption(value='d', label="Jamais vrai", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="RAADS",
            name="RAADS Questionnaire",
            description="80 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=40,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute RAADS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

"""
AUT_SYSTE - AUT_SYSTE Questionnaire
===================================

56 items questionnaire

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


@register_questionnaire("AUT_SYSTE")
@dataclass
class AutSyste(BaseQuestionnaire):
    """AUT_SYSTE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_SYSTE questionnaire with all 56 items."""
        
        questions_list = [
            Question(
                id='syste1',
                text="1. Quand j'écoute un morceau de musique, je reconnais toujours sa structure",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste10',
                text="10. Je suis curieux d’apprendre des choses sur les différentes religions",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste11',
                text="11. Je lis rarement des articles ou des pages internet qui concernent les nouvelles technologies",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste12',
                text="12. Je n'aime pas les jeux qui nécessitent beaucoup de stratégie",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste14',
                text="14. Je me fais un devoir d’écouter les nouvelles chaque matin",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste15',
                text="15. En mathématiques, je suis intrigué par les règles et les théories régissant les nombres",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste16',
                text="16. J’ai du mal à garder contact avec de vieux amis",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste17',
                text="17. Quand je raconte une histoire, j'omets souvent les détails et je raconte juste l'essentiel de ce qui s'est passé",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste18',
                text="18. Je comprends difficilement les notices d’instructions qui permettent d’assembler des éléments d’un appareil",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste19',
                text="19. Quand je vois un animal, j’aime savoir à quelle espèce précise il appartient",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste2',
                text="2. Je suis superstitieux",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste20',
                text="20. Si j’achetais un ordinateur, j’aimerais connaître des détails précis sur les capacités de son disque dur et de son processeur",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste21',
                text="21. J’aime prendre part à des activités sportives",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste22',
                text="22. Si je peux, j'essaie d’éviter de faire le ménage",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste23',
                text="23. Quand je cuisine, je ne réfléchis pas à la façon dont les ingrédients ou les différentes façons de faire contribuent au résultat final",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste24',
                text="24. Je trouve difficile de lire et de comprendre des cartes géographiques",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste26',
                text="26. Quand je regarde un meuble, je ne prête pas attention aux détails de sa fabrication",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste27',
                text="27. L’idée de m’adonner à des activités à risque me séduit",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste28',
                text="28. Quand j’apprends des choses à propos d’événements historiques, je ne me concentre pas sur les dates exactes",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste29',
                text="29. Quand je lis le journal je suis attiré par certaines rubriques, telles que les résultats du championnat de football ou les indices du marché boursier",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste3',
                text="3. Je prends souvent des résolutions, mais trouve difficile de m’y tenir",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste30',
                text="30. Quand j’apprends une langue, je m’intéresse aux règles grammaticales",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste31',
                text="31. Je trouve difficile d’apprendre à me repérer dans une ville nouvelle",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste32',
                text="32. Je n’aime pas particulièrement regarder des documentaires scientifiques à la TV, ni lire des articles scientifiques ou des articles sur la nature",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste33',
                text="33. Si j’achetais une chaîne stéréo, j’aimerais connaître ses caractéristiques techniques précises",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste34',
                text="34. Je trouve facile de comprendre exactement les règles de probabilité dans un pari",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste35',
                text="35. Je ne suis pas très méticuleux quand je fais du bricolage",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste36',
                text="36. Il est facile d’avoir une conversation avec une personne que je viens tout juste de rencontrer",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste37',
                text="37. Quand je regarde un bâtiment, je suis curieux de savoir comment il a été précisément construit",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste38',
                text="38. Quand il y a une élection, je ne m’intéresse pas aux scores de chaque parti",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste39',
                text="39. Quand je prête de l’argent à quelqu’un, je compte sur le fait que la personne me rembourse exactement ce qu'elle me doit",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste40',
                text="40. Je comprends difficilement les informations que m’envoie la banque sur les différents investissements et plans d’épargne",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste41',
                text="41. Quand je voyage en train, je me demande souvent comment le réseau ferroviaire est organisé",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste42',
                text="42. Quand j'achète un nouvel appareil, je ne lis pas minutieusement le manuel d'instruction",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste43',
                text="43. Si j’achetais un appareil photo, je ne regarderais pas avec attention la qualité de l’objectif",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste44',
                text="44. Quand je lis quelque chose, je vérifie toujours si c’est grammaticalement correct",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste45',
                text="45. Quand j'entends la météo, je ne suis pas très intéressé par les modèles météorologiques",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste46',
                text="46. Je me demande souvent comment ce serait d’être quelqu’un d’autre",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste47',
                text="47. Je trouve difficile de faire deux choses à la fois",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste48',
                text="48. Quand je regarde une montagne, je me demande précisément comment elle s’est formée ",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste49',
                text="49. J’arrive facilement à visualiser comment sont reliées les autoroutes de ma région",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste5',
                text="5. Si je devais acheter une voiture, j’aimerais avoir des informations précises sur les capacités du moteur",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste50',
                text="50. Quand je suis au restaurant, je mets souvent du temps à décider ce que je vais commander",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste51',
                text="51. Quand je suis dans un avion, je ne pense pas à l'aérodynamisme",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste52',
                text="52. J’oublie souvent les détails des conversations que j’ai eues",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste54',
                text="54. Si j’ai rencontré une personne une ou deux fois, je me souviens difficilement ce à quoi elle ressemble précisément",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste55',
                text="55. J’aime connaître le chemin que suit une rivière de sa source à la mer",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste56',
                text="56. Je ne lis pas très attentivement les documents juridiques",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste57',
                text="57. Je ne me demande pas comment fonctionne la communication sans fil",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste58',
                text="58. Je m’intéresse à la vie sur les autres planètes",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste59',
                text="59. Quand je voyage, j'aime connaître des détails précis concernant la culture du pays que je visite",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste6',
                text="6. En règle générale, quand j’observe un tableau, je ne réfléchis pas aux techniques utilisées pour le faire",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste60',
                text="60. Ça m’est égal de connaître les noms des plantes que je vois",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste7',
                text="7. S'il y avait un problème avec le réseau électrique chez moi, je pourrais le réparer moi-même",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste8',
                text="8. Quand je fais un rêve, je trouve difficile de me souvenir des détails précis le lendemain",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='syste9',
                text="9. Quand je regarde un film je préfère être avec un groupe d’amis plutôt que seul",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_SYSTE",
            name="AUT_SYSTE Questionnaire",
            description="56 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=28,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_SYSTE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

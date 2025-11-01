"""
GSS - GSS Questionnaire
=======================

42 items questionnaire

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


@register_questionnaire("GSS")
@dataclass
class Gss(BaseQuestionnaire):
    """GSS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize GSS questionnaire with all 42 items."""
        
        questions_list = [
            Question(
                id='gss01',
                text="1. Trouvez-vous désagréable la sensation physique que vous ressentez lorsque quelqu'un vous serre dans ses bras ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss02',
                text="2. Avez-vous des haut-le-coeur lorsque vous mangez des aliments particuliers, vous donnant peut-être la même impression que si vous alliez être malade ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss03',
                text="3. Trouvez-vous difficile de bien maitriser vos mains lorsque vous effectuez une tâche délicate (par exemple, lorsque vous ramassez des petits objets ou que vous transférez des objets d'une main à l'autre) ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss04',
                text="4. Vous arrive-il d'explorer la surface d'un objet avec vos mains avant de le saisir ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss05',
                text="5. Lorsque vous parlez à quelqu'un, avez-vous tendance à vous tenir à des distances atypiques, que ce soit très près (par exemple, moins d'1 mètre) ou très loin (par exemple, plus de 3 mètres) de cette personne? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss06',
                text="6. Trouvez-vous certains bruits/hauteurs de sons agaçant/irritant ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss07',
                text="7. Humez-vous l'odeur des aliments avant de les manger ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss08',
                text="8. Vous arrive-t-il d'avoir mal aux yeux / d'avoir des maux de tête à cause de lumières vives? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss09',
                text="9. Aimez-vous écouter en boucle le même morceau de musique / la même séquence d'un DVD ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss10',
                text="10. Vous-sentez-vous mal / pris de vertiges / bizarre si vous devez tendre les bras en hauteur ou vous baisser pour prendre quelque chose ?",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss11',
                text="11. Vous est-il déjà arrivé d'être fasciné par des petites particules (par exemple, des petits morceaux de poussière dans l'air) ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss12',
                text="12. Aimez-vous tourner sur vous-même encore et encore ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss13',
                text="13. Vous arrive-t-il de vous sentir mal simplement en sentant une odeur particulière ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss14',
                text="14. Trouvez-vous difficile d'entendre ce que les gens disent ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss15',
                text="15. Trouvez-vous désagréable de vous faire couper les cheveux (par exemple, parce que des bouts de cheveux tombent dans votre dos) ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss16',
                text="16. Vous arrive-t-il de remarquer que vous vous êtes fait mal alors que vous n'avez pas senti de douleur ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss17',
                text="17. Vous a-t-on déjà dit que vous mettiez trop de parfum / d'après-rasage ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss18',
                text="18. Vous arrive-t-il d'avoir l'impression que les lumières clignotent rapidement lorsque vous les regardez ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss19',
                text="19. Aimez-vous aligner les objets ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss20',
                text="20. Est-ce que vous vous balancez d'avant en arrière ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss21',
                text="21. Trouvez-vous difficile d'entrer dans un magasin où l'odeur est forte (par exemple, dans un magasin de parfum comme « Séphora » ou « Marionnaud ») ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss22',
                text="22. Coupez-vous les étiquettes de vos vêtements ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss23',
                text="23. Détestez-vous la sensation ou la texture de certains aliments dans votre bouche ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss24',
                text="24. Est-ce que vous évitez d'aller au restaurant à cause des odeurs particulières que vous pouvez y sentir ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss25',
                text="25. Est-ce que les bruits forts vous dérangent ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss26',
                text="26. Goûtez-vous les aliments du bout de votre langue avant de les manger ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss27',
                text="27. Vous arrive-t-il d'avoir le corps engourdi, comme si vous ne pouviez plus rien ressentir au contact de votre peau ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss28',
                text="28. Pensez-vous avoir un mauvais sens du goût? Un exemple de cela serait si la plupart des aliments n'a aucun goût pour vous. ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss29',
                text="29. Pensez-vous ne pas être conscient des signaux envoyés par votre corps (par exemple, si vous ne sentez pas souvent des sensations de faim / fatigue / soif) ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss30',
                text="30. Vous arrive-t-il de vous sentir mal/pris de vertiges lorsque vous jouez à des jeux au rythme soutenu, comme par exemple le basketball ou le football ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss31',
                text="31. Réagissez-vous très fortement lorsque vous entendez un bruit inattendu ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss32',
                text="32. Trouvez-vous cela dérangeant de marcher sur des surfaces irrégulières ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss33',
                text="33. Aimez-vous tout particulièrement écouter certains bruits (par exemple, le bruit d'un papier froissé) ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss34',
                text="34. Aimez-vous courir droit devant ou en rond, éventuellement en faisant des va-et-vient ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss35',
                text="35. Est-ce que vous mâchez et léchez des objets qui ne sont pas comestibles (par exemple, un capuchon de stylo ou le bouchon d'une bouteille) parce que vous aimez la sensation ressentie dans votre bouche ? \n	",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss36',
                text="36. Aimez-vous porter du parfum ou de l'après-rasage sentant très fort ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss37',
                text="37. Trouvez-vous que vous avez tendance à positionner votre corps différemment de la plupart des gens (par exemple, allongé sur le dos sur un canapé avec les jambes en l'air à la verticale) ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss38',
                text="38. Trouvez-vous difficile de faire vos lacets ou de boutonner vos vêtements ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss39',
                text="39. Avez-vous remarqué que vous êtes capable d'aller dehors sans manteau ou sans veste alors que les autres personnes pensent qu'il fait trop froid ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss40',
                text="40. Mangez-vous les mêmes plats la plupart du temps ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss41',
                text="41. Aimez-vous porter/tenir quelque chose (par exemple, un chapeau ou un crayon) pour savoir où sont les limites physiques de votre corps ?",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gss42',
                text="42. Agitez-vous vos doigts devant vos yeux ? ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="GSS",
            name="GSS Questionnaire",
            description="42 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=21,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute GSS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

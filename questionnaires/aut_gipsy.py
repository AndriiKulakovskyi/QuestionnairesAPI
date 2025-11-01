"""
AUT_GIPSY - AUT_GIPSY Questionnaire
===================================

46 items questionnaire

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


@register_questionnaire("AUT_GIPSY")
@dataclass
class AutGipsy(BaseQuestionnaire):
    """AUT_GIPSY Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_GIPSY questionnaire with all 46 items."""
        
        questions_list = [
            Question(
                id='gp111',
                text="11. Si vous avez eu ou avez encore besoin de suivre un régime alimentaire, celui-ci est ",
                options=[
                    AnswerOption(value='a', label="Sans gluten", score=0),
                    AnswerOption(value='b', label="Sans lactose", score=1),
                    AnswerOption(value='c', label="Sans caséine", score=2),
                    AnswerOption(value='d', label="Régime Paléo", score=3),
                    AnswerOption(value='e', label="Pauvre en glucides, riche en protéines", score=4),
                    AnswerOption(value='f', label="Régime cétonique", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp112',
                text="12. Un médecin a-t-il déjà officiellement posé chez vous un diagnostic de maladie gastro-intestinale ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp11202',
                text="En rémission",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp11203',
                text="Sous traitement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp113',
                text="13. A votre connaissance, a-t-on déjà diagnostiqué chez vous une maladie auto-immune comme:",
                options=[
                    AnswerOption(value='0', label="1", score=0),
                    AnswerOption(value='1', label="2", score=1),
                    AnswerOption(value='2', label="3", score=2),
                    AnswerOption(value='3', label="4", score=3),
                    AnswerOption(value='4', label="5", score=4),
                    AnswerOption(value='5', label="6", score=5),
                    AnswerOption(value='6', label="7", score=6),
                    AnswerOption(value='7', label="8", score=7),
                    AnswerOption(value='8', label="9", score=8),
                    AnswerOption(value='9', label="10", score=9),
                    AnswerOption(value='10', label="11", score=10),
                    AnswerOption(value='11', label="12", score=11),
                    AnswerOption(value='12', label="13", score=12),
                    AnswerOption(value='13', label="14", score=13),
                    AnswerOption(value='14', label="15", score=14),
                    AnswerOption(value='15', label="16", score=15),
                    AnswerOption(value='16', label="17", score=16),
                    AnswerOption(value='17', label="18", score=17)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp115',
                text="15. Avez-vous déjà dû prendre des traitements immunosuppresseurs ou immunostimulants ayant une diffusion générale, systémique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp213',
                text="13. Si votre enfant a dû suivre un régime spécifique, celui-ci était ",
                options=[
                    AnswerOption(value='a', label="Sans gluten", score=0),
                    AnswerOption(value='b', label="Sans lactose", score=1),
                    AnswerOption(value='c', label="Sans caséine", score=2),
                    AnswerOption(value='d', label="Régime Paléo", score=3),
                    AnswerOption(value='e', label="Pauvre en glucides, riche en protéines", score=4),
                    AnswerOption(value='f', label="Régime cétonique", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp214',
                text="14. Un médecin a-t-il officiellement diagnostiqué une maladie gastro-intestinale à votre enfant lorsqu’il était enfant ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp21402',
                text="Sa maladie était-elle en rémission ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp21403',
                text="A-t-il reçu un traitement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp21404',
                text="précisez le(s) traitement(s)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp215',
                text="15. Le début des symptômes gastro-intestinaux et/ou immunitaires correspond-il au moment de l’apparition ou de l’aggravation des symptômes psychiatriques, des changements de comportements ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp219',
                text="19. Après l’accouchement, le sujet a-t-il eu besoin d’être hospitalisé en unité de réanimation néonatale?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp220',
                text="20. Le sujet a-t-il souffert de complications à la naissance ? (par exemple: cyanose, jaunisse, hémorragie cérébrale, prématurité)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non,le sujet n’a eu aucun problème", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp223',
                text="23. Quel était le poids du bébé à la naissance ?",
                options=[
                    AnswerOption(value='a', label="<1000g", score=0),
                    AnswerOption(value='b', label="1000-1500g", score=1),
                    AnswerOption(value='c', label="1500-2000g", score=2),
                    AnswerOption(value='d', label="2000-2500g", score=3),
                    AnswerOption(value='e', label=">2500g", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp225',
                text="25. Existe-t-il des antécédents de fausse-couche ou de mort in utéro chez la mère du sujet ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp226',
                text="26. Le sujet est né par",
                options=[
                    AnswerOption(value='a', label="voie naturelle", score=0),
                    AnswerOption(value='b', label="césarienne", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp227',
                text="27. L’accouchement a-t-il nécessité l’utilisation de forceps ou de ventouse?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp228a',
                text="a.diabète gestationnel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp228b',
                text="b.éclampsie ou pré-éclampsie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp228c',
                text="c.hypothyroïdie ou hyperthyroïdie, problèmes thyroïdiens",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp228d',
                text="d.confusion",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp228e',
                text="e.rupture prématurée des membranes",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp228f',
                text="f.insuffisance cervicale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp228g',
                text="g.autres",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp229',
                text="29. La mère du sujet a-t-elle eu des infections pendant sa grossesse?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp22903',
                text="Pathogène connu?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp230',
                text="30. La mère du sujet prenait-elle des médicaments pendant sa grossesse?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp231',
                text="31. Pendant sa grossesse, la mère du sujet, a-t-elle été exposée à des facteurs environnementaux qui vous paraissent potentiellement dangereux (métaux lourds, conditions de travail difficiles, exposition aux radiations, voyage dans des zones à haut risque d’infections,…)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp232',
                text="32. Durant sa grossesse, la mère du sujet a-t-elle connu des épisodes de fièvre importants ou des frissons?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233a',
                text="Alcool",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233a01',
                text="alcools forts (rhum, vodka, whisky…)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233a03',
                text="alcools doux (vins, bière, cidre…) ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233b',
                text="Tabac",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233c',
                text="Café",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233d',
                text="Cannabis/ Marijuana",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233e',
                text="Cocaïne",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233f',
                text="Amphétamines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233g',
                text="Solvants",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233h',
                text="LSD",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233i',
                text="Kétamine/ Phencyclidine",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233j',
                text="Ecstasy/MDMA",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233k',
                text="Cannabis de synthèse",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp233l',
                text="Benzodiazépines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp234',
                text="34. Dans votre famille, vous ou une autre personne, souffre-t-elle des maladies auto-immunes suivantes",
                options=[
                    AnswerOption(value='0', label="1", score=0),
                    AnswerOption(value='1', label="2", score=1),
                    AnswerOption(value='2', label="3", score=2),
                    AnswerOption(value='3', label="4", score=3),
                    AnswerOption(value='4', label="5", score=4),
                    AnswerOption(value='5', label="6", score=5),
                    AnswerOption(value='6', label="7", score=6),
                    AnswerOption(value='7', label="8", score=7),
                    AnswerOption(value='8', label="9", score=8),
                    AnswerOption(value='9', label="10", score=9),
                    AnswerOption(value='10', label="11", score=10),
                    AnswerOption(value='11', label="12", score=11),
                    AnswerOption(value='12', label="13", score=12),
                    AnswerOption(value='13', label="14", score=13),
                    AnswerOption(value='14', label="15", score=14),
                    AnswerOption(value='15', label="16", score=15),
                    AnswerOption(value='16', label="17", score=16),
                    AnswerOption(value='17', label="18", score=17)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gp235',
                text="Avez-vous ou votre famille d’autres maladies significatives qui n’ont pas été recueillies dans ce questionnaire",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_GIPSY",
            name="AUT_GIPSY Questionnaire",
            description="46 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=23,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_GIPSY score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

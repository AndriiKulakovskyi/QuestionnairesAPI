"""
LTSG - LTSG Questionnaire
=========================

6 items questionnaire

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


@register_questionnaire("LTSG")
@dataclass
class Ltsg(BaseQuestionnaire):
    """LTSG Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize LTSG questionnaire with all 6 items."""
        
        questions_list = [
            Question(
                id='ltsg1spe1',
                text="Spécifier le type de médicaments utilisés :",
                options=[
                    AnswerOption(value='a', label="Antipsychotique", score=0),
                    AnswerOption(value='b', label="Antidépresseur", score=1),
                    AnswerOption(value='c', label="BDZ/ Hypnotique", score=2),
                    AnswerOption(value='d', label="Substances festives", score=3),
                    AnswerOption(value='e', label="Alcool", score=4),
                    AnswerOption(value='f', label="Gaz/Asphyxiant", score=5),
                    AnswerOption(value='g', label="Prescription autre que psychotrope", score=6),
                    AnswerOption(value='h', label="Sédatif en vente libre", score=7),
                    AnswerOption(value='i', label="Inconnu", score=8),
                    AnswerOption(value='j', label="Anticonvulsivant", score=9)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ltsg1spe1a',
                text="Spécifier les effets du médicament utilisé :",
                options=[
                    AnswerOption(value='a', label="Complètement conscient et lucide", score=0),
                    AnswerOption(value='b', label="Conscient mais somnolent/ engourdi", score=1),
                    AnswerOption(value='c', label="Léthargique avec diminution des capacités intellectuelles", score=2),
                    AnswerOption(value='d', label="Endormi mais facilement réveillé", score=3),
                    AnswerOption(value='e', label="Comateux - évitement des stimuli douloureux; réflexes intacts; blessures suffisantes pour l’hospitalisation", score=4),
                    AnswerOption(value='f', label="Comateux - pas d’évitement des stimuli douloureux; la plupart des réflexes intacts; pas de défaillance respiratoire ou circulatoire, blessures suffisantes pour surveillance aux Soins Intensifs.", score=5),
                    AnswerOption(value='g', label="Comateux – la plupart des réflexes absents, pas de défaillance respiratoire ou circulatoire, Soins Intensifs. et procédures médicales sérieuses", score=6),
                    AnswerOption(value='h', label="Comateux – tous les réflexes absents; défaillance respiratoire avec cyanose ou défaillance circulatoire et choc ou les deux", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ltsg1spe2',
                text="Spécifier le type de médicaments utilisés :",
                options=[
                    AnswerOption(value='a', label="Prescription autre que psychotrope", score=0),
                    AnswerOption(value='b', label="Médicament en vente libre", score=1),
                    AnswerOption(value='c', label="Autres substances ingérées", score=2),
                    AnswerOption(value='d', label="Substances festives", score=3),
                    AnswerOption(value='e', label="Lithium", score=4),
                    AnswerOption(value='f', label="Anticholinergique", score=5),
                    AnswerOption(value='g', label="Coupe faim", score=6),
                    AnswerOption(value='h', label="Inconnu", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ltsg1spe2a',
                text="Spécifier les effets du médicament utilisé :",
                options=[
                    AnswerOption(value='a', label="Pas de conséquences médicales ou de traitement, ou minime", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ltsg1spe3',
                text="spécifier :",
                options=[
                    AnswerOption(value='a', label="Surfaces griffées, pas ou peu de saignements, pas ou peu de soins requis pour les blessures ", score=0),
                    AnswerOption(value='b', label="Saignement modéré avec caillot avant qu’il n’y ait perte de sang significative; simples soins requis", score=1),
                    AnswerOption(value='c', label="Saignement des veines majeures, danger de perte de sang considérable sans intervention chirurgicale - suture nécessaire mais pas de transfusion, zones vitales\nintactes et pas de changement dans les signes vitaux, soins en ambulatoire ", score=2),
                    AnswerOption(value='d', label="Perte de sang importante, suture, transfusion nécessaire, réparation de tendons requise, blessures possibles sur la tête, le thorax, ou l’abdomen mais organes\nvitaux intacts et signes vitaux stables; rétablissement attendu après hospitalisation.", score=3),
                    AnswerOption(value='e', label="Perte de sang très importante avec choc, lésion des zones vitales avec changement dans les signes vitaux; rétablissement après hospitalisation peu\nprobable", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ltsg4',
                text="Quel est le déclencheur externe ?",
                options=[
                    AnswerOption(value='a', label="conjugal", score=0),
                    AnswerOption(value='b', label="autre facteur interpersonnel", score=1),
                    AnswerOption(value='c', label="professionnel", score=2),
                    AnswerOption(value='d', label="événement de vie", score=3),
                    AnswerOption(value='e', label="santé", score=4),
                    AnswerOption(value='f', label="autre", score=5),
                    AnswerOption(value='g', label="ne peut pas être évalué", score=6),
                    AnswerOption(value='h', label="abus sexuel", score=7),
                    AnswerOption(value='i', label="sévices physiques", score=8),
                    AnswerOption(value='j', label="autre, spécifiez", score=9)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="LTSG",
            name="LTSG Questionnaire",
            description="6 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute LTSG score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

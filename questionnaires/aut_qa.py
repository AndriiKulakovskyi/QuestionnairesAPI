"""
AUT_QA - AUT_QA Questionnaire
=============================

37 items questionnaire

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


@register_questionnaire("AUT_QA")
@dataclass
class AutQa(BaseQuestionnaire):
    """AUT_QA Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_QA questionnaire with all 37 items."""
        
        questions_list = [
            Question(
                id='qa10',
                text="10.Au sein d’un groupe, je peux facilement suivre les conversations de plusieurs personnes à la fois.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa11',
                text="11.Je trouve les situations de la vie en société faciles.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa12',
                text="12.J’ai tendance à remarquer certains détails que les autres ne voient pas.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa13',
                text="13.Je préfèrerais aller dans une bibliothèque plutôt qu’à une fête.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa14',
                text="14.Je trouve facile d’inventer des histoires.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa16',
                text="16.J’ai tendance à avoir des centres d’intérêt très importants.  Je me tracasse lorsque je ne peux m’y consacrer.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa17',
                text="17.J’apprécie le bavardage en société.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa18',
                text="18.Quand je parle, il n’est pas toujours facile pour les autres de placer un mot.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa2',
                text="2.Je préfère tout faire continuellement de la même manière.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa20',
                text="20.Quand je lis une histoire, je trouve qu’il est difficile de me représenter les intentions des personnages.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa21',
                text="21.Je n’aime pas particulièrement lire des romans.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa22',
                text="22.Je trouve qu’il est difficile de se faire de nouveaux amis.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa23',
                text="23.Je remarque sans cesse des schémas réguliers dans les choses qui m’entourent.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa24',
                text="24.Je préfèrerais aller au théâtre qu’au musée.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa25',
                text="25.Cela ne me dérange pas si mes habitudes quotidiennes sont perturbées.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa26',
                text="26.Je remarque souvent que je ne sais pas comment entretenir une conversation.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa27',
                text="27.Je trouve qu’il est facile de « lire entre les lignes » lorsque quelqu’un me parle.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa28',
                text="28.Je me concentre habituellement plus sur l’ensemble d’une image que sur les petits détails de celle-ci.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa3',
                text="3.Quand j’essaye d’imaginer quelque chose, il est très facile de m’en représenter une image mentalement.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa30',
                text="30.Je ne remarque habituellement pas les petits changements dans une situation ou dans l’apparence de quelqu’un.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa31',
                text="31.Je sais m’en rendre compte quand mon interlocuteur s’ennuie.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa32',
                text="32.Je trouve qu’il est facile de faire plus d’une chose à la fois.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa34',
                text="34.J’aime faire les choses de manière spontanée.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa36',
                text="36.Je trouve qu’il est facile de décoder ce que les autres pensent ou ressentent juste en regardant leur visage.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa39',
                text="39.Les gens me disent souvent que répète continuellement les mêmes choses.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa40',
                text="40.Quand j’étais enfant, j’aimais habituellement jouer à des jeux de rôle avec les autres.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa42',
                text="42.Je trouve qu’il est difficile de s’imaginer dans la peau d’un autre.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa43',
                text="43.J’aime planifier avec soin toute activité à laquelle je participe.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa44',
                text="44.J’aime les événements sociaux.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa45',
                text="45.Je trouve qu’il est difficile de décoder les intentions des autres.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa47',
                text="47.J’aime rencontrer de nouvelles personnes.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa48',
                text="48.Je suis une personne qui a le sens de la diplomatie.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa5',
                text="5.Mon attention est souvent attirée par des bruits discrets que les autres ne remarquent pas.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa50',
                text="50.Je trouve qu’il est très facile de jouer à des jeux de rôle avec des enfants.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa6',
                text="6.Je fais habituellement attention aux numéros de plaques d’immatriculation ou à d’autres types d’informations de ce genre.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa7',
                text="7.Les gens me disent souvent que ce que j’ai dit était impoli, même quand je pense moi que c’était poli.",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qa8',
                text="8.Quand je lis une histoire, je peux facilement imaginer à quoi les personnages pourraient ressembler.",
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
            code="AUT_QA",
            name="AUT_QA Questionnaire",
            description="37 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=18,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_QA score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

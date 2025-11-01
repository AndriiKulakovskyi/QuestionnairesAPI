"""
SACHS - SACHS Questionnaire
===========================

3 items questionnaire

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


@register_questionnaire("SACHS")
@dataclass
class Sachs(BaseQuestionnaire):
    """SACHS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize SACHS questionnaire with all 3 items."""
        
        questions_list = [
            Question(
                id='sachs1',
                text="1-  Caractéristiques des épisodes",
                options=[
                    AnswerOption(value='a', label="20 - Episode maniaque aigu ou mixte avec prédominance de l'euphorie, d'idées grandioses ou d'expansivité excessive, sans notion de cause médicale générale ou de cause étiologique secondaire ", score=0),
                    AnswerOption(value='b', label="15 - Episode aigu et franc de type mixte, ou manie irritable ou dysphorique, sans notion de cause médicale générale ou de cause étiologique secondaire", score=1),
                    AnswerOption(value='c', label="10 - Hypomanie ou cyclothymie franches sans cause médicale générale ou de cause étiologique secondaire", score=2),
                    AnswerOption(value='d', label="10 - Manie secondaire à l'utilisation d'antidépresseur ", score=3),
                    AnswerOption(value='e', label="5 -  Hypomanie franche secondaire à l'utilisation d'antidépresseur ", score=4),
                    AnswerOption(value='f', label="5- Episodes caractéristiques d'hypomanie mais dont les symptômes, la durée ou l'intensité sont atténués par rapport à un épisode franc d'hypomanie ou de cyclothymie ", score=5),
                    AnswerOption(value='g', label="5 - Episode dépressif unique avec manifestations psychotique ou signes atypiques : hypersomnie, hyperphagie, impression de jambes lourdes", score=6),
                    AnswerOption(value='h', label="5 - Dépression du post-partum ", score=7),
                    AnswerOption(value='i', label="2 - Dépression unipolaire typique et récurrente ", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='sachs2',
                text="2-  Age de début \\",
                options=[
                    AnswerOption(value='a', label="20 - 15 à 19 ans ", score=0),
                    AnswerOption(value='b', label="15 - Avant 15 et entre 20 et 30 ", score=1),
                    AnswerOption(value='c', label="10 - 30 à 45 ", score=2),
                    AnswerOption(value='d', label="5 -  Après 45 ", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='sachs5',
                text="5-  Histoire familiale ",
                options=[
                    AnswerOption(value='a', label="20 - Au moins 1 parent du 1er degré ayant un trouble bipolaire documenté ", score=0),
                    AnswerOption(value='b', label="15 - Un parent de second degré ayant un trouble bipolaire documenté", score=1),
                    AnswerOption(value='c', label="15 - Un parent du 1er degré ayant un trouble unipolaire documenté et un comportement suggérant un trouble bipolaire ", score=2),
                    AnswerOption(value='d', label="10 - Un parent du 1er degré ayant un trouble unipolaire documenté ou un trouble schizo-affectif ", score=3),
                    AnswerOption(value='e', label="10 - Un parent de second degré ayant un trouble bipolaire documenté et un comportement suggérant un trouble bipolaire ", score=4),
                    AnswerOption(value='f', label="5 - Un parent du 1er degré avec histoire documentée de dépendance à des toxiques ", score=5),
                    AnswerOption(value='g', label="5 - Un parent du 1er degré avec trouble bipolaire possible ", score=6),
                    AnswerOption(value='h', label="2 - Un parent du 1er degré avec trouble unipolaire possible ", score=7),
                    AnswerOption(value='i', label="2 - Un parent du 1er degré avec anxiété, trouble alimentaire, déficit de l'attention et hyperactivité possibles ", score=8),
                    AnswerOption(value='j', label="0 - Aucun de ces éléments ou aucun antécédent psychiatrique familial ", score=9)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="SACHS",
            name="SACHS Questionnaire",
            description="3 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute SACHS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result

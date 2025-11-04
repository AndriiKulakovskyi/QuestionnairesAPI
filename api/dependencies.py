"""
Dependencies and Questionnaire Registry for the API
"""

from typing import Dict, Optional, Any
from questionnaires import (
    QIDSSR16, QIDSError,
    MDQ, MDQError,
    ASRM, ASRMError,
    Epworth, EpworthError,
    EQ5DEL, EQ5DELError,
    Fagerstrom, FagerstromError,
    MARS, MARSError,
    MAThyS, MAThySError,
    PRISEM, PRISEMError,
    PSQI, PSQIError,
    STAIYA, STAIYAError,
    AIMShort, AIMShortError,
    ALSShort, ALSShortError,
    AQ12, AQ12Error,
    ASRS, ASRSError,
    BIS10, BIS10Error,
    CSM, CSMError,
    CTQ, CTQError,
    CTI, CTIError,
    WURS25, WURS25Error
)


class QuestionnaireRegistry:
    """
    Registry for managing questionnaire instances.
    Provides centralized access to all questionnaires organized by category.
    """
    
    def __init__(self):
        """Initialize the registry with all available questionnaires."""
        # Auto questionnaires (self-report)
        self.auto_questionnaires: Dict[str, Any] = {
            "QIDS-SR16.fr": QIDSSR16(),
            "MDQ.fr": MDQ(),
            "ASRM.fr": ASRM(),
            "Epworth.fr": Epworth(),
            "EQ5D-EL.fr": EQ5DEL(),
            "Fagerstrom.fr": Fagerstrom(),
            "MARS.fr": MARS(),
            "MAThyS.fr": MAThyS(),
            "PRISE-M.fr": PRISEM(),
            "PSQI.fr": PSQI(),
            "STAI-YA.fr": STAIYA(),
            "AIM-Short.fr": AIMShort(),
            "ALS-Short.fr": ALSShort(),
            "AQ12.fr": AQ12(),
            "ASRS.fr": ASRS(),
            "BIS10.fr": BIS10(),
            "CSM.fr": CSM(),
            "CTQ.fr": CTQ(),
            "CTI.fr": CTI(),
            "WURS25.fr": WURS25()
        }
        
        # Hetero questionnaires (clinician-rated)
        from questionnaires import ALDA, CGI, EGF, EtatPatient, FAST, MADRS, YMRS
        self.hetero_questionnaires: Dict[str, Any] = {
            "Alda.fr": ALDA(),
            "CGI.fr": CGI(),
            "EGF.fr": EGF(),
            "EtatPatient.fr": EtatPatient(),
            "FAST.fr": FAST(),
            "MADRS.fr": MADRS(),
            "YMRS.fr": YMRS()
        }
    
    def get_questionnaire(self, category: str, questionnaire_id: str) -> Optional[Any]:
        """
        Get a questionnaire instance by category and ID.
        
        Args:
            category: 'auto' or 'hetero'
            questionnaire_id: The questionnaire identifier (e.g., 'QIDS-SR16.fr')
            
        Returns:
            Questionnaire instance or None if not found
        """
        if category == "auto":
            return self.auto_questionnaires.get(questionnaire_id)
        elif category == "hetero":
            return self.hetero_questionnaires.get(questionnaire_id)
        return None
    
    def list_questionnaires(self, category: str) -> Dict[str, Any]:
        """
        Get all questionnaires for a category.
        
        Args:
            category: 'auto' or 'hetero'
            
        Returns:
            Dictionary of questionnaire_id -> instance
        """
        if category == "auto":
            return self.auto_questionnaires
        elif category == "hetero":
            return self.hetero_questionnaires
        return {}
    
    def get_questionnaire_metadata(self, category: str, questionnaire_id: str) -> Optional[Dict[str, Any]]:
        """
        Get metadata for a specific questionnaire.
        
        Args:
            category: 'auto' or 'hetero'
            questionnaire_id: The questionnaire identifier
            
        Returns:
            Metadata dictionary or None if not found
        """
        questionnaire = self.get_questionnaire(category, questionnaire_id)
        if questionnaire and hasattr(questionnaire, 'get_metadata'):
            return questionnaire.get_metadata()
        return None


# Global registry instance
registry = QuestionnaireRegistry()


def get_registry() -> QuestionnaireRegistry:
    """Dependency function to get the questionnaire registry."""
    return registry


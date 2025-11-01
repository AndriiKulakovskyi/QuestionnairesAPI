"""
Questionnaire Registry and Factory
===================================

This module provides a centralized registry for all available questionnaires
and a factory for creating instances.

The registry pattern allows for:
- Dynamic discovery of all available questionnaires
- Easy lookup by code or pathology domain
- Version management
- Metadata about each questionnaire

Author: Fondation FondaMental
Version: 2.0.0 (Refactored)
"""

from typing import Dict, List, Type, Optional
from .models import BaseQuestionnaire, PathologyDomain


class QuestionnaireRegistry:
    """
    Centralized registry of all available questionnaires.
    
    This is a singleton that maintains a catalog of all questionnaire classes.
    """
    
    _instance = None
    _questionnaires: Dict[str, Type[BaseQuestionnaire]] = {}
    
    def __new__(cls):
        """Singleton pattern - only one registry instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def register(
        self,
        code: str,
        questionnaire_class: Type[BaseQuestionnaire]
    ) -> None:
        """
        Register a questionnaire class.
        
        Args:
            code: Short code for the questionnaire (e.g., "YMRS")
            questionnaire_class: The class implementing the questionnaire
        
        Raises:
            ValueError: If code is already registered
        """
        if code in self._questionnaires:
            raise ValueError(
                f"Questionnaire with code '{code}' is already registered. "
                f"Use a different code or unregister the existing one first."
            )
        
        self._questionnaires[code] = questionnaire_class
    
    def unregister(self, code: str) -> None:
        """Unregister a questionnaire."""
        if code in self._questionnaires:
            del self._questionnaires[code]
    
    def get(self, code: str) -> Optional[Type[BaseQuestionnaire]]:
        """
        Get a questionnaire class by its code.
        
        Args:
            code: Questionnaire code
        
        Returns:
            Questionnaire class or None if not found
        """
        return self._questionnaires.get(code.upper())
    
    def list_all(self) -> List[str]:
        """List all registered questionnaire codes."""
        return sorted(self._questionnaires.keys())
    
    def list_by_pathology(self, pathology: PathologyDomain) -> List[str]:
        """
        List all questionnaires for a specific pathology domain.
        
        Args:
            pathology: The pathology domain
        
        Returns:
            List of questionnaire codes for that domain
        """
        result = []
        for code, questionnaire_class in self._questionnaires.items():
            # Instantiate to get pathology domain
            # (This is a simplification - ideally we'd have class-level metadata)
            try:
                instance = questionnaire_class()
                if instance.pathology_domain == pathology:
                    result.append(code)
            except Exception:
                # Skip if instantiation fails
                continue
        
        return sorted(result)
    
    def get_metadata(self, code: str) -> Optional[Dict]:
        """
        Get metadata about a questionnaire without instantiating it.
        
        Args:
            code: Questionnaire code
        
        Returns:
            Dictionary with metadata or None if not found
        """
        questionnaire_class = self.get(code)
        if not questionnaire_class:
            return None
        
        try:
            instance = questionnaire_class()
            return {
                'code': instance.code,
                'name': instance.name,
                'description': instance.description,
                'pathology_domain': instance.pathology_domain.value,
                'respondent_type': instance.respondent_type.value,
                'total_questions': len(instance.questions),
                'estimated_duration_minutes': instance.estimated_duration_minutes,
                'version': instance.version
            }
        except Exception as e:
            return {
                'code': code,
                'error': f"Failed to get metadata: {str(e)}"
            }


class QuestionnaireFactory:
    """
    Factory for creating questionnaire instances.
    
    Provides convenience methods for creating and configuring questionnaires.
    """
    
    def __init__(self):
        """Initialize factory with reference to registry."""
        self.registry = QuestionnaireRegistry()
    
    def create(self, code: str) -> BaseQuestionnaire:
        """
        Create an instance of a questionnaire by its code.
        
        Args:
            code: Questionnaire code (e.g., "YMRS")
        
        Returns:
            Instantiated questionnaire
        
        Raises:
            ValueError: If questionnaire code is not registered
        """
        questionnaire_class = self.registry.get(code)
        
        if not questionnaire_class:
            raise ValueError(
                f"Questionnaire '{code}' not found. "
                f"Available questionnaires: {self.registry.list_all()}"
            )
        
        return questionnaire_class()
    
    def create_for_visit(
        self,
        visit_type: str,
        pathology: Optional[PathologyDomain] = None
    ) -> List[BaseQuestionnaire]:
        """
        Create all questionnaires applicable for a specific visit type.
        
        Args:
            visit_type: Type of visit (e.g., "Initial", "Follow-up")
            pathology: Optional filter by pathology domain
        
        Returns:
            List of questionnaire instances
        """
        questionnaires = []
        
        for code in self.registry.list_all():
            questionnaire_class = self.registry.get(code)
            if not questionnaire_class:
                continue
            
            try:
                instance = questionnaire_class()
                
                # Check if this questionnaire is for this visit
                if visit_type not in instance.visit_types:
                    continue
                
                # Check pathology filter if specified
                if pathology and instance.pathology_domain != pathology:
                    continue
                
                questionnaires.append(instance)
            
            except Exception:
                # Skip questionnaires that fail to instantiate
                continue
        
        return questionnaires
    
    def get_all_codes(self) -> List[str]:
        """Get list of all available questionnaire codes."""
        return self.registry.list_all()
    
    def get_codes_by_pathology(self, pathology: PathologyDomain) -> List[str]:
        """Get list of questionnaire codes for a specific pathology."""
        return self.registry.list_by_pathology(pathology)


# ============================================================================
# Decorator for auto-registration
# ============================================================================

def register_questionnaire(code: str):
    """
    Decorator to automatically register a questionnaire class.
    
    Usage:
        @register_questionnaire("YMRS")
        class YMRS(BaseQuestionnaire):
            ...
    
    Args:
        code: Questionnaire code to register
    """
    def decorator(cls: Type[BaseQuestionnaire]):
        registry = QuestionnaireRegistry()
        registry.register(code, cls)
        return cls
    
    return decorator


# ============================================================================
# Global instances for convenience
# ============================================================================

# Singleton instances that can be imported
questionnaire_registry = QuestionnaireRegistry()
questionnaire_factory = QuestionnaireFactory()

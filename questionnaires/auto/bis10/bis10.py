# -*- coding: utf-8 -*-
"""
BIS-10 Short Version (12 items)
Barratt Impulsiveness Scale - French version

Short version validated by Kahn et al. (2019) for bipolar patients.
Two dimensions: Cognitive Impulsivity (5 items) and Behavioral Impulsivity (7 items).
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel


class BIS10Error(ValueError):
    """Custom exception for BIS-10 validation errors"""
    pass


class QuestionOption(BaseModel):
    """Model for a question option"""
    code: int
    label: str
    score: Optional[int] = None


class Question(BaseModel):
    """Model for a question"""
    id: str
    section_id: str
    text: str
    type: str
    required: bool
    options: List[QuestionOption]
    constraints: Dict[str, Any]
    reverse_scored: bool = False
    subscale: str


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    description: str
    question_ids: List[str]


class SubscaleResult(BaseModel):
    """Model for subscale results"""
    name: str
    label: str
    mean_score: float
    item_count: int
    range: tuple


class ScoreResult(BaseModel):
    """Model for score results"""
    overall_impulsivity: float
    subscales: Dict[str, SubscaleResult]
    interpretation: str
    warnings: List[str] = []


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class BIS10:
    """
    BIS-10 Short Version (12 items) Questionnaire Class
    
    French validation by Kahn et al. (2019) for bipolar patients.
    Measures impulsivity across two dimensions:
    - Cognitive Impulsivity (5 items)
    - Behavioral Impulsivity (7 items)
    
    Scoring uses means (not sums) to account for different item counts.
    """
    
    INSTRUMENT_ID = "BIS-10.fr"
    INSTRUMENT_NAME = "Barratt Impulsiveness Scale – BIS-10 (Version française)"
    ABBREVIATION = "BIS-10"
    LANGUAGE = "fr-FR"
    VERSION = "1.0 (12 items)"
    REFERENCE_PERIOD = "Mode de fonctionnement habituel"
    
    # Instruction text
    INSTRUCTION = (
        "Les gens agissent et réfléchissent différemment devant des situations variées. "
        "Ce questionnaire a pour but d'évaluer certaines de vos façons d'agir et de réfléchir. "
        "Lisez chaque énoncé et remplissez la case appropriée située sur la droite de la page. "
        "Ne passez pas trop de temps sur chaque énoncé. Répondez vite et honnêtement."
    )
    
    # 12 items used in short version (from 34-item full version)
    # Items shown: 1, 6, 8, 9, 12, 14, 17, 20, 21, 23, 25, 28
    ITEM_TEXTS = {
        1: "Je prépare soigneusement les tâches à accomplir",
        6: "J'ai des idées qui fusent",
        8: "Je suis maître de moi",
        9: "Je me concentre facilement",
        12: "Je réfléchis soigneusement",
        14: "Je dis les choses sans y penser",
        17: "J'agis sur un coup de tête",
        20: "J'agis selon l'inspiration du moment",
        21: "Je suis quelqu'un de réfléchi",
        23: "J'achète les choses sur un coup de tête",
        25: "Je change de passe-temps",
        28: "Je dépense ou paye à crédit plus que je ne gagne"
    }
    
    # Cognitive impulsivity items (reverse scored: 4=rarely to 1=always)
    COGNITIVE_ITEMS = [1, 8, 9, 12, 21]
    
    # Behavioral impulsivity items (normal scoring: 1=rarely to 4=always)
    BEHAVIORAL_ITEMS = [6, 14, 17, 20, 23, 25, 28]
    
    # Response options
    RESPONSE_OPTIONS = [
        {"code": 1, "label": "Rarement ou jamais"},
        {"code": 2, "label": "Occasionnellement"},
        {"code": 3, "label": "Souvent"},
        {"code": 4, "label": "Toujours ou presque toujours"}
    ]
    
    def __init__(self):
        """Initialize the BIS-10 questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="sec_instructions",
                label="Consigne",
                description=self.INSTRUCTION,
                question_ids=[]
            ),
            Section(
                id="sec_items",
                label="Items",
                description="Échelle de Likert en 4 points",
                question_ids=[f"q{i}" for i in sorted(self.ITEM_TEXTS.keys())]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = []
        
        for item_num in sorted(self.ITEM_TEXTS.keys()):
            is_cognitive = item_num in self.COGNITIVE_ITEMS
            subscale = "cognitive" if is_cognitive else "behavioral"
            
            questions.append(Question(
                id=f"q{item_num}",
                section_id="sec_items",
                text=f"{item_num}. {self.ITEM_TEXTS[item_num]}",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(**opt) for opt in self.RESPONSE_OPTIONS
                ],
                constraints={
                    "value_type": "integer",
                    "allowed_values": [1, 2, 3, 4]
                },
                reverse_scored=is_cognitive,
                subscale=subscale
            ))
        
        return questions
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get instrument metadata"""
        return {
            "id": self.INSTRUMENT_ID,
            "name": self.INSTRUMENT_NAME,
            "abbreviation": self.ABBREVIATION,
            "language": self.LANGUAGE,
            "version": self.VERSION,
            "reference_period": self.REFERENCE_PERIOD,
            "description": (
                "Version courte en 12 items de l'échelle d'impulsivité de Barratt. "
                "Mesure l'impulsivité cognitive (5 items) et comportementale (7 items). "
                "Scores calculés en moyennes."
            ),
            "sources": [
                "Baylé F et al. (2000) Canadian Journal of Psychiatry, 45:2, p156-165.",
                "Kahn et al. (2019) J Affect Disord. 253:203-209.",
                "Patton JH et al. (1995) J Clin Psychol 51:768-74."
            ],
            "total_questions": 12,
            "scoring_method": "means",
            "subscales": {
                "cognitive": {
                    "label": "Impulsivité cognitive",
                    "items": self.COGNITIVE_ITEMS,
                    "item_count": len(self.COGNITIVE_ITEMS),
                    "range": [1.0, 4.0]
                },
                "behavioral": {
                    "label": "Impulsivité comportementale",
                    "items": self.BEHAVIORAL_ITEMS,
                    "item_count": len(self.BEHAVIORAL_ITEMS),
                    "range": [1.0, 4.0]
                }
            },
            "overall_range": [1.0, 4.0]
        }
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """Get all sections"""
        return [section.model_dump() for section in self._sections]
    
    def get_questions(self, section_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get questions, optionally filtered by section
        
        Args:
            section_id: Optional section ID to filter questions
            
        Returns:
            List of questions as dictionaries
        """
        questions = self._questions
        if section_id:
            questions = [q for q in questions if q.section_id == section_id]
        return [q.model_dump() for q in questions]
    
    def get_question_by_id(self, question_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific question by ID"""
        for q in self._questions:
            if q.id == question_id:
                return q.model_dump()
        return None
    
    def validate_answers(self, answers: Dict[str, int]) -> ValidationResult:
        """
        Validate provided answers
        
        Args:
            answers: Dictionary of question_id -> answer mappings (1-4)
            
        Returns:
            ValidationResult with validation status and messages
        """
        errors = []
        warnings = []
        
        # Check for missing required questions
        expected_keys = [f"q{i}" for i in sorted(self.ITEM_TEXTS.keys())]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value ranges and types
        invalid = {}
        for k in expected_keys:
            if k in answers:
                try:
                    val = int(answers[k])
                    if val < 1 or val > 4:
                        invalid[k] = val
                except (ValueError, TypeError):
                    invalid[k] = answers[k]
        
        if invalid:
            errors.append(f"Valeurs invalides (doivent être des entiers entre 1 et 4): {invalid}")
        
        # Clinical warnings (only if no errors)
        if not errors:
            # Check if all values are identical
            values = [answers[k] for k in expected_keys]
            if len(set(values)) == 1:
                warnings.append(
                    "Toutes les réponses sont identiques. Veuillez vérifier que le patient "
                    "a bien compris les instructions."
                )
            
            # Check for extreme cognitive impulsivity (all cognitive items at minimum after reversal)
            cognitive_values = [answers[f"q{i}"] for i in self.COGNITIVE_ITEMS]
            if all(v == 4 for v in cognitive_values):
                warnings.append(
                    "Tous les items d'impulsivité cognitive indiquent un contrôle maximal. "
                    "Cela peut suggérer une sous-estimation."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_score(self, answers: Dict[str, int]) -> ScoreResult:
        """
        Calculate BIS-10 scores
        
        Args:
            answers: Dictionary with keys q1, q6, q8, q9, q12, q14, q17, q20, q21, q23, q25, q28
                    Values are 1-4
            
        Returns:
            ScoreResult with overall and subscale means
            
        Raises:
            BIS10Error: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise BIS10Error("; ".join(validation.errors))
        
        # Calculate cognitive impulsivity mean (reverse scored)
        # Cognitive items: 4=rarely → 1, 1=always → 4 (so: 5 - value)
        cognitive_scores = [5 - answers[f"q{i}"] for i in self.COGNITIVE_ITEMS]
        cognitive_mean = sum(cognitive_scores) / len(cognitive_scores)
        
        # Calculate behavioral impulsivity mean (normal scoring)
        behavioral_scores = [answers[f"q{i}"] for i in self.BEHAVIORAL_ITEMS]
        behavioral_mean = sum(behavioral_scores) / len(behavioral_scores)
        
        # Calculate overall impulsivity (mean of the two means)
        overall_mean = (cognitive_mean + behavioral_mean) / 2
        
        # Build subscale results
        subscales = {
            "cognitive": SubscaleResult(
                name="cognitive",
                label="Impulsivité cognitive",
                mean_score=round(cognitive_mean, 2),
                item_count=len(self.COGNITIVE_ITEMS),
                range=(1.0, 4.0)
            ),
            "behavioral": SubscaleResult(
                name="behavioral",
                label="Impulsivité comportementale",
                mean_score=round(behavioral_mean, 2),
                item_count=len(self.BEHAVIORAL_ITEMS),
                range=(1.0, 4.0)
            )
        }
        
        # Build interpretation
        interpretation = self._build_interpretation(
            overall_mean, cognitive_mean, behavioral_mean, validation.warnings
        )
        
        return ScoreResult(
            overall_impulsivity=round(overall_mean, 2),
            subscales=subscales,
            interpretation=interpretation,
            warnings=validation.warnings
        )
    
    def _build_interpretation(
        self,
        overall: float,
        cognitive: float,
        behavioral: float,
        warnings: List[str]
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Score d'impulsivité générale: {overall:.2f}/4.0. "
        
        # Overall interpretation
        if overall >= 3.0:
            interpretation += (
                "Niveau d'impulsivité très élevé. Le patient rapporte des difficultés importantes "
                "de contrôle impulsif nécessitant une évaluation et un suivi clinique."
            )
        elif overall >= 2.5:
            interpretation += (
                "Niveau d'impulsivité élevé. Le patient rapporte des difficultés de contrôle impulsif "
                "qui peuvent nécessiter une attention clinique."
            )
        elif overall >= 2.0:
            interpretation += (
                "Niveau d'impulsivité modéré. Le patient rapporte un contrôle impulsif globalement "
                "satisfaisant avec quelques difficultés occasionnelles."
            )
        else:
            interpretation += (
                "Niveau d'impulsivité faible. Le patient rapporte un bon contrôle impulsif "
                "dans son fonctionnement habituel."
            )
        
        # Subscale details
        interpretation += f"\n\nDimensions:\n"
        interpretation += f"• Impulsivité cognitive: {cognitive:.2f}/4.0 "
        if cognitive >= 3.0:
            interpretation += "(Très élevée - Difficultés majeures de concentration, réflexion et planification)"
        elif cognitive >= 2.5:
            interpretation += "(Élevée - Difficultés notables de réflexion et de concentration)"
        elif cognitive >= 2.0:
            interpretation += "(Modérée - Quelques difficultés cognitives occasionnelles)"
        else:
            interpretation += "(Faible - Bonne capacité de réflexion et de concentration)"
        
        interpretation += f"\n• Impulsivité comportementale: {behavioral:.2f}/4.0 "
        if behavioral >= 3.0:
            interpretation += "(Très élevée - Actions impulsives fréquentes, achats compulsifs)"
        elif behavioral >= 2.5:
            interpretation += "(Élevée - Tendance marquée à agir sans réfléchir)"
        elif behavioral >= 2.0:
            interpretation += "(Modérée - Quelques comportements impulsifs occasionnels)"
        else:
            interpretation += "(Faible - Bon contrôle comportemental)"
        
        # Clinical recommendations
        if overall >= 3.0:
            interpretation += (
                "\n\n⚠️ RECOMMANDATIONS CLINIQUES:\n"
                "• Évaluation des troubles du contrôle des impulsions\n"
                "• Dépistage TDAH si impulsivité cognitive élevée\n"
                "• Recherche de troubles addictifs ou comportements à risque\n"
                "• Évaluation de comorbidités (trouble bipolaire, personnalité borderline)\n"
                "• Thérapie cognitivo-comportementale ciblant l'impulsivité"
            )
        elif overall >= 2.5:
            interpretation += (
                "\n\nRecommandations:\n"
                "• Surveillance clinique si retentissement fonctionnel\n"
                "• Psychoéducation sur le contrôle des impulsions\n"
                "• Stratégies de gestion de l'impulsivité"
            )
        
        # Add warnings
        if warnings:
            interpretation += "\n\nAvertissements: " + " ".join(warnings)
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }

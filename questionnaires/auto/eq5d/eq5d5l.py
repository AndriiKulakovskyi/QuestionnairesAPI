# -*- coding: utf-8 -*-
"""
EQ-5D-5L (EuroQol 5 Dimensions 5 Levels)
French version - Generic health status measure
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel


class EQ5D5LError(ValueError):
    """Custom exception for EQ-5D-5L validation errors"""
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
    options: Optional[List[QuestionOption]] = None
    constraints: Dict[str, Any]


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    description: str
    question_ids: List[str]


class ScoreResult(BaseModel):
    """Model for score results"""
    profile: str
    vas_score: int
    index_value: Optional[float] = None
    interpretation: str
    dimension_scores: Dict[str, int]


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class EQ5D5L:
    """
    EQ-5D-5L Questionnaire Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Calculate profile and VAS scores
    """
    
    INSTRUMENT_ID = "EQ-5D-5L.fr"
    INSTRUMENT_NAME = "EQ-5D-5L – Version française"
    ABBREVIATION = "EQ-5D-5L"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "AUJOURD'HUI"
    
    # 5 dimensions with their labels and options
    DIMENSIONS = [
        ("Mobilité", [
            "Je n'ai aucun problème pour me déplacer à pied",
            "J'ai des problèmes légers pour me déplacer à pied",
            "J'ai des problèmes modérés pour me déplacer à pied",
            "J'ai des problèmes sévères pour me déplacer à pied",
            "Je suis incapable de me déplacer à pied"
        ]),
        ("Autonomie de la personne", [
            "Je n'ai aucun problème pour me laver ou m'habiller tout seul",
            "J'ai des problèmes légers pour me laver ou m'habiller tout seul",
            "J'ai des problèmes modérés pour me laver ou m'habiller tout seul",
            "J'ai des problèmes sévères pour me laver ou m'habiller tout seul",
            "Je suis incapable de me laver ou de m'habiller tout(e) seul(e)"
        ]),
        ("Activités courantes", [
            "Je n'ai aucun problème pour accomplir mes activités courantes",
            "J'ai des problèmes légers pour accomplir mes activités courantes",
            "J'ai des problèmes modérés pour accomplir mes activités courantes",
            "J'ai des problèmes sévères pour accomplir mes activités courantes",
            "Je suis incapable d'accomplir mes activités courantes"
        ]),
        ("Douleurs / Gêne", [
            "Je n'ai ni douleur, ni gêne",
            "J'ai des douleurs ou une gêne légère(s)",
            "J'ai des douleurs ou une gêne modérée(s)",
            "J'ai des douleurs ou une gêne sévère(s)",
            "J'ai des douleurs ou une gêne extrême(s)"
        ]),
        ("Anxiété / Dépression", [
            "Je ne suis ni anxieux(se), ni déprimé(e)",
            "Je suis légèrement anxieux(se) ou déprimé(e)",
            "Je suis modérément anxieux(se) ou déprimé(e)",
            "Je suis sévèrement anxieux(se) ou déprimé(e)",
            "Je suis extrêmement anxieux(se) ou déprimé(e)"
        ])
    ]
    
    # Perfect health profile
    PERFECT_HEALTH_PROFILE = "11111"
    
    def __init__(self):
        """Initialize the EQ-5D-5L questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="sec_dims",
                label="Dimensions (AUJOURD'HUI)",
                description="Cochez UNE case par rubrique",
                question_ids=[f"q{i}" for i in range(1, 6)]
            ),
            Section(
                id="sec_vas",
                label="EQ VAS",
                description="Votre santé aujourd'hui sur l'échelle 0–100",
                question_ids=["vas"]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = []
        
        # Q1-Q5: Five dimensions (scored 1-5, not 0-4!)
        for i, (dimension_title, options) in enumerate(self.DIMENSIONS, start=1):
            questions.append(Question(
                id=f"q{i}",
                section_id="sec_dims",
                text=f"{dimension_title} – cochez UNE case",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=level, label=options[level-1], score=None)
                    for level in range(1, 6)
                ],
                constraints={
                    "value_type": "integer",
                    "allowed_values": [1, 2, 3, 4, 5]
                }
            ))
        
        # VAS: Visual Analog Scale (0-100)
        questions.append(Question(
            id="vas",
            section_id="sec_vas",
            text="Votre santé AUJOURD'HUI (0=pire état de santé imaginable, 100=meilleur état de santé imaginable)",
            type="integer",
            required=True,
            options=None,
            constraints={
                "value_type": "integer",
                "min_value": 0,
                "max_value": 100
            }
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
            "description": "Mesure générique de l'état de santé : 5 dimensions à 5 niveaux (profil 11111–55555) et une échelle visuelle analogique (EQ VAS 0–100).",
            "sources": [
                "EQ-5D-EL.pdf (version FR)",
                "EQ5D5L_CotationScore.docx (cotation et crosswalk)",
                "EQ-5D-5L_Crosswalk_Index_Value_Calculator.xls (value sets – France)"
            ],
            "total_questions": 6,
            "dimensions": 5,
            "dimension_levels": 5,
            "vas_range": [0, 100],
            "profile_range": ["11111", "55555"]
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
            answers: Dictionary of question_id -> answer mappings
            
        Returns:
            ValidationResult with validation status and messages
        """
        errors = []
        warnings = []
        
        # Check for missing required questions (Q1-Q5 + VAS)
        expected_keys = [f"q{i}" for i in range(1, 6)] + ["vas"]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value ranges for Q1-Q5 (1-5, NOT 0-4!)
        dimension_keys = [f"q{i}" for i in range(1, 6)]
        invalid_dims = {k: v for k, v in answers.items() 
                       if k in dimension_keys and (not isinstance(v, int) or v < 1 or v > 5)}
        if invalid_dims:
            errors.append(f"Dimensions doivent être des entiers 1–5: {invalid_dims}")
        
        # Check VAS range (0-100)
        if "vas" in answers:
            if not isinstance(answers["vas"], int) or answers["vas"] < 0 or answers["vas"] > 100:
                errors.append(f"VAS doit être un entier 0–100 (reçu: {answers['vas']})")
        
        # Clinical warnings
        if not errors:
            # Check for perfect health (11111) but low VAS
            if all(answers.get(f"q{i}", 0) == 1 for i in range(1, 6)):
                if answers.get("vas", 100) < 70:
                    warnings.append(
                        "Profil 11111 (santé parfaite) mais VAS <70 - vérifier la cohérence."
                    )
            
            # Check for severe problems (many 4s or 5s) but high VAS
            severe_count = sum(1 for i in range(1, 6) if answers.get(f"q{i}", 1) >= 4)
            if severe_count >= 3 and answers.get("vas", 0) >= 70:
                warnings.append(
                    "Problèmes sévères dans plusieurs dimensions mais VAS élevée - vérifier la cohérence."
                )
            
            # Check for maximum problems across all dimensions
            if all(answers.get(f"q{i}", 1) == 5 for i in range(1, 6)):
                warnings.append(
                    "Profil 55555 (problèmes extrêmes dans toutes les dimensions) - "
                    "état de santé critique. Évaluation clinique urgente recommandée."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_profile(self, answers: Dict[str, int]) -> str:
        """
        Calculate the 5-digit health state profile
        
        Args:
            answers: Dictionary with Q1-Q5 answers
            
        Returns:
            5-digit profile string (e.g., "21341")
        """
        return "".join(str(answers[f"q{i}"]) for i in range(1, 6))
    
    def calculate_score(self, answers: Dict[str, int]) -> ScoreResult:
        """
        Calculate EQ-5D-5L profile and VAS score
        
        Args:
            answers: Dictionary with keys 'q1' through 'q5' and 'vas'
            
        Returns:
            ScoreResult with profile, VAS, and interpretation
            
        Raises:
            EQ5D5LError: If validation fails
            
        Note:
            Index value calculation requires crosswalk table (not included).
            To calculate index values, use the France value set from:
            EQ-5D-5L_Crosswalk_Index_Value_Calculator.xls
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise EQ5D5LError("; ".join(validation.errors))
        
        # Calculate profile (5-digit code)
        profile = self.calculate_profile(answers)
        
        # Get VAS score
        vas_score = answers["vas"]
        
        # Get dimension scores
        dimension_scores = {
            "mobility": answers["q1"],
            "self_care": answers["q2"],
            "usual_activities": answers["q3"],
            "pain_discomfort": answers["q4"],
            "anxiety_depression": answers["q5"]
        }
        
        # Build interpretation
        interpretation = self._build_interpretation(
            profile, vas_score, dimension_scores, validation.warnings
        )
        
        # Note: Index value would be calculated from crosswalk table
        # For now, we return None and note it in the interpretation
        index_value = None
        
        return ScoreResult(
            profile=profile,
            vas_score=vas_score,
            index_value=index_value,
            interpretation=interpretation,
            dimension_scores=dimension_scores
        )
    
    def _build_interpretation(
        self,
        profile: str,
        vas_score: int,
        dimension_scores: Dict[str, int],
        warnings: List[str]
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Profil de santé: {profile}. VAS: {vas_score}/100. "
        
        # Interpret profile
        if profile == self.PERFECT_HEALTH_PROFILE:
            interpretation += "État de santé parfait (aucun problème dans aucune dimension). "
        elif profile == "55555":
            interpretation += "Problèmes extrêmes dans toutes les dimensions - état critique. "
        else:
            # Count problem levels
            no_problems = sum(1 for v in dimension_scores.values() if v == 1)
            severe_problems = sum(1 for v in dimension_scores.values() if v >= 4)
            
            if no_problems == 5:
                interpretation += "Aucun problème rapporté. "
            elif severe_problems >= 3:
                interpretation += f"Problèmes sévères/extrêmes dans {severe_problems} dimensions. "
            else:
                interpretation += f"{no_problems} dimension(s) sans problème, {5 - no_problems} avec problèmes. "
        
        # Interpret VAS
        if vas_score >= 80:
            interpretation += "VAS élevée (très bonne perception de santé). "
        elif vas_score >= 60:
            interpretation += "VAS modérée (perception de santé acceptable). "
        elif vas_score >= 40:
            interpretation += "VAS basse (perception de santé médiocre). "
        else:
            interpretation += "VAS très basse (perception de santé très mauvaise). "
        
        # Add warnings
        if warnings:
            interpretation += " ".join(warnings) + " "
        
        # Note about index
        interpretation += (
            "Note: Le calcul de l'index d'utilité nécessite la table de correspondance "
            "(Crosswalk) avec les valeurs françaises."
        )
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }


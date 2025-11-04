# -*- coding: utf-8 -*-
"""
EQ-5D-5L (EuroQol 5 Dimensions 5 Levels)
French version - Generic measure of health status

SCORING METHODOLOGY:
===================

The EQ-5D-5L generates three types of scores:

1. HEALTH STATE PROFILE (5-digit code)
   - Concatenates responses from 5 dimensions (Q1-Q5)
   - Each digit represents level 1-5 for that dimension
   - Example: "21341" means:
     * Q1 (Mobility): 2 = Slight problems
     * Q2 (Self-care): 1 = No problems
     * Q3 (Usual activities): 3 = Moderate problems
     * Q4 (Pain/Discomfort): 4 = Severe problems
     * Q5 (Anxiety/Depression): 1 = No problems
   - Range: "11111" (perfect health) to "55555" (worst health)
   - Total possible states: 3,125 unique profiles

2. VAS (Visual Analog Scale) SCORE
   - Direct patient rating: 0-100
   - 0 = Worst imaginable health
   - 100 = Best imaginable health
   - Captures subjective perception of overall health

3. INDEX VALUE (Utility Score)
   - Converts health state profile to single utility value
   - Uses France-specific value set (Crosswalk method)
   - Range: -0.530 to 1.000
     * 1.0 = Perfect health (11111)
     * 0.0 = Death
     * <0.0 = States worse than death
   - Automatically calculated using built-in France crosswalk table

CLINICAL INTERPRETATION:
- Profile shows specific problem areas
- VAS shows overall health perception
- Index allows cost-effectiveness analysis (QALYs)
- Inconsistencies between profile and VAS flagged as warnings
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel
from .france_crosswalk import FRANCE_CROSSWALK


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
    dimensions: Dict[str, int]


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
    - Generate health state profile (5-digit code)
    - Calculate VAS score
    - Calculate utility index using France crosswalk
    - Provide clinical interpretation
    """
    
    INSTRUMENT_ID = "EQ-5D-5L.fr"
    INSTRUMENT_NAME = "EQ-5D-5L – Version française"
    ABBREVIATION = "EQ-5D-5L"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "AUJOURD'HUI"
    
    # 5 dimensions with their text and level descriptions
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
    
    DIMENSION_NAMES = [
        "Mobilité",
        "Autonomie",
        "Activités courantes",
        "Douleurs/Gêne",
        "Anxiété/Dépression"
    ]
    
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
        
        # Q1-Q5: Five dimensions (1-5 scale)
        for i, (title, level_texts) in enumerate(self.DIMENSIONS, start=1):
            questions.append(Question(
                id=f"q{i}",
                section_id="sec_dims",
                text=f"{title} – cochez UNE case",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=level, label=level_texts[level-1], score=None)
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
            text="Votre santé AUJOURD'HUI (0=pire, 100=meilleure)",
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
                "EQ-5D-5L.pdf (version FR)",
                "EQ5D5L_CotationScore.docx (cotation et crosswalk)",
                "EQ-5D-5L_Crosswalk_Index_Value_Calculator.xls (value sets – France)"
            ],
            "total_questions": 6,
            "dimensions": 5,
            "profile_range": ["11111", "55555"],
            "vas_range": [0, 100],
            "index_range": [-0.530, 1.000]
        }
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """Get all sections"""
        return [section.dict() for section in self._sections]
    
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
        return [q.dict() for q in questions]
    
    def get_question_by_id(self, question_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific question by ID"""
        for q in self._questions:
            if q.id == question_id:
                return q.dict()
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
        
        # Check for missing required questions (Q1-Q5 and VAS)
        expected_keys = [f"q{i}" for i in range(1, 6)] + ["vas"]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check Q1-Q5 ranges (1-5)
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
            # Check for worst possible health state (55555)
            if all(answers.get(f"q{i}", 0) == 5 for i in range(1, 6)):
                warnings.append(
                    "Profil 55555 - état de santé le plus défavorable. "
                    "Vérifier la cohérence avec le score VAS."
                )
            
            # Check for inconsistency between profile and VAS
            profile_values = [answers.get(f"q{i}", 1) for i in range(1, 6)]
            avg_level = sum(profile_values) / len(profile_values)
            vas = answers.get("vas", 50)
            
            # If profile is very bad but VAS is very high (or vice versa)
            if avg_level >= 4 and vas >= 80:
                warnings.append(
                    "Incohérence possible: profil indique des problèmes sévères "
                    "mais VAS élevé. Vérifier les réponses du patient."
                )
            elif avg_level <= 2 and vas <= 30:
                warnings.append(
                    "Incohérence possible: profil indique peu de problèmes "
                    "mais VAS très bas. Vérifier les réponses du patient."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_score(self, answers: Dict[str, int]) -> ScoreResult:
        """
        Calculate EQ-5D-5L profile, VAS score, and utility index
        
        SCORING PROCESS:
        ---------------
        1. Validate all answers (q1-q5: 1-5, vas: 0-100)
        2. Generate 5-digit health state profile by concatenating q1...q5
        3. Extract VAS score directly from 'vas' answer
        4. Look up utility index from France crosswalk table
        5. Create dimensions dictionary (dimension name -> level)
        6. Generate clinical interpretation
        
        EXAMPLE:
        --------
        Input: {"q1": 2, "q2": 1, "q3": 3, "q4": 4, "q5": 1, "vas": 75}
        Output:
          - profile: "21341"
          - vas_score: 75
          - index_value: 0.474 (from France crosswalk)
          - dimensions: {
              "Mobilité": 2,
              "Autonomie": 1,
              "Activités courantes": 3,
              "Douleurs/Gêne": 4,
              "Anxiété/Dépression": 1
            }
          - interpretation: Clinical text describing health state
        
        Args:
            answers: Dictionary with keys 'q1' through 'q5' (values 1-5) and 'vas' (value 0-100)
            
        Returns:
            ScoreResult with profile, VAS score, utility index, dimensions, and interpretation
            
        Raises:
            EQ5D5LError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise EQ5D5LError("; ".join(validation.errors))
        
        # Generate 5-digit profile (e.g., "21341")
        profile = "".join(str(answers[f"q{i}"]) for i in range(1, 6))
        
        # Get VAS score
        vas_score = answers["vas"]
        
        # Look up utility index from France crosswalk table
        index_value = FRANCE_CROSSWALK.get(profile)
        if index_value is None:
            raise EQ5D5LError(f"Profile {profile} not found in France crosswalk table")
        
        # Get dimension values
        dimensions = {
            self.DIMENSION_NAMES[i]: answers[f"q{i+1}"]
            for i in range(5)
        }
        
        # Build interpretation
        interpretation = self._build_interpretation(
            profile, vas_score, index_value, dimensions, validation.warnings
        )
        
        return ScoreResult(
            profile=profile,
            vas_score=vas_score,
            index_value=index_value,
            interpretation=interpretation,
            dimensions=dimensions
        )
    
    def _build_interpretation(
        self,
        profile: str,
        vas_score: int,
        index_value: float,
        dimensions: Dict[str, int],
        warnings: List[str]
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Profil de santé: {profile}. "
        interpretation += f"Score VAS: {vas_score}/100. "
        interpretation += f"Index d'utilité (France): {index_value:.3f}. "
        
        # Interpret profile
        if profile == "11111":
            interpretation += "État de santé optimal (aucun problème dans les 5 dimensions). "
        elif profile == "55555":
            interpretation += "État de santé le plus défavorable (problèmes extrêmes dans toutes les dimensions). "
        else:
            # Count dimensions with problems
            problems = sum(1 for v in dimensions.values() if v > 1)
            severe_problems = sum(1 for v in dimensions.values() if v >= 4)
            
            if severe_problems > 0:
                interpretation += f"{severe_problems} dimension(s) avec problèmes sévères ou extrêmes. "
            elif problems > 0:
                interpretation += f"{problems} dimension(s) avec problèmes. "
        
        # Interpret VAS
        if vas_score >= 80:
            interpretation += "VAS élevé - bonne perception de l'état de santé. "
        elif vas_score >= 50:
            interpretation += "VAS moyen - perception modérée de l'état de santé. "
        else:
            interpretation += "VAS bas - perception défavorable de l'état de santé. "
        
        # Interpret utility index
        if index_value >= 0.8:
            interpretation += "Index d'utilité élevé - très bonne qualité de vie. "
        elif index_value >= 0.5:
            interpretation += "Index d'utilité modéré - qualité de vie acceptable. "
        elif index_value >= 0:
            interpretation += "Index d'utilité bas - qualité de vie altérée. "
        else:
            interpretation += "Index d'utilité négatif - état jugé pire que la mort. "
        
        # Add warnings
        if warnings:
            interpretation += " ".join(warnings) + " "
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }
    
    def get_profile_description(self, profile: str) -> Dict[str, str]:
        """
        Get human-readable description of a health state profile
        
        Converts a 5-digit health state profile into descriptive text
        for each dimension.
        
        Args:
            profile: 5-digit string (e.g., "21341") where each digit is 1-5
            
        Returns:
            Dictionary mapping dimension names to level descriptions
            
        Example:
            profile "21341" returns:
            {
                "Mobilité": "J'ai des problèmes légers pour me déplacer à pied",
                "Autonomie de la personne": "Je n'ai aucun problème...",
                ...
            }
        """
        if len(profile) != 5 or not profile.isdigit():
            raise EQ5D5LError(f"Profil invalide: {profile}. Doit être 5 chiffres 1-5.")
        
        if not all(1 <= int(d) <= 5 for d in profile):
            raise EQ5D5LError(f"Profil invalide: {profile}. Chaque chiffre doit être 1-5.")
        
        description = {}
        for i, digit in enumerate(profile):
            level = int(digit)
            dim_name, level_texts = self.DIMENSIONS[i]
            description[dim_name] = level_texts[level - 1]
        
        return description


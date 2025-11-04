# -*- coding: utf-8 -*-
"""
PRISE-M (Profil des effets indésirables médicamenteux)
French version - Medication side effects profile for psychiatric treatments
"""

from typing import Dict, List, Optional, Any, Literal
from datetime import datetime
from pydantic import BaseModel


class PRISEMError(ValueError):
    """Custom exception for PRISE-M validation errors"""
    pass


class QuestionOption(BaseModel):
    """Model for a question option"""
    code: int
    label: str
    score: int


class Question(BaseModel):
    """Model for a question"""
    id: str
    section_id: str
    text: str
    type: str
    required: bool
    options: List[QuestionOption]
    constraints: Dict[str, Any]
    gender_specific: Optional[str] = None  # "F" or "M" if gender-specific


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    question_ids: List[str]


class ScoreResult(BaseModel):
    """Model for score results"""
    total_score: int
    excluded_item: str
    gender_used: Optional[str]
    warning: Optional[str]
    section_scores: Dict[str, int]
    interpretation: str
    range: tuple = (0, 62)


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class PRISEM:
    """
    PRISE-M (Profil des effets indésirables médicamenteux) Questionnaire Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Compute scores with gender-specific item exclusion
    """
    
    INSTRUMENT_ID = "PRISE-M.fr"
    INSTRUMENT_NAME = "PRISE-M – Profil des effets indésirables médicamenteux (version française)"
    ABBREVIATION = "PRISE-M"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "Semaine écoulée"
    
    # Gender-specific items
    ITEM_FEMALE = "q20"  # Règles irrégulières (irregular periods)
    ITEM_MALE = "q25"    # Troubles de l'érection (erectile dysfunction)
    
    # Items organized by section with labels
    ITEMS_BY_SECTION = [
        # Section 1: Troubles gastro-intestinaux
        ("Diarrhée", "sec1"),
        ("Constipation", "sec1"),
        ("Bouche sèche", "sec1"),
        ("Nausée, vomissement", "sec1"),
        # Section 2: Troubles cardiaques
        ("Palpitations", "sec2"),
        ("Vertiges", "sec2"),
        ("Douleurs dans la poitrine", "sec2"),
        # Section 3: Problèmes cutanés
        ("Augmentation de la transpiration", "sec3"),
        ("Démangeaisons", "sec3"),
        ("Sécheresse de la peau", "sec3"),
        # Section 4: Troubles neurologiques
        ("Mal à la tête", "sec4"),
        ("Tremblements", "sec4"),
        ("Mauvais contrôle moteur", "sec4"),
        ("Étourdissements", "sec4"),
        # Section 5: Vision/Audition
        ("Vision floue", "sec5"),
        ("Acouphènes (bourdonnements dans les oreilles)", "sec5"),
        # Section 6: Troubles uro-génital
        ("Difficultés pour uriner", "sec6"),
        ("Mictions douloureuses", "sec6"),
        ("Mictions fréquentes", "sec6"),
        ("Règles irrégulières (pour les femmes)", "sec6"),  # q20 - FEMALE
        # Section 7: Problèmes de sommeil
        ("Difficultés d'endormissement", "sec7"),
        ("Augmentation du temps de sommeil", "sec7"),
        # Section 8: Fonctions sexuelles
        ("Perte du désir sexuel", "sec8"),
        ("Difficultés à atteindre un orgasme", "sec8"),
        ("Troubles de l'érection (pour les hommes)", "sec8"),  # q25 - MALE
        # Section 9: Autres troubles
        ("Anxiété", "sec9"),
        ("Difficultés de concentration", "sec9"),
        ("Malaise général", "sec9"),
        ("Agitation", "sec9"),
        ("Fatigue", "sec9"),
        ("Diminution de l'énergie", "sec9"),
        ("Prise de poids", "sec9")
    ]
    
    SECTION_LABELS = [
        ("sec1", "1. Troubles gastro-intestinaux"),
        ("sec2", "2. Troubles cardiaques"),
        ("sec3", "3. Problèmes cutanés"),
        ("sec4", "4. Troubles neurologiques"),
        ("sec5", "5. Vision/Audition"),
        ("sec6", "6. Troubles uro-génital"),
        ("sec7", "7. Problèmes de sommeil"),
        ("sec8", "8. Fonctions sexuelles"),
        ("sec9", "9. Autres troubles")
    ]
    
    def __init__(self):
        """Initialize the PRISE-M questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        sections = []
        
        # Build section to questions mapping
        section_questions = {sec_id: [] for sec_id, _ in self.SECTION_LABELS}
        for i, (text, sec_id) in enumerate(self.ITEMS_BY_SECTION, start=1):
            section_questions[sec_id].append(f"q{i}")
        
        # Create sections
        for sec_id, label in self.SECTION_LABELS:
            sections.append(Section(
                id=sec_id,
                label=label,
                question_ids=section_questions[sec_id]
            ))
        
        return sections
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = []
        
        for i, (text, sec_id) in enumerate(self.ITEMS_BY_SECTION, start=1):
            q_id = f"q{i}"
            
            # Determine if gender-specific
            gender_specific = None
            if q_id == self.ITEM_FEMALE:
                gender_specific = "F"
            elif q_id == self.ITEM_MALE:
                gender_specific = "M"
            
            questions.append(Question(
                id=q_id,
                section_id=sec_id,
                text=text,
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Absent", score=0),
                    QuestionOption(code=1, label="Tolérable", score=1),
                    QuestionOption(code=2, label="Pénible", score=2)
                ],
                constraints={
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2]
                },
                gender_specific=gender_specific
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
            "description": "Questionnaire de 32 items cotés 0–2 (ABSENT=0, TOLÉRABLE=1, PÉNIBLE=2). Score = somme de 31 items avec un item alternatif selon le sexe (♀ Règles irrégulières / ♂ Troubles de l'érection).",
            "sources": [
                "PRISE-M.pdf (formulaire FR)",
                "PRISE-M_CotationScore.docx (consignes et cotation)"
            ],
            "total_questions": 32,
            "scoring_range": [0, 62],
            "gender_specific_items": {
                "female": self.ITEM_FEMALE,
                "male": self.ITEM_MALE
            },
            "sections": len(self._sections),
            "scoring_note": "Le score total somme 31 items (32 moins 1 item selon le sexe)"
        }
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """Get all sections"""
        return [section.dict() for section in self._sections]
    
    def get_questions(
        self, 
        section_id: Optional[str] = None,
        gender: Optional[Literal["F", "M"]] = None
    ) -> List[Dict[str, Any]]:
        """
        Get questions, optionally filtered by section and/or gender
        
        Args:
            section_id: Optional section ID to filter questions
            gender: Optional gender to filter gender-specific questions
            
        Returns:
            List of questions as dictionaries
        """
        questions = self._questions
        
        if section_id:
            questions = [q for q in questions if q.section_id == section_id]
        
        if gender:
            # Filter out the gender-specific item not relevant to this gender
            gender_upper = gender.upper()
            if gender_upper == "F":
                questions = [q for q in questions if q.id != self.ITEM_MALE]
            elif gender_upper == "M":
                questions = [q for q in questions if q.id != self.ITEM_FEMALE]
        
        return [q.dict() for q in questions]
    
    def get_question_by_id(self, question_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific question by ID"""
        for q in self._questions:
            if q.id == question_id:
                return q.dict()
        return None
    
    def validate_answers(
        self, 
        answers: Dict[str, int],
        gender: Optional[Literal["F", "M"]] = None
    ) -> ValidationResult:
        """
        Validate provided answers
        
        Args:
            answers: Dictionary of question_id -> answer mappings (0-2)
            gender: Optional gender ("F" or "M")
            
        Returns:
            ValidationResult with validation status and messages
        """
        errors = []
        warnings = []
        
        # Check for missing required questions
        expected_keys = [f"q{i}" for i in range(1, 33)]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value ranges (0, 1, or 2)
        invalid = {k: v for k, v in answers.items() 
                  if k in expected_keys and (not isinstance(v, int) or v not in (0, 1, 2))}
        if invalid:
            errors.append(f"Valeurs invalides (0, 1 ou 2 attendus): {invalid}")
        
        # Clinical warnings (only if no errors)
        if not errors:
            # Check gender-specific items
            val_female = answers.get(self.ITEM_FEMALE, 0)
            val_male = answers.get(self.ITEM_MALE, 0)
            
            # Warning if both gender-specific items are endorsed
            if val_female != 0 and val_male != 0:
                warnings.append(
                    f"Les deux items spécifiques au sexe sont renseignés: "
                    f"{self.ITEM_FEMALE} (femme)={val_female}, {self.ITEM_MALE} (homme)={val_male}. "
                    f"Vérifier la cohérence."
                )
            
            # Warning if gender not provided and items are ambiguous
            if gender is None and val_female == 0 and val_male == 0:
                warnings.append(
                    "Sexe non fourni et les deux items spécifiques au sexe sont absents. "
                    "L'item masculin sera exclu par défaut."
                )
            
            # Check for severe burden (many items at level 2)
            severe_count = sum(1 for k in expected_keys if answers.get(k, 0) == 2)
            if severe_count >= 10:
                warnings.append(
                    f"{severe_count} items sont cotés 'Pénible' (2). "
                    "Charge élevée d'effets indésirables - révision du traitement recommandée."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def _determine_excluded_item(
        self, 
        answers: Dict[str, int],
        gender: Optional[Literal["F", "M"]]
    ) -> tuple[str, Optional[str]]:
        """
        Determine which gender-specific item to exclude from scoring
        
        Returns:
            (excluded_item_id, warning_message)
        """
        # If gender is explicitly provided, use it
        if gender:
            gender_upper = gender.upper()
            if gender_upper == "F":
                return self.ITEM_MALE, None
            elif gender_upper == "M":
                return self.ITEM_FEMALE, None
        
        # If gender not provided, infer from responses
        val_female = answers.get(self.ITEM_FEMALE, 0)
        val_male = answers.get(self.ITEM_MALE, 0)
        
        # If only female item is endorsed, assume female
        if val_female != 0 and val_male == 0:
            return self.ITEM_MALE, (
                f"Sexe non fourni: exclusion de {self.ITEM_MALE} (homme) "
                f"car {self.ITEM_FEMALE} (femme) est renseigné."
            )
        
        # If only male item is endorsed, assume male
        if val_male != 0 and val_female == 0:
            return self.ITEM_FEMALE, (
                f"Sexe non fourni: exclusion de {self.ITEM_FEMALE} (femme) "
                f"car {self.ITEM_MALE} (homme) est renseigné."
            )
        
        # Default: exclude male item
        return self.ITEM_MALE, f"Sexe non fourni: exclusion par défaut de {self.ITEM_MALE}."
    
    def calculate_score(
        self, 
        answers: Dict[str, int],
        gender: Optional[Literal["F", "M"]] = None
    ) -> ScoreResult:
        """
        Calculate PRISE-M total score
        
        Args:
            answers: Dictionary with keys 'q1' through 'q32', values 0-2
            gender: Optional gender ("F" or "M") for determining which item to exclude
            
        Returns:
            ScoreResult with total score, excluded item, and interpretation
            
        Raises:
            PRISEMError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers, gender)
        if not validation.valid:
            raise PRISEMError("; ".join(validation.errors))
        
        # Determine which item to exclude
        excluded_item, warning = self._determine_excluded_item(answers, gender)
        
        # Calculate total score (sum of 31 items, excluding gender-specific item)
        total = sum(
            answers[f"q{i}"] 
            for i in range(1, 33) 
            if f"q{i}" != excluded_item
        )
        
        # Calculate section scores
        section_scores = self._calculate_section_scores(answers, excluded_item)
        
        # Safety check
        if total < 0 or total > 62:
            raise PRISEMError(f"Score hors bornes: {total}")
        
        # Determine gender used
        gender_used = None
        if excluded_item == self.ITEM_MALE:
            gender_used = "F"
        elif excluded_item == self.ITEM_FEMALE:
            gender_used = "M"
        
        # Build interpretation
        interpretation = self._build_interpretation(
            total, section_scores, gender_used, validation.warnings
        )
        
        return ScoreResult(
            total_score=total,
            excluded_item=excluded_item,
            gender_used=gender_used,
            warning=warning,
            section_scores=section_scores,
            interpretation=interpretation
        )
    
    def _calculate_section_scores(
        self, 
        answers: Dict[str, int],
        excluded_item: str
    ) -> Dict[str, int]:
        """Calculate scores for each section"""
        section_scores = {}
        
        for section in self._sections:
            # Sum all items in this section, except the excluded one
            score = sum(
                answers.get(q_id, 0)
                for q_id in section.question_ids
                if q_id != excluded_item
            )
            section_scores[section.id] = score
        
        return section_scores
    
    def _build_interpretation(
        self, 
        total: int,
        section_scores: Dict[str, int],
        gender_used: Optional[str],
        warnings: List[str]
    ) -> str:
        """Build clinical interpretation text"""
        gender_label = "FEMME" if gender_used == "F" else ("HOMME" if gender_used == "M" else "NON SPÉCIFIÉ")
        interpretation = f"Score total PRISE-M: {total}/62 (sexe: {gender_label}). "
        
        # Severity interpretation
        if total >= 40:
            interpretation += "Score très élevé (≥40) indiquant une charge importante d'effets indésirables. "
        elif total >= 25:
            interpretation += "Score élevé (25-39) suggérant des effets indésirables significatifs. "
        elif total >= 15:
            interpretation += "Score modéré (15-24) avec effets indésirables présents mais modérés. "
        else:
            interpretation += "Score bas (<15) suggérant peu d'effets indésirables. "
        
        # Highlight problematic sections
        problematic_sections = []
        for sec_id, score in section_scores.items():
            section = next(s for s in self._sections if s.id == sec_id)
            # Calculate max possible for this section
            max_score = len(section.question_ids) * 2
            # Adjust if excluded item is in this section
            if any(q in [self.ITEM_FEMALE, self.ITEM_MALE] for q in section.question_ids):
                max_score -= 2  # One less item
            
            if max_score > 0:
                percentage = (score / max_score) * 100
                if percentage >= 60:  # Section with high burden
                    section_label = section.label.split(". ", 1)[1] if ". " in section.label else section.label
                    problematic_sections.append(f"{section_label} ({score}/{max_score})")
        
        if problematic_sections:
            interpretation += f"Sections problématiques: {', '.join(problematic_sections)}. "
        
        # Clinical recommendation
        if total >= 25:
            interpretation += (
                "Révision du traitement médicamenteux recommandée. "
                "Envisager ajustement posologique, changement de molécule, "
                "ou traitement symptomatique des effets indésirables."
            )
        elif total >= 15:
            interpretation += "Suivi régulier recommandé pour surveiller l'évolution des effets indésirables."
        
        # Add warnings
        if warnings:
            interpretation += " " + " ".join(warnings)
        
        return interpretation.strip()
    
    def get_full_questionnaire(
        self,
        gender: Optional[Literal["F", "M"]] = None
    ) -> Dict[str, Any]:
        """
        Get complete questionnaire structure for frontend
        
        Args:
            gender: Optional gender to filter gender-specific questions
        """
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions(gender=gender)
        }


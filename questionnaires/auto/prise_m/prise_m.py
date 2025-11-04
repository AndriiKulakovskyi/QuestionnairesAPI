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
    display_if: Optional[Dict[str, Any]] = None  # JSONLogic condition for visibility
    required_if: Optional[Dict[str, Any]] = None  # JSONLogic condition for conditional requirement


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    question_ids: List[str]


class ScoreResult(BaseModel):
    """Model for score results"""
    total_score: int
    excluded_items: List[str]  # Changed from excluded_item to excluded_items
    items_scored: int  # Number of items actually scored
    gender_used: Optional[str]
    warning: Optional[str]
    section_scores: Dict[str, int]
    interpretation: str
    range: tuple = (0, 62)  # Default, adjusted based on items_scored


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
        """Build all questions with conditional logic"""
        questions = []
        
        for i, (text, sec_id) in enumerate(self.ITEMS_BY_SECTION, start=1):
            q_id = f"q{i}"
            
            # Determine if gender-specific and add conditional logic
            gender_specific = None
            display_if = None
            required_if = None
            
            if q_id == self.ITEM_FEMALE:
                # Q20: Only show for females
                gender_specific = "F"
                display_if = {"==": [{"var": "gender"}, "F"]}
                required_if = {"==": [{"var": "gender"}, "F"]}
            elif q_id == self.ITEM_MALE:
                # Q25: Only show for males
                gender_specific = "M"
                display_if = {"==": [{"var": "gender"}, "M"]}
                required_if = {"==": [{"var": "gender"}, "M"]}
            
            # Gender-specific questions are not hard-required
            # They become required only when visible (via required_if)
            base_required = True if gender_specific is None else False
            
            questions.append(Question(
                id=q_id,
                section_id=sec_id,
                text=text,
                type="single_choice",
                required=base_required,
                options=[
                    QuestionOption(code=0, label="Absent", score=0),
                    QuestionOption(code=1, label="Tolérable", score=1),
                    QuestionOption(code=2, label="Pénible", score=2)
                ],
                constraints={
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2]
                },
                gender_specific=gender_specific,
                display_if=display_if,
                required_if=required_if
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
            "scoring_note": "Le score total somme 31 items (32 moins 1 item selon le sexe)",
            "branching_logic": {
                "type": "gender_conditional",
                "description": "Questions q20 and q25 are conditionally shown based on gender"
            }
        }
    
    def get_respondent_schema(self) -> Dict[str, Any]:
        """
        Get respondent demographic schema required for this questionnaire.
        This defines where gender comes from and how it's captured.
        """
        return {
            "schema_version": "1.0",
            "description": "Demographic information required for PRISE-M administration",
            "fields": [
                {
                    "id": "gender",
                    "label": "Sexe",
                    "label_en": "Gender",
                    "type": "single_choice",
                    "required": True,
                    "purpose": "Determines which gender-specific question to display (q20 for F, q25 for M)",
                    "options": [
                        {
                            "code": "F",
                            "label": "Femme",
                            "label_en": "Female",
                            "triggers": "Shows q20 (irregular periods), hides q25 (erectile dysfunction)"
                        },
                        {
                            "code": "M",
                            "label": "Homme",
                            "label_en": "Male",
                            "triggers": "Shows q25 (erectile dysfunction), hides q20 (irregular periods)"
                        },
                        {
                            "code": "X",
                            "label": "Autre / Préfère ne pas dire",
                            "label_en": "Other / Prefer not to say",
                            "triggers": "Hides both q20 and q25, scoring uses 30 items"
                        }
                    ],
                    "validation": {
                        "required_message": "Gender is required to determine which questions to display"
                    }
                }
            ],
            "notes": [
                "Gender must be collected before displaying questionnaire items",
                "Gender determines visibility of q20 (female-specific) and q25 (male-specific)",
                "For non-binary/other gender, both items are hidden and scoring adjusts accordingly"
            ]
        }
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """Get all sections"""
        return [section.model_dump() for section in self._sections]
    
    def get_questions(
        self, 
        section_id: Optional[str] = None,
        gender: Optional[Literal["F", "M", "X"]] = None
    ) -> List[Dict[str, Any]]:
        """
        Get questions, optionally filtered by section and/or gender
        
        Args:
            section_id: Optional section ID to filter questions
            gender: Optional gender to filter gender-specific questions
                    "F" = Female (shows q20, hides q25)
                    "M" = Male (shows q25, hides q20)
                    "X" = Other/Non-binary (hides both q20 and q25)
            
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
            elif gender_upper == "X":
                # For non-binary/other, exclude both gender-specific items
                questions = [q for q in questions if q.id not in [self.ITEM_FEMALE, self.ITEM_MALE]]
        
        return [q.model_dump() for q in questions]
    
    def get_question_by_id(self, question_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific question by ID"""
        for q in self._questions:
            if q.id == question_id:
                return q.model_dump()
        return None
    
    def validate_answers(
        self, 
        answers: Dict[str, int],
        gender: Optional[Literal["F", "M", "X"]] = None
    ) -> ValidationResult:
        """
        Validate provided answers
        
        Args:
            answers: Dictionary of question_id -> answer mappings (0-2)
            gender: Optional gender ("F", "M", or "X")
            
        Returns:
            ValidationResult with validation status and messages
        """
        errors = []
        warnings = []
        
        # Determine which questions are expected based on gender
        expected_keys = [f"q{i}" for i in range(1, 33)]
        if gender:
            gender_upper = gender.upper()
            if gender_upper == "F":
                # Female: exclude q25
                expected_keys = [k for k in expected_keys if k != self.ITEM_MALE]
            elif gender_upper == "M":
                # Male: exclude q20
                expected_keys = [k for k in expected_keys if k != self.ITEM_FEMALE]
            elif gender_upper == "X":
                # Non-binary/Other: exclude both q20 and q25
                expected_keys = [k for k in expected_keys if k not in [self.ITEM_FEMALE, self.ITEM_MALE]]
        
        # Check for missing required questions
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value ranges (0, 1, or 2)
        all_keys = [f"q{i}" for i in range(1, 33)]
        invalid = {k: v for k, v in answers.items() 
                  if k in all_keys and (not isinstance(v, int) or v not in (0, 1, 2))}
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
    
    def _determine_excluded_items(
        self, 
        answers: Dict[str, int],
        gender: Optional[Literal["F", "M", "X"]]
    ) -> tuple[List[str], Optional[str]]:
        """
        Determine which gender-specific items to exclude from scoring
        
        Returns:
            (excluded_item_ids, warning_message)
        """
        # If gender is explicitly provided, use it
        if gender:
            gender_upper = gender.upper()
            if gender_upper == "F":
                return [self.ITEM_MALE], None
            elif gender_upper == "M":
                return [self.ITEM_FEMALE], None
            elif gender_upper == "X":
                # Non-binary/Other: exclude both items
                return [self.ITEM_FEMALE, self.ITEM_MALE], (
                    f"Sexe non-binaire/autre: exclusion de {self.ITEM_FEMALE} et {self.ITEM_MALE}. "
                    "Score basé sur 30 items."
                )
        
        # If gender not provided, infer from responses
        val_female = answers.get(self.ITEM_FEMALE, 0)
        val_male = answers.get(self.ITEM_MALE, 0)
        
        # If only female item is endorsed, assume female
        if val_female != 0 and val_male == 0:
            return [self.ITEM_MALE], (
                f"Sexe non fourni: exclusion de {self.ITEM_MALE} (homme) "
                f"car {self.ITEM_FEMALE} (femme) est renseigné."
            )
        
        # If only male item is endorsed, assume male
        if val_male != 0 and val_female == 0:
            return [self.ITEM_FEMALE], (
                f"Sexe non fourni: exclusion de {self.ITEM_FEMALE} (femme) "
                f"car {self.ITEM_MALE} (homme) est renseigné."
            )
        
        # Default: exclude male item
        return [self.ITEM_MALE], f"Sexe non fourni: exclusion par défaut de {self.ITEM_MALE}."
    
    def calculate_score(
        self, 
        answers: Dict[str, int],
        gender: Optional[Literal["F", "M", "X"]] = None
    ) -> ScoreResult:
        """
        Calculate PRISE-M total score
        
        Args:
            answers: Dictionary with keys 'q1' through 'q32', values 0-2
            gender: Optional gender ("F", "M", or "X") for determining which items to exclude
                    "F" = Female: score 31 items (exclude q25), range 0-62
                    "M" = Male: score 31 items (exclude q20), range 0-62
                    "X" = Other/Non-binary: score 30 items (exclude both q20 and q25), range 0-60
            
        Returns:
            ScoreResult with total score, excluded items, and interpretation
            
        Raises:
            PRISEMError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers, gender)
        if not validation.valid:
            raise PRISEMError("; ".join(validation.errors))
        
        # Determine which items to exclude
        excluded_items, warning = self._determine_excluded_items(answers, gender)
        
        # Calculate total score (sum of items, excluding gender-specific items)
        total = sum(
            answers[f"q{i}"] 
            for i in range(1, 33) 
            if f"q{i}" not in excluded_items
        )
        
        # Calculate items scored
        items_scored = 32 - len(excluded_items)
        
        # Calculate section scores
        section_scores = self._calculate_section_scores(answers, excluded_items)
        
        # Determine expected range based on items scored
        max_score = items_scored * 2
        
        # Safety check
        if total < 0 or total > max_score:
            raise PRISEMError(f"Score hors bornes: {total} (attendu 0-{max_score})")
        
        # Determine gender used
        gender_used = None
        if self.ITEM_MALE in excluded_items and self.ITEM_FEMALE not in excluded_items:
            gender_used = "F"
        elif self.ITEM_FEMALE in excluded_items and self.ITEM_MALE not in excluded_items:
            gender_used = "M"
        elif self.ITEM_MALE in excluded_items and self.ITEM_FEMALE in excluded_items:
            gender_used = "X"
        
        # Build interpretation
        interpretation = self._build_interpretation(
            total, section_scores, gender_used, validation.warnings, items_scored
        )
        
        return ScoreResult(
            total_score=total,
            excluded_items=excluded_items,
            items_scored=items_scored,
            gender_used=gender_used,
            warning=warning,
            section_scores=section_scores,
            interpretation=interpretation,
            range=(0, max_score)
        )
    
    def _calculate_section_scores(
        self, 
        answers: Dict[str, int],
        excluded_items: List[str]
    ) -> Dict[str, int]:
        """Calculate scores for each section"""
        section_scores = {}
        
        for section in self._sections:
            # Sum all items in this section, except the excluded ones
            score = sum(
                answers.get(q_id, 0)
                for q_id in section.question_ids
                if q_id not in excluded_items
            )
            section_scores[section.id] = score
        
        return section_scores
    
    def _build_interpretation(
        self, 
        total: int,
        section_scores: Dict[str, int],
        gender_used: Optional[str],
        warnings: List[str],
        items_scored: int
    ) -> str:
        """Build clinical interpretation text"""
        gender_label = (
            "FEMME" if gender_used == "F" else 
            "HOMME" if gender_used == "M" else 
            "NON-BINAIRE/AUTRE" if gender_used == "X" else 
            "NON SPÉCIFIÉ"
        )
        max_score = items_scored * 2
        interpretation = f"Score total PRISE-M: {total}/{max_score} (sexe: {gender_label}, {items_scored} items). "
        
        # Severity interpretation (adjusted thresholds for non-standard item counts)
        # For 31 items (F/M): standard thresholds
        # For 30 items (X): adjust proportionally
        threshold_high_severe = 40 if items_scored == 31 else int(40 * items_scored / 31)
        threshold_high = 25 if items_scored == 31 else int(25 * items_scored / 31)
        threshold_moderate = 15 if items_scored == 31 else int(15 * items_scored / 31)
        
        if total >= threshold_high_severe:
            interpretation += f"Score très élevé (≥{threshold_high_severe}) indiquant une charge importante d'effets indésirables. "
        elif total >= threshold_high:
            interpretation += f"Score élevé ({threshold_high}-{threshold_high_severe-1}) suggérant des effets indésirables significatifs. "
        elif total >= threshold_moderate:
            interpretation += f"Score modéré ({threshold_moderate}-{threshold_high-1}) avec effets indésirables présents mais modérés. "
        else:
            interpretation += f"Score bas (<{threshold_moderate}) suggérant peu d'effets indésirables. "
        
        # Highlight problematic sections
        problematic_sections = []
        for sec_id, score in section_scores.items():
            section = next(s for s in self._sections if s.id == sec_id)
            # Calculate max possible for this section (accounting for excluded items)
            section_item_count = len(section.question_ids)
            # Check if any excluded items are in this section
            excluded_in_section = sum(1 for q in section.question_ids if q in [self.ITEM_FEMALE, self.ITEM_MALE])
            max_score_section = (section_item_count - excluded_in_section) * 2
            
            if max_score_section > 0:
                percentage = (score / max_score_section) * 100
                if percentage >= 60:  # Section with high burden
                    section_label = section.label.split(". ", 1)[1] if ". " in section.label else section.label
                    problematic_sections.append(f"{section_label} ({score}/{max_score_section})")
        
        if problematic_sections:
            interpretation += f"Sections problématiques: {', '.join(problematic_sections)}. "
        
        # Clinical recommendation
        if total >= threshold_high:
            interpretation += (
                "Révision du traitement médicamenteux recommandée. "
                "Envisager ajustement posologique, changement de molécule, "
                "ou traitement symptomatique des effets indésirables."
            )
        elif total >= threshold_moderate:
            interpretation += "Suivi régulier recommandé pour surveiller l'évolution des effets indésirables."
        
        # Add warnings
        if warnings:
            interpretation += " " + " ".join(warnings)
        
        return interpretation.strip()
    
    def get_branching_logic(self) -> Dict[str, Any]:
        """
        Get explicit branching logic rules for frontend implementation.
        This provides machine-readable visibility and requirement rules.
        """
        return {
            "schema_version": "1.0",
            "type": "conditional_visibility",
            "rules": [
                {
                    "rule_id": "q20_visibility",
                    "question_id": "q20",
                    "rule_type": "display",
                    "condition": {"==": [{"var": "gender"}, "F"]},
                    "description": "Show q20 (irregular periods) only for females",
                    "action_if_true": "show",
                    "action_if_false": "hide"
                },
                {
                    "rule_id": "q20_requirement",
                    "question_id": "q20",
                    "rule_type": "required",
                    "condition": {"==": [{"var": "gender"}, "F"]},
                    "description": "q20 is required only when visible (female)",
                    "action_if_true": "required",
                    "action_if_false": "optional"
                },
                {
                    "rule_id": "q25_visibility",
                    "question_id": "q25",
                    "rule_type": "display",
                    "condition": {"==": [{"var": "gender"}, "M"]},
                    "description": "Show q25 (erectile dysfunction) only for males",
                    "action_if_true": "show",
                    "action_if_false": "hide"
                },
                {
                    "rule_id": "q25_requirement",
                    "question_id": "q25",
                    "rule_type": "required",
                    "condition": {"==": [{"var": "gender"}, "M"]},
                    "description": "q25 is required only when visible (male)",
                    "action_if_true": "required",
                    "action_if_false": "optional"
                }
            ],
            "context_variables": {
                "gender": {
                    "source": "respondent.gender",
                    "type": "string",
                    "allowed_values": ["F", "M", "X"],
                    "description": "Gender from respondent demographics"
                }
            },
            "fallback_behavior": {
                "when_gender_is_X": {
                    "q20": "hide",
                    "q25": "hide",
                    "scoring_adjustment": "use_30_items",
                    "description": "For non-binary/other gender, hide both items"
                },
                "when_gender_missing": {
                    "action": "block_questionnaire",
                    "message": "Gender is required to determine which questions to display"
                }
            },
            "scoring_logic": {
                "method": "sum",
                "items_included": "all_visible",
                "conditional_inclusions": [
                    {
                        "condition": {"==": [{"var": "gender"}, "F"]},
                        "include": ["q20"],
                        "exclude": ["q25"],
                        "expected_item_count": 31,
                        "score_range": [0, 62]
                    },
                    {
                        "condition": {"==": [{"var": "gender"}, "M"]},
                        "include": ["q25"],
                        "exclude": ["q20"],
                        "expected_item_count": 31,
                        "score_range": [0, 62]
                    },
                    {
                        "condition": {"==": [{"var": "gender"}, "X"]},
                        "include": [],
                        "exclude": ["q20", "q25"],
                        "expected_item_count": 30,
                        "score_range": [0, 60]
                    }
                ],
                "on_missing_response": "block_submit",
                "validation_message": "All visible questions must be answered before submission"
            }
        }
    
    def get_full_questionnaire(
        self,
        gender: Optional[Literal["F", "M", "X"]] = None,
        include_logic: bool = True
    ) -> Dict[str, Any]:
        """
        Get complete questionnaire structure for frontend
        
        Args:
            gender: Optional gender to filter gender-specific questions ("F", "M", or "X")
            include_logic: Whether to include branching logic and respondent schema
        """
        result = {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions(gender=gender)
        }
        
        if include_logic:
            result["respondent"] = self.get_respondent_schema()
            result["logic"] = self.get_branching_logic()
        
        return result


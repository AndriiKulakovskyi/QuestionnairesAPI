# -*- coding: utf-8 -*-
"""
MDQ (Mood Disorder Questionnaire)
French version - Screening tool for bipolar disorder spectrum
"""

from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
from pydantic import BaseModel, Field


class MDQError(ValueError):
    """Custom exception for MDQ validation errors"""
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
    display_if: Optional[Dict[str, Any]] = None  # JSONLogic condition for visibility
    required_if: Optional[Dict[str, Any]] = None  # JSONLogic condition for conditional requirement


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    description: str
    question_ids: List[str]


class ScreeningResult(BaseModel):
    """Model for screening results"""
    q1_total: int
    q2_concurrent: bool
    q3_impact_level: int
    q3_impact_label: str
    screening_result: str
    interpretation: str


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class MDQ:
    """
    MDQ (Mood Disorder Questionnaire) Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Compute screening results
    """
    
    INSTRUMENT_ID = "MDQ.fr"
    INSTRUMENT_NAME = "Questionnaire des Troubles de l'Humeur (MDQ) – Version française"
    ABBREVIATION = "MDQ"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "Au cours de votre vie (épisodes passés ou actuels)"
    
    # Q1 item texts from official French version
    Q1_TEXTS = [
        "… vous vous sentiez si bien et si remonté que d'autres pensaient que vous n'étiez pas comme d'habitude ou que vous alliez vous attirer des ennuis",
        "… vous étiez si irritable que vous criiez après les gens ou provoquiez des bagarres ou des disputes",
        "… vous vous sentiez beaucoup plus sûr(e) de vous que d'habitude",
        "… vous dormiez beaucoup moins que d'habitude et cela ne vous manquait pas vraiment",
        "… vous étiez beaucoup plus bavard(e) et parliez beaucoup plus vite que d'habitude",
        "… des pensées traversaient rapidement votre tête et vous ne pouviez pas les ralentir",
        "… vous étiez si facilement distrait(e) que vous aviez des difficultés à vous concentrer ou à poursuivre la même idée",
        "… vous aviez beaucoup plus d'énergie que d'habitude",
        "… vous étiez beaucoup plus actif(ve) ou faisiez beaucoup plus de choses que d'habitude",
        "… vous étiez beaucoup plus sociable ou extraverti(e), par ex. vous téléphoniez à vos amis la nuit",
        "… vous étiez beaucoup plus intéressé(e) par le sexe que d'habitude",
        "… vous faisiez des choses inhabituelles ou jugées excessives, imprudentes ou risquées",
        "… vous dépensiez de l'argent d'une manière si inadaptée que cela vous attirait des ennuis pour vous ou votre famille"
    ]
    
    Q3_IMPACT_LABELS = {
        0: "Pas de problème",
        1: "Problème mineur",
        2: "Problème moyen",
        3: "Problème sérieux"
    }
    
    def __init__(self):
        """Initialize the MDQ questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="sec1",
                label="Question 1 (13 items)",
                description="Symptômes maniaques/hypomaniaques",
                question_ids=[f"q1_{i}" for i in range(1, 14)]
            ),
            Section(
                id="sec2",
                label="Questions 2 et 3",
                description="Concordance temporelle et impact fonctionnel",
                question_ids=["q2", "q3"]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions with conditional logic"""
        questions = []
        
        # Build Q1 items (13 yes/no questions)
        for i, text in enumerate(self.Q1_TEXTS, start=1):
            questions.append(Question(
                id=f"q1_{i}",
                section_id="sec1",
                text=f"1.{i} {text}",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=1, label="Oui", score=1),
                    QuestionOption(code=0, label="Non", score=0)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1]}
            ))
        
        # Build the condition for Q2 and Q3: sum of Q1 items >= 2
        q1_sum_condition = {
            ">=": [
                {"+": [
                    {"var": f"answers.q1_{i}"} for i in range(1, 14)
                ]},
                2
            ]
        }
        
        # Q2: Temporal concurrence (conditional on Q1 sum >= 2)
        questions.append(Question(
            id="q2",
            section_id="sec2",
            text="2. Si ≥2 réponses 'oui' à la Q1, ces réponses sont-elles apparues durant la même période ?",
            type="single_choice",
            required=False,  # Not hard-required, becomes required when visible
            display_if=q1_sum_condition,
            required_if=q1_sum_condition,
            options=[
                QuestionOption(code=1, label="Oui", score=None),
                QuestionOption(code=0, label="Non", score=None)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1]}
        ))
        
        # Q3: Functional impact (conditional on Q1 sum >= 2)
        questions.append(Question(
            id="q3",
            section_id="sec2",
            text="3. À quel point ces problèmes ont-ils eu un impact sur votre fonctionnement ?",
            type="single_choice",
            required=False,  # Not hard-required, becomes required when visible
            display_if=q1_sum_condition,
            required_if=q1_sum_condition,
            options=[
                QuestionOption(code=0, label="Pas de problème", score=None),
                QuestionOption(code=1, label="Problème mineur", score=None),
                QuestionOption(code=2, label="Problème moyen", score=None),
                QuestionOption(code=3, label="Problème sérieux", score=None)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
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
            "description": "Outil de dépistage du trouble bipolaire (spectre) en 13 items principaux (oui/non) + 2 questions d'agrégation temporelle et d'impact fonctionnel.",
            "sources": [
                "Hirschfeld RM et al., Am J Psychiatry, 2000",
                "mdq.pdf (version FR fournie)",
                "MDQ_CotationScore.docx (règles de cotation)"
            ],
            "notes": [
                "Critères positifs classiques: ≥7 réponses 'oui' à Q1 + Q2='oui' + Q3='problème moyen' ou 'problème sérieux'."
            ],
            "total_questions": 15,
            "screening_criteria": "MDQ POSITIF si (Q1≥7) ET (Q2=oui) ET (Q3=problème moyen ou sérieux)"
        }
    
    def get_branching_logic(self) -> Dict[str, Any]:
        """
        Get explicit branching logic rules for frontend implementation.
        This provides machine-readable visibility and requirement rules.
        """
        # Build the list of Q1 item IDs for the condition
        q1_items = [f"q1_{i}" for i in range(1, 14)]
        
        return {
            "schema_version": "1.0",
            "type": "answer_dependent",
            "description": "Q2 and Q3 are only shown if at least 2 'yes' answers in Q1",
            "rules": [
                {
                    "rule_id": "q2_visibility",
                    "question_id": "q2",
                    "rule_type": "display",
                    "condition": {
                        ">=": [
                            {"+": [{"var": f"answers.{item}"} for item in q1_items]},
                            2
                        ]
                    },
                    "description": "Show Q2 only if at least 2 'yes' answers in Q1",
                    "action_if_true": "show",
                    "action_if_false": "hide"
                },
                {
                    "rule_id": "q2_requirement",
                    "question_id": "q2",
                    "rule_type": "required",
                    "condition": {
                        ">=": [
                            {"+": [{"var": f"answers.{item}"} for item in q1_items]},
                            2
                        ]
                    },
                    "description": "Q2 is required only when visible (Q1 sum >= 2)",
                    "action_if_true": "required",
                    "action_if_false": "optional"
                },
                {
                    "rule_id": "q3_visibility",
                    "question_id": "q3",
                    "rule_type": "display",
                    "condition": {
                        ">=": [
                            {"+": [{"var": f"answers.{item}"} for item in q1_items]},
                            2
                        ]
                    },
                    "description": "Show Q3 only if at least 2 'yes' answers in Q1",
                    "action_if_true": "show",
                    "action_if_false": "hide"
                },
                {
                    "rule_id": "q3_requirement",
                    "question_id": "q3",
                    "rule_type": "required",
                    "condition": {
                        ">=": [
                            {"+": [{"var": f"answers.{item}"} for item in q1_items]},
                            2
                        ]
                    },
                    "description": "Q3 is required only when visible (Q1 sum >= 2)",
                    "action_if_true": "required",
                    "action_if_false": "optional"
                }
            ],
            "context_variables": {
                "q1_sum": {
                    "source": "calculated",
                    "formula": {
                        "sum": q1_items
                    },
                    "type": "integer",
                    "range": [0, 13],
                    "description": "Sum of all Q1 'yes' responses"
                }
            },
            "fallback_behavior": {
                "when_q1_sum_lt_2": {
                    "q2": "hide",
                    "q3": "hide",
                    "description": "Hide Q2 and Q3 if less than 2 yes answers in Q1"
                },
                "validation": {
                    "hidden_questions_not_required": True,
                    "description": "Hidden questions (Q2, Q3) are not validated when Q1 sum < 2"
                }
            },
            "scoring_impact": {
                "description": "Q2 and Q3 do not contribute to numeric score, only to screening result interpretation",
                "screening_threshold": {
                    "positive_if": "Q1 >= 7 AND Q2 = yes AND Q3 >= 2 (moderate or serious)"
                }
            }
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
        Validate provided answers with conditional logic for Q2 and Q3
        
        Args:
            answers: Dictionary of question_id -> answer mappings
            
        Returns:
            ValidationResult with validation status and messages
        """
        errors = []
        warnings = []
        
        # Check for missing Q1 questions (always required)
        q1_keys = [f"q1_{i}" for i in range(1, 14)]
        missing_q1 = [k for k in q1_keys if k not in answers]
        if missing_q1:
            errors.append(f"Items Q1 manquants: {', '.join(missing_q1)}")
        
        # Calculate Q1 sum for conditional logic
        q1_sum = sum(answers.get(k, 0) for k in q1_keys)
        
        # Q2 and Q3 are only required if Q1 sum >= 2
        if q1_sum >= 2:
            if "q2" not in answers:
                errors.append("Q2 est requise lorsque ≥2 réponses 'oui' à Q1")
            if "q3" not in answers:
                errors.append("Q3 est requise lorsque ≥2 réponses 'oui' à Q1")
        else:
            # Q2 and Q3 should not be present if Q1 sum < 2
            if "q2" in answers:
                warnings.append("Q2 est fournie alors que Q1 < 2 'oui' (Q2 devrait être cachée)")
            if "q3" in answers:
                warnings.append("Q3 est fournie alors que Q1 < 2 'oui' (Q3 devrait être cachée)")
        
        # Check Q1 values (binary 0/1)
        bad_q1 = {k: v for k, v in answers.items() 
                  if k in q1_keys and (not isinstance(v, int) or v not in (0, 1))}
        if bad_q1:
            errors.append(f"Q1 items doivent être binaires 0 (non) ou 1 (oui): {bad_q1}")
        
        # Check Q2 values (binary 0/1)
        if "q2" in answers and (not isinstance(answers["q2"], int) or answers["q2"] not in (0, 1)):
            errors.append("Q2 doit être binaire 0 (non) ou 1 (oui).")
        
        # Check Q3 values (0-3)
        if "q3" in answers and (not isinstance(answers["q3"], int) or answers["q3"] not in (0, 1, 2, 3)):
            errors.append("Q3 doit être un entier 0–3.")
        
        # Clinical consistency warnings (only if no errors)
        if not errors:
            # Warning: Q3 indicates problem but no Q1 symptoms
            if q1_sum == 0 and answers.get('q3', 0) in (1, 2, 3):
                warnings.append(
                    "Q3 indique un problème alors qu'aucun symptôme Q1 n'est coché 'oui'. "
                    "Vérifier la cohérence."
                )
            
            # Warning: Q2 yes but less than 2 symptoms
            if q1_sum < 2 and answers.get('q2', 0) == 1:
                warnings.append(
                    "Q2='oui' (simultanéité) avec <2 symptômes 'oui'. "
                    "Vérifier la compréhension des consignes."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_screening(self, answers: Dict[str, int]) -> ScreeningResult:
        """
        Calculate MDQ screening result
        
        Standard criteria: MDQ POSITIVE if:
        - Q1 sum >= 7 AND
        - Q2 == 1 (yes) AND
        - Q3 in (2, 3) (moderate or serious problem)
        
        Args:
            answers: Dictionary with Q1 items (q1_1 to q1_13), q2, and q3
            
        Returns:
            ScreeningResult with detailed screening information
            
        Raises:
            MDQError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise MDQError("; ".join(validation.errors))
        
        # Calculate Q1 total
        q1_keys = [f"q1_{i}" for i in range(1, 14)]
        q1_total = sum(answers[k] for k in q1_keys)
        
        # Get Q2 and Q3 values
        q2_concurrent = answers["q2"] == 1
        q3_impact = answers["q3"]
        q3_impact_label = self.Q3_IMPACT_LABELS[q3_impact]
        
        # Determine screening result
        is_positive = (q1_total >= 7) and q2_concurrent and (q3_impact in (2, 3))
        screening_result = "POSITIF" if is_positive else "NEGATIF"
        
        # Build interpretation
        interpretation = self._build_interpretation(
            q1_total, q2_concurrent, q3_impact, q3_impact_label, screening_result
        )
        
        return ScreeningResult(
            q1_total=q1_total,
            q2_concurrent=q2_concurrent,
            q3_impact_level=q3_impact,
            q3_impact_label=q3_impact_label,
            screening_result=screening_result,
            interpretation=interpretation
        )
    
    def _build_interpretation(
        self, 
        q1_total: int, 
        q2_concurrent: bool, 
        q3_impact: int,
        q3_impact_label: str,
        screening_result: str
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"MDQ {screening_result}. "
        interpretation += f"Symptômes Q1: {q1_total}/13. "
        interpretation += f"Simultanéité (Q2): {'Oui' if q2_concurrent else 'Non'}. "
        interpretation += f"Impact fonctionnel (Q3): {q3_impact_label}. "
        
        if screening_result == "POSITIF":
            interpretation += (
                "Ce résultat suggère la présence possible d'un trouble du spectre bipolaire. "
                "Une évaluation clinique approfondie est recommandée."
            )
        else:
            interpretation += (
                "Ce résultat ne suggère pas de trouble du spectre bipolaire au moment du dépistage. "
            )
            
            # Add specific feedback for negative results
            if q1_total >= 7 and not q2_concurrent:
                interpretation += "Note: Symptômes présents mais non simultanés. "
            elif q1_total >= 7 and q3_impact < 2:
                interpretation += "Note: Symptômes présents mais impact fonctionnel limité. "
        
        return interpretation.strip()
    
    def get_full_questionnaire(self, include_logic: bool = True) -> Dict[str, Any]:
        """
        Get complete questionnaire structure for frontend
        
        Args:
            include_logic: Whether to include branching logic
        """
        result = {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }
        
        if include_logic:
            result["logic"] = self.get_branching_logic()
        
        return result

# -*- coding: utf-8 -*-
"""
QIDS-SR16 (Quick Inventory of Depressive Symptomatology - Self Report 16)
French version - Self-assessment scale measuring depression severity
"""

from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
from pydantic import BaseModel, Field, validator


class QIDSError(ValueError):
    """Custom exception for QIDS validation errors"""
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
    help: Optional[str] = None


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    description: str
    question_ids: List[str]


class ScoreResult(BaseModel):
    """Model for score results"""
    total_score: int
    severity: str
    domain_scores: Dict[str, int]
    interpretation: str
    range: Tuple[int, int] = (0, 27)


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class QIDSSR16:
    """
    QIDS-SR16 Questionnaire Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Compute scores
    """
    
    INSTRUMENT_ID = "QIDS-SR16.fr"
    INSTRUMENT_NAME = "Auto-questionnaire court sur les symptômes de la dépression"
    ABBREVIATION = "QIDS-SR16"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "7 derniers jours"
    
    # Severity cutoffs
    CUTOFFS = [
        (0, 5, "Pas de dépression"),
        (6, 10, "Dépression légère"),
        (11, 15, "Dépression modérée"),
        (16, 20, "Dépression sévère"),
        (21, 27, "Dépression très sévère"),
    ]
    
    def __init__(self):
        """Initialize the QIDS-SR16 questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="part1",
                label="PARTIE 1",
                description="Items 1 à 9",
                question_ids=[f"q{i}" for i in range(1, 10)]
            ),
            Section(
                id="part2",
                label="PARTIE 2",
                description="Items 10 à 16",
                question_ids=[f"q{i}" for i in range(10, 17)]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = [
            Question(
                id="q1",
                section_id="part1",
                text="Endormissement",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Je ne mets jamais plus de 30 minutes à m'endormir.", score=0),
                    QuestionOption(code=1, label="Moins d'une fois sur deux, je mets au moins 30 minutes à m'endormir.", score=1),
                    QuestionOption(code=2, label="Plus d'une fois sur deux, je mets au moins 30 minutes à m'endormir.", score=2),
                    QuestionOption(code=3, label="Plus d'une fois sur deux, je mets plus d'une heure à m'endormir.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q2",
                section_id="part1",
                text="Sommeil pendant la nuit",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Je ne me réveille pas la nuit.", score=0),
                    QuestionOption(code=1, label="Sommeil agité/léger et quelques réveils brefs chaque nuit.", score=1),
                    QuestionOption(code=2, label="Je me réveille au moins une fois par nuit, mais je me rendors facilement.", score=2),
                    QuestionOption(code=3, label="Plus d'une fois sur deux, plusieurs réveils nocturnes avec ≥20 min éveillé(e).", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q3",
                section_id="part1",
                text="Réveil avant l'heure prévue",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="La plupart du temps, réveil ≤30 min avant l'heure de lever.", score=0),
                    QuestionOption(code=1, label="Plus d'une fois sur deux, réveil >30 min avant l'heure de lever.", score=1),
                    QuestionOption(code=2, label="Presque toujours réveil ≥1 h avant, mais je me rendors.", score=2),
                    QuestionOption(code=3, label="Réveil ≥1 h avant et impossible de me rendormir.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q4",
                section_id="part1",
                text="Sommeil excessif",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="≤7–8 h par nuit, pas de sieste.", score=0),
                    QuestionOption(code=1, label="≤10 h/24 h siestes comprises.", score=1),
                    QuestionOption(code=2, label="≤12 h/24 h siestes comprises.", score=2),
                    QuestionOption(code=3, label=">12 h/24 h siestes comprises.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q5",
                section_id="part1",
                text="Tristesse",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Je ne me sens pas triste.", score=0),
                    QuestionOption(code=1, label="Je me sens triste moins de la moitié du temps.", score=1),
                    QuestionOption(code=2, label="Je me sens triste plus de la moitié du temps.", score=2),
                    QuestionOption(code=3, label="Je me sens triste presque tout le temps.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q6",
                section_id="part1",
                text="Diminution de l'appétit",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Appétit inchangé.", score=0),
                    QuestionOption(code=1, label="Je mange un peu moins souvent ou en plus petite quantité.", score=1),
                    QuestionOption(code=2, label="Je mange beaucoup moins et seulement en me forçant.", score=2),
                    QuestionOption(code=3, label="Je mange rarement sur 24 h et seulement en me forçant énormément ou persuadé(e).", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q7",
                section_id="part1",
                text="Augmentation de l'appétit",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Appétit inchangé.", score=0),
                    QuestionOption(code=1, label="Besoin de manger plus souvent.", score=1),
                    QuestionOption(code=2, label="Je mange régulièrement plus souvent et/ou en plus grande quantité.", score=2),
                    QuestionOption(code=3, label="Grand besoin de manger davantage pendant et entre les repas.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q8",
                section_id="part1",
                text="Perte de poids (15 derniers jours)",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Aucun changement de poids.", score=0),
                    QuestionOption(code=1, label="Impression d'avoir perdu un peu de poids.", score=1),
                    QuestionOption(code=2, label="Perdu 1 kg ou plus.", score=2),
                    QuestionOption(code=3, label="Perdu plus de 2 kg.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q9",
                section_id="part1",
                text="Prise de poids (15 derniers jours)",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Aucun changement de poids.", score=0),
                    QuestionOption(code=1, label="Impression d'avoir pris un peu de poids.", score=1),
                    QuestionOption(code=2, label="Pris 1 kg ou plus.", score=2),
                    QuestionOption(code=3, label="Pris plus de 2 kg.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q10",
                section_id="part2",
                text="Concentration / Prise de décisions",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Aucun changement de ma capacité habituelle.", score=0),
                    QuestionOption(code=1, label="Parfois indécis(e) ou concentration limitée.", score=1),
                    QuestionOption(code=2, label="La plupart du temps, difficulté à me concentrer/à décider.", score=2),
                    QuestionOption(code=3, label="Impossible de me concentrer pour lire ou de décider même de choses insignifiantes.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q11",
                section_id="part2",
                text="Opinion de moi-même",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Autant de valeur/mérite que les autres.", score=0),
                    QuestionOption(code=1, label="Je me critique plus que d'habitude.", score=1),
                    QuestionOption(code=2, label="Je crois fortement causer des problèmes aux autres.", score=2),
                    QuestionOption(code=3, label="Je pense presque tout le temps à mes défauts.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q12",
                section_id="part2",
                text="Idées de mort ou de suicide",
                type="single_choice",
                required=True,
                help="En cas d'idéation suicidaire, alerter immédiatement le clinicien.",
                options=[
                    QuestionOption(code=0, label="Je ne pense pas au suicide ni à la mort.", score=0),
                    QuestionOption(code=1, label="Je pense que la vie est sans intérêt ou à sa valeur.", score=1),
                    QuestionOption(code=2, label="Je pense au suicide/la mort plusieurs fois par semaine pendant plusieurs minutes.", score=2),
                    QuestionOption(code=3, label="Pensées suicidaires détaillées, plan ou tentative.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q13",
                section_id="part2",
                text="Enthousiasme général / Intérêt",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Aucun changement d'intérêt pour personnes/activités.", score=0),
                    QuestionOption(code=1, label="Je m'intéresse moins.", score=1),
                    QuestionOption(code=2, label="Intérêt conservé pour une ou deux activités seulement.", score=2),
                    QuestionOption(code=3, label="Presque plus d'intérêt.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q14",
                section_id="part2",
                text="Énergie / Fatigabilité",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Autant d'énergie que d'habitude.", score=0),
                    QuestionOption(code=1, label="Je me fatigue plus facilement que d'habitude.", score=1),
                    QuestionOption(code=2, label="Gros effort pour commencer/terminer les activités quotidiennes.", score=2),
                    QuestionOption(code=3, label="Je ne peux vraiment pas faire mes activités quotidiennes.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q15",
                section_id="part2",
                text="Impression de ralentissement",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Je pense/parle/bouge aussi vite que d'habitude.", score=0),
                    QuestionOption(code=1, label="Je réfléchis plus lentement ou voix étouffée/monocorde.", score=1),
                    QuestionOption(code=2, label="Réponses lentes, sûr(e) de réfléchir plus lentement.", score=2),
                    QuestionOption(code=3, label="Souvent incapable de répondre sans gros efforts.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ),
            Question(
                id="q16",
                section_id="part2",
                text="Impression d'agitation",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=0, label="Je ne me sens pas agité(e).", score=0),
                    QuestionOption(code=1, label="Souvent agité(e), besoin de changer de position.", score=1),
                    QuestionOption(code=2, label="Impulsions de bouger, plutôt agité(e).", score=2),
                    QuestionOption(code=3, label="Par moments, incapable de rester assis(e), besoin de faire les cent pas.", score=3)
                ],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            )
        ]
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
            "description": "Échelle d'auto-évaluation en 16 items mesurant la sévérité des symptômes dépressifs sur 9 domaines DSM, chaque item coté de 0 à 3.",
            "sources": [
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC2929841/",
                "https://med-fom-ubcsad.sites.olt.ubc.ca/files/2013/11/QIDS-SR.pdf",
                "https://loricalabresemd.com/wp-content/uploads/2017/12/qids-sr16.pdf"
            ],
            "total_questions": 16,
            "scoring_range": [0, 27]
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
        
        # Check for missing required questions
        expected_keys = [f"q{i}" for i in range(1, 17)]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value ranges
        invalid = {k: v for k, v in answers.items() 
                  if k in expected_keys and (not isinstance(v, int) or v < 0 or v > 3)}
        if invalid:
            errors.append(f"Valeurs invalides (doivent être des entiers 0–3): {invalid}")
        
        # Clinical consistency warnings
        if not errors:
            # Check appetite increase/decrease consistency
            if answers.get('q6', 0) >= 2 and answers.get('q7', 0) >= 2:
                warnings.append(
                    "Scores élevés simultanés à la diminution (Q6) et à l'augmentation (Q7) de l'appétit – "
                    "vérifier la cohérence clinique."
                )
            
            # Check weight gain/loss consistency
            if answers.get('q8', 0) >= 2 and answers.get('q9', 0) >= 2:
                warnings.append(
                    "Scores élevés simultanés perte de poids (Q8) et prise de poids (Q9) – "
                    "vérifier la cohérence clinique."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_score(self, answers: Dict[str, int]) -> ScoreResult:
        """
        Calculate QIDS-SR16 total score and severity
        
        Args:
            answers: Dictionary with keys 'q1' through 'q16', values 0-3
            
        Returns:
            ScoreResult with total score, severity, and domain scores
            
        Raises:
            QIDSError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise QIDSError("; ".join(validation.errors))
        
        # Calculate domain scores (max of related items)
        sleep_domain = max(answers['q1'], answers['q2'], answers['q3'], answers['q4'])
        appetite_weight_domain = max(answers['q6'], answers['q7'], answers['q8'], answers['q9'])
        psychomotor_domain = max(answers['q15'], answers['q16'])
        
        # Calculate total score (sum of 9 domains)
        total = (
            sleep_domain +
            answers['q5'] +  # Sadness
            appetite_weight_domain +
            answers['q10'] +  # Concentration
            answers['q11'] +  # Self-view
            answers['q12'] +  # Suicidal ideation
            answers['q13'] +  # Interest
            answers['q14'] +  # Energy
            psychomotor_domain
        )
        
        # Safety check
        if total < 0 or total > 27:
            raise QIDSError(f"Score hors bornes: {total}")
        
        # Determine severity
        severity = None
        for lo, hi, label in self.CUTOFFS:
            if lo <= total <= hi:
                severity = label
                break
        
        # Build interpretation
        interpretation = self._build_interpretation(total, severity, answers)
        
        return ScoreResult(
            total_score=total,
            severity=severity,
            domain_scores={
                "sleep": sleep_domain,
                "sadness": answers['q5'],
                "appetite_weight": appetite_weight_domain,
                "concentration": answers['q10'],
                "self_view": answers['q11'],
                "suicidal_ideation": answers['q12'],
                "interest": answers['q13'],
                "energy": answers['q14'],
                "psychomotor": psychomotor_domain
            },
            interpretation=interpretation
        )
    
    def _build_interpretation(self, total: int, severity: str, answers: Dict[str, int]) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Score total: {total}/27 - {severity}. "
        
        # Add alerts for critical items
        if answers.get('q12', 0) >= 2:
            interpretation += "⚠️ ALERTE: Idéation suicidaire présente - évaluation clinique urgente requise. "
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }


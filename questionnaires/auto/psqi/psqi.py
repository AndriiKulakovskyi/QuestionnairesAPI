# -*- coding: utf-8 -*-
"""
PSQI (Pittsburgh Sleep Quality Index)
French version - Sleep quality assessment questionnaire
"""

from typing import Dict, List, Optional, Any, Union, Tuple
from datetime import datetime
from pydantic import BaseModel
import re


class PSQIError(ValueError):
    """Custom exception for PSQI validation errors"""
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
    options: Optional[List[QuestionOption]] = None
    constraints: Dict[str, Any]


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    question_ids: List[str]


class ComponentScore(BaseModel):
    """Model for a component score"""
    name: str
    label: str
    score: int
    range: tuple = (0, 3)


class ScoreResult(BaseModel):
    """Model for score results"""
    total_score: int
    components: Dict[str, ComponentScore]
    sleep_efficiency_pct: float
    time_in_bed_hours: float
    sleep_hours: float
    interpretation: str
    range: tuple = (0, 21)


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class PSQI:
    """
    PSQI (Pittsburgh Sleep Quality Index) Questionnaire Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers (including time formats)
    - Compute 7 component scores and total score
    """
    
    INSTRUMENT_ID = "PSQI.fr"
    INSTRUMENT_NAME = "Indice de Qualité du Sommeil de Pittsburgh (PSQI) – Version française"
    ABBREVIATION = "PSQI"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "30 derniers jours"
    
    # Frequency options for Q5a-j, Q7, Q8
    FREQUENCY_OPTIONS = [
        {"code": 0, "label": "Jamais au cours des 30 derniers jours", "score": 0},
        {"code": 1, "label": "Moins d'une fois par semaine", "score": 1},
        {"code": 2, "label": "Une ou deux fois par semaine", "score": 2},
        {"code": 3, "label": "Trois fois par semaine ou plus", "score": 3},
    ]
    
    # Q5 sub-items (sleep disturbances)
    Q5_ITEMS = {
        "a": "Vous n'êtes pas arrivé(e) à vous endormir en 30 minutes",
        "b": "Réveil au milieu de la nuit ou trop tôt",
        "c": "Levers nocturnes pour aller aux toilettes",
        "d": "Difficultés respiratoires",
        "e": "Toux ou ronflement bruyant",
        "f": "Trop froid",
        "g": "Trop chaud",
        "h": "Cauchemars",
        "i": "Douleurs",
        "j": "Autre raison (préciser)"
    }
    
    # Component names
    COMPONENTS = {
        "subjective_quality": "Qualité subjective",
        "latency": "Latence du sommeil",
        "duration": "Durée du sommeil",
        "efficiency": "Efficience du sommeil",
        "disturbances": "Troubles du sommeil",
        "medication": "Médication pour dormir",
        "daytime_dysfunction": "Dysfonctionnement diurne"
    }
    
    def __init__(self):
        """Initialize the PSQI questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="times",
                label="Heures / Durées",
                question_ids=["q1", "q2", "q3", "q4"]
            ),
            Section(
                id="sleep_problems",
                label="Difficultés de sommeil (fréquence)",
                question_ids=[f"q5{c}" for c in self.Q5_ITEMS.keys()]
            ),
            Section(
                id="globals",
                label="Éléments globaux",
                question_ids=["q6", "q7", "q8", "q9"]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = []
        
        # Q1: Bedtime
        questions.append(Question(
            id="q1",
            section_id="times",
            text="Heure habituelle du coucher (HH:MM, 24h) au cours des 30 derniers jours",
            type="time",
            required=True,
            constraints={"pattern": r"^\d{2}:\d{2}$"}
        ))
        
        # Q2: Sleep latency in minutes
        questions.append(Question(
            id="q2",
            section_id="times",
            text="Temps pour s'endormir (minutes)",
            type="integer",
            required=True,
            constraints={"min_value": 0}
        ))
        
        # Q3: Wake time
        questions.append(Question(
            id="q3",
            section_id="times",
            text="Heure habituelle du lever (HH:MM, 24h) au cours des 30 derniers jours",
            type="time",
            required=True,
            constraints={"pattern": r"^\d{2}:\d{2}$"}
        ))
        
        # Q4: Hours of actual sleep
        questions.append(Question(
            id="q4",
            section_id="times",
            text="Heures de sommeil effectif par nuit (HH:MM ou nombre d'heures, p.ex. 6.5)",
            type="string",
            required=True,
            constraints={"pattern": r"^(\d{1,2}:\d{2}|(\d+(\.\d+)?))$"}
        ))
        
        # Q5a-j: Sleep disturbances (frequency)
        for code, text in self.Q5_ITEMS.items():
            questions.append(Question(
                id=f"q5{code}",
                section_id="sleep_problems",
                text=f"5{code}. {text} – fréquence (30 derniers jours)",
                type="single_choice",
                required=True,
                options=[QuestionOption(**opt) for opt in self.FREQUENCY_OPTIONS],
                constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
            ))
        
        # Q6: Subjective sleep quality
        questions.append(Question(
            id="q6",
            section_id="globals",
            text="Qualité du sommeil en général (30 derniers jours)",
            type="single_choice",
            required=True,
            options=[
                QuestionOption(code=0, label="Très bonne", score=0),
                QuestionOption(code=1, label="Assez bonne", score=1),
                QuestionOption(code=2, label="Assez mauvaise", score=2),
                QuestionOption(code=3, label="Très mauvaise", score=3)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
        ))
        
        # Q7: Sleep medication frequency
        questions.append(Question(
            id="q7",
            section_id="globals",
            text="Prise de médicaments pour dormir (fréquence)",
            type="single_choice",
            required=True,
            options=[QuestionOption(**opt) for opt in self.FREQUENCY_OPTIONS],
            constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
        ))
        
        # Q8: Daytime sleepiness frequency
        questions.append(Question(
            id="q8",
            section_id="globals",
            text="Difficulté à rester éveillé(e) (fréquence)",
            type="single_choice",
            required=True,
            options=[QuestionOption(**opt) for opt in self.FREQUENCY_OPTIONS],
            constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
        ))
        
        # Q9: Motivation difficulty
        questions.append(Question(
            id="q9",
            section_id="globals",
            text="Difficulté à être suffisamment motivé(e) pour vos activités",
            type="single_choice",
            required=True,
            options=[
                QuestionOption(code=0, label="Pas difficile du tout", score=0),
                QuestionOption(code=1, label="Légèrement difficile", score=1),
                QuestionOption(code=2, label="Assez difficile", score=2),
                QuestionOption(code=3, label="Très difficile", score=3)
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
            "description": "Auto-questionnaire en 19 items (patients) dont 9 sont scorés ici (Q1–Q9). Production de 7 sous-scores (0–3) et d'un score total (0–21).",
            "sources": [
                "PSQI.pdf – Formulaire FR (pages 1–2)",
                "PSQI_cotationScore.docx – Règles de cotation officielles (FR)",
                "Buysse DJ et al., Psychiatry Res. 1989;28(2):193–213."
            ],
            "total_questions": 14,  # Q1-4 + Q5a-j (10) + Q6-9
            "scoring_range": [0, 21],
            "components": 7,
            "component_names": list(self.COMPONENTS.keys())
        }
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """Get all sections"""
        return [section.dict() for section in self._sections]
    
    def get_questions(self, section_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get questions, optionally filtered by section"""
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
    
    @staticmethod
    def _parse_time(time_str: str) -> Tuple[int, int]:
        """Parse HH:MM time string to (hours, minutes)"""
        if not isinstance(time_str, str) or not re.match(r"^\d{2}:\d{2}$", time_str):
            raise PSQIError(f"Format HH:MM attendu (reçu: {time_str!r})")
        
        h, m = time_str.split(":")
        h, m = int(h), int(m)
        
        if not (0 <= h <= 23 and 0 <= m <= 59):
            raise PSQIError(f"Heure invalide: {time_str!r}")
        
        return h, m
    
    @staticmethod
    def _hours_between(bedtime: str, waketime: str) -> float:
        """Calculate hours between bedtime and waketime (handles midnight crossover)"""
        bh, bm = PSQI._parse_time(bedtime)
        wh, wm = PSQI._parse_time(waketime)
        
        bed_minutes = bh * 60 + bm
        wake_minutes = wh * 60 + wm
        
        # Handle midnight crossover
        if wake_minutes < bed_minutes:
            wake_minutes += 24 * 60
        
        minutes = wake_minutes - bed_minutes
        return minutes / 60.0
    
    @staticmethod
    def _parse_sleep_hours(value: Union[str, int, float]) -> float:
        """Parse sleep hours (accepts HH:MM or decimal)"""
        if isinstance(value, (int, float)):
            v = float(value)
            if v < 0:
                raise PSQIError("q4 (heures de sommeil) doit être >= 0")
            return v
        
        if isinstance(value, str):
            # Try HH:MM format
            if re.match(r"^\d{1,2}:\d{2}$", value):
                h, m = value.split(":")
                return int(h) + int(m) / 60.0
            
            # Try decimal format
            try:
                v = float(value)
                if v < 0:
                    raise PSQIError("q4 (heures de sommeil) doit être >= 0")
                return v
            except ValueError:
                pass
        
        raise PSQIError(f"q4 invalide (attendu HH:MM ou nombre d'heures), reçu: {value!r}")
    
    def validate_answers(self, answers: Dict[str, Any]) -> ValidationResult:
        """Validate provided answers"""
        errors = []
        warnings = []
        
        # Check for missing required questions
        required_keys = ["q1", "q2", "q3", "q4", "q6", "q7", "q8", "q9"]
        required_keys += [f"q5{c}" for c in self.Q5_ITEMS.keys()]
        
        missing = [k for k in required_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate time formats
        for q_id in ["q1", "q3"]:
            if q_id in answers:
                try:
                    self._parse_time(str(answers[q_id]))
                except PSQIError as e:
                    errors.append(f"{q_id}: {str(e)}")
        
        # Validate Q2 (minutes)
        if "q2" in answers:
            try:
                val = int(answers["q2"])
                if val < 0:
                    errors.append("q2 (minutes pour s'endormir) doit être >= 0")
            except (ValueError, TypeError):
                errors.append("q2 doit être un nombre entier de minutes")
        
        # Validate Q4 (sleep hours)
        if "q4" in answers:
            try:
                self._parse_sleep_hours(answers["q4"])
            except PSQIError as e:
                errors.append(str(e))
        
        # Validate frequency items (Q5a-j, Q6-Q9)
        frequency_items = [f"q5{c}" for c in self.Q5_ITEMS.keys()] + ["q6", "q7", "q8", "q9"]
        for q_id in frequency_items:
            if q_id in answers:
                try:
                    val = int(answers[q_id])
                    if val not in (0, 1, 2, 3):
                        errors.append(f"{q_id} doit être entre 0 et 3")
                except (ValueError, TypeError):
                    errors.append(f"{q_id} doit être un entier (0-3)")
        
        # Check time in bed coherence (only if no errors)
        if not errors and all(k in answers for k in ["q1", "q3"]):
            try:
                time_in_bed = self._hours_between(str(answers["q1"]), str(answers["q3"]))
                if time_in_bed < 3:
                    warnings.append(
                        f"Temps au lit très court ({time_in_bed:.1f}h). "
                        "Vérifier la cohérence des heures de coucher et lever."
                    )
                elif time_in_bed > 14:
                    warnings.append(
                        f"Temps au lit très long ({time_in_bed:.1f}h). "
                        "Vérifier la cohérence des heures de coucher et lever."
                    )
            except PSQIError:
                pass  # Already caught in format validation
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_score(self, answers: Dict[str, Any]) -> ScoreResult:
        """Calculate PSQI total score and 7 components"""
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise PSQIError("; ".join(validation.errors))
        
        # Parse time-based values
        time_in_bed_h = self._hours_between(str(answers["q1"]), str(answers["q3"]))
        sleep_hours = self._parse_sleep_hours(answers["q4"])
        
        if time_in_bed_h <= 0:
            raise PSQIError("Temps au lit nul/négatif: vérifier q1/q3.")
        
        # Calculate sleep efficiency
        efficiency_pct = (sleep_hours / time_in_bed_h) * 100.0
        
        # Component 1: Subjective quality (Q6)
        subjective_quality = int(answers["q6"])
        
        # Component 2: Sleep latency (Q2 + Q5a bucketed)
        latency = self._calculate_latency(int(answers["q2"]), int(answers["q5a"]))
        
        # Component 3: Sleep duration (Q4)
        duration = self._calculate_duration(sleep_hours)
        
        # Component 4: Sleep efficiency
        efficiency = self._calculate_efficiency(efficiency_pct)
        
        # Component 5: Sleep disturbances (Q5b-j)
        disturbances = self._calculate_disturbances(answers)
        
        # Component 6: Medication (Q7)
        medication = int(answers["q7"])
        
        # Component 7: Daytime dysfunction (Q8 + Q9)
        daytime_dysfunction = self._calculate_daytime_dysfunction(
            int(answers["q8"]), int(answers["q9"])
        )
        
        # Total score
        total = (subjective_quality + latency + duration + efficiency +
                disturbances + medication + daytime_dysfunction)
        
        # Build components dict
        components = {
            "subjective_quality": ComponentScore(
                name="subjective_quality",
                label=self.COMPONENTS["subjective_quality"],
                score=subjective_quality
            ),
            "latency": ComponentScore(
                name="latency",
                label=self.COMPONENTS["latency"],
                score=latency
            ),
            "duration": ComponentScore(
                name="duration",
                label=self.COMPONENTS["duration"],
                score=duration
            ),
            "efficiency": ComponentScore(
                name="efficiency",
                label=self.COMPONENTS["efficiency"],
                score=efficiency
            ),
            "disturbances": ComponentScore(
                name="disturbances",
                label=self.COMPONENTS["disturbances"],
                score=disturbances
            ),
            "medication": ComponentScore(
                name="medication",
                label=self.COMPONENTS["medication"],
                score=medication
            ),
            "daytime_dysfunction": ComponentScore(
                name="daytime_dysfunction",
                label=self.COMPONENTS["daytime_dysfunction"],
                score=daytime_dysfunction
            )
        }
        
        # Build interpretation
        interpretation = self._build_interpretation(
            total, components, efficiency_pct, time_in_bed_h, sleep_hours
        )
        
        return ScoreResult(
            total_score=total,
            components=components,
            sleep_efficiency_pct=efficiency_pct,
            time_in_bed_hours=time_in_bed_h,
            sleep_hours=sleep_hours,
            interpretation=interpretation
        )
    
    @staticmethod
    def _calculate_latency(q2_minutes: int, q5a_score: int) -> int:
        """Calculate latency component (Q2 + Q5a bucketed)"""
        # Code Q2 minutes
        if q2_minutes <= 15:
            q2_code = 0
        elif q2_minutes <= 30:
            q2_code = 1
        elif q2_minutes <= 60:
            q2_code = 2
        else:
            q2_code = 3
        
        # Sum and re-bucket
        latency_sum = q2_code + q5a_score
        
        if latency_sum == 0:
            return 0
        elif latency_sum in (1, 2):
            return 1
        elif latency_sum in (3, 4):
            return 2
        else:  # 5-6
            return 3
    
    @staticmethod
    def _calculate_duration(sleep_hours: float) -> int:
        """Calculate duration component from sleep hours"""
        if sleep_hours >= 7:
            return 0
        elif 6 <= sleep_hours < 7:
            return 1
        elif 5 <= sleep_hours < 6:
            return 2
        else:  # < 5
            return 3
    
    @staticmethod
    def _calculate_efficiency(efficiency_pct: float) -> int:
        """Calculate efficiency component from percentage"""
        if efficiency_pct >= 85:
            return 0
        elif 75 <= efficiency_pct < 85:
            return 1
        elif 65 <= efficiency_pct < 75:
            return 2
        else:  # < 65
            return 3
    
    def _calculate_disturbances(self, answers: Dict[str, Any]) -> int:
        """Calculate disturbances component (sum Q5b-j)"""
        dist_sum = sum(int(answers[f"q5{c}"]) for c in "bcdefghij")
        
        if dist_sum == 0:
            return 0
        elif 1 <= dist_sum <= 9:
            return 1
        elif 10 <= dist_sum <= 18:
            return 2
        else:  # 19-27
            return 3
    
    @staticmethod
    def _calculate_daytime_dysfunction(q8_score: int, q9_score: int) -> int:
        """Calculate daytime dysfunction component (Q8 + Q9 bucketed)"""
        dysfunction_sum = q8_score + q9_score
        
        if dysfunction_sum == 0:
            return 0
        elif dysfunction_sum in (1, 2):
            return 1
        elif dysfunction_sum in (3, 4):
            return 2
        else:  # 5-6
            return 3
    
    def _build_interpretation(
        self,
        total: int,
        components: Dict[str, ComponentScore],
        efficiency_pct: float,
        time_in_bed_h: float,
        sleep_hours: float
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Score total PSQI: {total}/21. "
        
        # Overall interpretation
        if total <= 5:
            interpretation += "Bonne qualité de sommeil. "
        else:
            interpretation += (
                f"Mauvaise qualité de sommeil (seuil clinique: score >5). "
            )
        
        # Add component details
        problematic_components = []
        for name, comp in components.items():
            if comp.score >= 2:  # Score ≥2 is problematic
                problematic_components.append(f"{comp.label} ({comp.score}/3)")
        
        if problematic_components:
            interpretation += f"Composantes problématiques: {', '.join(problematic_components)}. "
        
        # Add metrics
        interpretation += (
            f"Métriques: {sleep_hours:.1f}h de sommeil effectif, "
            f"{time_in_bed_h:.1f}h au lit, efficience {efficiency_pct:.1f}%. "
        )
        
        # Clinical recommendations
        if total > 5:
            interpretation += (
                "Évaluation clinique recommandée pour explorer les troubles du sommeil. "
            )
            
            # Specific recommendations based on components
            if components["medication"].score >= 2:
                interpretation += "Médication pour dormir fréquente: évaluer la dépendance. "
            if components["efficiency"].score >= 2:
                interpretation += "Efficience faible: envisager thérapie cognitivo-comportementale. "
            if components["disturbances"].score >= 2:
                interpretation += "Troubles nombreux: investigation des causes recommandée. "
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }


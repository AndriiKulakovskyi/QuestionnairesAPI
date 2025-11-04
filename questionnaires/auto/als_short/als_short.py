"""
ALS-short (Affective Lability Scale - Version courte)

This module implements the short version of the Affective Lability Scale (ALS),
which assesses emotional lability - rapid shifts in mood states.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class ALSShortError(Exception):
    """Custom exception for ALS-short questionnaire errors."""
    pass


class ALSShort:
    """
    ALS-short (Affective Lability Scale - Short Version)
    
    An 18-item self-report questionnaire measuring affective lability
    (mood instability) across three dimensions: Anxiety-Depression,
    Depression-Elation, and Anger.
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (ALS-18)
        language: Language code
        version: Version number
        reference_period: Time frame for responses (typical functioning)
        description: Brief description of the questionnaire
    """
    
    # Subscale item mappings (1-indexed)
    ANXIETY_DEPRESSION_ITEMS = [1, 3, 5, 6, 7]
    DEPRESSION_ELATION_ITEMS = [2, 10, 12, 13, 15, 16, 17, 18]
    ANGER_ITEMS = [4, 8, 9, 11, 14]
    
    # Item texts in French
    ITEM_TEXTS = [
        "À certains moments, je me sens aussi détendu(e) que n'importe qui, et en quelques minutes, je deviens si nerveux(se) que j'ai l'impression d'avoir la tête vide et d'avoir un vertige.",
        "Il y a des moments où j'ai très peu d'énergie, et peu de temps après, j'ai autant d'énergie que la plupart des gens.",
        "Durant une minute, je pense me sentir très bien, et la minute suivante, je suis tendu(e), je réagis à la moindre chose et je suis nerveux(se).",
        "J'oscille souvent entre des moments où je contrôle très bien mon humeur à des moments où je ne la contrôle plus du tout.",
        "Très souvent, je me sens très nerveux(se) et tendu(e), et ensuite soudainement, je me sens très triste et abattu(e).",
        "Quelque fois je passe de sentiments très anxieux au sujet de quelque chose à des sentiments très tristes à leur propos.",
        "J'oscille entre des moments où je me sens parfaitement calme à des moments où je me sens très tendu(e) et nerveux(se).",
        "Il y a des moments où je me sens parfaitement calme durant une minute, et la minute suivante, la moindre chose me rend furieux(se).",
        "Fréquemment, je me sens OK, mais ensuite tout d'un coup, je deviens si fou que je pourrais frapper quelque chose.",
        "Souvent, je peux penser clairement et bien me concentrer pendant une minute, et la minute suivante, j'ai beaucoup de difficultés à me concentrer et à penser clairement.",
        "Il y a des moments où je me sens si furieux(se) que je ne peux pas m'arrêter de hurler après les autres, et peu de temps après, je ne pense plus du tout à crier après eux.",
        "J'oscille entre des périodes où je me sens plein d'énergie et d'autres où j'ai si peu d'énergie que c'est un énorme effort juste d'aller là où je dois aller.",
        "Il y a des moments où je me sens absolument admirable et d'autres juste après où je me sens exactement comme n'importe qui d'autre.",
        "Il y a des moments où je me sens tellement furieux(se) que mon cœur bat très fort et/ou je tremble, et des autres peu après, où je me sens détendu(e).",
        "J'oscille entre n'être pas productif(ve) à des périodes où je suis aussi productif(ve) que tout le monde.",
        "Quelque fois, j'ai beaucoup d'énergie une minute, et la minute suivante, j'ai tellement peu d'énergie que je ne peux presque rien faire.",
        "Il y a des moments où j'ai plus d'énergie que d'habitude et plus que la plupart des gens, et rapidement après, j'ai à peu près le même niveau d'énergie que n'importe qui d'autre.",
        "À certains moments, j'ai l'impression de tout faire très lentement, et très rapidement après, j'ai l'impression de ne pas être plus lent que quelqu'un d'autre."
    ]
    
    # Response options (A=3, B=2, C=1, D=0)
    RESPONSE_OPTIONS = [
        {"code": 3, "label": "A – Très caractéristique de moi, extrêmement descriptif", "score": 3},
        {"code": 2, "label": "B – Assez caractéristique de moi, assez bonne description de moi", "score": 2},
        {"code": 1, "label": "C – Assez peu caractéristique de moi, ne me décrit pas", "score": 1},
        {"code": 0, "label": "D – Absolument pas caractéristique de moi, ne me décrit pas du tout", "score": 0}
    ]
    
    def __init__(self):
        """Initialize the ALS-short questionnaire."""
        self.id = "ALS-short.fr"
        self.name = "Affective Lability Scale – Version courte (FR)"
        self.abbreviation = "ALS-18"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Mode de fonctionnement habituel (hors périodes d'humeur anormalement basse ou élevée)"
        self.description = (
            "Labilité émotionnelle auto-rapportée. Version courte à 18 items. "
            "Réponses A–D mappées à 3–0. Trois sous-scores et un score total (moyennes 0–3)."
        )
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get questionnaire metadata.
        
        Returns:
            Dictionary containing questionnaire metadata
        """
        return {
            "id": self.id,
            "name": self.name,
            "abbreviation": self.abbreviation,
            "language": self.language,
            "version": self.version,
            "reference_period": self.reference_period,
            "description": self.description,
            "num_items": 18,
            "response_scale": "4-point scale (A/B/C/D mapped to 3/2/1/0)",
            "score_range": [0.0, 3.0],
            "score_type": "mean",
            "subscales": {
                "anxiety_depression": {"items": self.ANXIETY_DEPRESSION_ITEMS, "num_items": 5},
                "depression_elation": {"items": self.DEPRESSION_ELATION_ITEMS, "num_items": 8},
                "anger": {"items": self.ANGER_ITEMS, "num_items": 5}
            }
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        for i, text in enumerate(self.ITEM_TEXTS, start=1):
            # Determine which subscale(s) this item belongs to
            subscales = []
            if i in self.ANXIETY_DEPRESSION_ITEMS:
                subscales.append("anxiety_depression")
            if i in self.DEPRESSION_ELATION_ITEMS:
                subscales.append("depression_elation")
            if i in self.ANGER_ITEMS:
                subscales.append("anger")
            
            question = {
                "id": f"q{i}",
                "number": i,
                "section_id": "sec1",
                "text": f"{i}. {text}",
                "type": "single_choice",
                "required": True,
                "options": self.RESPONSE_OPTIONS.copy(),
                "subscales": subscales
            }
            questions.append(question)
        return questions
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """
        Get questionnaire sections.
        
        Returns:
            List of section dictionaries
        """
        return [
            {
                "id": "sec1",
                "label": "ALS – 18 items (A..D → 3..0)",
                "description": "Cochez A, B, C ou D selon ce qui vous décrit le mieux",
                "question_ids": [f"q{i}" for i in range(1, 19)]
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate questionnaire responses.
        
        Args:
            answers: Dictionary mapping question IDs to response values (0-3)
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            ALSShortError: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all 18 items are present
        expected_items = [f"q{i}" for i in range(1, 19)]
        missing = [qid for qid in expected_items if qid not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate each response value
        for qid in expected_items:
            if qid in answers:
                value = answers[qid]
                if not isinstance(value, int):
                    errors.append(f"{qid}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value < 0 or value > 3:
                    errors.append(f"{qid}: la valeur doit être entre 0 et 3 (A=3,B=2,C=1,D=0) (reçu: {value})")
        
        # Check for unusual patterns
        if not errors and len(set(answers.values())) == 1:
            warnings.append(
                "Toutes les réponses sont identiques. Veuillez vérifier que le patient "
                "a bien compris les instructions."
            )
        
        # Check for all maximum (high lability)
        if not errors and all(answers.get(f"q{i}", -1) == 3 for i in range(1, 19)):
            warnings.append(
                "Toutes les réponses indiquent une labilité maximale (A). "
                "Vérifier la sincérité des réponses ou la présence d'une détresse sévère."
            )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate ALS-short scores.
        
        Args:
            answers: Dictionary mapping question IDs (q1-q18) to response values (0-3)
        
        Returns:
            Dictionary containing:
                - subscale_scores: Scores for each subscale (0.0-3.0)
                - total_score: Total mean score (0.0-3.0)
                - item_scores: Individual item scores
                - interpretation: Clinical interpretation
        
        Raises:
            ALSShortError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise ALSShortError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate subscale scores
        anxiety_depression_score = self._calculate_subscale_mean(
            answers, self.ANXIETY_DEPRESSION_ITEMS
        )
        depression_elation_score = self._calculate_subscale_mean(
            answers, self.DEPRESSION_ELATION_ITEMS
        )
        anger_score = self._calculate_subscale_mean(
            answers, self.ANGER_ITEMS
        )
        
        # Calculate total score (mean of all 18 items)
        total_score = sum(answers[f"q{i}"] for i in range(1, 19)) / 18.0
        
        # Collect item scores
        item_scores = {}
        for i in range(1, 19):
            qid = f"q{i}"
            item_scores[qid] = {
                "score": answers[qid],
                "subscales": []
            }
            if i in self.ANXIETY_DEPRESSION_ITEMS:
                item_scores[qid]["subscales"].append("anxiety_depression")
            if i in self.DEPRESSION_ELATION_ITEMS:
                item_scores[qid]["subscales"].append("depression_elation")
            if i in self.ANGER_ITEMS:
                item_scores[qid]["subscales"].append("anger")
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            total_score,
            anxiety_depression_score,
            depression_elation_score,
            anger_score
        )
        
        return {
            "subscale_scores": {
                "anxiety_depression": round(anxiety_depression_score, 2),
                "depression_elation": round(depression_elation_score, 2),
                "anger": round(anger_score, 2)
            },
            "total_score": round(total_score, 2),
            "score_range": [0.0, 3.0],
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _calculate_subscale_mean(self, answers: Dict[str, int], items: List[int]) -> float:
        """
        Calculate mean score for a subscale.
        
        Args:
            answers: Dictionary of answers
            items: List of item numbers (1-indexed)
        
        Returns:
            Mean score (0.0-3.0)
        """
        return sum(answers[f"q{i}"] for i in items) / float(len(items))
    
    def _generate_interpretation(
        self,
        total_score: float,
        anxiety_depression: float,
        depression_elation: float,
        anger: float
    ) -> str:
        """
        Generate clinical interpretation based on scores.
        
        Args:
            total_score: Total mean score
            anxiety_depression: Anxiety-Depression subscale score
            depression_elation: Depression-Elation subscale score
            anger: Anger subscale score
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = f"Score total de {total_score:.2f}/3.00 indique "
        
        if total_score < 0.75:
            interpretation += (
                "une labilité émotionnelle très faible. Le patient rapporte une stabilité "
                "émotionnelle dans la norme, avec peu de fluctuations d'humeur rapides."
            )
        elif total_score < 1.5:
            interpretation += (
                "une labilité émotionnelle faible à modérée. Le patient rapporte des "
                "fluctuations d'humeur occasionnelles mais dans les limites normales."
            )
        elif total_score < 2.25:
            interpretation += (
                "une labilité émotionnelle modérée à élevée. Le patient rapporte des "
                "fluctuations d'humeur fréquentes qui peuvent affecter le fonctionnement quotidien. "
                "Une évaluation clinique approfondie est recommandée."
            )
        else:
            interpretation += (
                "une labilité émotionnelle sévère. Le patient rapporte des fluctuations "
                "d'humeur très fréquentes et rapides, suggérant une instabilité émotionnelle "
                "significative nécessitant une attention clinique immédiate."
            )
        
        # Add subscale details
        interpretation += "\n\nDétails par dimension:"
        
        interpretation += f"\n• Anxiété-Dépression ({anxiety_depression:.2f}/3.00): "
        if anxiety_depression >= 2.25:
            interpretation += "Oscillations marquées entre anxiété et tristesse."
        elif anxiety_depression >= 1.5:
            interpretation += "Oscillations modérées entre anxiété et tristesse."
        else:
            interpretation += "Oscillations faibles ou absentes entre anxiété et tristesse."
        
        interpretation += f"\n• Dépression-Élation ({depression_elation:.2f}/3.00): "
        if depression_elation >= 2.25:
            interpretation += "Oscillations marquées entre dépression et élévation d'humeur."
        elif depression_elation >= 1.5:
            interpretation += "Oscillations modérées entre dépression et élévation d'humeur."
        else:
            interpretation += "Oscillations faibles ou absentes entre dépression et élévation d'humeur."
        
        interpretation += f"\n• Colère ({anger:.2f}/3.00): "
        if anger >= 2.25:
            interpretation += "Oscillations marquées vers/depuis la colère, contrôle émotionnel difficile."
        elif anger >= 1.5:
            interpretation += "Oscillations modérées vers/depuis la colère."
        else:
            interpretation += "Oscillations faibles ou absentes vers/depuis la colère."
        
        return interpretation
    
    def get_schema(self) -> Dict[str, Any]:
        """
        Get complete questionnaire schema in JSON format.
        
        Returns:
            Complete questionnaire schema
        """
        return {
            "instrument": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions(),
            "logic": {
                "validators": [
                    {
                        "id": "presence_all",
                        "level": "error",
                        "message": "Les 18 items doivent être renseignés (A..D mappés à 3..0)."
                    },
                    {
                        "id": "range_0_3",
                        "level": "error",
                        "message": "Chaque item doit être un entier 0..3 (A=3,B=2,C=1,D=0)."
                    }
                ]
            },
            "scoring": {
                "variables": [],
                "scales": [
                    {
                        "id": "als_anx_dep",
                        "label": "Anxiété–Dépression (moyenne 0–3)",
                        "description": "Moyenne des items 1,3,5,6,7",
                        "items": [f"q{i}" for i in self.ANXIETY_DEPRESSION_ITEMS],
                        "range": [0, 3]
                    },
                    {
                        "id": "als_dep_elat",
                        "label": "Dépression–Élation (moyenne 0–3)",
                        "description": "Moyenne des items 2,10,12,13,15,16,17,18",
                        "items": [f"q{i}" for i in self.DEPRESSION_ELATION_ITEMS],
                        "range": [0, 3]
                    },
                    {
                        "id": "als_colere",
                        "label": "Colère (moyenne 0–3)",
                        "description": "Moyenne des items 4,8,9,11,14",
                        "items": [f"q{i}" for i in self.ANGER_ITEMS],
                        "range": [0, 3]
                    },
                    {
                        "id": "als_total",
                        "label": "ALS – Score total (moyenne 0–3)",
                        "description": "Moyenne des 18 items (A=3…D=0).",
                        "items": [f"q{i}" for i in range(1, 19)],
                        "range": [0, 3]
                    }
                ]
            },
            "provenance": {
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z",
                "validated_by": "IngénieurQuestionnaire",
                "validation_date": datetime.utcnow().date().isoformat()
            }
        }


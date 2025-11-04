"""
CSM (Composite Scale of Morningness)

This module implements the CSM, a 13-item self-report questionnaire measuring
morningness-eveningness preferences (chronotype).
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class CSMError(Exception):
    """Custom exception for CSM questionnaire errors."""
    pass


class CSM:
    """
    CSM (Composite Scale of Morningness)
    
    A 13-item self-report questionnaire assessing circadian preference
    (morningness-eveningness). Higher scores indicate greater morningness.
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (CSM)
        language: Language code
        version: Version number
        reference_period: Time frame for responses
        description: Brief description of the questionnaire
    """
    
    # Allowed values per item (heterogeneous scoring)
    ALLOWED_VALUES = {
        "q1": {1, 2, 3, 4, 5},  # 5-point
        "q2": {1, 2, 3, 4, 5},  # 5-point
        "q3": {1, 2, 3, 4},     # 4-point
        "q4": {1, 2, 3, 4},     # 4-point
        "q5": {1, 2, 3, 4},     # 4-point
        "q6": {1, 2, 3, 4},     # 4-point
        "q7": {1, 2, 3, 4, 5},  # 5-point
        "q8": {1, 2, 3, 4},     # 4-point
        "q9": {1, 2, 3, 4},     # 4-point
        "q10": {1, 2, 3, 4},    # 4-point
        "q11": {1, 2, 3, 4},    # 4-point
        "q12": {1, 2, 3, 4},    # 4-point
        "q13": {1, 2, 3, 4}     # 4-point
    }
    
    # Question definitions with their options
    QUESTIONS = [
        {
            "id": "q1",
            "text": "Heure de lever préférée si entièrement libre d'organiser la journée ?",
            "options": [
                (5, "entre 5h 00 et 6h 30"),
                (4, "entre 6h 30 et 7h 45"),
                (3, "entre 7h 45 et 9h 45"),
                (2, "entre 9h 45 et 11h 00"),
                (1, "entre 11h 00 et midi")
            ]
        },
        {
            "id": "q2",
            "text": "Heure de coucher préférée si entièrement libre d'organiser la soirée ?",
            "options": [
                (5, "entre 20h 00 et 21h 00"),
                (4, "entre 21h 00 et 22h 15"),
                (3, "entre 22h 15 et 0h 30"),
                (2, "entre 0h 30 et 1h 45"),
                (1, "entre 1h 45 et 3h 00")
            ]
        },
        {
            "id": "q3",
            "text": "Facilité à vous lever le matin (conditions adéquates) ?",
            "options": [
                (1, "pas facile du tout"),
                (2, "pas très facile"),
                (3, "assez facile"),
                (4, "très facile")
            ]
        },
        {
            "id": "q4",
            "text": "Éveil durant la demi-heure suivant le réveil ?",
            "options": [
                (1, "pas du tout réveillé"),
                (2, "peu éveillé"),
                (3, "relativement éveillé"),
                (4, "très éveillé")
            ]
        },
        {
            "id": "q5",
            "text": "État général durant la demi-heure suivant le réveil ?",
            "options": [
                (1, "très fatigué"),
                (2, "plutôt fatigué"),
                (3, "plutôt en forme"),
                (4, "tout à fait frais et dispos")
            ]
        },
        {
            "id": "q6",
            "text": "Forme pour pratiquer une séance de sport 7–8h le matin (deux fois/semaine) ?",
            "options": [
                (4, "Bonne forme"),
                (3, "Forme raisonnable"),
                (2, "Vous trouvez cela difficile"),
                (1, "Vous trouvez cela très difficile")
            ]
        },
        {
            "id": "q7",
            "text": "Heure du soir à laquelle vous devez aller vous coucher (fatigue) ?",
            "options": [
                (5, "entre 20h 00 et 21h 00"),
                (4, "entre 21h 00 et 22h 15"),
                (3, "entre 22h 15 et 0h 30"),
                (2, "entre 0h 30 et 1h 45"),
                (1, "entre 1h 45 et 3h 00")
            ]
        },
        {
            "id": "q8",
            "text": "Plage horaire à laquelle vous seriez le plus efficace pour un examen de 2h ?",
            "options": [
                (4, "entre 8h 00 et 10h 00"),
                (3, "entre 11h 00 et 13h 00"),
                (2, "entre 15h 00 et 17h 00"),
                (1, "entre 19h 00 et 21h 00")
            ]
        },
        {
            "id": "q9",
            "text": "Vous vous décririez comme…",
            "options": [
                (4, "tout à fait « du matin »"),
                (3, "plutôt « du matin » que « du soir »"),
                (2, "plutôt « du soir » que « du matin »"),
                (1, "tout à fait « du soir »")
            ]
        },
        {
            "id": "q10",
            "text": "Heure de lever préférée pour une journée de travail de 8h (librement organisée) ?",
            "options": [
                (4, "avant 6h 30"),
                (3, "entre 6h 30 et 7h 30"),
                (2, "entre 7h 30 et 8h 30"),
                (1, "après 8h 30")
            ]
        },
        {
            "id": "q11",
            "text": "Si vous deviez toujours vous lever à 6h 00, cela vous paraîtrait…",
            "options": [
                (1, "affreusement difficile"),
                (2, "plutôt difficile et déplaisant"),
                (3, "déplaisant sans plus"),
                (4, "sans aucune difficulté")
            ]
        },
        {
            "id": "q12",
            "text": "Après une bonne nuit, temps pour être pleinement réveillé ?",
            "options": [
                (4, "moins de 10 minutes"),
                (3, "entre 11 et 20 minutes"),
                (2, "entre 21 et 40 minutes"),
                (1, "plus de 40 minutes")
            ]
        },
        {
            "id": "q13",
            "text": "Dans quelle partie de la journée êtes-vous le plus actif(ve) ?",
            "options": [
                (4, "nettement actif le matin"),
                (3, "plutôt actif le matin"),
                (2, "plutôt actif le soir"),
                (1, "nettement actif le soir")
            ]
        }
    ]
    
    def __init__(self):
        """Initialize the CSM questionnaire."""
        self.id = "CSM.fr"
        self.name = "Composite Scale of Morningness (CSM) – Version française"
        self.abbreviation = "CSM"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Rythme de vie habituel (sans contrainte)"
        self.description = (
            "Échelle de matinalité en 13 items. Cotation hétérogène par item "
            "(scores 1..5 ou 1..4 selon la question). Score total = somme des items (13–55)."
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
            "num_items": 13,
            "response_scale": "Heterogeneous (1-5 for Q1,Q2,Q7; 1-4 for others)",
            "score_range": [13, 55],
            "score_type": "sum",
            "interpretation": "Higher score = greater morningness preference"
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        for i, q_data in enumerate(self.QUESTIONS, start=1):
            question = {
                "id": q_data["id"],
                "number": i,
                "section_id": "sec1",
                "text": f"{i}. {q_data['text']}",
                "type": "single_choice",
                "required": True,
                "options": [
                    {"code": code, "label": label, "score": code}
                    for code, label in q_data["options"]
                ],
                "allowed_values": sorted(list(self.ALLOWED_VALUES[q_data["id"]]))
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
                "label": "CSM – 13 items",
                "description": "Cochez UNE réponse par question",
                "question_ids": [f"q{i}" for i in range(1, 14)]
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate questionnaire responses.
        
        Args:
            answers: Dictionary mapping question IDs to response values
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            CSMError: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all 13 items are present
        expected_items = [f"q{i}" for i in range(1, 14)]
        missing = [qid for qid in expected_items if qid not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate each response value against allowed values for that item
        for qid in expected_items:
            if qid in answers:
                value = answers[qid]
                allowed = self.ALLOWED_VALUES[qid]
                
                if not isinstance(value, int):
                    errors.append(f"{qid}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value not in allowed:
                    errors.append(
                        f"{qid}: la valeur doit être dans {sorted(allowed)} (reçu: {value})"
                    )
        
        # Check for unusual patterns
        if not errors and len(set(answers.values())) == 1:
            warnings.append(
                "Toutes les réponses sont identiques. Veuillez vérifier que le patient "
                "a bien compris les instructions."
            )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate CSM score.
        
        Args:
            answers: Dictionary mapping question IDs (q1-q13) to response values
        
        Returns:
            Dictionary containing:
                - total_score: Sum of all items (13-55)
                - chronotype: Chronotype category
                - item_scores: Individual item scores
                - interpretation: Clinical interpretation
        
        Raises:
            CSMError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise CSMError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate total score (sum of all items)
        total_score = sum(answers[f"q{i}"] for i in range(1, 14))
        
        # Determine chronotype category
        chronotype = self._get_chronotype(total_score)
        
        # Collect item scores
        item_scores = {}
        for i in range(1, 14):
            qid = f"q{i}"
            item_scores[qid] = {
                "score": answers[qid],
                "allowed_range": sorted(list(self.ALLOWED_VALUES[qid]))
            }
        
        # Generate interpretation
        interpretation = self._generate_interpretation(total_score, chronotype)
        
        return {
            "total_score": total_score,
            "score_range": [13, 55],
            "chronotype": chronotype,
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_chronotype(self, total_score: int) -> str:
        """
        Determine chronotype category based on total score.
        
        Args:
            total_score: Total CSM score (13-55)
        
        Returns:
            Chronotype category label
        """
        # Note: These thresholds are approximate as exact norms vary by study
        # General interpretation: higher = more morning type
        if total_score >= 47:
            return "Type matinal marqué"
        elif total_score >= 41:
            return "Type modérément matinal"
        elif total_score >= 31:
            return "Type intermédiaire"
        elif total_score >= 23:
            return "Type modérément vespéral"
        else:
            return "Type vespéral marqué"
    
    def _generate_interpretation(self, total_score: int, chronotype: str) -> str:
        """
        Generate clinical interpretation based on score.
        
        Args:
            total_score: Total CSM score
            chronotype: Chronotype category
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = f"Score CSM de {total_score}/55 indique un {chronotype}.\n\n"
        
        if total_score >= 47:
            interpretation += (
                "Le patient présente une préférence circadienne très marquée pour le matin. "
                "Il se sent naturellement en forme tôt le matin, se couche tôt, et a une "
                "performance optimale en matinée.\n\n"
                "Caractéristiques typiques:\n"
                "• Réveil spontané et facile tôt le matin\n"
                "• Meilleure performance cognitive et physique en matinée\n"
                "• Fatigue précoce en soirée\n"
                "• Difficulté avec les activités tardives\n\n"
                "Recommandations:\n"
                "• Planifier les activités importantes en matinée\n"
                "• Respecter un horaire de coucher précoce\n"
                "• Éviter les obligations professionnelles tardives si possible"
            )
        elif total_score >= 41:
            interpretation += (
                "Le patient présente une tendance modérée à être matinal. "
                "Il préfère se lever relativement tôt et est plus performant en matinée.\n\n"
                "Caractéristiques typiques:\n"
                "• Réveil matinal relativement facile\n"
                "• Bonne forme en matinée\n"
                "• Préférence pour un coucher pas trop tardif\n"
                "• Performance satisfaisante en journée\n\n"
                "Recommandations:\n"
                "• Privilégier les activités exigeantes en matinée\n"
                "• Maintenir une régularité des horaires\n"
                "• Adapter l'emploi du temps aux préférences circadiennes"
            )
        elif total_score >= 31:
            interpretation += (
                "Le patient présente un type circadien intermédiaire (neutre). "
                "Il s'adapte relativement bien aux horaires matinaux comme vespéraux.\n\n"
                "Caractéristiques typiques:\n"
                "• Flexibilité horaire\n"
                "• Adaptation aux contraintes professionnelles\n"
                "• Performance stable tout au long de la journée\n"
                "• Pas de préférence marquée matin/soir\n\n"
                "Recommandations:\n"
                "• Profiter de cette flexibilité circadienne\n"
                "• Maintenir une régularité des horaires pour un sommeil optimal\n"
                "• Adapter selon les besoins professionnels/personnels"
            )
        elif total_score >= 23:
            interpretation += (
                "Le patient présente une tendance modérée à être vespéral (du soir). "
                "Il préfère se coucher tard et a de la difficulté avec les levers précoces.\n\n"
                "Caractéristiques typiques:\n"
                "• Difficulté à se lever tôt\n"
                "• Éveil lent le matin\n"
                "• Meilleure forme en après-midi et soirée\n"
                "• Préférence pour un coucher tardif\n\n"
                "Recommandations:\n"
                "• Éviter les obligations très matinales si possible\n"
                "• Planifier les activités importantes en après-midi\n"
                "• Exposition à la lumière vive le matin pour avancer la phase circadienne si nécessaire\n"
                "• Éviter la lumière forte le soir"
            )
        else:
            interpretation += (
                "Le patient présente un type vespéral marqué (couche-tard). "
                "Il a une préférence circadienne très marquée pour le soir, avec des difficultés "
                "importantes pour les activités matinales.\n\n"
                "Caractéristiques typiques:\n"
                "• Difficulté majeure au réveil matinal\n"
                "• Éveil très lent, sensation de brouillard matinal\n"
                "• Performance optimale en soirée\n"
                "• Coucher naturellement très tardif\n\n"
                "Recommandations:\n"
                "• Aménagements professionnels si possible (horaires flexibles)\n"
                "• Éviter les levers très précoces\n"
                "• Chronothérapie si désynchronisation problématique\n"
                "• Exposition lumineuse matinale progressive\n"
                "• Hygiène du sommeil stricte\n\n"
                "⚠️ Attention: Les personnes très vespérales en horaires matinaux forcés "
                "peuvent développer des troubles du sommeil, fatigue chronique, ou symptômes dépressifs."
            )
        
        # Add clinical significance
        interpretation += "\n\n=== SIGNIFICATION CLINIQUE ===\n"
        
        if total_score >= 41 or total_score <= 23:
            interpretation += (
                "Un chronotype marqué (très matinal ou très vespéral) peut avoir des implications "
                "importantes pour:\n"
                "• La santé mentale (risque de dépression si désynchronisation chronique)\n"
                "• La performance professionnelle\n"
                "• Les relations sociales\n"
                "• La qualité de vie globale\n\n"
                "Une adaptation de l'environnement au chronotype naturel est recommandée "
                "lorsque possible."
            )
        else:
            interpretation += (
                "Un type circadien intermédiaire offre une bonne flexibilité d'adaptation. "
                "Maintenir une régularité des horaires optimise le sommeil et la vigilance."
            )
        
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
                        "message": "Les 13 items doivent être renseignés."
                    },
                    {
                        "id": "range_per_item",
                        "level": "error",
                        "message": "Chaque item doit respecter ses valeurs autorisées (voir options)."
                    }
                ]
            },
            "scoring": {
                "scales": [
                    {
                        "id": "csm_total",
                        "label": "CSM – Score total",
                        "description": "Somme des 13 items (13–55). Score élevé = préférence matinale plus marquée.",
                        "items": [f"q{i}" for i in range(1, 14)],
                        "range": [13, 55]
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


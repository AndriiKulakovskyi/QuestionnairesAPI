"""
ASRS v1.1 (Adult ADHD Self-Report Scale)

This module implements the ASRS v1.1, an 18-item screening tool for adult ADHD
developed by the World Health Organization.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class ASRSError(Exception):
    """Custom exception for ASRS questionnaire errors."""
    pass


class ASRS:
    """
    ASRS v1.1 (Adult ADHD Self-Report Scale)
    
    An 18-item screening questionnaire for adult ADHD, consisting of:
    - Part A: 6 screening items with specific thresholds
    - Part B: 12 additional informative items
    
    Screening is POSITIVE if ≥4 Part A items meet their thresholds.
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (ASRS v1.1)
        language: Language code
        version: Version number
        reference_period: Time frame for responses (6 months)
        description: Brief description of the questionnaire
    """
    
    # Part A thresholds for "shaded" responses
    # Items 1-3: threshold ≥2, Items 4-6: threshold ≥3
    PART_A_THRESHOLDS = {
        1: 2,  # a1 ≥ 2
        2: 2,  # a2 ≥ 2
        3: 2,  # a3 ≥ 2
        4: 3,  # a4 ≥ 3
        5: 3,  # a5 ≥ 3
        6: 3   # a6 ≥ 3
    }
    
    # Item texts for Part A (screening items)
    PART_A_TEXTS = [
        "A1. À quelle fréquence vous arrive-t-il d'avoir des difficultés à finaliser les détails d'un projet une fois que les parties les plus stimulantes ont été faites ?",
        "A2. À quelle fréquence vous arrive-t-il d'avoir des difficultés à mettre de l'ordre dans les choses ou dans votre vie quand vous devez faire quelque chose qui demande de l'organisation ?",
        "A3. À quelle fréquence avez-vous des difficultés à vous rappeler d'honorer des rendez-vous ou des obligations ?",
        "A4. Quand vous avez une tâche qui requiert beaucoup de réflexion, à quelle fréquence remettez-vous les choses à plus tard ?",
        "A5. À quelle fréquence vous arrive-t-il de remuer ou de vous tortiller avec les mains ou les pieds lorsque vous devez rester assis(e) pendant une longue période ?",
        "A6. À quelle fréquence vous sentez-vous trop actif(ve), obligé(e) d'agir comme si vous étiez « drivé(e) par un moteur » ?"
    ]
    
    # Item texts for Part B (additional items)
    PART_B_TEXTS = [
        "B7. À quelle fréquence vous arrive-t-il de faire des fautes d'étourderie lorsque vous travaillez sur un projet ou une tâche qui demande de l'attention ?",
        "B8. À quelle fréquence vous arrive-t-il d'avoir des difficultés à vous concentrer lorsque vous faites un travail ennuyeux ou répétitif ?",
        "B9. À quelle fréquence vous arrive-t-il d'avoir des difficultés à vous concentrer sur les propos de votre interlocuteur, même s'il s'adresse directement à vous ?",
        "B10. À la maison ou au travail, à quelle fréquence vous arrive-t-il d'égarer des choses ou d'avoir des difficultés à les retrouver ?",
        "B11. À quelle fréquence vous arrive-t-il d'être distrait(e) par l'activité ou par le bruit autour de vous ?",
        "B12. À quelle fréquence vous arrive-t-il de quitter votre siège pendant des réunions ou d'autres situations où vous devez rester assis(e) ?",
        "B13. À quelle fréquence vous arrive-t-il d'avoir des difficultés à attendre votre tour ?",
        "B14. À quelle fréquence vous arrive-t-il d'interrompre les gens ou d'empiéter sur les activités des autres (par exemple : se mêler de ce que font d'autres gens) ?",
        "B15. À quelle fréquence vous arrive-t-il d'avoir des difficultés à vous détendre et à vous reposer ?",
        "B16. À quelle fréquence vous arrive-t-il d'achever la plupart des tâches que vous commencez ? (item inversé pour le sens clinique, mais non pour la cotation ASRS)",
        "B17. À quelle fréquence vous arrive-t-il d'éviter ou d'avoir du mal à commencer des tâches qui demandent un effort mental soutenu ?",
        "B18. À quelle fréquence vous arrive-t-il de parler trop, plus que les autres ?"
    ]
    
    # Response options (0-4)
    RESPONSE_OPTIONS = [
        {"code": 0, "label": "Jamais", "score": 0},
        {"code": 1, "label": "Rarement", "score": 1},
        {"code": 2, "label": "Parfois", "score": 2},
        {"code": 3, "label": "Souvent", "score": 3},
        {"code": 4, "label": "Très souvent", "score": 4}
    ]
    
    def __init__(self):
        """Initialize the ASRS v1.1 questionnaire."""
        self.id = "ASRS-v1.1.fr"
        self.name = "Échelle d'autoévaluation du TDAH chez l'adulte (ASRS v1.1) – Version française"
        self.abbreviation = "ASRS v1.1"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Au cours des 6 derniers mois"
        self.description = (
            "18 items (Partie A: 6 items de dépistage; Partie B: 12 items complémentaires). "
            "Réponses 0..4 (0=Jamais … 4=Très souvent). "
            "Dépistage POSITIF si ≥4 cases ombrées cochées en Partie A avec seuils par item."
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
            "response_scale": "5-point scale (0=Jamais to 4=Très souvent)",
            "part_a_items": 6,
            "part_b_items": 12,
            "screening_threshold": "≥4 shaded items in Part A",
            "thresholds": self.PART_A_THRESHOLDS
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        
        # Part A questions
        for i, text in enumerate(self.PART_A_TEXTS, start=1):
            question = {
                "id": f"a{i}",
                "number": i,
                "section_id": "partA",
                "text": text,
                "type": "single_choice",
                "required": True,
                "options": self.RESPONSE_OPTIONS.copy(),
                "threshold": self.PART_A_THRESHOLDS[i],
                "part": "A"
            }
            questions.append(question)
        
        # Part B questions
        for j, text in enumerate(self.PART_B_TEXTS, start=7):
            question = {
                "id": f"b{j}",
                "number": j,
                "section_id": "partB",
                "text": text,
                "type": "single_choice",
                "required": True,
                "options": self.RESPONSE_OPTIONS.copy(),
                "part": "B"
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
                "id": "partA",
                "label": "Partie A (items de dépistage, A1–A6)",
                "description": "Fréquence au cours des 6 derniers mois",
                "question_ids": [f"a{i}" for i in range(1, 7)]
            },
            {
                "id": "partB",
                "label": "Partie B (items complémentaires, B7–B18)",
                "description": "Fréquence au cours des 6 derniers mois",
                "question_ids": [f"b{i}" for i in range(7, 19)]
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate questionnaire responses.
        
        Args:
            answers: Dictionary mapping question IDs to response values (0-4)
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            ASRSError: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all items are present
        a_keys = [f"a{i}" for i in range(1, 7)]
        b_keys = [f"b{i}" for i in range(7, 19)]
        expected_items = a_keys + b_keys
        missing = [qid for qid in expected_items if qid not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate each response value
        for qid in expected_items:
            if qid in answers:
                value = answers[qid]
                if not isinstance(value, int):
                    errors.append(f"{qid}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value < 0 or value > 4:
                    errors.append(f"{qid}: la valeur doit être entre 0 et 4 (reçu: {value})")
        
        # Check for unusual patterns in Part A
        if not errors:
            a_values = [answers.get(f"a{i}", -1) for i in range(1, 7)]
            if len(set(a_values)) == 1 and a_values[0] != -1:
                warnings.append(
                    "Toutes les réponses de la Partie A sont identiques. "
                    "Veuillez vérifier que le patient a bien compris les instructions."
                )
            
            # Check if all responses are "Jamais" (possible denial)
            if all(answers.get(qid, -1) == 0 for qid in a_keys):
                warnings.append(
                    "Toutes les réponses de la Partie A sont à 0 (Jamais). "
                    "Cela peut indiquer une sous-évaluation des symptômes."
                )
            
            # Check if all responses are "Très souvent" (possible over-reporting)
            if all(answers.get(qid, -1) == 4 for qid in a_keys):
                warnings.append(
                    "Toutes les réponses de la Partie A sont à 4 (Très souvent). "
                    "Vérifier la validité des réponses ou la présence de symptômes sévères."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_screening(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate ASRS v1.1 screening result.
        
        Args:
            answers: Dictionary mapping question IDs to response values (0-4)
        
        Returns:
            Dictionary containing:
                - screening_result: "POSITIF" or "NEGATIF"
                - shaded_count: Number of Part A items meeting threshold (0-6)
                - shaded_items: List of shaded item IDs
                - part_a_responses: Responses for Part A items
                - part_b_responses: Responses for Part B items (informative)
                - interpretation: Clinical interpretation
        
        Raises:
            ASRSError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise ASRSError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate shaded items in Part A
        shaded_count = 0
        shaded_items = []
        part_a_details = {}
        
        for i in range(1, 7):
            qid = f"a{i}"
            value = answers[qid]
            threshold = self.PART_A_THRESHOLDS[i]
            is_shaded = value >= threshold
            
            if is_shaded:
                shaded_count += 1
                shaded_items.append(qid)
            
            part_a_details[qid] = {
                "value": value,
                "threshold": threshold,
                "shaded": is_shaded
            }
        
        # Determine screening result
        screening_result = "POSITIF" if shaded_count >= 4 else "NEGATIF"
        
        # Collect Part B responses (informative)
        part_b_details = {}
        for j in range(7, 19):
            qid = f"b{j}"
            part_b_details[qid] = {
                "value": answers[qid]
            }
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            screening_result,
            shaded_count,
            part_a_details,
            part_b_details
        )
        
        return {
            "screening_result": screening_result,
            "shaded_count": shaded_count,
            "shaded_items": shaded_items,
            "part_a_responses": part_a_details,
            "part_b_responses": part_b_details,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _generate_interpretation(
        self,
        screening_result: str,
        shaded_count: int,
        part_a_details: Dict[str, Any],
        part_b_details: Dict[str, Any]
    ) -> str:
        """
        Generate clinical interpretation based on screening result.
        
        Args:
            screening_result: "POSITIF" or "NEGATIF"
            shaded_count: Number of shaded items (0-6)
            part_a_details: Details of Part A responses
            part_b_details: Details of Part B responses
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = f"Résultat du dépistage ASRS v1.1: {screening_result}\n"
        interpretation += f"Nombre d'items ombrés en Partie A: {shaded_count}/6\n\n"
        
        if screening_result == "POSITIF":
            interpretation += (
                "⚠️ DÉPISTAGE POSITIF - Le patient présente un profil compatible avec un TDAH adulte.\n\n"
                "Recommandations:\n"
                "• Évaluation diagnostique complète par un spécialiste (psychiatre, neurologue)\n"
                "• Entretien clinique structuré (DIVA, CAADID)\n"
                "• Recherche d'antécédents d'enfance de TDAH\n"
                "• Évaluation du retentissement fonctionnel (professionnel, social, familial)\n"
                "• Dépistage de comorbidités (anxiété, dépression, troubles addictifs)\n\n"
                "ATTENTION: L'ASRS est un outil de dépistage, pas un outil diagnostique. "
                "Un résultat positif nécessite une confirmation diagnostique par un clinicien."
            )
        else:
            if shaded_count >= 3:
                interpretation += (
                    "DÉPISTAGE NÉGATIF - Cependant, le nombre d'items ombrés est proche du seuil.\n\n"
                    "Recommandations:\n"
                    "• Surveillance clinique si symptômes gênants rapportés\n"
                    "• Réévaluation si aggravation des symptômes\n"
                    "• Considérer d'autres diagnostics différentiels (anxiété, dépression)\n"
                )
            else:
                interpretation += (
                    "DÉPISTAGE NÉGATIF - Le profil n'est pas compatible avec un TDAH adulte.\n\n"
                    "Recommandations:\n"
                    "• Si symptômes gênants présents, explorer d'autres diagnostics différentiels\n"
                    "• Considérer: troubles anxieux, dépression, troubles du sommeil, stress\n"
                    "• Réévaluer si symptômes nouveaux ou aggravation\n"
                )
        
        # Analyze Part A symptom pattern
        interpretation += "\n=== ANALYSE DES SYMPTÔMES (Partie A) ===\n"
        
        inattention_items = ["a1", "a2", "a3", "a4"]  # Items liés à l'inattention
        hyperactivity_items = ["a5", "a6"]  # Items liés à l'hyperactivité
        
        inattention_shaded = sum(1 for item in inattention_items 
                                 if part_a_details[item]["shaded"])
        hyperactivity_shaded = sum(1 for item in hyperactivity_items 
                                   if part_a_details[item]["shaded"])
        
        interpretation += f"\n• Symptômes d'inattention: {inattention_shaded}/4 items ombrés"
        if inattention_shaded >= 3:
            interpretation += " (symptômes marqués)"
        elif inattention_shaded >= 2:
            interpretation += " (symptômes modérés)"
        
        interpretation += f"\n• Symptômes d'hyperactivité: {hyperactivity_shaded}/2 items ombrés"
        if hyperactivity_shaded == 2:
            interpretation += " (symptômes marqués)"
        elif hyperactivity_shaded == 1:
            interpretation += " (symptômes modérés)"
        
        # Part B summary (informative)
        part_b_high = sum(1 for qid in part_b_details 
                         if part_b_details[qid]["value"] >= 3)
        interpretation += f"\n\nPartie B (informative): {part_b_high}/12 items avec réponse 'Souvent' ou 'Très souvent'"
        
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
                        "message": "Les 18 items doivent être renseignés (0=Jamais … 4=Très souvent)."
                    },
                    {
                        "id": "range_0_4",
                        "level": "error",
                        "message": "Chaque item doit être un entier entre 0 et 4."
                    }
                ]
            },
            "scoring": {
                "variables": [
                    {"id": f"a{i}_shaded", "description": f"Item A{i} meets threshold (≥{self.PART_A_THRESHOLDS[i]})"} 
                    for i in range(1, 7)
                ] + [
                    {"id": "a_shaded_count", "description": "Count of shaded items in Part A"}
                ],
                "scales": [
                    {
                        "id": "asrs_screen_result",
                        "label": "ASRS v1.1 – Résultat du dépistage (Partie A)",
                        "description": "POSITIF si ≥4 cases ombrées (selon seuils) cochées en Partie A ; sinon NÉGATIF.",
                        "items": [f"a{i}" for i in range(1, 7)],
                        "range": ["NEGATIF", "POSITIF"]
                    }
                ]
            },
            "provenance": {
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z",
                "validated_by": "IngénieurQuestionnaire",
                "validation_date": datetime.utcnow().date().isoformat(),
                "references": [
                    "Kessler RC et al., Psychol Med. 2005;35:245–256.",
                    "World Health Organization (WHO) Adult ADHD Self-Report Scale"
                ]
            }
        }


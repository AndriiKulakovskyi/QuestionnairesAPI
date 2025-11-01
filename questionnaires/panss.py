"""
Questionnaire: PANSS (Positive and Negative Syndrome Scale)
Échelle des Syndromes Positifs et Négatifs
"""

from typing import Dict, List, Optional, Any


class PANSSQuestionnaire:
    """PANSS - Positive and Negative Syndrome Scale
    
    Hétéro-évaluation standardisée de la schizophrénie en 30 items:
    - 7 Symptômes positifs (P1-P7)
    - 7 Symptômes négatifs (N1-N7)
    - 16 Psychopathologie générale (G1-G16)
    
    Chaque item coté de 1 (absent) à 7 (extrême).
    Score total: 30-210
    
    Développé par Kay, Fiszbein & Opler (1986)
    Traduction française: Lépine (1989)
    """
    
    def __init__(self):
        self.name = "PANSS - Positive and Negative Syndrome Scale"
        self.description = ("Évaluation clinique standardisée de la schizophrénie en 30 items. "
                           "Mesure les symptômes positifs, négatifs et la psychopathologie générale.")
        self.used_in_applications = ["eschizo"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 30 PANSS items
        
        Each item is rated on a 7-point scale from 1 (absent) to 7 (extreme)
        """
        
        # Standard 7-point scale for all items
        response_scale = {
            1: "NÉANT - Définition non applicable",
            2: "MINIME - Pathologie discutable",
            3: "FAIBLE - Présent mais léger",
            4: "MODÉRÉ - Significatif",
            5: "MODÉRÉ, PRONONCÉ - Marqué",
            6: "PRONONCÉ - Sévère",
            7: "EXTRÊME - Très sévère"
        }
        
        # P items: Positive symptoms
        positive_items = [
            (1, "P1. DÉLIRE", "radhtml_p1"),
            (2, "P2. TROUBLES DE LA PENSÉE", "radhtml_p2"),
            (3, "P3. COMPORTEMENT HALLUCINATOIRE", "radhtml_p3"),
            (4, "P4. EXCITATION", "radhtml_p4"),
            (5, "P5. MÉGALOMANIE", "radhtml_p5"),
            (6, "P6. MÉFIANCE/COMPLEXE DE PERSÉCUTION", "radhtml_p6"),
            (7, "P7. HOSTILITÉ", "radhtml_p7")
        ]
        
        # N items: Negative symptoms
        negative_items = [
            (8, "N1. AFFECT ÉMOUSSÉ", "radhtml_n1"),
            (9, "N2. RETRAIT ÉMOTIONNEL", "radhtml_n2"),
            (10, "N3. CONTACT FAIBLE", "radhtml_n3"),
            (11, "N4. RETRAIT SOCIAL PASSIF/APATHIQUE", "radhtml_n4"),
            (12, "N5. DIFFICULTÉ DE RAISONNER DANS L'ABSTRAIT", "radhtml_n5"),
            (13, "N6. MANQUE DE SPONTANÉITÉ ET FLOT DE CONVERSATION", "radhtml_n6"),
            (14, "N7. PENSÉE STÉRÉOTYPÉE", "radhtml_n7")
        ]
        
        # G items: General psychopathology
        general_items = [
            (15, "G1. PRÉOCCUPATIONS SOMATIQUES", "radhtml_g1"),
            (16, "G2. ANXIÉTÉ", "radhtml_g2"),
            (17, "G3. SENTIMENTS DE CULPABILITÉ", "radhtml_g3"),
            (18, "G4. TENSION", "radhtml_g4"),
            (19, "G5. MANIÉRISME ET TROUBLES DE LA POSTURE", "radhtml_g5"),
            (20, "G6. DÉPRESSION", "radhtml_g6"),
            (21, "G7. RALENTISSEMENT PSYCHOMOTEUR", "radhtml_g7"),
            (22, "G8. MANQUE DE COOPÉRATION", "radhtml_g8"),
            (23, "G9. CONTENU INHABITUEL DE LA PENSÉE", "radhtml_g9"),
            (24, "G10. DÉSORIENTATION", "radhtml_g10"),
            (25, "G11. MANQUE D'ATTENTION", "radhtml_g11"),
            (26, "G12. MANQUE DE JUGEMENT ET DE PRISE DE CONSCIENCE", "radhtml_g12"),
            (27, "G13. TROUBLES DE LA VOLITION", "radhtml_g13"),
            (28, "G14. MAUVAIS CONTRÔLE PULSIONNEL", "radhtml_g14"),
            (29, "G15. PRÉOCCUPATION EXCESSIVE DE SOI", "radhtml_g15"),
            (30, "G16. ÉVITEMENT SOCIAL ACTIF", "radhtml_g16")
        ]
        
        # Combine all items
        all_items = positive_items + negative_items + general_items
        
        questions = []
        for item_num, text, field_id in all_items:
            question = {
                'id': field_id,
                'number': item_num,
                'text': text,
                'type': 'radio',
                'options': response_scale,
                'required': True
            }
            questions.append(question)
        
        return questions
    
    def calculate_score(self, responses: Dict[str, int]) -> Dict[str, Any]:
        """Calculate PANSS scores
        
        Generates:
        1. Positive symptoms subscale (P1-P7): Range 7-49
        2. Negative symptoms subscale (N1-N7): Range 7-49  
        3. General psychopathology subscale (G1-G16): Range 16-112
        4. Total PANSS score: Range 30-210
        5. Optional: Composite factor scores (multiple models available)
        
        Args:
            responses: Dictionary mapping field IDs to ratings (1-7)
            
        Returns:
            Dictionary containing all subscale scores, total, and interpretations
        """
        errors = []
        
        # Validate all responses
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses:
                errors.append(f"Item {question['text']} manquant")
            elif responses[q_id] < 1 or responses[q_id] > 7:
                errors.append(f"Item {question['text']} doit être entre 1 et 7")
        
        if errors:
            return {
                'valid': False,
                'errors': errors
            }
        
        # Calculate positive symptoms (P1-P7)
        positive_items = ['radhtml_p1', 'radhtml_p2', 'radhtml_p3', 'radhtml_p4',
                         'radhtml_p5', 'radhtml_p6', 'radhtml_p7']
        positive_score = sum(responses[item] for item in positive_items)
        
        # Calculate negative symptoms (N1-N7)
        negative_items = ['radhtml_n1', 'radhtml_n2', 'radhtml_n3', 'radhtml_n4',
                         'radhtml_n5', 'radhtml_n6', 'radhtml_n7']
        negative_score = sum(responses[item] for item in negative_items)
        
        # Calculate general psychopathology (G1-G16)
        general_items = ['radhtml_g1', 'radhtml_g2', 'radhtml_g3', 'radhtml_g4',
                        'radhtml_g5', 'radhtml_g6', 'radhtml_g7', 'radhtml_g8',
                        'radhtml_g9', 'radhtml_g10', 'radhtml_g11', 'radhtml_g12',
                        'radhtml_g13', 'radhtml_g14', 'radhtml_g15', 'radhtml_g16']
        general_score = sum(responses[item] for item in general_items)
        
        # Calculate total score
        total_score = positive_score + negative_score + general_score
        
        # Calculate composite factor scores (Wallwork 2012 model - most recent)
        factor_scores = self._calculate_wallwork_factors(responses)
        
        return {
            'positive_score': positive_score,
            'positive_range': '7-49',
            'positive_interpretation': self._interpret_subscale(positive_score, 7, 49),
            
            'negative_score': negative_score,
            'negative_range': '7-49',
            'negative_interpretation': self._interpret_subscale(negative_score, 7, 49),
            
            'general_score': general_score,
            'general_range': '16-112',
            'general_interpretation': self._interpret_subscale(general_score, 16, 112),
            
            'total_score': total_score,
            'total_range': '30-210',
            'total_interpretation': self._interpret_total(total_score),
            
            'factor_scores': factor_scores,
            
            'valid': True,
            'errors': []
        }
    
    def _calculate_wallwork_factors(self, responses: Dict[str, int]) -> Dict[str, int]:
        """Calculate 5-factor model scores (Wallwork et al., 2012)
        
        This is a validated factor structure for PANSS
        """
        # Positive factor: P1, P3, P5, P6, G9
        positive_factor = (responses['radhtml_p1'] + responses['radhtml_p3'] + 
                          responses['radhtml_p5'] + responses['radhtml_p6'] + 
                          responses['radhtml_g9'])
        
        # Negative factor: N1, N2, N3, N4, N6, G7, G16
        negative_factor = (responses['radhtml_n1'] + responses['radhtml_n2'] + 
                          responses['radhtml_n3'] + responses['radhtml_n4'] + 
                          responses['radhtml_n6'] + responses['radhtml_g7'] + 
                          responses['radhtml_g16'])
        
        # Disorganized (Cognitive) factor: P2, N5, G11, G13
        disorganized_factor = (responses['radhtml_p2'] + responses['radhtml_n5'] + 
                              responses['radhtml_g11'] + responses['radhtml_g13'])
        
        # Excited factor: P4, P7, G8, G14
        excited_factor = (responses['radhtml_p4'] + responses['radhtml_p7'] + 
                         responses['radhtml_g8'] + responses['radhtml_g14'])
        
        # Depressed (Emotional distress) factor: G2, G3, G6
        depressed_factor = (responses['radhtml_g2'] + responses['radhtml_g3'] + 
                           responses['radhtml_g6'])
        
        return {
            'positive_factor': positive_factor,
            'negative_factor': negative_factor,
            'disorganized_factor': disorganized_factor,
            'excited_factor': excited_factor,
            'depressed_factor': depressed_factor
        }
    
    def _interpret_subscale(self, score: int, min_val: int, max_val: int) -> str:
        """Interpret subscale score based on percentage of maximum"""
        # Calculate as percentage of maximum possible score
        range_size = max_val - min_val
        score_above_min = score - min_val
        percentage = (score_above_min / range_size) * 100
        
        if percentage < 20:
            return "Symptomatologie minimale"
        elif percentage < 40:
            return "Symptomatologie légère"
        elif percentage < 60:
            return "Symptomatologie modérée"
        elif percentage < 80:
            return "Symptomatologie importante"
        else:
            return "Symptomatologie sévère"
    
    def _interpret_total(self, score: int) -> str:
        """Interpret total PANSS score
        
        General guidelines (not strict cutoffs):
        - < 60: Mild
        - 60-95: Moderate
        - 96-120: Marked
        - > 120: Severe
        """
        if score < 60:
            return "Schizophrénie légère"
        elif score < 96:
            return "Schizophrénie modérée"
        elif score < 121:
            return "Schizophrénie marquée"
        else:
            return "Schizophrénie sévère"


# Example usage
if __name__ == "__main__":
    questionnaire = PANSSQuestionnaire()
    
    # Example: Patient with moderate schizophrenia
    example_responses = {
        # Positive symptoms (moderate)
        'radhtml_p1': 4,  # Délire modéré
        'radhtml_p2': 3,  # Troubles pensée faibles
        'radhtml_p3': 4,  # Hallucinations modérées
        'radhtml_p4': 2,  # Excitation minime
        'radhtml_p5': 2,  # Mégalomanie minime
        'radhtml_p6': 4,  # Méfiance modérée
        'radhtml_p7': 2,  # Hostilité minime
        
        # Negative symptoms (moderate)
        'radhtml_n1': 4,  # Affect émoussé modéré
        'radhtml_n2': 3,  # Retrait émotionnel faible
        'radhtml_n3': 4,  # Contact faible modéré
        'radhtml_n4': 3,  # Retrait social faible
        'radhtml_n5': 3,  # Difficulté abstraction faible
        'radhtml_n6': 3,  # Manque spontanéité faible
        'radhtml_n7': 3,  # Pensée stéréotypée faible
        
        # General psychopathology (mild-moderate)
        'radhtml_g1': 2,  # Préoccupations somatiques minimes
        'radhtml_g2': 3,  # Anxiété faible
        'radhtml_g3': 2,  # Culpabilité minime
        'radhtml_g4': 3,  # Tension faible
        'radhtml_g5': 2,  # Maniérisme minime
        'radhtml_g6': 3,  # Dépression faible
        'radhtml_g7': 3,  # Ralentissement faible
        'radhtml_g8': 2,  # Manque coopération minime
        'radhtml_g9': 3,  # Contenu inhabituel faible
        'radhtml_g10': 2,  # Désorientation minime
        'radhtml_g11': 3,  # Manque attention faible
        'radhtml_g12': 4,  # Manque jugement modéré
        'radhtml_g13': 3,  # Troubles volition faibles
        'radhtml_g14': 2,  # Contrôle pulsionnel minime
        'radhtml_g15': 3,  # Préoccupation soi faible
        'radhtml_g16': 3   # Évitement social faible
    }
    
    result = questionnaire.calculate_score(example_responses)
    
    print(f"=== PANSS - Positive and Negative Syndrome Scale ===\n")
    print(f"Symptômes Positifs (P): {result['positive_score']}/{result['positive_range']}")
    print(f"  → {result['positive_interpretation']}\n")
    
    print(f"Symptômes Négatifs (N): {result['negative_score']}/{result['negative_range']}")
    print(f"  → {result['negative_interpretation']}\n")
    
    print(f"Psychopathologie Générale (G): {result['general_score']}/{result['general_range']}")
    print(f"  → {result['general_interpretation']}\n")
    
    print(f"Score Total PANSS: {result['total_score']}/{result['total_range']}")
    print(f"  → {result['total_interpretation']}\n")
    
    print(f"=== Scores Factoriels (Wallwork 2012) ===")
    factors = result['factor_scores']
    print(f"Facteur Positif: {factors['positive_factor']}")
    print(f"Facteur Négatif: {factors['negative_factor']}")
    print(f"Facteur Désorganisé: {factors['disorganized_factor']}")
    print(f"Facteur Excitation: {factors['excited_factor']}")
    print(f"Facteur Dépressif: {factors['depressed_factor']}")


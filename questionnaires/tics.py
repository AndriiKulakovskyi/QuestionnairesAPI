"""
Tics Scale - Chronic Motor and Vocal Tics Assessment
A comprehensive checklist assessing motor and vocal tics across multiple domains.
"""

class TicsQuestionnaire:
    def __init__(self):
        """Initialize the Tics questionnaire."""
        self.name = "Tics"
        self.full_name = "Tics moteurs et vocaux chroniques - Chronic Motor and Vocal Tics Scale"
        self.description = "Questionnaire d'évaluation des tics moteurs et vocaux (actuels, passés, jamais)"
        
        # The questionnaire has 54 items covering motor and vocal tics
        self.num_items = 54
        self.questions = []
        
        # Define tic categories
        self.motor_tics_categories = [
            ("eye_movements", "Mouvements des yeux", [1, 2]),
            ("face_movements", "Mouvements du visage", [3, 4]),
            ("head_movements", "Mouvements de la tête", [5, 6]),
            ("shoulder_movements", "Mouvements des épaules", [7, 8]),
            ("arm_hand_movements", "Mouvements des bras/mains", [9, 10]),
            ("leg_foot_movements", "Mouvements des jambes/pieds", [11, 12]),
            ("trunk_movements", "Mouvements du tronc", [13]),
            ("simple_motor_other", "Autres tics moteurs simples", [14]),
            ("complex_motor", "Tics moteurs complexes", [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),
        ]
        
        self.vocal_tics_categories = [
            ("simple_vocal", "Tics vocaux simples", [26, 27, 28, 29, 30, 31]),
            ("complex_vocal", "Tics vocaux complexes", [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]),
        ]
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all 54 Tics items."""
        
        motor_tics_text = [
            # Eye movements
            "Cligner des yeux, loucher, mouvements rapides des yeux",
            "Faire des gestes des yeux, comme sembler surpris",
            # Face movements  
            "Se mordre la langue, mâcher la lèvre, grincer des dents",
            "Écarter les narines, sourire, expressions bizarres",
            # Head movements
            "Toucher son épaule avec le menton",
            "Jeter la tête en arrière",
            # Shoulder movements
            "Sursauts des épaules",
            "Hausser les épaules",
            # Arm/hand movements
            "Fléchir ou étendre rapidement les bras, se mordre les ongles",
            "Se passer la main dans les cheveux, toucher des objets",
            # Leg/foot movements
            "Taper, sauter, secouer le pied",
            "Faire un pas puis reculer",
            # Trunk movements
            "Contracter l'abdomen, contracter les fesses",
            # Simple motor other
            "Autres tics moteurs simples",
            # Complex motor (items 15-25)
            "Tics liés à des comportements compulsifs",
            "Tics dépendant du stimulus",
            "Gestes obscènes/impolis",
            "Position inhabituelle",
            "Se pencher sur soi-même",
            "Tourner sur soi-même",
            "Comportements soudains et impulsifs",
            "Comportements d'automutilation",
            "Comportement de coproraxie",
            "Comportement d'échopraxie",
            "Autres tics moteurs complexes",
        ]
        
        vocal_tics_text = [
            # Simple vocal (items 26-31)
            "Se racler la gorge, tousser, renifler",
            "Siffler, respiration bruyante",
            "Crier, aboyer, grogner",
            "Claquer la langue, claquer les dents",
            "Cracher",
            "Autres sons vocaux simples",
            # Complex vocal (items 32-42)
            "Syllabes ou mots répétés hors contexte",
            "Utiliser des mots ou phrases offensants",
            "Coprolalie (mots obscènes)",
            "Écholalie (répéter les autres)",
            "Palilalie (répéter ses propres mots)",
            "Parler à soi-même",
            "Bloquer sur des mots",
            "Accent inhabituel, changement de ton",
            "Autres problèmes de langage",
            "Sons animaux",
            "Autres tics vocaux complexes",
        ]
        
        response_options = ["Jamais eu", "Déjà eu", "Actuellement (semaine dernière)"]
        
        for idx, text in enumerate(motor_tics_text + vocal_tics_text, 1):
            is_motor = idx <= 25
            self.questions.append({
                "id": f"TIC{idx}",
                "text": text,
                "type": "motor" if is_motor else "vocal",
                "responses": response_options,
                "scoring": {"Jamais eu": 1, "Déjà eu": 2, "Actuellement (semaine dernière)": 3}
            })
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate Tics assessment summary.
        
        Args:
            responses: Dictionary mapping question IDs to response values (1-3)
                      (e.g., {"TIC1": 3, "TIC2": 1, ...})
        
        Returns:
            Dictionary containing:
            - motor_tics: Summary of motor tics
            - vocal_tics: Summary of vocal tics
            - current_tics: List of current tics
            - past_tics: List of past tics
            - interpretation: Clinical interpretation
        """
        if not responses:
            return {
                "motor_tics": {"current": 0, "past": 0, "total": 0},
                "vocal_tics": {"current": 0, "past": 0, "total": 0},
                "current_tics": [],
                "past_tics": [],
                "interpretation": "No responses provided"
            }
        
        motor_current = 0
        motor_past = 0
        vocal_current = 0
        vocal_past = 0
        
        current_tics = []
        past_tics = []
        
        for q in self.questions:
            q_id = q["id"]
            if q_id in responses:
                value = responses[q_id]
                
                if value == 3:  # Currently present
                    current_tics.append(q["text"])
                    if q["type"] == "motor":
                        motor_current += 1
                    else:
                        vocal_current += 1
                elif value == 2:  # Past but not current
                    past_tics.append(q["text"])
                    if q["type"] == "motor":
                        motor_past += 1
                    else:
                        vocal_past += 1
        
        # Interpret results
        total_current = motor_current + vocal_current
        has_current_motor = motor_current > 0
        has_current_vocal = vocal_current > 0
        
        if has_current_motor and has_current_vocal:
            interpretation = f"Tics moteurs et vocaux actuels présents - Évaluation pour syndrome de Gilles de la Tourette recommandée"
        elif has_current_motor:
            interpretation = f"Tics moteurs actuels présents ({motor_current} types)"
        elif has_current_vocal:
            interpretation = f"Tics vocaux actuels présents ({vocal_current} types)"
        else:
            interpretation = "Pas de tics actuels rapportés"
        
        return {
            "motor_tics": {
                "current": motor_current,
                "past": motor_past,
                "total": motor_current + motor_past
            },
            "vocal_tics": {
                "current": vocal_current,
                "past": vocal_past,
                "total": vocal_current + vocal_past
            },
            "current_tics": current_tics,
            "past_tics": past_tics,
            "total_current": total_current,
            "interpretation": interpretation
        }


if __name__ == '__main__':
    # Example usage
    tics = TicsQuestionnaire()
    
    print(f"Questionnaire: {tics.full_name}")
    print(f"Number of items: {tics.num_items}\n")
    
    # Example 1: Current motor and vocal tics
    print("Example 1: Current motor and vocal tics (Tourette's pattern)")
    responses1 = {
        "TIC1": 3, "TIC2": 1, "TIC3": 2, "TIC4": 3,
        "TIC7": 3, "TIC9": 2,
        "TIC26": 3, "TIC27": 3, "TIC28": 1
    }
    result1 = tics.calculate_score(responses1)
    print(f"Motor tics - Current: {result1['motor_tics']['current']}, Past: {result1['motor_tics']['past']}")
    print(f"Vocal tics - Current: {result1['vocal_tics']['current']}, Past: {result1['vocal_tics']['past']}")
    print(f"Total current tics: {result1['total_current']}")
    print(f"Interpretation: {result1['interpretation']}\n")
    
    # Example 2: Only past tics
    print("Example 2: Only past tics (in remission)")
    responses2 = {f"TIC{i}": 2 for i in range(1, 15)}
    result2 = tics.calculate_score(responses2)
    print(f"Motor tics - Current: {result2['motor_tics']['current']}, Past: {result2['motor_tics']['past']}")
    print(f"Interpretation: {result2['interpretation']}\n")
    
    # Example 3: No tics
    print("Example 3: No tics reported")
    responses3 = {f"TIC{i}": 1 for i in range(1, 20)}
    result3 = tics.calculate_score(responses3)
    print(f"Interpretation: {result3['interpretation']}\n")


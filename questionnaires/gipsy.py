"""
Gi-PSY - Gastrointestinal-Psychiatric Symptoms Inventory
A questionnaire assessing GI symptoms and their relationship to psychiatric symptoms.
"""

class GIPSYQuestionnaire:
    def __init__(self):
        """Initialize the Gi-PSY questionnaire."""
        self.name = "Gi-PSY"
        self.full_name = "Gastrointestinal-Psychiatric Symptoms Inventory (Gi-PSY)"
        self.description = "Inventaire des symptômes gastro-intestinaux et psychiatriques - évaluation des troubles GI et immunitaires"
        
        # Part A: Adult symptoms (17 main items + sub-questions)
        # Part B: Childhood symptoms (24 items)
        self.num_items_part_a = 17
        self.num_items_part_b = 24
        self.total_items = self.num_items_part_a + self.num_items_part_b
        
        self.frequency_options = {
            0: "Jamais",
            1: "Rarement",
            2: "Quelquefois",
            3: "Souvent",
            4: "Très souvent"
        }
        
        self.pain_intensity_options = {
            0: "Aucune douleur",
            1: "Intensité Légère",
            2: "Intensité Moyenne",
            3: "Intensité Sévère",
            4: "Intensité Extrême"
        }
        
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize Gi-PSY items."""
        
        # Part A: Adult GI symptoms
        part_a_questions = [
            {"id": "GP101", "text": "Durant toute votre vie adulte, à quelle fréquence avez-vous eu des épisodes de selles anormalement molles ou liquides (au minimum 2 semaines) ?", "type": "frequency"},
            {"id": "GP102", "text": "Durant toute votre vie adulte, à quelle fréquence avez-vous eu des épisodes de constipation (au minimum 2 semaines) ?", "type": "frequency"},
            {"id": "GP103", "text": "Durant toute votre vie adulte, à quelle fréquence vous est-il arrivé d'avoir des selles anormalement nauséabondes ou de couleur inhabituelle ?", "type": "frequency"},
            {"id": "GP104", "text": "Durant toute votre vie adulte, à quelle fréquence vous est-il arrivé d'avoir des ballonnements abdominaux importants (au moins 2 semaines) ?", "type": "frequency"},
            {"id": "GP105", "text": "Durant toute votre vie adulte, à quelle fréquence avez-vous eu des périodes d'inconfort ou de douleurs abdominales importantes (plus de 2 semaines) ?", "type": "frequency"},
            {"id": "GP106", "text": "Lorsque vous aviez ces douleurs, ont-elles limité vos activités quotidiennes ?", "type": "frequency"},
            {"id": "GP107A", "text": "Pourriez-vous évaluer l'intensité moyenne de ces inconforts ou douleurs abdominales ?", "type": "pain_intensity"},
            {"id": "GP107B", "text": "A quelle période les symptômes digestifs ont-ils débuté ?", "type": "onset_period"},
            {"id": "GP108", "text": "Durant toute votre vie adulte, à quelle fréquence avez-vous ressenti un reflux (remontées acides) ?", "type": "frequency"},
            {"id": "GP109", "text": "Combien d'épisodes d'intolérance alimentaire ou d'allergie alimentaire avez-vous connus ?", "type": "frequency"},
            {"id": "GP110", "text": "Combien de fois avez-vous eu besoin de suivre un régime alimentaire spécifique pour éviter des troubles gastro-intestinaux ?", "type": "frequency"},
            {"id": "GP112", "text": "Un médecin a-t-il déjà officiellement posé chez vous un diagnostic de maladie gastro-intestinale ?", "type": "yes_no"},
            {"id": "GP113", "text": "A-t-on déjà diagnostiqué chez vous une maladie auto-immune ?", "type": "checklist"},
            {"id": "GP114", "text": "Précisez l'âge de début de ces troubles auto-immuns", "type": "onset_period"},
            {"id": "GP115", "text": "Avez-vous déjà dû prendre des traitements immunosuppresseurs ou immunostimulants ?", "type": "yes_no"},
            {"id": "GP116", "text": "Avez-vous déjà expérimenté des douleurs articulaires dérangeantes ?", "type": "frequency"},
            {"id": "GP117", "text": "Avez-vous déjà expérimenté des problèmes dermatologiques importants ?", "type": "frequency"},
        ]
        
        # Part B: Childhood symptoms (parent report)
        part_b_questions = [
            {"id": "GP201", "text": "Durant son enfance, à quelle fréquence votre enfant a-t-il connu des épisodes avec des selles anormalement liquides ou molles ?", "type": "frequency"},
            {"id": "GP202", "text": "Durant son enfance, à quelle fréquence votre enfant a-t-il connu des périodes de constipation ?", "type": "frequency"},
            {"id": "GP203", "text": "Durant son enfance, à quelle fréquence votre enfant a-t-il eu des selles anormalement nauséabondes ?", "type": "frequency"},
            {"id": "GP204", "text": "Durant son enfance, à quelle fréquence votre enfant a-t-il connu des ballonnements abdominaux importants ?", "type": "frequency"},
            {"id": "GP205", "text": "Durant son enfance, à quelle fréquence votre enfant s'est-il plaint de douleurs abdominales importantes ?", "type": "frequency"},
            {"id": "GP206", "text": "Cet inconfort a-t-il limité ses activités quotidiennes ?", "type": "frequency"},
            {"id": "GP207", "text": "Évaluer l'intensité de ces douleurs abdominales", "type": "pain_intensity"},
            {"id": "GP208", "text": "Durant son enfance, votre enfant s'est plaint-il de reflux (remontées acides) ?", "type": "frequency"},
            {"id": "GP209", "text": "Durant son enfance, votre enfant a-t-il présenté une intolérance ou allergie alimentaire ?", "type": "frequency"},
            {"id": "GP210", "text": "Durant son enfance, votre enfant a-t-il eu besoin de suivre un régime spécifique ?", "type": "frequency"},
            {"id": "GP211", "text": "Durant son enfance, votre enfant a expérimenté des douleurs articulaires dérangeantes ?", "type": "frequency"},
            {"id": "GP212", "text": "Durant son enfance, votre enfant a-t-il expérimenté des problèmes dermatologiques importants ?", "type": "frequency"},
            {"id": "GP214", "text": "Un médecin a-t-il diagnostiqué une maladie gastro-intestinale à votre enfant ?", "type": "yes_no"},
            {"id": "GP215", "text": "Le début des symptômes GI correspond-il à l'apparition/aggravation des symptômes psychiatriques ?", "type": "yes_no"},
            {"id": "GP216", "text": "Durant son enfance, votre enfant a-t-il été atteint d'infection ou maladie parasitaire ?", "type": "frequency"},
            {"id": "GP217", "text": "Durant son enfance, votre enfant a-t-il souffert d'otites sévères à répétition ?", "type": "frequency"},
            {"id": "GP218", "text": "Votre enfant semblait-il avoir « mauvaise mine » par rapport aux autres enfants ?", "type": "frequency"},
            {"id": "GP219", "text": "Après l'accouchement, le sujet a-t-il eu besoin d'être hospitalisé en réanimation néonatale ?", "type": "yes_no"},
            {"id": "GP220", "text": "Le sujet a-t-il souffert de complications à la naissance ?", "type": "yes_no"},
            {"id": "GP222", "text": "Quelle a été la durée de la grossesse pour cet enfant ?", "type": "gestation"},
            {"id": "GP223", "text": "Quel était le poids du bébé à la naissance ?", "type": "birth_weight"},
            {"id": "GP224", "text": "Durant son enfance, le sujet a-t-il eu besoin de prendre des antibiotiques (au moins 2 semaines) ?", "type": "frequency"},
        ]
        
        self.questions = part_a_questions + part_b_questions
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate Gi-PSY scores.
        
        Args:
            responses: Dictionary mapping question IDs to response values
        
        Returns:
            Dictionary containing:
            - part_a_score: Score for adult GI symptoms
            - part_b_score: Score for childhood GI symptoms
            - total_gi_burden: Overall GI symptom burden
            - autoimmune_present: Boolean for autoimmune conditions
            - interpretation: Clinical interpretation
        """
        if not responses:
            return {
                "part_a_score": 0,
                "part_b_score": 0,
                "total_gi_burden": 0,
                "autoimmune_present": False,
                "interpretation": "No responses provided"
            }
        
        # Calculate Part A score (frequency items only)
        part_a_frequency_items = ["GP101", "GP102", "GP103", "GP104", "GP105", 
                                   "GP106", "GP108", "GP109", "GP110", "GP116", "GP117"]
        part_a_score = sum(responses.get(item, 0) for item in part_a_frequency_items)
        
        # Calculate Part B score (frequency items only)
        part_b_frequency_items = ["GP201", "GP202", "GP203", "GP204", "GP205", 
                                   "GP206", "GP208", "GP209", "GP210", "GP211", 
                                   "GP212", "GP216", "GP217", "GP218", "GP224"]
        part_b_score = sum(responses.get(item, 0) for item in part_b_frequency_items)
        
        # Check for autoimmune conditions
        autoimmune_present = responses.get("GP113", 0) > 0 or responses.get("GP115", 0) == 1
        
        # Check for GI diagnosis
        gi_diagnosis = responses.get("GP112", 0) == 1 or responses.get("GP214", 0) == 1
        
        # Check for GI-psychiatric temporal relationship
        temporal_link = responses.get("GP215", 0) == 1
        
        total_gi_burden = part_a_score + part_b_score
        
        # Interpret results
        if total_gi_burden >= 40:
            severity = "Charge GI sévère - Symptômes GI marqués et fréquents"
        elif total_gi_burden >= 25:
            severity = "Charge GI modérée - Symptômes GI significatifs"
        elif total_gi_burden >= 10:
            severity = "Charge GI légère - Quelques symptômes GI"
        else:
            severity = "Charge GI minime - Peu de symptômes GI"
        
        notes = []
        if autoimmune_present:
            notes.append("Présence de pathologie auto-immune")
        if gi_diagnosis:
            notes.append("Diagnostic GI formel posé")
        if temporal_link:
            notes.append("Lien temporel GI-psychiatrique suggéré")
        
        interpretation = severity
        if notes:
            interpretation += " | " + " | ".join(notes)
        
        return {
            "part_a_score": part_a_score,
            "part_b_score": part_b_score,
            "total_gi_burden": total_gi_burden,
            "autoimmune_present": autoimmune_present,
            "gi_diagnosis": gi_diagnosis,
            "temporal_link": temporal_link,
            "interpretation": interpretation
        }


if __name__ == '__main__':
    # Example usage
    gipsy = GIPSYQuestionnaire()
    
    print(f"Questionnaire: {gipsy.full_name}")
    print(f"Total items: {gipsy.total_items} (Part A: {gipsy.num_items_part_a}, Part B: {gipsy.num_items_part_b})\n")
    
    # Example 1: High GI burden
    print("Example 1: High GI burden with autoimmune condition")
    responses1 = {
        "GP101": 4, "GP102": 3, "GP103": 3, "GP104": 4, "GP105": 4,
        "GP106": 4, "GP108": 3, "GP109": 4, "GP110": 3, "GP116": 3, "GP117": 2,
        "GP112": 1, "GP113": 1, "GP115": 1,
        "GP201": 3, "GP202": 4, "GP203": 2, "GP204": 3, "GP205": 4,
        "GP206": 3, "GP208": 3, "GP209": 4, "GP210": 3, "GP211": 2,
        "GP212": 3, "GP216": 2, "GP217": 3, "GP218": 3, "GP224": 4,
        "GP214": 1, "GP215": 1
    }
    result1 = gipsy.calculate_score(responses1)
    print(f"Part A score (Adult): {result1['part_a_score']}")
    print(f"Part B score (Childhood): {result1['part_b_score']}")
    print(f"Total GI burden: {result1['total_gi_burden']}")
    print(f"Interpretation: {result1['interpretation']}\n")
    
    # Example 2: Minimal GI symptoms
    print("Example 2: Minimal GI symptoms")
    responses2 = {item: 0 for item in ["GP101", "GP102", "GP103", "GP104", "GP105",
                                        "GP106", "GP108", "GP109", "GP110", "GP116", "GP117",
                                        "GP201", "GP202", "GP203", "GP204", "GP205",
                                        "GP206", "GP208", "GP209", "GP210", "GP211",
                                        "GP212", "GP216", "GP217", "GP218", "GP224"]}
    responses2.update({"GP112": 0, "GP113": 0, "GP115": 0, "GP214": 0, "GP215": 0})
    result2 = gipsy.calculate_score(responses2)
    print(f"Total GI burden: {result2['total_gi_burden']}")
    print(f"Interpretation: {result2['interpretation']}\n")


"""
MCDD - Multiple Complex Developmental Disorder
A diagnostic checklist assessing 3 domains of developmental psychopathology.
"""

class MCDDQuestionnaire:
    def __init__(self):
        """Initialize the MCDD questionnaire."""
        self.name = "MCDD"
        self.full_name = "Multiple Complex Developmental Disorder - Troubles Complexes du Développement"
        self.description = "Liste de critères diagnostiques évaluant les déficits dans la régulation affective, les comportements sociaux et la pensée"
        self.num_items = 15
        self.questions = []
        
        # Define which items belong to which domain
        self.domains = {
            "regulation_affective": [1, 2, 3, 4],  # Déficit dans la régulation des états affectifs ou de l'anxiété
            "deficits_sociaux": [5, 6],  # Déficit dans les comportements sociaux
            "trouble_pensee": [7, 8, 9, 10, 11, 12, 13, 14, 15]  # Présence d'un trouble de la pensée
        }
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all 15 MCDD diagnostic criteria."""
        
        questions_data = [
            # Domain 1: Déficit dans la régulation des états affectifs ou de l'anxiété
            ("Peurs ou phobies inhabituelles ou particulières", "regulation_affective"),
            ("Réactions anxieuses idiosyncrasiques ou bizarres fréquentes", "regulation_affective"),
            ("Attaques de panique récurrentes", "regulation_affective"),
            ("Episodes ponctuels de désorganisation ponctués par des comportements immatures ou violents prononcés", "regulation_affective"),
            
            # Domain 2: Déficit dans les comportements sociaux
            ("Désintérêt social, détachement, évitement, retrait", "deficits_sociaux"),
            ("Attachement visiblement perturbé ou ambivalent", "deficits_sociaux"),
            
            # Domain 3: Présence d'un trouble de la pensée
            ("Pensée magique et irrationnelle", "trouble_pensee"),
            ("Intrusions subites dans un processus de pensée normal", "trouble_pensee"),
            ("Idées bizarres", "trouble_pensee"),
            ("Répétition de mots n'ayant aucun sens ou néologismes", "trouble_pensee"),
            ("Facilement perplexe ou confus", "trouble_pensee"),
            ("Idées de grandeur, dont fantasme d'omnipotence", "trouble_pensee"),
            ("Préoccupations paranoïaques, persécutives", "trouble_pensee"),
            ("Surinvestissement de figures ou personnages fantasmés ou imaginaires", "trouble_pensee"),
            ("Idées de référence", "trouble_pensee"),
        ]
        
        response_options = ["Oui", "Non", "Inconnu"]
        
        for idx, (text, domain) in enumerate(questions_data, 1):
            self.questions.append({
                "id": f"MCDD{idx}",
                "text": text,
                "domain": domain,
                "responses": response_options,
                "scoring": {"Oui": 1, "Non": 0, "Inconnu": None}  # Inconnu invalidates the item
            })
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate MCDD domain scores.
        
        Args:
            responses: Dictionary mapping question IDs to response values
                      (e.g., {"MCDD1": "Oui", "MCDD2": "Non", ...})
        
        Returns:
            Dictionary containing:
            - domain_scores: Dictionary with scores for each domain
            - total_present: Total number of criteria present
            - interpretation: Clinical interpretation
            - validity: Whether all items were validly answered
        """
        if not responses:
            return {
                "domain_scores": {},
                "total_present": 0,
                "interpretation": "No responses provided",
                "validity": "invalid"
            }
        
        domain_scores = {
            "regulation_affective": {"present": 0, "total": len(self.domains["regulation_affective"])},
            "deficits_sociaux": {"present": 0, "total": len(self.domains["deficits_sociaux"])},
            "trouble_pensee": {"present": 0, "total": len(self.domains["trouble_pensee"])}
        }
        
        total_present = 0
        has_unknown = False
        
        for q in self.questions:
            q_id = q["id"]
            if q_id in responses:
                response = responses[q_id]
                score = q["scoring"].get(response)
                
                if score is None:
                    has_unknown = True
                elif score == 1:
                    total_present += 1
                    domain = q["domain"]
                    domain_scores[domain]["present"] += 1
        
        # Interpret results
        validity = "partial" if has_unknown else "valid"
        
        # MCDD criteria: Should have symptoms in all 3 domains
        domain1_present = domain_scores["regulation_affective"]["present"] > 0
        domain2_present = domain_scores["deficits_sociaux"]["present"] > 0
        domain3_present = domain_scores["trouble_pensee"]["present"] > 0
        
        if domain1_present and domain2_present and domain3_present:
            interpretation = "Critères MCDD présents dans les 3 domaines - MCDD possible"
        elif (domain1_present and domain2_present) or (domain1_present and domain3_present) or (domain2_present and domain3_present):
            interpretation = "Critères MCDD présents dans 2 domaines - MCDD partiel"
        else:
            interpretation = "Critères MCDD insuffisants - MCDD absent"
        
        return {
            "domain_scores": domain_scores,
            "total_present": total_present,
            "interpretation": interpretation,
            "validity": validity
        }


if __name__ == '__main__':
    # Example usage
    mcdd = MCDDQuestionnaire()
    
    print(f"Questionnaire: {mcdd.full_name}")
    print(f"Number of items: {mcdd.num_items}\n")
    
    # Example 1: All criteria present
    print("Example 1: MCDD criteria present across all 3 domains")
    responses1 = {f"MCDD{i}": "Oui" for i in range(1, 16)}
    result1 = mcdd.calculate_score(responses1)
    print(f"Total criteria present: {result1['total_present']}")
    for domain, scores in result1['domain_scores'].items():
        print(f"  {domain}: {scores['present']}/{scores['total']}")
    print(f"Interpretation: {result1['interpretation']}")
    print(f"Validity: {result1['validity']}\n")
    
    # Example 2: Partial MCDD (domain 1 and 3 only)
    print("Example 2: Partial MCDD (affective regulation and thought disorder)")
    responses2 = {
        "MCDD1": "Oui", "MCDD2": "Oui", "MCDD3": "Non", "MCDD4": "Oui",
        "MCDD5": "Non", "MCDD6": "Non",
        "MCDD7": "Oui", "MCDD8": "Non", "MCDD9": "Oui", "MCDD10": "Non",
        "MCDD11": "Oui", "MCDD12": "Non", "MCDD13": "Oui", "MCDD14": "Non", "MCDD15": "Oui"
    }
    result2 = mcdd.calculate_score(responses2)
    print(f"Total criteria present: {result2['total_present']}")
    for domain, scores in result2['domain_scores'].items():
        print(f"  {domain}: {scores['present']}/{scores['total']}")
    print(f"Interpretation: {result2['interpretation']}")
    print(f"Validity: {result2['validity']}\n")
    
    # Example 3: MCDD absent
    print("Example 3: MCDD absent")
    responses3 = {f"MCDD{i}": "Non" for i in range(1, 16)}
    result3 = mcdd.calculate_score(responses3)
    print(f"Total criteria present: {result3['total_present']}")
    print(f"Interpretation: {result3['interpretation']}\n")


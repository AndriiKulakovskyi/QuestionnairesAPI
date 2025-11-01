"""
COMPREP - Cognition et Actes Répétitifs (Repetitive Cognitions and Behaviors)
A clinical interview assessing sensations and perceptions preceding repetitive behaviors.
"""

class COMPREPQuestionnaire:
    def __init__(self):
        """Initialize the COMPREP questionnaire."""
        self.name = "COMPREP"
        self.full_name = "Cognition et Actes Répétitifs - Repetitive Cognitions and Behaviors Interview"
        self.description = "Entretien clinique évaluant les sensations et perceptions précédant ou accompagnant les comportements répétitifs"
        
        # Main domains assessed
        self.domains = [
            "just_right_sensations",  # Sensations "Juste comme il faut"
            "energy_tension",          # Énergie/tension
            "incompleteness",          # Incomplétude
            "other_mental_sensations", # Autres sensations mentales
            "physical_sensations",     # Sensations physiques
            "physical_anxiety",        # Anxiété physique
            "isolated_impulse"         # Impulsion isolée
        ]
        
        self.frequency_options = {
            0: "Jamais",
            1: "Rarement",
            2: "Quelquefois",
            3: "Souvent",
            4: "Sévère"
        }
        
        self.severity_options = {
            0: "Aucune",
            1: "Légère",
            2: "Modérée",
            3: "Sévère",
            4: "Extrême"
        }
        
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize COMPREP interview items."""
        
        # Domain A: "Just Right" Sensations (4 subtypes)
        just_right_questions = [
            {"id": "REPA1", "domain": "just_right_visual", "text": "'Juste comme il faut' visuel - Sensation qu'un objet n'est pas visuellement 'juste comme il faut'"},
            {"id": "REPA2", "domain": "just_right_tactile", "text": "'Juste comme il faut' tactile - Besoin de toucher jusqu'à obtenir une sensation 'juste comme il faut'"},
            {"id": "REPA3", "domain": "just_right_auditory", "text": "'Juste comme il faut' auditif - Besoin d'entendre un son 'juste comme il faut'"},
            {"id": "REPA4", "domain": "just_right_internal", "text": "'Juste comme il faut' interne - Sensation interne non liée à une modalité sensorielle"},
        ]
        
        # Domain B: Energy/Tension
        energy_questions = [
            {"id": "REPB", "domain": "energy_tension", "text": "Tension interne généralisée, énergie mentale qui sera libérée par les comportements répétitifs"},
        ]
        
        # Domain C: Incompleteness
        incompleteness_questions = [
            {"id": "REPC", "domain": "incompleteness", "text": "Sensation d'incomplétude, d'insatisfaction, d'imperfection"},
        ]
        
        # Domain D: Other Mental Sensations
        other_mental_questions = [
            {"id": "REPD", "domain": "other_mental", "text": "Autres sensations mentales précédant les comportements répétitifs"},
        ]
        
        # Section 2: Physical Sensations
        physical_questions = [
            {"id": "REP2", "domain": "physical_sensations", "text": "Sensations physiques désagréables (démangeaisons, brûlures, picotements)"},
        ]
        
        # Section 3: Physical Anxiety
        anxiety_questions = [
            {"id": "REP3", "domain": "physical_anxiety", "text": "Anxiété physique avant/pendant les comportements répétitifs"},
        ]
        
        # Section 4: Isolated Impulse
        impulse_questions = [
            {"id": "REP4", "domain": "isolated_impulse", "text": "Comportements précédés uniquement par la sensation de 'besoin de les faire'"},
        ]
        
        self.questions = (just_right_questions + energy_questions + incompleteness_questions + 
                         other_mental_questions + physical_questions + anxiety_questions + impulse_questions)
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate COMPREP scores.
        
        Args:
            responses: Dictionary mapping question IDs to dictionaries containing:
                      - present: 1 if present, 0 if absent
                      - frequency: 0-4 (Jamais to Sévère)
                      - severity: 0-4 (Aucune to Extrême)
                      - behaviors: text description of associated behaviors
        
        Returns:
            Dictionary containing:
            - domain_scores: Dictionary with scores for each domain
            - total_score: Total severity score across all domains
            - num_domains_present: Number of domains with symptoms
            - interpretation: Clinical interpretation
        """
        if not responses:
            return {
                "domain_scores": {},
                "total_score": 0,
                "num_domains_present": 0,
                "interpretation": "No responses provided"
            }
        
        domain_scores = {}
        total_severity = 0
        domains_present = 0
        
        # Group questions by domain
        domain_groups = {}
        for q in self.questions:
            domain = q["domain"]
            if domain not in domain_groups:
                domain_groups[domain] = []
            domain_groups[domain].append(q["id"])
        
        # Calculate scores for each domain
        for domain, question_ids in domain_groups.items():
            domain_present = False
            domain_severity = 0
            domain_frequency = 0
            
            for q_id in question_ids:
                if q_id in responses:
                    response = responses[q_id]
                    if isinstance(response, dict):
                        if response.get("present", 0) == 1:
                            domain_present = True
                            domain_severity += response.get("severity", 0)
                            domain_frequency += response.get("frequency", 0)
                    elif response == 1:  # Simple binary response
                        domain_present = True
                        domains_present += 1
            
            if domain_present:
                domains_present += 1
                total_severity += domain_severity
            
            domain_scores[domain] = {
                "present": domain_present,
                "severity": domain_severity,
                "frequency": domain_frequency
            }
        
        # Interpret results
        if total_severity >= 20:
            severity = "Phénomènes sensoriels sévères - Sensations prémonitrices marquées"
        elif total_severity >= 12:
            severity = "Phénomènes sensoriels modérés - Sensations prémonitrices significatives"
        elif total_severity >= 4:
            severity = "Phénomènes sensoriels légers - Quelques sensations prémonitrices"
        else:
            severity = "Phénomènes sensoriels minimaux ou absents"
        
        # Characterize pattern
        dominant_domains = [d for d, score in domain_scores.items() if score["present"]]
        pattern_description = f"{len(dominant_domains)} domaine(s) présent(s)"
        if dominant_domains:
            pattern_description += f": {', '.join(dominant_domains[:3])}"
        
        return {
            "domain_scores": domain_scores,
            "total_severity": total_severity,
            "num_domains_present": domains_present,
            "interpretation": f"{severity} | {pattern_description}"
        }


if __name__ == '__main__':
    # Example usage
    comprep = COMPREPQuestionnaire()
    
    print(f"Questionnaire: {comprep.full_name}")
    print(f"Number of domains: {len(comprep.domains)}\n")
    
    # Example 1: Multiple sensory phenomena present
    print("Example 1: Multiple sensory phenomena with high severity")
    responses1 = {
        "REPA1": {"present": 1, "frequency": 4, "severity": 4, "behaviors": "Arranging objects"},
        "REPA2": {"present": 1, "frequency": 3, "severity": 3, "behaviors": "Touching surfaces"},
        "REPB": {"present": 1, "frequency": 4, "severity": 4, "behaviors": "Multiple tics"},
        "REPC": {"present": 1, "frequency": 3, "severity": 3, "behaviors": "Checking rituals"},
        "REP2": {"present": 1, "frequency": 2, "severity": 2, "behaviors": "Skin picking"},
        "REP3": {"present": 1, "frequency": 3, "severity": 3, "behaviors": "Hand washing"},
        "REP4": {"present": 1, "frequency": 2, "severity": 1, "behaviors": "Blinking"},
    }
    result1 = comprep.calculate_score(responses1)
    print(f"Total severity: {result1['total_severity']}")
    print(f"Number of domains present: {result1['num_domains_present']}")
    print(f"Interpretation: {result1['interpretation']}\n")
    
    # Example 2: Minimal phenomena
    print("Example 2: Minimal sensory phenomena")
    responses2 = {
        "REPA1": {"present": 0, "frequency": 0, "severity": 0},
        "REPA2": {"present": 0, "frequency": 0, "severity": 0},
        "REPB": {"present": 1, "frequency": 1, "severity": 1, "behaviors": "Mild tension"},
        "REPC": {"present": 0, "frequency": 0, "severity": 0},
        "REP2": {"present": 0, "frequency": 0, "severity": 0},
        "REP3": {"present": 0, "frequency": 0, "severity": 0},
        "REP4": {"present": 0, "frequency": 0, "severity": 0},
    }
    result2 = comprep.calculate_score(responses2)
    print(f"Total severity: {result2['total_severity']}")
    print(f"Interpretation: {result2['interpretation']}\n")


"""
CGI-S - Clinical Global Impressions - Severity
A clinician-rated scale assessing overall illness severity.
"""

class CGISeverityQuestionnaire:
    def __init__(self):
        """Initialize the CGI-Severity questionnaire."""
        self.name = "CGI-S"
        self.full_name = "Clinical Global Impressions - Severity (CGI-S)"
        self.description = "Échelle d'impressions cliniques globales - Gravité de la maladie (évaluation clinicienne)"
        self.num_items = 1
        self.questions = []
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize CGI-Severity item."""
        self.questions = [{
            "id": "GRAVMDI",
            "text": "En fonction de votre expérience clinique totale avec ce type de patient, quel est le niveau de gravité des troubles mentaux actuels du patient ?",
            "responses": [
                "non évalué",
                "normal, pas du tout malade",
                "à la limite",
                "légèrement malade",
                "modérément malade",
                "manifestement malade",
                "gravement malade",
                "parmi les patients les plus malades"
            ],
            "scoring": {
                "non évalué": 0,
                "normal, pas du tout malade": 1,
                "à la limite": 2,
                "légèrement malade": 3,
                "modérément malade": 4,
                "manifestement malade": 5,
                "gravement malade": 6,
                "parmi les patients les plus malades": 7
            }
        }]
    
    def calculate_score(self, severity_rating: int) -> dict:
        """
        Calculate CGI-Severity score.
        
        Args:
            severity_rating: Severity rating (0-7)
                            0 = non évalué
                            1 = normal, pas du tout malade
                            2 = à la limite
                            3 = légèrement malade
                            4 = modérément malade
                            5 = manifestement malade
                            6 = gravement malade
                            7 = parmi les patients les plus malades
        
        Returns:
            Dictionary containing:
            - severity_score: The severity rating (0-7)
            - severity_label: Text label for the severity
            - interpretation: Clinical interpretation
        """
        severity_labels = {
            0: "non évalué",
            1: "normal, pas du tout malade",
            2: "à la limite",
            3: "légèrement malade",
            4: "modérément malade",
            5: "manifestement malade",
            6: "gravement malade",
            7: "parmi les patients les plus malades"
        }
        
        if severity_rating not in severity_labels:
            raise ValueError(f"Invalid severity rating: {severity_rating}. Must be 0-7.")
        
        interpretations = {
            0: "Non évalué",
            1: "Pas de maladie psychiatrique",
            2: "Symptômes subcliniques",
            3: "Maladie légère - Symptômes présents mais fonctionnement peu altéré",
            4: "Maladie modérée - Symptômes nets avec altération fonctionnelle",
            5: "Maladie marquée - Symptômes et altération fonctionnelle importants",
            6: "Maladie grave - Symptômes sévères avec altération fonctionnelle majeure",
            7: "Maladie extrêmement sévère - Symptômes parmi les plus graves"
        }
        
        return {
            "severity_score": severity_rating,
            "severity_label": severity_labels[severity_rating],
            "interpretation": interpretations[severity_rating]
        }


if __name__ == '__main__':
    # Example usage
    cgi_s = CGISeverityQuestionnaire()
    
    print(f"Questionnaire: {cgi_s.full_name}")
    print(f"Number of items: {cgi_s.num_items}\n")
    
    # Test all severity levels
    for severity in range(0, 8):
        result = cgi_s.calculate_score(severity)
        print(f"Severity {severity}: {result['severity_label']}")
        print(f"  Interpretation: {result['interpretation']}\n")


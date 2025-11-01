"""
Questionnaire: EQ-5D (EuroQol-5 Dimensions)
Questionnaire de qualité de vie en 5 dimensions
"""

from typing import Dict, List, Optional, Any


class EQ5DQuestionnaire:
    """EQ-5D - EuroQol-5 Dimensions
    
    Auto-questionnaire de qualité de vie en 5 dimensions:
    - Mobilité
    - Autonomie de la personne (self-care)
    - Activités courantes
    - Douleur/Gêne
    - Anxiété/Dépression
    
    Plus une échelle visuelle analogique (EQ-VAS) de 0 à 100 pour l'état de santé.
    
    Le score est un indice d'utilité dérivé d'une table de valorisation nationale française.
    """
    
    def __init__(self):
        self.name = "EQ-5D - EuroQol-5 Dimensions"
        self.description = ("Questionnaire de qualité de vie en 5 dimensions avec échelle visuelle analogique. "
                           "Génère un indice d'utilité (0-1) et un score VAS (0-100).")
        self.used_in_applications = ["ebipolar", "eschizo", "asperger"]
        self.questions = self._init_questions()
        # Load French utility values (partial table - most common states)
        self.utility_values = self._load_utility_values()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize the 5 EQ-5D dimensions"""
        
        questions = [
            {
                'id': 'MOBILITY',
                'dimension': 'Mobilité',
                'text': "Je me déplace à pied",
                'options': {
                    1: "Je n'ai aucun problème pour me déplacer à pied",
                    2: "J'ai des problèmes légers pour me déplacer à pied",
                    3: "J'ai des problèmes modérés pour me déplacer à pied",
                    4: "J'ai des problèmes sévères pour me déplacer à pied",
                    5: "Je suis incapable de me déplacer à pied"
                }
            },
            {
                'id': 'SELFCARE',
                'dimension': 'Autonomie de la personne',
                'text': "Je me lave ou m'habille tout seul",
                'options': {
                    1: "Je n'ai aucun problème pour me laver ou m'habiller tout seul",
                    2: "J'ai des problèmes légers pour me laver ou m'habiller tout seul",
                    3: "J'ai des problèmes modérés pour me laver ou m'habiller tout seul",
                    4: "J'ai des problèmes sévères pour me laver ou m'habiller tout seul",
                    5: "Je suis incapable de me laver ou de m'habiller tout(e) seul(e)"
                }
            },
            {
                'id': 'ACTIVITY',
                'dimension': 'Activités courantes',
                'text': "J'accomplis mes activités courantes (travail, études, travaux domestiques, activités familiales ou loisirs)",
                'options': {
                    1: "Je n'ai aucun problème pour accomplir mes activités courantes",
                    2: "J'ai des problèmes légers pour accomplir mes activités courantes",
                    3: "J'ai des problèmes modérés pour accomplir mes activités courantes",
                    4: "J'ai des problèmes sévères pour accomplir mes activités courantes",
                    5: "Je suis incapable d'accomplir mes activités courantes"
                }
            },
            {
                'id': 'PAIN',
                'dimension': 'Douleur/Gêne',
                'text': "J'éprouve de la douleur ou de la gêne",
                'options': {
                    1: "Je n'ai ni douleur ni gêne",
                    2: "J'ai une douleur ou gêne légère",
                    3: "J'ai une douleur ou gêne modérée",
                    4: "J'ai une douleur ou gêne sévère",
                    5: "J'ai une douleur ou gêne extrême"
                }
            },
            {
                'id': 'ANXIETY',
                'dimension': 'Anxiété/Dépression',
                'text': "Je suis anxieux(se) ou déprimé(e)",
                'options': {
                    1: "Je ne suis ni anxieux(se), ni déprimé(e)",
                    2: "Je suis légèrement anxieux(se) ou déprimé(e)",
                    3: "Je suis modérément anxieux(se) ou déprimé(e)",
                    4: "Je suis sévèrement anxieux(se) ou déprimé(e)",
                    5: "Je suis extrêmement anxieux(se) ou déprimé(e)"
                }
            }
        ]
        
        return questions
    
    def _load_utility_values(self) -> Dict[str, float]:
        """Load French value set for EQ-5D utility scores
        
        Returns a dictionary mapping health states (e.g., "11111") to utility values.
        This is a subset of the full 3,125 possible states.
        
        Full utility table based on French population preferences.
        Values range from 1.0 (perfect health) to negative values (states worse than death).
        """
        # This is a simplified version with common states
        # In production, you'd load all 3,125 states from a complete lookup table
        utility_table = {
            # Perfect health and minor issues
            "11111": 1.000,
            "11112": 0.929,
            "11113": 0.910,
            "11114": 0.769,
            "11115": 0.622,
            "11121": 0.910,
            "11122": 0.839,
            "11123": 0.820,
            "11131": 0.888,
            "11132": 0.817,
            "11211": 0.875,
            "11212": 0.803,
            "11311": 0.853,
            "12111": 0.853,
            "13111": 0.831,
            "21111": 0.825,
            "22222": 0.539,
            "33333": 0.185,
            "44444": -0.074,
            "55555": -0.525,
            # Add more common combinations as needed
        }
        return utility_table
    
    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate EQ-5D scores
        
        Generates:
        1. Health state code (5-digit string like "12321")
        2. Utility index (0-1 or negative, from French value set)
        3. EQ-VAS score (0-100, self-rated health today)
        
        Args:
            responses: Dictionary with:
                - 'MOBILITY': 1-5
                - 'SELFCARE': 1-5
                - 'ACTIVITY': 1-5
                - 'PAIN': 1-5
                - 'ANXIETY': 1-5
                - 'EQ_VAS': 0-100 (optional)
                
        Returns:
            Dictionary containing health state, utility index, VAS, and interpretations
        """
        errors = []
        result = {}
        
        # Validate and extract dimension scores
        health_state_digits = []
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses:
                errors.append(f"{question['dimension']} manquante")
                continue
            
            try:
                value = int(responses[q_id])
                if value < 1 or value > 5:
                    errors.append(f"{question['dimension']} doit être entre 1 et 5")
                else:
                    health_state_digits.append(str(value))
            except (ValueError, TypeError):
                errors.append(f"{question['dimension']} invalide")
        
        if len(health_state_digits) == 5:
            health_state = ''.join(health_state_digits)
            result['health_state'] = health_state
            
            # Look up utility index
            if health_state in self.utility_values:
                result['utility_index'] = self.utility_values[health_state]
            else:
                # If exact state not in table, estimate based on component scores
                result['utility_index'] = self._estimate_utility(health_state_digits)
                result['utility_estimated'] = True
            
            result['utility_interpretation'] = self._interpret_utility(result['utility_index'])
        
        # Process EQ-VAS if provided
        if 'EQ_VAS' in responses:
            try:
                vas = float(responses['EQ_VAS'])
                if vas < 0 or vas > 100:
                    errors.append("EQ-VAS doit être entre 0 et 100")
                else:
                    result['eq_vas'] = vas
                    result['vas_interpretation'] = self._interpret_vas(vas)
            except (ValueError, TypeError):
                errors.append("EQ-VAS invalide")
        
        result['valid'] = len(errors) == 0
        result['errors'] = errors
        
        return result
    
    def _estimate_utility(self, digits: List[str]) -> float:
        """Estimate utility index for states not in lookup table
        
        Uses a simple additive model based on French value set coefficients.
        Real implementation would use the official TTO-based algorithm.
        
        Args:
            digits: List of 5 digits representing health state
            
        Returns:
            Estimated utility value
        """
        # Simplified estimation - subtract penalties for each problem level
        base = 1.0
        
        dimension_weights = [0.150, 0.125, 0.135, 0.140, 0.155]  # Approximate French weights
        
        for i, digit in enumerate(digits):
            level = int(digit)
            if level > 1:
                # Each level above 1 reduces utility
                penalty = dimension_weights[i] * (level - 1) * 0.35
                base -= penalty
        
        return round(base, 3)
    
    def _interpret_utility(self, utility: float) -> str:
        """Interpret utility index value"""
        if utility >= 0.9:
            return "Excellente qualité de vie"
        elif utility >= 0.7:
            return "Bonne qualité de vie"
        elif utility >= 0.5:
            return "Qualité de vie moyenne"
        elif utility >= 0.3:
            return "Qualité de vie faible"
        elif utility >= 0:
            return "Qualité de vie très faible"
        else:
            return "État pire que la mort (selon l'échelle)"
    
    def _interpret_vas(self, vas: float) -> str:
        """Interpret EQ-VAS score"""
        if vas >= 80:
            return "Très bon état de santé perçu"
        elif vas >= 60:
            return "Bon état de santé perçu"
        elif vas >= 40:
            return "État de santé perçu moyen"
        elif vas >= 20:
            return "Mauvais état de santé perçu"
        else:
            return "Très mauvais état de santé perçu"


# Example usage
if __name__ == "__main__":
    questionnaire = EQ5DQuestionnaire()
    
    # Example: Person with moderate problems
    example_responses = {
        'MOBILITY': 2,    # Problèmes légers
        'SELFCARE': 1,    # Aucun problème
        'ACTIVITY': 3,    # Problèmes modérés
        'PAIN': 2,        # Légère douleur
        'ANXIETY': 2,     # Légèrement anxieux
        'EQ_VAS': 65      # Health state today: 65/100
    }
    
    result = questionnaire.calculate_score(example_responses)
    
    print(f"État de santé EQ-5D: {result.get('health_state')}")
    print(f"Indice d'utilité: {result.get('utility_index'):.3f}")
    print(f"  → {result.get('utility_interpretation')}")
    if 'utility_estimated' in result:
        print(f"  (estimation - état non dans la table de référence)")
    print(f"\nEQ-VAS: {result.get('eq_vas')}/100")
    print(f"  → {result.get('vas_interpretation')}")


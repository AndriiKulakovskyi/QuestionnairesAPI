import random
from typing import Dict, List, Any, Optional

class ADHDRSQuestionnaire:
    """
    ADHD-RS (ADHD Rating Scale) - Adult/Child Version
    
    Description:
    18-item scale assessing DSM-IV symptoms of ADHD, divided into two subscales:
    - Inattention (9 items): items 1-9
    - Hyperactivity/Impulsivity (9 items): items 10-18
    
    Plus 1 diagnostic question about symptom onset before age 7.
    
    Responses:
    - 0: Rarement ou jamais
    - 1: Quelquefois
    - 2: Souvent
    - 3: Très souvent
    
    Scoring:
    - Inattention score: sum of items 1-9
    - Hyperactivity/Impulsivity score: sum of items 10-18
    - Total score: sum of all 18 items
    - Range: 0-54
    
    Note: Two versions exist (adult self-report and parent-report for children),
    with slight wording differences but identical scoring.
    """
    
    def __init__(self):
        self.name = "ADHD-RS"
        self.description = "ADHD Rating Scale - 18-item DSM-IV based assessment"
        self.num_items = 18  # Plus 1 diagnostic question
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize the 18 ADHD items."""
        
        # Inattention items (1-9)
        inattention_items = [
            "Ne parvient pas à prêter attention aux détails, ou fait des fautes d'étourderie",
            "A du mal à soutenir son attention au travail ou dans les jeux",
            "Semble ne pas écouter quand on lui parle personnellement",
            "Ne se conforme pas aux consignes et ne parvient pas à mener à terme ses tâches",
            "A du mal à organiser ses travaux ou ses activités",
            "Évite, a en aversion, ou fait à contre-cœur les tâches nécessitant un effort mental soutenu",
            "Perd les objets nécessaires à son travail ou à ses activités",
            "Se laisse facilement distraire par des stimuli externes",
            "A des oublis fréquents dans la vie quotidienne"
        ]
        
        # Hyperactivity/Impulsivity items (10-18)
        hyperactivity_items = [
            "Remue les mains ou les pieds, ou se tortille sur son siège",
            "Se lève en classe ou dans d'autres situations où il est supposé rester assis",
            "Court ou grimpe partout, dans des situations où cela est inapproprié",
            "A du mal à se tenir tranquille dans les jeux ou les activités de loisir",
            "Est 'sur la brèche' ou agit comme s'il était 'monté sur ressorts'",
            "Parle trop",
            "Laisse échapper la réponse à une question qui n'est pas encore entièrement posée",
            "A du mal à attendre son tour",
            "Interrompt les autres ou impose sa présence"
        ]
        
        # Create questions with response options
        response_options = {
            0: "Rarement ou jamais",
            1: "Quelquefois",
            2: "Souvent",
            3: "Très souvent"
        }
        
        item_num = 1
        for item_text in inattention_items:
            self.questions.append({
                'id': f'ADHDRS{item_num}',
                'text': item_text,
                'responses': response_options,
                'subscale': 'Inattention'
            })
            item_num += 1
        
        for item_text in hyperactivity_items:
            self.questions.append({
                'id': f'ADHDRS{item_num}',
                'text': item_text,
                'responses': response_options,
                'subscale': 'Hyperactivity/Impulsivity'
            })
            item_num += 1
        
        # Add diagnostic question (not scored)
        self.diagnostic_question = {
            'id': 'ADHDRS19',
            'text': "Certains de ces comportements étaient-ils présents avant l'âge de 7 ans ?",
            'responses': {0: "Non", 1: "Oui", 9: "NA"}
        }
    
    def calculate_score(self, responses: List[int]) -> Dict[str, Any]:
        """
        Calculate ADHD-RS scores.
        
        Args:
            responses: List of 18 integers (0-3) for items 1-18
        
        Returns:
            Dictionary containing subscale scores, total score, and interpretation
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")
        
        # Validate response range
        if any(r < 0 or r > 3 for r in responses):
            raise ValueError("All responses must be between 0 and 3")
        
        # Calculate subscale scores
        inattention_score = sum(responses[0:9])
        hyperactivity_score = sum(responses[9:18])
        total_score = inattention_score + hyperactivity_score
        
        # Interpretation based on clinical cutoffs
        # Adult cutoffs: Total ≥24 suggests ADHD; subscale ≥12 suggests that subtype
        # Child cutoffs vary by age and gender (normative data required for precise interpretation)
        
        inattention_interpretation = self._interpret_subscale(inattention_score)
        hyperactivity_interpretation = self._interpret_subscale(hyperactivity_score)
        total_interpretation = self._interpret_total(total_score)
        
        return {
            'total_score': total_score,
            'inattention_score': inattention_score,
            'hyperactivity_score': hyperactivity_score,
            'interpretation': total_interpretation,
            'inattention_interpretation': inattention_interpretation,
            'hyperactivity_interpretation': hyperactivity_interpretation,
            'subscales': {
                'Inattention': {
                    'score': inattention_score,
                    'max': 27,
                    'interpretation': inattention_interpretation
                },
                'Hyperactivity/Impulsivity': {
                    'score': hyperactivity_score,
                    'max': 27,
                    'interpretation': hyperactivity_interpretation
                }
            },
            'max_score': 54,
            'details': {
                'items_1_9_inattention': responses[0:9],
                'items_10_18_hyperactivity': responses[9:18]
            }
        }
    
    def _interpret_subscale(self, score: int) -> str:
        """Interpret subscale score (9 items, max 27)."""
        if score < 6:
            return "Minimal symptoms"
        elif score < 12:
            return "Mild symptoms"
        elif score < 18:
            return "Moderate symptoms - clinical concern"
        else:
            return "Severe symptoms - strong clinical concern"
    
    def _interpret_total(self, score: int) -> str:
        """Interpret total ADHD-RS score."""
        if score < 12:
            return "Minimal ADHD symptoms"
        elif score < 24:
            return "Mild ADHD symptoms"
        elif score < 36:
            return "Moderate ADHD symptoms - likely meets diagnostic criteria"
        else:
            return "Severe ADHD symptoms - strong likelihood of ADHD diagnosis"


if __name__ == '__main__':
    # Example usage
    adhd_rs = ADHDRSQuestionnaire()
    
    print(f"Questionnaire: {adhd_rs.name}")
    print(f"Description: {adhd_rs.description}")
    print(f"Number of items: {adhd_rs.num_items}\n")
    
    # Example 1: High inattention, low hyperactivity (ADHD-I subtype)
    print("=" * 70)
    print("Example 1: High Inattention, Low Hyperactivity")
    print("=" * 70)
    responses1 = [3,3,3,3,2,2,2,2,2,  # Inattention: high
                  0,0,1,0,0,1,0,0,0]  # Hyperactivity: low
    result1 = adhd_rs.calculate_score(responses1)
    print(f"Total Score: {result1['total_score']}/54")
    print(f"Inattention: {result1['inattention_score']}/27 - {result1['inattention_interpretation']}")
    print(f"Hyperactivity/Impulsivity: {result1['hyperactivity_score']}/27 - {result1['hyperactivity_interpretation']}")
    print(f"Interpretation: {result1['interpretation']}")
    
    # Example 2: High hyperactivity, low inattention (ADHD-H subtype)
    print("\n" + "=" * 70)
    print("Example 2: Low Inattention, High Hyperactivity")
    print("=" * 70)
    responses2 = [0,1,0,0,1,0,1,0,0,  # Inattention: low
                  3,3,2,3,3,2,2,3,3]  # Hyperactivity: high
    result2 = adhd_rs.calculate_score(responses2)
    print(f"Total Score: {result2['total_score']}/54")
    print(f"Inattention: {result2['inattention_score']}/27 - {result2['inattention_interpretation']}")
    print(f"Hyperactivity/Impulsivity: {result2['hyperactivity_score']}/27 - {result2['hyperactivity_interpretation']}")
    print(f"Interpretation: {result2['interpretation']}")
    
    # Example 3: Combined type (both high)
    print("\n" + "=" * 70)
    print("Example 3: Combined Type (Both High)")
    print("=" * 70)
    responses3 = [3,2,3,2,2,3,2,2,3,  # Inattention: high
                  2,3,2,2,3,2,3,2,2]  # Hyperactivity: high
    result3 = adhd_rs.calculate_score(responses3)
    print(f"Total Score: {result3['total_score']}/54")
    print(f"Inattention: {result3['inattention_score']}/27 - {result3['inattention_interpretation']}")
    print(f"Hyperactivity/Impulsivity: {result3['hyperactivity_score']}/27 - {result3['hyperactivity_interpretation']}")
    print(f"Interpretation: {result3['interpretation']}")
    
    # Example 4: Minimal symptoms
    print("\n" + "=" * 70)
    print("Example 4: Minimal Symptoms")
    print("=" * 70)
    responses4 = [0,1,0,1,0,0,1,0,0,
                  0,0,1,0,1,0,0,0,1]
    result4 = adhd_rs.calculate_score(responses4)
    print(f"Total Score: {result4['total_score']}/54")
    print(f"Inattention: {result4['inattention_score']}/27 - {result4['inattention_interpretation']}")
    print(f"Hyperactivity/Impulsivity: {result4['hyperactivity_score']}/27 - {result4['hyperactivity_interpretation']}")
    print(f"Interpretation: {result4['interpretation']}")


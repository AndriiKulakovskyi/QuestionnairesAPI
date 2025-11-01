import random
from typing import Dict, List, Any

class THADAQuestionnaire:
    """
    THADA - Trouble Hyperactif avec Déficit de l'Attention
    (ADHD Retrospective Assessment)
    
    Description:
    21-item retrospective assessment of childhood ADHD symptoms.
    Assesses whether symptoms were present in childhood ("Déjà"),
    currently present ("Actuellement"), or never present ("Jamais").
    
    Additional diagnostic questions:
    - Item 22: School performance
    - Item 23: Age of onset
    - Item 24-27: Treatment history
    
    Responses:
    1 = Jamais (Never)
    2 = Déjà (Previously, in childhood)
    3 = Actuellement (Currently, in the past week)
    
    Scoring:
    Items endorsed as "Déjà" or "Actuellement" count toward symptom presence.
    Higher scores indicate more ADHD symptoms.
    """
    
    def __init__(self):
        self.name = "THADA"
        self.description = "Trouble Hyperactif avec Déficit de l'Attention - Retrospective Assessment"
        self.num_items = 21  # Scored items
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize the 21 THADA items."""
        items = [
            "Du mal à rester assis (à l'école, à la maison)",
            "Bouger toujours sur votre chaise",
            "Du mal à jouer calmement",
            "Parler beaucoup, plus que les autres",
            "Faire une chose puis une autre sans terminer la première",
            "Du mal à faire attention (travail scolaire, jeux)",
            "Du mal à terminer les choses (travail, tâches ménagères)",
            "Facilement déconcentré par n'importe quoi",
            "Parler alors que d'autres sont en train de parler, interrompre",
            "Répondre aux questions avant qu'elles soient terminées",
            "Du mal à attendre votre tour",
            "Se précipiter sans penser aux conséquences",
            "Perdre beaucoup de choses (jouets, livres, clés)",
            "Ne pas écouter, rêvasser beaucoup",
            "Avoir des accidents fréquents",
            "Besoin de plus de supervision que les autres",
            "Être négligé et sale",
            "Être maladroit",
            "Être considéré comme hyperactif",
            "Se battre avec les autres enfants",
            "Être rejeté par les autres enfants"
        ]
        
        response_options = {
            1: "Jamais",
            2: "Déjà (dans l'enfance)",
            3: "Actuellement (semaine dernière)"
        }
        
        for i, text in enumerate(items):
            self.questions.append({
                'id': f'THAD{i+1}',
                'text': text,
                'responses': response_options
            })
        
        # Additional diagnostic questions (not scored)
        self.diagnostic_questions = {
            'ECPRIM': {
                'text': "Réussite durant l'école primaire (CP au CM2)",
                'responses': {1: "Mauvaise", 2: "Raisonnable", 3: "Moyenne", 4: "Bonne"}
            },
            'AGEPREC': {
                'text': "Âge le plus précoce d'apparition des symptômes",
                'type': 'numeric',
                'unit': 'ans'
            },
            'ATTAIDE': {
                'text': "Avez-vous cherché de l'aide pour des problèmes attentionnels?",
                'responses': {1: "Oui", 0: "Non"}
            },
            'ATTDIAG': {
                'text': "Le diagnostic de trouble attentionnel a-t-il été évoqué?",
                'responses': {1: "Oui", 0: "Non"}
            },
            'ATTMED': {
                'text': "Avez-vous pris des médicaments pour les troubles attentionnels?",
                'responses': {1: "Oui", 0: "Non"}
            }
        }
    
    def calculate_score(self, responses: List[int]) -> Dict[str, Any]:
        """
        Calculate THADA scores.
        
        Args:
            responses: List of 21 integers (1-3) for items 1-21
        
        Returns:
            Dictionary containing scores and interpretation
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")
        
        # Validate response range
        if any(r < 1 or r > 3 for r in responses):
            raise ValueError("All responses must be between 1 and 3")
        
        # Count symptoms endorsed (Déjà or Actuellement)
        childhood_symptoms = sum(1 for r in responses if r == 2)
        current_symptoms = sum(1 for r in responses if r == 3)
        any_symptoms = sum(1 for r in responses if r > 1)
        
        # Calculate raw score (treating 2 and 3 equally)
        total_score = sum(1 for r in responses if r > 1)
        
        # Symptom categories based on item groupings
        hyperactivity_items = [0, 1, 2, 3, 17, 18]  # Items 1, 2, 3, 4, 18, 19
        inattention_items = [5, 6, 7, 13]  # Items 6, 7, 8, 14
        impulsivity_items = [8, 9, 10, 11]  # Items 9, 10, 11, 12
        
        hyperactivity_score = sum(1 for i in hyperactivity_items if responses[i] > 1)
        inattention_score = sum(1 for i in inattention_items if responses[i] > 1)
        impulsivity_score = sum(1 for i in impulsivity_items if responses[i] > 1)
        
        return {
            'total_score': total_score,
            'childhood_symptoms': childhood_symptoms,
            'current_symptoms': current_symptoms,
            'hyperactivity': hyperactivity_score,
            'inattention': inattention_score,
            'impulsivity': impulsivity_score,
            'interpretation': self._interpret(total_score, childhood_symptoms, current_symptoms),
            'details': {
                'hyperactivity_max': len(hyperactivity_items),
                'inattention_max': len(inattention_items),
                'impulsivity_max': len(impulsivity_items)
            }
        }
    
    def _interpret(self, total: int, childhood: int, current: int) -> str:
        """Interpret THADA score."""
        interpretation = []
        
        if total < 4:
            interpretation.append("Minimal ADHD symptoms")
        elif total < 8:
            interpretation.append("Mild ADHD symptoms")
        elif total < 12:
            interpretation.append("Moderate ADHD symptoms - clinical concern")
        else:
            interpretation.append("Significant ADHD symptoms")
        
        if childhood >= 6:
            interpretation.append("Strong childhood symptom history")
        elif childhood > 0:
            interpretation.append("Some childhood symptoms reported")
        
        if current >= 6:
            interpretation.append("Current symptoms present")
        elif current > 0:
            interpretation.append("Some current symptoms")
        
        return " | ".join(interpretation)


if __name__ == '__main__':
    thada = THADAQuestionnaire()
    
    print(f"Questionnaire: {thada.name}")
    print(f"Description: {thada.description}")
    print(f"Number of items: {thada.num_items}\n")
    
    # Example 1: Strong childhood history, minimal current
    print("=" * 70)
    print("Example 1: Strong Childhood History, Minimal Current Symptoms")
    print("=" * 70)
    responses1 = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    result1 = thada.calculate_score(responses1)
    print(f"Total Symptoms: {result1['total_score']}/21")
    print(f"Childhood: {result1['childhood_symptoms']}, Current: {result1['current_symptoms']}")
    print(f"Hyperactivity: {result1['hyperactivity']}, Inattention: {result1['inattention']}, Impulsivity: {result1['impulsivity']}")
    print(f"Interpretation: {result1['interpretation']}")
    
    # Example 2: Current symptoms, minimal childhood
    print("\n" + "=" * 70)
    print("Example 2: Current Symptoms, Minimal Childhood History")
    print("=" * 70)
    responses2 = [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    result2 = thada.calculate_score(responses2)
    print(f"Total Symptoms: {result2['total_score']}/21")
    print(f"Childhood: {result2['childhood_symptoms']}, Current: {result2['current_symptoms']}")
    print(f"Hyperactivity: {result2['hyperactivity']}, Inattention: {result2['inattention']}, Impulsivity: {result2['impulsivity']}")
    print(f"Interpretation: {result2['interpretation']}")
    
    # Example 3: Mixed childhood and current
    print("\n" + "=" * 70)
    print("Example 3: Mixed Childhood and Current Symptoms")
    print("=" * 70)
    responses3 = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    result3 = thada.calculate_score(responses3)
    print(f"Total Symptoms: {result3['total_score']}/21")
    print(f"Childhood: {result3['childhood_symptoms']}, Current: {result3['current_symptoms']}")
    print(f"Hyperactivity: {result3['hyperactivity']}, Inattention: {result3['inattention']}, Impulsivity: {result3['impulsivity']}")
    print(f"Interpretation: {result3['interpretation']}")
    
    # Example 4: Minimal symptoms
    print("\n" + "=" * 70)
    print("Example 4: Minimal Symptoms")
    print("=" * 70)
    responses4 = [1] * 21
    result4 = thada.calculate_score(responses4)
    print(f"Total Symptoms: {result4['total_score']}/21")
    print(f"Childhood: {result4['childhood_symptoms']}, Current: {result4['current_symptoms']}")
    print(f"Hyperactivity: {result4['hyperactivity']}, Inattention: {result4['inattention']}, Impulsivity: {result4['impulsivity']}")
    print(f"Interpretation: {result4['interpretation']}")

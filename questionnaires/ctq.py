"""
Questionnaire: CTQ (Childhood Trauma Questionnaire)
Questionnaire sur les Traumatismes de l'Enfance
"""

from typing import Dict, List, Optional, Any


class CTQQuestionnaire:
    """CTQ - Childhood Trauma Questionnaire
    
    Auto-questionnaire d'évaluation des traumatismes vécus pendant l'enfance et l'adolescence.
    28 items répartis en 5 sous-échelles : abus physiques, abus émotionnels, abus sexuels,
    négligence émotionnelle, négligence physique. Inclut également une échelle de déni.
    """
    
    def __init__(self):
        self.name = "CTQ - Childhood Trauma Questionnaire"
        self.description = ("Questionnaire sur les traumatismes de l'enfance en 28 items. "
                           "Ce questionnaire porte sur certaines expériences que vous auriez pu vivre "
                           "au cours de votre enfance ou de votre adolescence.")
        self.used_in_applications = ["ebipolar", "eschizo"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 28 CTQ items with their response options"""
        
        # Standard options for all questions
        standard_options = {
            "Jamais": 1,
            "Rarement": 2,
            "Quelquefois": 3,
            "Souvent": 4,
            "Très souvent": 5
        }
        
        # Reverse-scored options
        reverse_options = {
            "Jamais": 5,
            "Rarement": 4,
            "Quelquefois": 3,
            "Souvent": 2,
            "Très souvent": 1
        }
        
        question_texts = [
            "Il m'est arrivé de ne pas avoir assez à manger",
            "Je savais qu'il y avait quelqu'un pour prendre soin de moi et me protéger",  # Reverse
            "Des membres de ma famille me disaient que j'étais « stupide » ou « paresseux » ou « laid »",
            "Mes parents étaient trop saouls ou « pétés » pour s'occuper de la famille",
            "Il y avait quelqu'un dans ma famille qui m'aidait à sentir que j'étais important ou particulier",  # Reverse
            "Je devais porter des vêtements sales",
            "Je me sentais aimé(e)",  # Reverse
            "Je pensais que mes parents n'avaient pas souhaité ma naissance",
            "J'ai été frappé(e) si fort par un membre de ma famille que j'ai dû consulter un docteur ou aller à l'hôpital",
            "Je n'aurais rien voulu changer à ma famille",  # Denial
            "Un membre de ma famille m'a frappé(e) si fort que j'ai eu des bleus ou des marques",
            "J'étais puni(e) au moyen d'une ceinture, d'un bâton, d'une corde ou de quelque autre objet dur",
            "Les membres de ma famille étaient attentifs les uns aux autres",  # Reverse
            "Les membres de ma famille me disaient des choses blessantes ou insultantes",
            "Je pense que j'ai été physiquement maltraité(e)",
            "J'ai eu une enfance parfaite",  # Denial
            "J'ai été frappé(e) ou battu(e) si fort que quelqu'un l'a remarqué (par ex. un professeur, un voisin ou un docteur)",
            "J'avais le sentiment que quelqu'un dans ma famille me détestait",
            "Les membres de ma famille se sentaient proches les uns des autres",  # Reverse
            "Quelqu'un a essayé de me faire des attouchements sexuels ou de m'en faire faire",
            "Quelqu'un a menacé de me blesser ou de raconter des mensonges à mon sujet si je ne faisais pas quelque chose de nature sexuelle avec lui",
            "J'avais la meilleure famille du monde",  # Denial
            "Quelqu'un a essayé de me faire faire des actes sexuels ou de me faire regarder de tels actes",
            "J'ai été victime d'abus sexuels",
            "Je pense que j'ai été maltraité affectivement",
            "Il y avait quelqu'un pour m'emmener chez le docteur si j'en avais besoin",  # Reverse
            "Je pense qu'on a abusé de moi sexuellement",
            "Ma famille était une source de force et de soutien"  # Reverse
        ]
        
        # Items that are reverse scored: 2, 5, 7, 13, 19, 26, 28
        reverse_items = {2, 5, 7, 13, 19, 26, 28}
        
        # Denial items: 10, 16, 22
        denial_items = {10, 16, 22}
        
        questions = []
        for i, text in enumerate(question_texts, start=1):
            question = {
                'id': f'rad_ctq{i}',
                'number': i,
                'text': f"{i}. {text}",
                'type': 'radio',
                'options': reverse_options if i in reverse_items else standard_options,
                'required': True,
                'reverse_scored': i in reverse_items,
                'denial_item': i in denial_items
            }
            questions.append(question)
            
        return questions
    
    def validate_responses(self, responses: Dict[str, str]) -> Dict[str, List[str]]:
        """Validate responses and return any errors
        
        Args:
            responses: Dictionary mapping question IDs to response strings
            
        Returns:
            Dictionary with 'errors' key containing list of error messages
        """
        errors = []
        
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses or responses[q_id] is None:
                errors.append(f"La question {question['number']} doit être renseignée")
            elif responses[q_id] not in question['options']:
                errors.append(f"Valeur invalide pour la question {question['number']}")
        
        return {'errors': errors, 'valid': len(errors) == 0}
    
    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate CTQ subscales and total score
        
        Subscales:
        - Physical Abuse: items 9, 11, 12, 15, 17
        - Emotional Neglect: items 5, 7, 13, 19, 28 (all reverse scored)
        - Physical Neglect: items 1, 2, 4, 6, 26 (items 2, 26 reverse scored)
        - Sexual Abuse: items 20, 21, 23, 24, 27
        - Emotional Abuse: items 3, 8, 14, 18, 25
        - Denial: items 10, 16, 22
        
        Total score is sum of the 5 trauma subscales (not including denial).
        
        Args:
            responses: Dictionary mapping question IDs to response strings
            
        Returns:
            Dictionary containing scores, validity, errors, and interpretations
        """
        # Validate responses first
        validation = self.validate_responses(responses)
        if not validation['valid']:
            return {
                'score': None,
                'subscales': {},
                'valid': False,
                'errors': validation['errors']
            }
        
        # Get numeric values for all responses
        values = {}
        for question in self.questions:
            q_id = question['id']
            response_text = responses.get(q_id)
            values[question['number']] = question['options'][response_text]
        
        # Calculate subscales
        physical_abuse = sum([values[i] for i in [9, 11, 12, 15, 17]])
        emotional_neglect = sum([values[i] for i in [5, 7, 13, 19, 28]])
        physical_neglect = sum([values[i] for i in [1, 2, 4, 6, 26]])
        sexual_abuse = sum([values[i] for i in [20, 21, 23, 24, 27]])
        emotional_abuse = sum([values[i] for i in [3, 8, 14, 18, 25]])
        denial = sum([values[i] for i in [10, 16, 22]])
        
        # Total score (sum of 5 trauma subscales, not including denial)
        total_score = physical_abuse + emotional_neglect + physical_neglect + sexual_abuse + emotional_abuse
        
        return {
            'score': total_score,
            'subscales': {
                'physical_abuse': physical_abuse,
                'emotional_neglect': emotional_neglect,
                'physical_neglect': physical_neglect,
                'sexual_abuse': sexual_abuse,
                'emotional_abuse': emotional_abuse,
                'denial': denial
            },
            'valid': True,
            'errors': [],
            'interpretations': {
                'physical_abuse': self._interpret_physical_abuse(physical_abuse),
                'emotional_neglect': self._interpret_emotional_neglect(emotional_neglect),
                'physical_neglect': self._interpret_physical_neglect(physical_neglect),
                'sexual_abuse': self._interpret_sexual_abuse(sexual_abuse),
                'emotional_abuse': self._interpret_emotional_abuse(emotional_abuse),
                'denial': self._interpret_denial(denial)
            }
        }
    
    def _interpret_physical_abuse(self, score: int) -> str:
        """Interpret physical abuse subscale score (range 5-25)"""
        if score < 8:
            return "Pas de traumatisme"
        elif score < 10:
            return "Léger"
        elif score < 13:
            return "Modéré"
        else:
            return "Sévère"
    
    def _interpret_emotional_neglect(self, score: int) -> str:
        """Interpret emotional neglect subscale score (range 5-25)"""
        if score < 10:
            return "Pas de traumatisme"
        elif score < 15:
            return "Léger"
        elif score < 18:
            return "Modéré"
        else:
            return "Sévère"
    
    def _interpret_physical_neglect(self, score: int) -> str:
        """Interpret physical neglect subscale score (range 5-25)"""
        if score < 8:
            return "Pas de traumatisme"
        elif score < 10:
            return "Léger"
        elif score < 13:
            return "Modéré"
        else:
            return "Sévère"
    
    def _interpret_sexual_abuse(self, score: int) -> str:
        """Interpret sexual abuse subscale score (range 5-25)"""
        if score < 6:
            return "Pas de traumatisme"
        elif score < 8:
            return "Léger"
        elif score < 13:
            return "Modéré"
        else:
            return "Sévère"
    
    def _interpret_emotional_abuse(self, score: int) -> str:
        """Interpret emotional abuse subscale score (range 5-25)"""
        if score < 9:
            return "Pas de traumatisme"
        elif score < 13:
            return "Léger"
        elif score < 16:
            return "Modéré"
        else:
            return "Sévère"
    
    def _interpret_denial(self, score: int) -> str:
        """Interpret denial subscale score (range 3-15)
        
        High denial score suggests potential minimization of childhood trauma
        """
        if score >= 11:
            return "Risque élevé de déni/minimisation"
        elif score >= 8:
            return "Risque modéré de déni/minimisation"
        else:
            return "Pas de déni apparent"


# Example usage
if __name__ == "__main__":
    questionnaire = CTQQuestionnaire()
    
    # Example responses (moderate trauma across subscales)
    example_responses = {
        'rad_ctq1': "Quelquefois",      # Physical neglect
        'rad_ctq2': "Souvent",           # Physical neglect (reverse)
        'rad_ctq3': "Rarement",          # Emotional abuse
        'rad_ctq4': "Jamais",            # Physical neglect
        'rad_ctq5': "Souvent",           # Emotional neglect (reverse)
        'rad_ctq6': "Rarement",          # Physical neglect
        'rad_ctq7': "Souvent",           # Emotional neglect (reverse)
        'rad_ctq8': "Quelquefois",       # Emotional abuse
        'rad_ctq9': "Jamais",            # Physical abuse
        'rad_ctq10': "Rarement",         # Denial
        'rad_ctq11': "Rarement",         # Physical abuse
        'rad_ctq12': "Jamais",           # Physical abuse
        'rad_ctq13': "Quelquefois",      # Emotional neglect (reverse)
        'rad_ctq14': "Rarement",         # Emotional abuse
        'rad_ctq15': "Jamais",           # Physical abuse
        'rad_ctq16': "Jamais",           # Denial
        'rad_ctq17': "Jamais",           # Physical abuse
        'rad_ctq18': "Quelquefois",      # Emotional abuse
        'rad_ctq19': "Quelquefois",      # Emotional neglect (reverse)
        'rad_ctq20': "Jamais",           # Sexual abuse
        'rad_ctq21': "Jamais",           # Sexual abuse
        'rad_ctq22': "Rarement",         # Denial
        'rad_ctq23': "Jamais",           # Sexual abuse
        'rad_ctq24': "Jamais",           # Sexual abuse
        'rad_ctq25': "Rarement",         # Emotional abuse
        'rad_ctq26': "Souvent",          # Physical neglect (reverse)
        'rad_ctq27': "Jamais",           # Sexual abuse
        'rad_ctq28': "Souvent"           # Emotional neglect (reverse)
    }
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score total CTQ: {result['score']}/125")
    print(f"\nSous-échelles:")
    for subscale, score in result['subscales'].items():
        interpretation = result['interpretations'].get(subscale, "")
        print(f"  {subscale}: {score} - {interpretation}")


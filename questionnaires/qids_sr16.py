"""
Questionnaire: QIDS-SR16 (Quick Inventory of Depressive Symptomatology - Self Report)
Inventaire Rapide de Symptomatologie Dépressive - Auto-questionnaire 16 items
"""

from typing import Dict, List, Optional, Any


class QIDSSR16Questionnaire:
    """QIDS-SR16 - Quick Inventory of Depressive Symptomatology
    
    Auto-questionnaire d'évaluation de la dépression en 16 items.
    Certains items ont une logique conditionnelle (appétit et poids).
    """
    
    def __init__(self):
        self.name = "QIDS-SR16 - Quick Inventory of Depressive Symptomatology"
        self.description = ("Inventaire rapide de symptomatologie dépressive en 16 items. "
                           "Auto-questionnaire évaluant les symptômes des 7 derniers jours.")
        self.used_in_applications = ["cedr"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 16 QIDS-SR16 items"""
        
        questions = [
            {
                'id': 'QIDS1',
                'number': 1,
                'text': "Endormissement :",
                'type': 'radio',
                'options': {
                    0: "0 Je ne mets jamais plus de 30 minutes à m'endormir.",
                    1: "1 Moins d'une fois sur deux, je mets au moins 30 minutes à m'endormir.",
                    2: "2 Plus d'une fois sur deux, je mets au moins 30 minutes à m'endormir.",
                    3: "3 Plus d'une fois sur deux, je mets plus d'une heure à m'endormir."
                },
                'required': True
            },
            {
                'id': 'QIDS2',
                'number': 2,
                'text': "Sommeil pendant la nuit :",
                'type': 'radio',
                'options': {
                    0: "0 Je ne me réveille pas la nuit.",
                    1: "1 J'ai un sommeil agité, léger et quelques réveils brefs chaque nuit.",
                    2: "2 Je me réveille au moins une fois par nuit, mais je me rendors facilement.",
                    3: "3 Plus d'une fois sur deux, je me réveille plus d'une fois par nuit et reste éveillé(e) 20 minutes ou plus."
                },
                'required': True
            },
            {
                'id': 'QIDS3',
                'number': 3,
                'text': "Réveil avant l'heure prévue :",
                'type': 'radio',
                'options': {
                    0: "0 La plupart du temps, je me réveille 30 minutes ou moins avant le moment où je dois me lever.",
                    1: "1 Plus d'une fois sur deux, je me réveille plus de 30 minutes avant le moment où je dois me lever.",
                    2: "2 Je me réveille presque toujours une heure ou plus avant le moment où je dois me lever, mais je finis par me rendormir.",
                    3: "3 Je me réveille au moins une heure avant le moment où je dois me lever et je n'arrive pas à me rendormir."
                },
                'required': True
            },
            {
                'id': 'QIDS4',
                'number': 4,
                'text': "Sommeil excessif :",
                'type': 'radio',
                'options': {
                    0: "0 Je ne dors pas plus de 7 à 8 heures par nuit, et je ne fais pas de sieste dans la journée.",
                    1: "1 Je ne dors pas plus de 10 heures sur un jour entier de 24 heures, siestes comprises.",
                    2: "2 Je ne dors pas plus de 12 heures sur un jour entier de 24 heures, siestes comprises.",
                    3: "3 Je dors plus de 12 heures sur un jour entier de 24 heures, siestes comprises."
                },
                'required': True
            },
            {
                'id': 'QIDS5',
                'number': 5,
                'text': "Tristesse :",
                'type': 'radio',
                'options': {
                    0: "0 Je ne me sens pas triste.",
                    1: "1 Je me sens triste moins de la moitié du temps.",
                    2: "2 Je me sens triste plus de la moitié du temps.",
                    3: "3 Je me sens triste presque tout le temps."
                },
                'required': True
            },
            {
                'id': 'QIDS6',
                'number': 6,
                'text': "Diminution de l'appétit :",
                'type': 'radio',
                'options': {
                    0: "0 J'ai le même appétit que d'habitude.",
                    1: "1 Je mange un peu moins souvent ou en plus petite quantité que d'habitude.",
                    2: "2 Je mange beaucoup moins que d'habitude et seulement en me forçant.",
                    3: "3 Je mange rarement sur un jour entier de 24 heures et seulement en me forçant énormément ou quand on me persuade de manger."
                },
                'required': False,  # Conditional with QIDS7
                'mutually_exclusive_with': 'QIDS7'
            },
            {
                'id': 'QIDS7',
                'number': 7,
                'text': "Augmentation de l'appétit :",
                'type': 'radio',
                'options': {
                    0: "0 J'ai le même appétit que d'habitude.",
                    1: "1 J'éprouve le besoin de manger plus souvent que d'habitude.",
                    2: "2 Je mange régulièrement plus souvent et/ou en plus grosse quantité que d'habitude.",
                    3: "3 J'éprouve un grand besoin de manger plus que d'habitude pendant et entre les repas."
                },
                'required': False,  # Conditional with QIDS6
                'mutually_exclusive_with': 'QIDS6'
            },
            {
                'id': 'QIDS8',
                'number': 8,
                'text': "Perte de poids (au cours des 15 derniers jours) :",
                'type': 'radio',
                'options': {
                    0: "0 Mon poids n'a pas changé.",
                    1: "1 J'ai l'impression d'avoir perdu un peu de poids.",
                    2: "2 J'ai perdu 1 kg ou plus.",
                    3: "3 J'ai perdu plus de 2 kg."
                },
                'required': False,  # Conditional with QIDS9
                'mutually_exclusive_with': 'QIDS9'
            },
            {
                'id': 'QIDS9',
                'number': 9,
                'text': "Prise de poids (au cours des 15 derniers jours) :",
                'type': 'radio',
                'options': {
                    0: "0 Mon poids n'a pas changé.",
                    1: "1 J'ai l'impression d'avoir pris un peu de poids.",
                    2: "2 J'ai pris 1 kg ou plus.",
                    3: "3 J'ai pris plus de 2 kg."
                },
                'required': False,  # Conditional with QIDS8
                'mutually_exclusive_with': 'QIDS8'
            },
            {
                'id': 'QIDS10',
                'number': 10,
                'text': "Concentration/Prise de décisions :",
                'type': 'radio',
                'options': {
                    0: "0 Il n'y a aucun changement dans ma capacité habituelle à me concentrer ou à prendre des décisions.",
                    1: "1 Je me sens parfois indécis(e) ou je trouve parfois que ma concentration est limitée.",
                    2: "2 La plupart du temps, j'ai du mal à me concentrer ou à prendre des décisions.",
                    3: "3 Je n'arrive pas me concentrer assez pour lire ou je n'arrive pas à prendre des décisions même si elles sont insignifiantes."
                },
                'required': True
            },
            {
                'id': 'QIDS11',
                'number': 11,
                'text': "Opinion de moi-même :",
                'type': 'radio',
                'options': {
                    0: "0 Je considère que j'ai autant de valeur que les autres et que je suis aussi méritant(e) que les autres.",
                    1: "1 Je me critique plus que d'habitude.",
                    2: "2 Je crois fortement que je cause des problèmes aux autres.",
                    3: "3 Je pense presque tout le temps à mes petits et mes gros défauts."
                },
                'required': True
            },
            {
                'id': 'QIDS12',
                'number': 12,
                'text': "Idées de mort ou de suicide :",
                'type': 'radio',
                'options': {
                    0: "0 Je ne pense pas au suicide ni à la mort.",
                    1: "1 Je pense que la vie est sans intérêt ou je me demande si elle vaut la peine d'être vécue.",
                    2: "2 Je pense au suicide ou à la mort plusieurs fois par semaine pendant plusieurs minutes.",
                    3: "3 Je pense au suicide ou à la mort plusieurs fois par jours en détail, j'ai envisagé le suicide de manière précise ou j'ai réellement tenté de mettre fin à mes jours."
                },
                'required': True
            },
            {
                'id': 'QIDS13',
                'number': 13,
                'text': "Enthousiasme général :",
                'type': 'radio',
                'options': {
                    0: "0 Il n'y pas de changement par rapport à d'habitude dans la manière dont je m'intéresse aux gens ou à mes activités.",
                    1: "1 Je me rends compte que je m'intéresse moins aux gens et à mes activités.",
                    2: "2 Je me rends compte que je n'ai d'intérêt que pour une ou deux des activités que j'avais auparavant.",
                    3: "3 Je n'ai pratiquement plus d'intérêt pour les activités que j'avais auparavant."
                },
                'required': True
            },
            {
                'id': 'QIDS14',
                'number': 14,
                'text': "Énergie :",
                'type': 'radio',
                'options': {
                    0: "0 J'ai autant d'énergie que d'habitude.",
                    1: "1 Je me fatigue plus facilement que d'habitude.",
                    2: "2 Je dois faire un gros effort pour commencer ou terminer mes activités quotidiennes (par exemple, faire les courses, les devoirs, la cuisine ou aller au travail).",
                    3: "3 Je ne peux vraiment pas faire mes activités quotidiennes parce que je n'ai simplement plus d'énergie."
                },
                'required': True
            },
            {
                'id': 'QIDS15',
                'number': 15,
                'text': "Impression de ralentissement :",
                'type': 'radio',
                'options': {
                    0: "0 Je pense, je parle et je bouge aussi vite que d'habitude.",
                    1: "1 Je trouve que je réfléchis plus lentement ou que ma voix est étouffée ou monocorde.",
                    2: "2 Il me faut plusieurs secondes pour répondre à la plupart des questions et je suis sûr(e) que je réfléchis plus lentement.",
                    3: "3 Je suis souvent incapable de répondre aux questions si je ne fais pas de gros efforts."
                },
                'required': True
            },
            {
                'id': 'QIDS16',
                'number': 16,
                'text': "Impression d'agitation :",
                'type': 'radio',
                'options': {
                    0: "0 Je ne me sens pas agité(e).",
                    1: "1 Je suis souvent agité(e), je me tords les mains ou j'ai besoin de changer de position quand je suis assis(e)",
                    2: "2 J'éprouve le besoin soudain de bouger et je suis plutôt agité(e).",
                    3: "3 Par moments, je suis incapable de rester assis(e) et j'ai besoin de faire les cent pas."
                },
                'required': True
            }
        ]
        
        return questions
    
    def validate_responses(self, responses: Dict[str, Any]) -> Dict[str, List[str]]:
        """Validate responses with conditional logic
        
        Args:
            responses: Dictionary mapping question IDs to response values
            
        Returns:
            Dictionary with 'errors' key containing list of error messages
        """
        errors = []
        
        # Check items 6 and 7 (appetite) - at least one must be filled
        qids6 = responses.get('QIDS6')
        qids7 = responses.get('QIDS7')
        
        if qids6 is None and qids7 is None:
            errors.append("Au moins un des items 6 (Diminution de l'appétit) ou 7 (Augmentation de l'appétit) doit être renseigné")
        
        # Check items 8 and 9 (weight) - at least one must be filled
        qids8 = responses.get('QIDS8')
        qids9 = responses.get('QIDS9')
        
        if qids8 is None and qids9 is None:
            errors.append("Au moins un des items 8 (Perte de poids) ou 9 (Prise de poids) doit être renseigné")
        
        # Check other required items
        for question in self.questions:
            if question.get('required', False):
                q_id = question['id']
                if q_id not in responses or responses[q_id] is None:
                    errors.append(f"L'item {question['number']} doit être renseigné")
        
        return {'errors': errors, 'valid': len(errors) == 0}
    
    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate QIDS-SR16 score with complex logic
        
        Scoring algorithm (from JavaScript):
        - Items 1-4: Take maximum of the 4 sleep items
        - Item 5: Direct score
        - Items 6-9: Take maximum of appetite items (6,7) and maximum of weight items (8,9)
        - Items 10-14: Direct scores
        - Items 15-16: Take maximum of psychomotor items
        
        Total score range: 0-27
        
        Args:
            responses: Dictionary mapping question IDs to response values (0-3)
            
        Returns:
            Dictionary containing score, validity, errors, and interpretation
        """
        # Validate responses first
        validation = self.validate_responses(responses)
        if not validation['valid']:
            return {
                'score': None,
                'valid': False,
                'errors': validation['errors']
            }
        
        # Handle conditional items (if one not filled, set to 0)
        if responses.get('QIDS6') is None and responses.get('QIDS7') is not None:
            responses['QIDS6'] = 0
        if responses.get('QIDS7') is None and responses.get('QIDS6') is not None:
            responses['QIDS7'] = 0
        if responses.get('QIDS8') is None and responses.get('QIDS9') is not None:
            responses['QIDS8'] = 0
        if responses.get('QIDS9') is None and responses.get('QIDS8') is not None:
            responses['QIDS9'] = 0
        
        # Sleep items (1-4): take maximum
        sleep_items = [responses.get(f'QIDS{i}', 0) for i in range(1, 5)]
        sleep_score = max(sleep_items)
        
        # Appetite/weight items (6-9): take max of appetite pair and max of weight pair
        appetite_score = max(responses.get('QIDS6', 0), responses.get('QIDS7', 0))
        weight_score = max(responses.get('QIDS8', 0), responses.get('QIDS9', 0))
        
        # Psychomotor items (15-16): take maximum
        psychomotor_items = [responses.get('QIDS15', 0), responses.get('QIDS16', 0)]
        psychomotor_score = max(psychomotor_items)
        
        # Direct score items: 5, 10-14
        direct_score = sum([
            responses.get('QIDS5', 0),
            responses.get('QIDS10', 0),
            responses.get('QIDS11', 0),
            responses.get('QIDS12', 0),
            responses.get('QIDS13', 0),
            responses.get('QIDS14', 0)
        ])
        
        # Total score
        total_score = sleep_score + appetite_score + weight_score + psychomotor_score + direct_score
        
        return {
            'score': total_score,
            'valid': True,
            'errors': [],
            'interpretation': self._interpret_score(total_score),
            'subscores': {
                'sleep': sleep_score,
                'appetite': appetite_score,
                'weight': weight_score,
                'psychomotor': psychomotor_score,
                'other_symptoms': direct_score
            }
        }
    
    def _interpret_score(self, score: int) -> str:
        """Provide interpretation of QIDS-SR16 score
        
        Standard severity levels:
        - 0-5: Absence de dépression
        - 6-10: Dépression légère
        - 11-15: Dépression modérée
        - 16-20: Dépression sévère
        - 21-27: Dépression très sévère
        
        Args:
            score: Total QIDS-SR16 score (0-27)
            
        Returns:
            Interpretation text
        """
        if score <= 5:
            return "Absence de dépression"
        elif score <= 10:
            return "Dépression légère"
        elif score <= 15:
            return "Dépression modérée"
        elif score <= 20:
            return "Dépression sévère"
        else:
            return "Dépression très sévère"


# Example usage
if __name__ == "__main__":
    questionnaire = QIDSSR16Questionnaire()
    
    # Example responses (moderate depression with decreased appetite and weight loss)
    example_responses = {
        'QIDS1': 2,
        'QIDS2': 2,
        'QIDS3': 1,
        'QIDS4': 0,
        'QIDS5': 2,
        'QIDS6': 2,  # Decreased appetite
        'QIDS7': None,  # Not increased appetite
        'QIDS8': 2,  # Weight loss
        'QIDS9': None,  # Not weight gain
        'QIDS10': 2,
        'QIDS11': 1,
        'QIDS12': 1,
        'QIDS13': 2,
        'QIDS14': 2,
        'QIDS15': 1,
        'QIDS16': 0
    }
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score QIDS-SR16: {result['score']}")
    print(f"Interprétation: {result['interpretation']}")
    print(f"Sous-scores: {result['subscores']}")


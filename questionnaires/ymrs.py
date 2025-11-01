"""
Questionnaire: YMRS (Young Mania Rating Scale)
Échelle de manie de Young
"""

from typing import Dict, List, Optional, Any


class YMRSQuestionnaire:
    """YMRS - Young Mania Rating Scale
    
    Échelle hétéro-évaluation de la manie en 11 items.
    Cotation basée sur l'observation clinique et l'entretien.
    """
    
    def __init__(self):
        self.name = "YMRS - Young Mania Rating Scale"
        self.description = ("Échelle d'évaluation de la manie en 11 items. "
                           "Le but de chaque item est d'estimer la sévérité de cette anomalie chez le patient. "
                           "Lorsque plusieurs descriptions sont données pour un degré particulier de sévérité, "
                           "une seule description est suffisante pour pouvoir attribuer ce degré.")
        self.used_in_applications = ["ebipolar", "eschizo"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 11 YMRS items with their response options"""
        
        questions = [
            {
                'id': 'radhtml_ymrs1',
                'number': 1,
                'text': "Elevation de l'humeur",
                'type': 'radio',
                'options': {
                    'a': "0 Absente",
                    'b': "1 Légèrement ou possiblement élevée lorsqu'on l'interroge",
                    'c': "2 Elévation subjective nette ; optimiste, plein d'assurance ; gai ; contenu approprié",
                    'd': "3 Elevée, au contenu appropriée, plaisantin",
                    'e': "4 Euphorique ; rires inappropriés ; chante"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs2',
                'number': 2,
                'text': "Activité motrice et énergie augmentées",
                'type': 'radio',
                'options': {
                    'a': "0 Absente",
                    'b': "1 Subjectivement élevées",
                    'c': "2 Animé ; expression gestuelle plus élevée",
                    'd': "3 Energie excessive ; parfois hyperactif ; agité (peut être calmé)",
                    'e': "4 Excitation motrice ; hyperactivité continuelle (ne peut être calmé)"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs3',
                'number': 3,
                'text': "Intérêt sexuel",
                'type': 'radio',
                'options': {
                    'a': "0 Normal, non augmenté",
                    'b': "1 Augmentation légère ou possible",
                    'c': "2 Clairement augmenté lorsqu'on l'interroge",
                    'd': "3 Parle spontanément de la sexualité ; élabore sur des thèmes sexuels ; se décrit comme étant hyper sexuel",
                    'e': "4 Agissements sexuels manifestes (envers les patients, les membres de l'équipe, ou l'évaluateur)"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs4',
                'number': 4,
                'text': "Sommeil",
                'type': 'radio',
                'options': {
                    'a': "0 Ne rapporte pas de diminution de sommeil",
                    'b': "1 Dort jusqu'à une heure de moins que d'habitude",
                    'c': "2 Sommeil réduit de plus d'une heure par rapport à d'habitude",
                    'd': "3 Rapporte un moins grand besoin de sommeil",
                    'e': "4 Nie le besoin de sommeil"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs5',
                'number': 5,
                'text': "Irritabilité",
                'type': 'radio',
                'options': {
                    'a': "0 Absente",
                    'b': "1 Subjectivement augmentée",
                    'c': "2 Irritable par moment durant l'entretien ; épisodes récents d'énervement ou de colère dans le service",
                    'd': "3 Fréquemment irritable durant l'entretien ; brusque ; abrupt",
                    'e': "4 Hostile, non coopératif ; évaluation impossible"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs6',
                'number': 6,
                'text': "Discours (débit et quantité)",
                'type': 'radio',
                'options': {
                    'a': "0 Pas augmenté",
                    'b': "1 Se sent bavard",
                    'c': "2 Augmentation du débit et de la quantité par moment ; prolixe par moment",
                    'd': "3 Soutenu ; augmentation consistante du débit ou de la quantité ; difficile à interrompre",
                    'e': "4 Sous pression ; impossible à interrompre ; discours continu"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs7',
                'number': 7,
                'text': "Langage - troubles de la pensée",
                'type': 'radio',
                'options': {
                    'a': "0 Absent",
                    'b': "1 Circonstanciel ; légère distractivité ; pensées rapides",
                    'c': "2 Distractivité ; perd le fil de ses idées ; change fréquemment de sujet ; pensées accélérées",
                    'd': "3 Fuite des idées ; réponses hors sujet ; difficile à suivre ; fait des rimes ; écholalie",
                    'e': "4 Incohérent ; communication impossible"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs8',
                'number': 8,
                'text': "Contenu",
                'type': 'radio',
                'options': {
                    'a': "0 Normal",
                    'b': "1 Projets discutables ; intérêts nouveaux",
                    'c': "2 Projet(s) particulier(s) ; hyper religieux",
                    'd': "3 Idées de grandeur ou de persécution ; idées de référence",
                    'e': "4 Délires ; hallucinations"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs9',
                'number': 9,
                'text': "Comportement agressif et perturbateur",
                'type': 'radio',
                'options': {
                    'a': "0 Absent, coopératif",
                    'b': "1 Sarcastique ; parle fort par moment, sur la défensive",
                    'c': "2 Exigeant ; fait des menaces dans le service",
                    'd': "3 Menace l'évaluateur ; crie ; évaluation difficile",
                    'e': "4 Agressif physiquement ; destructeur ; évaluation impossible"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs10',
                'number': 10,
                'text': "Apparence",
                'type': 'radio',
                'options': {
                    'a': "0 Soignée et habillement adéquat",
                    'b': "1 Légèrement négligé",
                    'c': "2 Peu soigné ; modérément débraillé ; trop habillé",
                    'd': "3 Débraillé ; à moitié nu ; maquillage criarde",
                    'e': "4 Complètement négligé ; orné ; accoutrement bizarre"
                },
                'required': True
            },
            {
                'id': 'radhtml_ymrs11',
                'number': 11,
                'text': "Introspection",
                'type': 'radio',
                'options': {
                    'a': "0 Présente ; admet être malade ; reconnaît le besoin de traitement",
                    'b': "1 Eventuellement malade",
                    'c': "2 Admet des changements de comportement, mais nie la maladie",
                    'd': "3 Admet de possibles changements de comportement, mais nie la maladie",
                    'e': "4 Nie tout changement de comportement"
                },
                'required': True
            }
        ]
        
        return questions
    
    def _letter_to_score(self, letter: str) -> int:
        """Convert letter response to numeric score
        
        Args:
            letter: Response letter ('a', 'b', 'c', 'd', 'e')
            
        Returns:
            Numeric score (0-4)
        """
        score_map = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4
        }
        return score_map.get(letter.lower(), 0)
    
    def validate_responses(self, responses: Dict[str, str]) -> Dict[str, List[str]]:
        """Validate responses and return any errors
        
        Args:
            responses: Dictionary mapping question IDs to response letters
            
        Returns:
            Dictionary with 'errors' key containing list of error messages
        """
        errors = []
        
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses or responses[q_id] is None:
                errors.append(f"L'item {question['number']} doit être renseigné")
            elif responses[q_id].lower() not in question['options']:
                errors.append(f"Valeur invalide pour l'item {question['number']}")
        
        return {'errors': errors, 'valid': len(errors) == 0}
    
    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate the YMRS total score
        
        The YMRS score is the sum of all 11 items.
        Each item is scored 0-4, giving a total range of 0-44.
        
        Args:
            responses: Dictionary mapping question IDs to response letters ('a'-'e')
            
        Returns:
            Dictionary containing:
                - 'score': Total YMRS score (0-44)
                - 'valid': Whether calculation was possible
                - 'errors': List of error messages if any
                - 'interpretation': Severity level interpretation
        """
        # Validate responses first
        validation = self.validate_responses(responses)
        if not validation['valid']:
            return {
                'score': None,
                'valid': False,
                'errors': validation['errors']
            }
        
        # Calculate total score by summing all items
        total_score = 0
        for question in self.questions:
            q_id = question['id']
            letter_response = responses.get(q_id, 'a')
            total_score += self._letter_to_score(letter_response)
        
        return {
            'score': total_score,
            'valid': True,
            'errors': [],
            'interpretation': self._interpret_score(total_score)
        }
    
    def _interpret_score(self, score: int) -> str:
        """Provide interpretation of the YMRS score
        
        Standard YMRS cutoffs:
        - < 12: Rémission / Absence de manie
        - 12-20: Hypomanie
        - >= 21: Manie
        
        Args:
            score: Total YMRS score (0-44)
            
        Returns:
            Interpretation text
        """
        if score < 12:
            return "Rémission / Absence de manie"
        elif score < 21:
            return "Hypomanie"
        else:
            return "Manie"


# Example usage
if __name__ == "__main__":
    questionnaire = YMRSQuestionnaire()
    
    # Example responses (moderate mania)
    example_responses = {
        'radhtml_ymrs1': 'c',   # Elevation 2
        'radhtml_ymrs2': 'd',   # Activity 3
        'radhtml_ymrs3': 'b',   # Sexual interest 1
        'radhtml_ymrs4': 'c',   # Sleep 2
        'radhtml_ymrs5': 'c',   # Irritability 2
        'radhtml_ymrs6': 'c',   # Speech 2
        'radhtml_ymrs7': 'b',   # Thought disorder 1
        'radhtml_ymrs8': 'c',   # Content 2
        'radhtml_ymrs9': 'b',   # Disruptive behavior 1
        'radhtml_ymrs10': 'b',  # Appearance 1
        'radhtml_ymrs11': 'c'   # Insight 2
    }
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score YMRS: {result['score']}/44")
    print(f"Interprétation: {result['interpretation']}")


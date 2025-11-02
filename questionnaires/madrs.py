"""
Questionnaire: MADRS (Montgomery-Åsberg Depression Rating Scale)
Échelle d'évaluation de la dépression de Montgomery et Åsberg
"""

from typing import Dict, List, Optional, Any


class MADRSQuestionnaire:
    """MADRS - Montgomery-Åsberg Depression Rating Scale
    
    Échelle hétéro-évaluation de la dépression en 10 items.
    Cotation basée sur l'entretien clinique.
    """
    
    def __init__(self):
        self.name = "MADRS - Montgomery-Åsberg Depression Rating Scale"
        self.description = ("Échelle d'évaluation de la dépression en 10 items. "
                           "La cotation doit se fonder sur l'entretien clinique allant de questions générales "
                           "sur les symptômes à des questions plus précises qui permettent une cotation exacte "
                           "de la sévérité. Le cotateur doit décider si la note est à un point nettement défini "
                           "de l'échelle (0, 2, 4, 6) ou à un point intermédiaire (1, 3, 5).")
        self.used_in_applications = ["cedr", "ebipolar", "eschizo"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 10 MADRS items with their response options"""
        
        questions = [
            {
                'id': 'MADRS1',
                'number': 1,
                'text': ("Tristesse apparente : Correspond au découragement, à la dépression et au désespoir "
                        "(plus qu'un simple cafard passager) reflétés par la parole, la mimique et la posture. "
                        "Coter selon la profondeur et l'incapacité à se dérider."),
                'type': 'radio',
                'options': {
                    0: "0 Pas de tristesse",
                    1: "1",
                    2: "2 Semble découragé mais peut se dérider sans difficulté",
                    3: "3",
                    4: "4 Paraît triste et malheureux la plupart du temps",
                    5: "5",
                    6: "6 Semble malheureux tout le temps. Extrêmement découragé"
                },
                'required': True
            },
            {
                'id': 'MADRS2',
                'number': 2,
                'text': ("Tristesse exprimée : Correspond à l'expression d'une humeur dépressive, que celle-ci "
                        "soit apparente ou non. Inclut le cafard, le découragement ou le sentiment de détresse "
                        "sans espoir. Coter selon l'intensité, la durée à laquelle l'humeur est dite être "
                        "influencée par les événements."),
                'type': 'radio',
                'options': {
                    0: "0 Tristesse occasionnelle en rapport avec les circonstances",
                    1: "1",
                    2: "2 Triste ou cafardeux, mais se déride sans difficulté",
                    3: "3",
                    4: "4 Sentiment envahissant de tristesse ou de dépression ; l'humeur est encore influencée par les circonstances extérieures",
                    5: "5",
                    6: "6 Tristesse, désespoir ou découragement permanents ou sans fluctuations"
                },
                'required': True
            },
            {
                'id': 'MADRS3',
                'number': 3,
                'text': ("Tension intérieure : Correspond aux sentiments de malaise mal défini, d'irritabilité, "
                        "d'agitation intérieure, de tension nerveuse allant jusqu'à la panique, l'effroi ou "
                        "l'angoisse. Coter selon l'intensité, la fréquence, la durée, le degré de réassurance nécessaire."),
                'type': 'radio',
                'options': {
                    0: "0 Calme. Tension intérieure seulement passagère",
                    1: "1",
                    2: "2 Sentiments occasionnels d'irritabilité et de malaise mal défini",
                    3: "3",
                    4: "4 Sentiments continuels de tension intérieure ou panique intermittente que le malade ne peut maîtriser qu'avec difficulté",
                    5: "5",
                    6: "6 Effroi ou angoisse sans relâche. Panique envahissante"
                },
                'required': True
            },
            {
                'id': 'MADRS4',
                'number': 4,
                'text': ("Réduction de sommeil : Correspond à une réduction de la durée ou de la profondeur du "
                        "sommeil par comparaison avec le sommeil du patient lorsqu'il n'est pas malade."),
                'type': 'radio',
                'options': {
                    0: "0 Dort comme d'habitude",
                    1: "1",
                    2: "2 Légère difficulté à s'endormir ou sommeil légèrement réduit, léger ou agité",
                    3: "3",
                    4: "4 Sommeil réduit ou interrompu au moins deux heures",
                    5: "5",
                    6: "6 Moins de deux ou trois heures de sommeil"
                },
                'required': True
            },
            {
                'id': 'MADRS5',
                'number': 5,
                'text': ("Réduction de l'appétit : Correspond au sentiment d'une perte de l'appétit comparé à "
                        "l'appétit habituel. Coter l'absence de désir de nourriture ou le besoin de se forcer pour manger."),
                'type': 'radio',
                'options': {
                    0: "0 Appétit normal ou augmenté",
                    1: "1",
                    2: "2 Appétit légèrement réduit",
                    3: "3",
                    4: "4 Pas d'appétit. Nourriture sans goût",
                    5: "5",
                    6: "6 Ne mange que si on le persuade"
                },
                'required': True
            },
            {
                'id': 'MADRS6',
                'number': 6,
                'text': ("Difficultés de concentration : Correspond aux difficultés à rassembler ses pensées allant "
                        "jusqu'à l'incapacité à se concentrer. Coter l'intensité, la fréquence et le degré d'incapacité."),
                'type': 'radio',
                'options': {
                    0: "0 Pas de difficultés de concentration",
                    1: "1",
                    2: "2 Difficultés occasionnelles à rassembler ses pensées",
                    3: "3",
                    4: "4 Difficultés à se concentrer et à maintenir son attention, ce qui réduit la capacité à lire ou à soutenir une conversation",
                    5: "5",
                    6: "6 Incapable de lire ou de converser sans grande difficulté"
                },
                'required': True
            },
            {
                'id': 'MADRS7',
                'number': 7,
                'text': ("Lassitude : Correspond à une difficulté à se mettre en train ou une lenteur à commencer "
                        "et à accomplir les activités quotidiennes."),
                'type': 'radio',
                'options': {
                    0: "0 Guère de difficultés à se mettre en route. Pas de lenteur",
                    1: "1",
                    2: "2 Difficultés à commencer des activités",
                    3: "3",
                    4: "4 Difficultés à commencer des activités routinières qui sont poursuivies avec effort",
                    5: "5",
                    6: "6 Grande lassitude. Incapable de faire quoi que ce soit sans aide"
                },
                'required': True
            },
            {
                'id': 'MADRS8',
                'number': 8,
                'text': ("Incapacité à ressentir : Correspond à l'expérience subjective d'une réduction d'intérêt "
                        "pour le monde environnant, ou les activités qui donnent normalement du plaisir. La capacité "
                        "à réagir avec une émotion appropriée aux circonstances ou aux gens est réduite."),
                'type': 'radio',
                'options': {
                    0: "0 Intérêt normal pour le monde environnant et pour les gens",
                    1: "1",
                    2: "2 Capacité réduite à prendre du plaisir à ses intérêts habituels",
                    3: "3",
                    4: "4 Perte d'intérêt pour le monde environnant. Perte de sentiment pour les amis et les connaissances",
                    5: "5",
                    6: "6 Sentiment d'être paralysé émotionnellement, incapacité à ressentir de la colère, du chagrin ou du plaisir et impossibilité complète ou même douloureuse de ressentir quelque chose pour les proches parents et amis"
                },
                'required': True
            },
            {
                'id': 'MADRS9',
                'number': 9,
                'text': ("Pensées pessimistes : Correspond aux idées de culpabilité, d'infériorité, d'auto-accusation, "
                        "de pêché, de remords ou de ruine."),
                'type': 'radio',
                'options': {
                    0: "0 Pas de pensée pessimiste",
                    1: "1",
                    2: "2 Idées intermittentes d'échec, d'auto-accusation ou d'auto-dépréciation",
                    3: "3",
                    4: "4 Auto-accusations persistantes ou idées de culpabilité ou péché précises mais encore rationnelles. Pessimisme croissant à propos du futur",
                    5: "5",
                    6: "6 Idées délirantes de ruine, de remords ou péché inexpiable. Auto-accusations absurdes ou inébranlables"
                },
                'required': True
            },
            {
                'id': 'MADRS10',
                'number': 10,
                'text': ("Idées de suicide : Correspond au sentiment que la vie ne vaut pas la peine d'être vécue, "
                        "qu'une mort naturelle serait la bienvenue, idées de suicide et préparatifs au suicide. "
                        "Les tentatives de suicide ne doivent pas, en elles-mêmes, influencer la cotation."),
                'type': 'radio',
                'options': {
                    0: "0 Jouit de la vie ou la prend comme elle vient",
                    1: "1",
                    2: "2 Fatigué de la vie, idées de suicide seulement passagères",
                    3: "3",
                    4: "4 Il vaudrait mieux être mort. Les idées de suicide sont courantes et le suicide est considéré comme une solution possible mais sans projet ou intention précis",
                    5: "5",
                    6: "6 Projets explicites de suicide si l'occasion se présente. Préparatifs de suicide"
                },
                'required': True
            }
        ]
        
        return questions
    
    def get_instructions(self) -> str:
        """Return the MADRS questionnaire instructions"""
        return (
            "CONSIGNES\n\n"
            "La cotation doit se fonder sur l'entretien clinique allant de questions générales sur les symptômes "
            "à des questions plus précises qui permettent une cotation exacte de la sévérité. Le cotateur doit "
            "décider si la note est à un point nettement défini de l'échelle (0, 2, 4, 6) ou à un point intermédiaire "
            "(1, 3, 5). Il est rare qu'un patient déprimé ne puisse pas être coté sur les items de l'échelle. Si des "
            "réponses précises ne peuvent être obtenues du malade, toutes les indications pertinentes et les "
            "informations d'autres sources doivent être utilisées comme base de la cotation en accord avec la "
            "clinique. Cocher pour chaque item la case qui correspond au chiffre le plus adéquat."
        )

    def validate_responses(self, responses: Dict[str, int]) -> Dict[str, List[str]]:
        """Validate responses and return any errors
        
        Args:
            responses: Dictionary mapping question IDs to response values
            
        Returns:
            Dictionary with 'errors' key containing list of error messages
        """
        errors = []
        
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses or responses[q_id] is None:
                errors.append(f"L'item {question['number']} doit être renseigné")
            elif responses[q_id] not in question['options']:
                errors.append(f"Valeur invalide pour l'item {question['number']}")
        
        return {'errors': errors, 'valid': len(errors) == 0}
    
    def calculate_score(self, responses: Dict[str, int]) -> Dict[str, Any]:
        """Calculate the MADRS total score
        
        The MADRS score is simply the sum of all 10 items (each scored 0-6).
        Total score range: 0-60
        
        Args:
            responses: Dictionary mapping question IDs (e.g., 'MADRS1') to response values (0-6)
            
        Returns:
            Dictionary containing:
                - 'score': Total MADRS score (0-60)
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
            total_score += responses.get(q_id, 0)
        
        return {
            'score': total_score,
            'valid': True,
            'errors': [],
            'interpretation': self._interpret_score(total_score)
        }
    
    def _interpret_score(self, score: int) -> str:
        """Provide interpretation of the MADRS score
        
        Standard MADRS severity cutoffs:
        - 0-6: Absence de dépression ou rémission
        - 7-19: Dépression légère
        - 20-34: Dépression modérée
        - 35-60: Dépression sévère
        
        Args:
            score: Total MADRS score (0-60)
            
        Returns:
            Interpretation text
        """
        if score <= 6:
            return "Absence de dépression ou rémission"
        elif score <= 19:
            return "Dépression légère"
        elif score <= 34:
            return "Dépression modérée"
        else:
            return "Dépression sévère"


# Example usage
if __name__ == "__main__":
    questionnaire = MADRSQuestionnaire()
    
    # Example responses (moderate depression)
    example_responses = {
        'MADRS1': 3,
        'MADRS2': 4,
        'MADRS3': 2,
        'MADRS4': 3,
        'MADRS5': 2,
        'MADRS6': 3,
        'MADRS7': 4,
        'MADRS8': 3,
        'MADRS9': 2,
        'MADRS10': 1
    }
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score MADRS: {result['score']}")
    print(f"Interprétation: {result['interpretation']}")


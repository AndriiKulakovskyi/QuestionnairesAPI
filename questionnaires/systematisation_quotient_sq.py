"""
Questionnaire: Quotient de Systématisation (SQ)
Systemising Quotient - Baron-Cohen
"""

from typing import Dict, List, Optional, Any


class SystematisationQuotientQuestionnaire:
    """Quotient de Systématisation (SQ) - Baron-Cohen
    
    Questionnaire d'auto-évaluation mesurant la tendance à systématiser,
    c'est-à-dire l'aptitude à analyser ou construire des systèmes.
    """
    
    def __init__(self):
        self.name = "Quotient de Systématisation (SQ)"
        self.description = "Questionnaire d'auto-évaluation en 60 items mesurant la tendance à systématiser"
        self.used_in_applications = ["asperger"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 60 questions with their response options"""
        
        questions = []
        
        question_texts = {
            1: "Quand j'écoute un morceau de musique, je reconnais toujours sa structure",
            2: "Je suis superstitieux",
            3: "Je prends souvent des résolutions, mais trouve difficile de m'y tenir",
            4: "Je préfère lire des livres concernant la réalité (biographies, livres scientifiques, actualités...) plutôt que des oeuvres de fiction",
            5: "Si je devais acheter une voiture, j'aimerais avoir des informations précises sur les capacités du moteur",
            6: "En règle générale, quand j'observe un tableau, je ne réfléchis pas aux techniques utilisées pour le faire",
            7: "S'il y avait un problème avec le réseau électrique chez moi, je pourrais le réparer moi-même",
            8: "Quand je fais un rêve, je trouve difficile de me souvenir des détails précis le lendemain",
            9: "Quand je regarde un film je préfère être avec un groupe d'amis plutôt que seul",
            10: "Je suis curieux d'apprendre des choses sur les différentes religions",
            11: "Je lis rarement des articles ou des pages internet qui concernent les nouvelles technologies",
            12: "Je n'aime pas les jeux qui nécessitent beaucoup de stratégie",
            13: "Je suis fasciné(e) par le fonctionnement des machines",
            14: "Je me fais un devoir d'écouter les nouvelles chaque matin",
            15: "En mathématiques, je suis intrigué par les règles et les théories régissant les nombres",
            16: "J'ai du mal à garder contact avec de vieux amis",
            17: "Quand je raconte une histoire, j'omets souvent les détails et je raconte juste l'essentiel de ce qui s'est passé",
            18: "Je comprends difficilement les notices d'instructions qui permettent d'assembler des éléments d'un appareil",
            19: "Quand je vois un animal, j'aime savoir à quelle espèce précise il appartient",
            20: "Si j'achetais un ordinateur, j'aimerais connaître des détails précis sur les capacités de son disque dur et de son processeur",
            21: "J'aime prendre part à des activités sportives",
            22: "Si je peux, j'essaie d'éviter de faire le ménage",
            23: "Quand je cuisine, je ne réfléchis pas à la façon dont les ingrédients ou les différentes façons de faire contribuent au résultat final",
            24: "Je trouve difficile de lire et de comprendre des cartes géographiques",
            25: "Si j'avais une collection (ex : CD, pièces de monnaie, timbres), elle serait très bien classée",
            26: "Quand je regarde un meuble, je ne prête pas attention aux détails de sa fabrication",
            27: "L'idée de m'adonner à des activités à risque me séduit",
            28: "Quand j'apprends des choses à propos d'événements historiques, je ne me concentre pas sur les dates exactes",
            29: "Quand je lis le journal je suis attiré par certaines rubriques, telles que les résultats du championnat de football ou les indices du marché boursier",
            30: "Quand j'apprends une langue, je m'intéresse aux règles grammaticales",
            31: "Je trouve difficile d'apprendre à me repérer dans une ville nouvelle",
            32: "Je n'aime pas particulièrement regarder des documentaires scientifiques à la TV, ni lire des articles scientifiques ou des articles sur la nature",
            33: "Si j'achetais une chaîne stéréo, j'aimerais connaître ses caractéristiques techniques précises",
            34: "Je trouve facile de comprendre exactement les règles de probabilité dans un pari",
            35: "Je ne suis pas très méticuleux quand je fais du bricolage",
            36: "Il est facile d'avoir une conversation avec une personne que je viens tout juste de rencontrer",
            37: "Quand je regarde un bâtiment, je suis curieux de savoir comment il a été précisément construit",
            38: "Quand il y a une élection, je ne m'intéresse pas aux scores de chaque parti",
            39: "Quand je prête de l'argent à quelqu'un, je compte sur le fait que la personne me rembourse exactement ce qu'elle me doit",
            40: "Je comprends difficilement les informations que m'envoie la banque sur les différents investissements et plans d'épargne",
            41: "Quand je voyage en train, je me demande souvent comment le réseau ferroviaire est organisé",
            42: "Quand j'achète un nouvel appareil, je ne lis pas minutieusement le manuel d'instruction",
            43: "Si j'achetais un appareil photo, je ne regarderais pas avec attention la qualité de l'objectif",
            44: "Quand je lis quelque chose, je vérifie toujours si c'est grammaticalement correct",
            45: "Quand j'entends la météo, je ne suis pas très intéressé par les modèles météorologiques",
            46: "Je me demande souvent comment ce serait d'être quelqu'un d'autre",
            47: "Je trouve difficile de faire deux choses à la fois",
            48: "Quand je regarde une montagne, je me demande précisément comment elle s'est formée",
            49: "J'arrive facilement à visualiser comment sont reliées les autoroutes de ma région",
            50: "Quand je suis au restaurant, je mets souvent du temps à décider ce que je vais commander",
            51: "Quand je suis dans un avion, je ne pense pas à l'aérodynamisme",
            52: "J'oublie souvent les détails des conversations que j'ai eues",
            53: "Quand je me promène à la campagne, je suis intéressé(e) par les différences entre les diverses espèces d'arbres",
            54: "Si j'ai rencontré une personne une ou deux fois, je me souviens difficilement ce à quoi elle ressemble précisément",
            55: "J'aime connaître le chemin que suit une rivière de sa source à la mer",
            56: "Je ne lis pas très attentivement les documents juridiques",
            57: "Je ne me demande pas comment fonctionne la communication sans fil",
            58: "Je m'intéresse à la vie sur les autres planètes",
            59: "Quand je voyage, j'aime connaître des détails précis concernant la culture du pays que je visite",
            60: "Ça m'est égal de connaître les noms des plantes que je vois"
        }
        
        # Response options (same for all questions)
        response_options = {
            -1: "",  # Empty/not answered
            1: "Fortement d'accord",
            2: "Légèrement d'accord",
            3: "Légèrement en désaccord",
            4: "Fortement en désaccord"
        }
        
        # Items that use reverse scoring (scoring function 1)
        # These correspond to indices: 0,3,4,6,12,14,18,19,24,28,29,32,33,36,40,43,47,48,52,54
        # Which are questions: 1,4,5,7,13,15,19,20,25,29,30,33,34,37,41,44,48,49,53,55
        reverse_score_items_1 = {1, 4, 5, 7, 13, 15, 19, 20, 25, 29, 30, 33, 34, 37, 41, 44, 48, 49, 53, 55}
        
        # Items that use reverse scoring (scoring function 2)
        # These correspond to indices: 5,10,11,17,22,23,25,27,30,31,34,37,39,41,42,44,50,55,56,59
        # Which are questions: 6,11,12,18,23,24,26,28,31,32,35,38,40,42,43,45,51,56,57,60
        reverse_score_items_2 = {6, 11, 12, 18, 23, 24, 26, 28, 31, 32, 35, 38, 40, 42, 43, 45, 51, 56, 57, 60}
        
        for q_num, q_text in question_texts.items():
            question = {
                'id': f'SYSTE{q_num}',
                'number': q_num,
                'text': f"{q_num}. {q_text}",
                'type': 'select',
                'options': response_options,
                'required': True,
                'reverse_score_type': None
            }
            
            if q_num in reverse_score_items_1:
                question['reverse_score_type'] = 1
            elif q_num in reverse_score_items_2:
                question['reverse_score_type'] = 2
                
            questions.append(question)
            
        return questions
    
    def _reverse_score_type_1(self, value: int) -> int:
        """Reverse scoring for type 1 items
        
        Scoring logic from JavaScript:
        function valeur_inverse_SYSTEMATISATION1(val){
            if(val == 1) return 2;
            if(val == 2) return 1;
            if(val == 3) return 0;
            if(val == 4) return 0;
        }
        """
        scoring_map = {
            1: 2,  # Fortement d'accord -> 2 points
            2: 1,  # Légèrement d'accord -> 1 point
            3: 0,  # Légèrement en désaccord -> 0 point
            4: 0   # Fortement en désaccord -> 0 point
        }
        return scoring_map.get(value, 0)
    
    def _reverse_score_type_2(self, value: int) -> int:
        """Reverse scoring for type 2 items
        
        Scoring logic from JavaScript:
        function valeur_inverse_SYSTEMATISATION2(val){
            if(val == 1) return 0;
            if(val == 2) return 0;
            if(val == 3) return 1;
            if(val == 4) return 2;
        }
        """
        scoring_map = {
            1: 0,  # Fortement d'accord -> 0 point
            2: 0,  # Légèrement d'accord -> 0 point
            3: 1,  # Légèrement en désaccord -> 1 point
            4: 2   # Fortement en désaccord -> 2 points
        }
        return scoring_map.get(value, 0)
    
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
            if q_id not in responses or responses[q_id] is None or responses[q_id] == -1:
                errors.append(f"La question {question['number']} doit être renseignée")
            elif responses[q_id] not in question['options']:
                errors.append(f"Valeur invalide pour la question {question['number']}")
        
        return {'errors': errors, 'valid': len(errors) == 0}
    
    def calculate_score(self, responses: Dict[str, int]) -> Dict[str, Any]:
        """Calculate the SQ score
        
        Args:
            responses: Dictionary mapping question IDs (e.g., 'SYSTE1') to response values (1-4)
            
        Returns:
            Dictionary containing:
                - 'score': Total score (0-120)
                - 'valid': Whether calculation was possible
                - 'errors': List of error messages if any
        """
        # Validate responses first
        validation = self.validate_responses(responses)
        if not validation['valid']:
            return {
                'score': None,
                'valid': False,
                'errors': validation['errors']
            }
        
        total_score = 0
        
        for question in self.questions:
            q_id = question['id']
            response_value = responses.get(q_id)
            
            if response_value is None or response_value == -1:
                continue
                
            # Apply appropriate scoring based on reverse_score_type
            if question['reverse_score_type'] == 1:
                total_score += self._reverse_score_type_1(response_value)
            elif question['reverse_score_type'] == 2:
                total_score += self._reverse_score_type_2(response_value)
        
        return {
            'score': total_score,
            'valid': True,
            'errors': [],
            'interpretation': self._interpret_score(total_score)
        }
    
    def _interpret_score(self, score: int) -> str:
        """Provide interpretation of the score
        
        Args:
            score: Total SQ score (0-120)
            
        Returns:
            Interpretation text
        """
        if score >= 80:
            return "Score élevé de systématisation"
        elif score >= 40:
            return "Score moyen de systématisation"
        else:
            return "Score faible de systématisation"


# Example usage
if __name__ == "__main__":
    questionnaire = SystematisationQuotientQuestionnaire()
    
    # Example responses (all questions answered with "Fortement d'accord")
    example_responses = {f'SYSTE{i}': 1 for i in range(1, 61)}
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score SQ: {result['score']}")
    print(f"Interprétation: {result['interpretation']}")


"""
Questionnaire: AQ (Autism Quotient)
Quotient du Spectre Autistique
"""

from typing import Dict, List, Optional, Any


class AQQuestionnaire:
    """AQ - Autism Quotient (Autism Spectrum Quotient)
    
    Auto-questionnaire de dépistage des traits autistiques en 50 items.
    Évalue les caractéristiques associées au spectre autistique chez les adultes
    d'intelligence normale.
    
    Développé par Baron-Cohen et al. (2001)
    
    5 sous-échelles (10 items chacune):
    - Compétences sociales
    - Attention switching (changement d'attention)
    - Attention aux détails
    - Communication
    - Imagination
    
    Chaque item: "Fortement d'accord" / "Légèrement d'accord" / 
                 "Légèrement en désaccord" / "Fortement en désaccord"
    
    Score total: 0-50 (1 point par trait autistique présent)
    Cutoff suggestif: ≥ 32 (sensible aux traits autistiques cliniquement significatifs)
    """
    
    def __init__(self):
        self.name = "AQ - Autism Quotient"
        self.description = ("Questionnaire de dépistage des traits autistiques en 50 items. "
                           "Évalue les caractéristiques du spectre autistique chez les adultes.")
        self.used_in_applications = ["asperger"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 50 AQ items with reverse scoring indicators"""
        
        # Response options (same for all items)
        response_options = {
            1: "Fortement d'accord",
            2: "Légèrement d'accord",
            3: "Légèrement en désaccord",
            4: "Fortement en désaccord"
        }
        
        # All 50 items with their text and scoring direction
        # 'agree_scores': True if agree responses (1,2) score a point
        # 'agree_scores': False if disagree responses (3,4) score a point
        items_data = [
            (1, "Je préfère réaliser des activités avec d'autres personnes plutôt que seul(e).", False),
            (2, "Je préfère tout faire continuellement de la même manière.", True),
            (3, "Quand j'essaye d'imaginer quelque chose, il est très facile de m'en représenter une image mentalement.", False),
            (4, "Je suis fréquemment tellement absorbé(e) par une chose que je perds tout le reste de vue.", True),
            (5, "Mon attention est souvent attirée par des bruits discrets que les autres ne remarquent pas.", True),
            (6, "Je fais habituellement attention aux numéros de plaques d'immatriculation ou à d'autres types d'informations de ce genre.", True),
            (7, "Les gens me disent souvent que ce que j'ai dit était impoli, même quand je pense moi que c'était poli.", True),
            (8, "Quand je lis une histoire, je peux facilement imaginer à quoi les personnages pourraient ressembler.", False),
            (9, "Je suis fasciné(e) par les dates.", True),
            (10, "Au sein d'un groupe, je peux facilement suivre les conversations de plusieurs personnes à la fois.", False),
            (11, "Je trouve les situations de la vie en société faciles.", False),
            (12, "J'ai tendance à remarquer certains détails que les autres ne voient pas.", True),
            (13, "Je préfèrerais aller dans une bibliothèque plutôt qu'à une fête.", True),
            (14, "Je trouve facile d'inventer des histoires.", False),
            (15, "Je suis plus facilement attiré(e) par les gens que par les objets.", False),
            (16, "J'ai tendance à avoir des centres d'intérêt très importants. Je me tracasse lorsque je ne peux m'y consacrer.", True),
            (17, "J'apprécie le bavardage en société.", False),
            (18, "Quand je parle, il n'est pas toujours facile pour les autres de placer un mot.", True),
            (19, "Je suis fasciné(e) par les chiffres.", True),
            (20, "Quand je lis une histoire, je trouve qu'il est difficile de me représenter les intentions des personnages.", True),
            (21, "Je n'aime pas particulièrement lire des romans.", True),
            (22, "Je trouve qu'il est difficile de se faire de nouveaux amis.", True),
            (23, "Je remarque sans cesse des schémas réguliers dans les choses qui m'entourent.", True),
            (24, "Je préfèrerais aller au théâtre qu'au musée.", False),
            (25, "Cela ne me dérange pas si mes habitudes quotidiennes sont perturbées.", False),
            (26, "Je remarque souvent que je ne sais pas comment entretenir une conversation.", True),
            (27, "Je trouve qu'il est facile de « lire entre les lignes » lorsque quelqu'un me parle.", False),
            (28, "Je me concentre habituellement plus sur l'ensemble d'une image que sur les petits détails de celle-ci.", False),
            (29, "Je ne suis pas très doué(e) pour me souvenir des numéros de téléphone.", False),
            (30, "Je ne remarque habituellement pas les petits changements dans une situation ou dans l'apparence de quelqu'un.", False),
            (31, "Je sais m'en rendre compte quand mon interlocuteur s'ennuie.", False),
            (32, "Je trouve qu'il est facile de faire plus d'une chose à la fois.", False),
            (33, "Quand je parle au téléphone, je ne suis pas sûr(e) de savoir quand c'est à mon tour de parler.", True),
            (34, "J'aime faire les choses de manière spontanée.", False),
            (35, "Je suis souvent le(la) dernier(ère) à comprendre le sens d'une blague.", True),
            (36, "Je trouve qu'il est facile de décoder ce que les autres pensent ou ressentent juste en regardant leur visage.", False),
            (37, "Si je suis interrompu(e), je peux facilement revenir à ce que j'étais en train de faire.", False),
            (38, "Je suis doué(e) pour le bavardage en société.", False),
            (39, "Les gens me disent souvent que je répète continuellement les mêmes choses.", True),
            (40, "Quand j'étais enfant, j'aimais habituellement jouer à des jeux de rôle avec les autres.", False),
            (41, "J'aime collectionner des informations sur des catégories de choses (types de voitures, d'oiseaux, de trains, de plantes, ...).", True),
            (42, "Je trouve qu'il est difficile de s'imaginer dans la peau d'un autre.", True),
            (43, "J'aime planifier avec soin toute activité à laquelle je participe.", True),
            (44, "J'aime les événements sociaux.", False),
            (45, "Je trouve qu'il est difficile de décoder les intentions des autres.", True),
            (46, "Les nouvelles situations me rendent anxieux(se).", True),
            (47, "J'aime rencontrer de nouvelles personnes.", False),
            (48, "Je suis une personne qui a le sens de la diplomatie.", False),
            (49, "Je ne suis pas très doué(e) pour me souvenir des dates de naissance des gens.", False),
            (50, "Je trouve qu'il est très facile de jouer à des jeux de rôle avec des enfants.", False)
        ]
        
        questions = []
        for num, text, agree_scores in items_data:
            question = {
                'id': f'QA{num}',
                'number': num,
                'text': f"{num}. {text}",
                'type': 'select',
                'options': response_options,
                'agree_scores': agree_scores,  # True if agreeing indicates autism trait
                'required': True
            }
            questions.append(question)
        
        return questions
    
    def calculate_score(self, responses: Dict[str, int]) -> Dict[str, Any]:
        """Calculate AQ total score
        
        Scoring: Each item can contribute 0 or 1 point.
        - For items where 'agree_scores' = True: score 1 if response is 1 or 2 (agree)
        - For items where 'agree_scores' = False: score 1 if response is 3 or 4 (disagree)
        
        Total score range: 0-50
        
        Interpretation:
        - 0-25: Low (typical range for general population)
        - 26-31: Borderline (some autistic traits)
        - 32+: High (clinically significant autistic traits - suggests possible ASD)
        
        Average scores:
        - General population: 16.4
        - Asperger/HFA adults: 35.8
        
        Args:
            responses: Dictionary mapping 'QA1'-'QA50' to response values (1-4)
            
        Returns:
            Dictionary with total score and interpretation
        """
        errors = []
        
        # Validate all responses
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses:
                errors.append(f"Item {question['number']} manquant")
            elif responses[q_id] not in [1, 2, 3, 4]:
                errors.append(f"Item {question['number']}: réponse doit être entre 1 et 4")
        
        if errors:
            return {
                'valid': False,
                'errors': errors
            }
        
        # Calculate total score
        total_score = 0
        for question in self.questions:
            q_id = question['id']
            response = responses[q_id]
            
            if question['agree_scores']:
                # Agreeing indicates autistic trait (score if 1 or 2)
                if response in [1, 2]:
                    total_score += 1
            else:
                # Disagreeing indicates autistic trait (score if 3 or 4)
                if response in [3, 4]:
                    total_score += 1
        
        return {
            'total_score': total_score,
            'range': '0-50',
            'interpretation': self._interpret_score(total_score),
            'valid': True,
            'errors': []
        }
    
    def _interpret_score(self, score: int) -> str:
        """Interpret AQ total score"""
        if score < 26:
            return f"Score faible ({score}/50) - Peu de traits autistiques (population générale)"
        elif score < 32:
            return f"Score intermédiaire ({score}/50) - Quelques traits autistiques présents"
        else:
            return f"Score élevé ({score}/50) - Traits autistiques cliniquement significatifs (suggestif d'un TSA)"


# Example usage
if __name__ == "__main__":
    questionnaire = AQQuestionnaire()
    
    # Example: Person with moderate-high autistic traits
    example_responses = {f'QA{i}': 2 if i % 3 == 0 else 3 for i in range(1, 51)}
    
    # Simulate some autistic traits
    example_responses.update({
        'QA2': 1,   # Prefer routine (agree)
        'QA4': 1,   # Absorbed by interests (agree)
        'QA5': 2,   # Notice details (agree)
        'QA7': 2,   # Social communication difficulties (agree)
        'QA9': 1,   # Fascinated by dates (agree)
        'QA12': 1,  # Notice details (agree)
        'QA13': 1,  # Prefer library to party (agree)
        'QA16': 1,  # Strong interests (agree)
        'QA19': 2,  # Fascinated by numbers (agree)
        'QA20': 1,  # Difficulty understanding intentions (agree)
        'QA22': 1,  # Difficulty making friends (agree)
        'QA23': 1,  # Notice patterns (agree)
        'QA26': 2,  # Difficulty with conversation (agree)
        'QA33': 1,  # Difficulty with turn-taking (agree)
        'QA35': 1,  # Difficulty understanding jokes (agree)
        'QA39': 2,  # Repetitive speech (agree)
        'QA41': 1,  # Collecting information (agree)
        'QA42': 1,  # Difficulty with empathy (agree)
        'QA43': 2,  # Need for planning (agree)
        'QA45': 1,  # Difficulty decoding intentions (agree)
        'QA46': 1,  # Anxiety with change (agree)
        # Reverse-scored items (disagree = autistic trait)
        'QA1': 4,   # Don't prefer social activities (disagree)
        'QA3': 4,   # Difficulty with imagination (disagree)
        'QA8': 3,   # Difficulty imagining characters (disagree)
        'QA10': 4,  # Can't follow multiple conversations (disagree)
        'QA11': 4,  # Social situations difficult (disagree)
        'QA14': 4,  # Difficulty inventing stories (disagree)
        'QA15': 4,  # More attracted to objects (disagree)
        'QA17': 4,  # Don't enjoy social chat (disagree)
        'QA27': 4,  # Difficulty reading between lines (disagree)
        'QA31': 4,  # Can't tell if others bored (disagree)
        'QA36': 4,  # Can't decode facial expressions (disagree)
        'QA38': 4,  # Not good at social chat (disagree)
        'QA40': 4,  # Didn't enjoy pretend play (disagree)
        'QA44': 4,  # Don't enjoy social events (disagree)
        'QA47': 4,  # Don't enjoy meeting new people (disagree)
        'QA48': 4,  # Not diplomatic (disagree)
    })
    
    result = questionnaire.calculate_score(example_responses)
    
    print(f"=== AQ - Autism Quotient ===\n")
    print(f"Score Total: {result['total_score']}/{result['range']}")
    print(f"\n{result['interpretation']}\n")
    print(f"Note: Score ≥ 32 suggère des traits autistiques cliniquement significatifs")
    print(f"      Score moyen population générale: 16.4")
    print(f"      Score moyen Asperger/TSA: 35.8")


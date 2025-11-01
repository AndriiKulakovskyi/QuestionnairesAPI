import random
from typing import Any, Dict, List

class ERDQuestionnaire:
    """ERD - Échelle de Ralentissement Dépressif (Widlöcher)
    
    Clinician-rated scale assessing psychomotor retardation in depression.
    
    Structure:
    - 15 items assessing:
      • Motor behavior (1-7): gait, trunk/limb movements, hands, face, speech
      • Cognitive function (8-14): attention, thought processes, time perception, memory, concentration
      • Global assessment (15): overall retardation
    
    Scoring:
    - Each item: 0-4 scale
      0 = Normal
      1 = Slight/possible retardation
      2 = Definite retardation
      3 = Marked retardation
      4 = Severe/extreme retardation
    - Total score: 0-60
    - Item 15 is global assessment (not included in total)
    - Actual total: 0-56 (items 1-14)
    
    Interpretation:
    - 0-10: No retardation
    - 11-20: Mild retardation
    - 21-35: Moderate retardation
    - 36-56: Severe retardation
    
    Clinical Use:
    - Depression severity assessment
    - Psychomotor symptom monitoring
    - Treatment response evaluation
    - Differential diagnosis
    """

    def __init__(self):
        self.name = "ERD - Échelle de Ralentissement Dépressif (Widlöcher)"
        self.description = "Évaluation du ralentissement psychomoteur (clinicien)."
        self.num_items = 15
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 15 ERD items."""
        
        questions = [
            # Motor behavior items
            {
                "id": "ERD1",
                "number": 1,
                "text": "Démarche, foulée (sur un parcours standard)",
                "domain": "motor",
                "options": {
                    "Normale.": 0,
                    "Léger ralentissement dont le caractère pathologique est certain.": 1,
                    "On remarque une seule des particularités suivantes : Manque de souplesse dans la foulée ou le ballant des bras, Le patient traîne les pieds, Foulée d'amplitude normale mais ralentie, Foulée ralentie, à petits pas.": 2,
                    "Plusieurs de ces signes sont nets": 3,
                    "Le patient doit être soutenu pour marcher.": 4
                }
            },
            {
                "id": "ERD2",
                "number": 2,
                "text": "Lenteur et rareté des mouvements : TRONC",
                "domain": "motor",
                "options": {
                    "Mouvements adaptés, normaux en amplitude, souplesse et rythme, le tronc est confortablement calé dans le fauteuil, les épaules dégagées.Attitude et mouvements sont en harmonie avec le discours": 0,
                    "Il existe peut-être un léger \"tassement\" difficile à interpréter.": 1,
                    "Un certain figeage est indiscutable": 2,
                    "Ne mobilise que rarement ses membres, avec lenteur, d'un geste gauche et de faible amplitude ou encore les racines sont figées et seules les mains bougent. Tronc immobile, soit plaqué contre le dossier, soit les épaules tombantes": 3,
                    "Refus de se lever du lit ou complètement figé dans le fauteuil. Aucun mouvement du tronc, aucune mobilité tête-tronc.": 4
                }
            },
            {
                "id": "ERD3",
                "number": 3,
                "text": "Lenteur et rareté des mouvements : MEMBRES",
                "domain": "motor",
                "options": {
                    "Les mouvements des membres sont normaux.": 0,
                    "Peut-être une certaine raideur, une certaine lenteur.": 1,
                    "Mobilité nettement diminuée.": 2,
                    "Rare mobilisation, mouvement gauche ou raide, ou encore bras ou jambes collés au corps ou au fauteuil.": 3,
                    "Membres figés dans une position, refuse de bouger.": 4
                }
            },
            {
                "id": "ERD4",
                "number": 4,
                "text": "Mains et doigts",
                "domain": "motor",
                "options": {
                    "Mouvements adaptés, normaux. Gesticulation accompagnant le discours.": 0,
                    "Diminution de la gesticulation, mains immobiles mais non crispées.": 1,
                    "Mains immobiles, doigts sans souplesse ou crispés.": 2,
                    "Position figée des doigts, mains crispées l'une contre l'autre ou sur les accoudoirs.": 3,
                    "Hypertonicité ou catalepsie.": 4
                }
            },
            {
                "id": "ERD5",
                "number": 5,
                "text": "Traits du visage, mimique, regard",
                "domain": "motor",
                "options": {
                    "Mimique normale, en rapport avec le discours. Regard mobile. Clignements normaux.": 0,
                    "Raideur légère du visage, pauvreté relative de la mimique. Regard peu mobile, raréfaction du clignement.": 1,
                    "Visage figé, atone, inexpressif ou figé dans la tristesse. Regard relativement immobile.": 2,
                    "Traits figés. Regard immobile vide ou perdu dans le vague. Yeux ouverts, rigidité du cou.": 3,
                    "Refus d'ouvrir les yeux ou bien yeux exorbités, rigidité intense, refus de mobiliser la tête.": 4
                }
            },
            {
                "id": "ERD6",
                "number": 6,
                "text": "Voix et débit verbal",
                "domain": "motor",
                "options": {
                    "Voix bien timbrée, débit de parole normal.": 0,
                    "Voix monotone ou débit ralenti.": 1,
                    "Voix atone et monotone, intensité diminuée et/ou débit ralenti.": 2,
                    "Réponses monosyllabiques ou très brèves.": 3,
                    "Mutisme.": 4
                }
            },
            {
                "id": "ERD7",
                "number": 7,
                "text": "Latence des réponses",
                "domain": "motor",
                "options": {
                    "Le patient répond sans délai.": 0,
                    "Latence notée mais de façon incertaine.": 1,
                    "Latence nette.": 2,
                    "Latence prolongée et répétée. Relances indispensables.": 3,
                    "Absence de réponse. Aucune relance n'est efficace.": 4
                }
            },
            # Cognitive function items
            {
                "id": "ERD8",
                "number": 8,
                "text": "Capacité d'attention",
                "domain": "cognitive",
                "options": {
                    "Normale.": 0,
                    "Attention normale lors de l'entretien mais le malade signale des difficultés attentionnelles hors entretien.": 1,
                    "Le malade parvient à maintenir son attention de façon prolongée lors de l'entretien mais se fatigue.": 2,
                    "Difficultés répétées à maintenir son attention sur une question ou un thème donné en cours d'entretien.": 3,
                    "Impossible de fixer l'attention du malade.": 4
                }
            },
            {
                "id": "ERD9",
                "number": 9,
                "text": "Cours de la pensée",
                "domain": "cognitive",
                "options": {
                    "Pas de ralentissement, pas de difficulté pour trouver ses mots.": 0,
                    "Discours très légèrement ralenti.": 1,
                    "Discours ralenti, un peu laborieux, quelques difficultés à trouver ses mots.": 2,
                    "Discours très ralenti, très laborieux, difficultés fréquentes pour trouver ses mots.": 3,
                    "Discours incohérent ou impossible à obtenir.": 4
                }
            },
            {
                "id": "ERD10",
                "number": 10,
                "text": "Contenu de la pensée : degré d'incertitude, indécision",
                "domain": "cognitive",
                "options": {
                    "Pas d'indécision, d'hésitation ou de doutes.": 0,
                    "A du mal à donner une réponse et hésite souvent avant de se décider.": 1,
                    "Besoin fréquent de répéter la question et hésite longuement avant de répondre.": 2,
                    "N'arrive pas à se décider pour donner une réponse, même en répétant la question.": 3,
                    "Ne peut donner aucune réponse malgré les relances.": 4
                }
            },
            {
                "id": "ERD11",
                "number": 11,
                "text": "Capacité d'anticipation, projection dans l'avenir",
                "domain": "cognitive",
                "options": {
                    "Imagination normale du vécu futur.": 0,
                    "Capacité diminuée pour des projets lointains mais conservée pour le proche avenir.": 1,
                    "Difficultés à se projeter même dans un avenir proche.": 2,
                    "Incapacité à imaginer le lendemain.": 3,
                    "Ne peut répondre.": 4
                }
            },
            {
                "id": "ERD12",
                "number": 12,
                "text": "Perception par le malade de l'écoulement du temps présent",
                "domain": "cognitive",
                "options": {
                    "Identique au vécu habituel.": 0,
                    "Le temps présent passe lentement mais ceci tient à l'inactivité, l'hospitalisation...": 1,
                    "Un écoulement plus lent du temps perçu existe mais n'est retrouvé que par un interrogatoire précis.": 2,
                    "Le malade signale spontanément ou facilement un écoulement ralenti du temps présent en réponse à une question directe.": 3,
                    "Le temps présent est suspendu (perception douloureuse d'un présent infini).": 4
                }
            },
            {
                "id": "ERD13",
                "number": 13,
                "text": "Mémoire",
                "domain": "cognitive",
                "options": {
                    "Le sujet affirme ne présenter aucun trouble mnésique, l'expérimentateur n'en retrouve pas à l'interrogatoire.": 0,
                    "Une difficulté mnésique est évoquée par le malade mais difficile à objectiver.": 1,
                    "Le trouble de la mémoire est objectivable (difficulté à se souvenir du repas de la veille...) mais peu gênant.": 2,
                    "Le trouble de la mémoire est décrit comme un handicap (ne retrouve plus ses affaires, oublie qui est venu le voir et quand).": 3,
                    "Véritable amnésie.": 4
                }
            },
            {
                "id": "ERD14",
                "number": 14,
                "text": "Concentration",
                "domain": "cognitive",
                "options": {
                    "Faculté de concentration normale.": 0,
                    "Le malade pense pouvoir se concentrer normalement, mais certaines tâches demandant un effort de concentration, semblent difficiles à réaliser.": 1,
                    "Le malade signale une gêne dans certaines tâches qu'il met sur le compte de ses difficultés de concentration (lecture, calcul, tâches professionnelles...)": 2,
                    "Une difficulté importante de concentration rend impossible la compréhension d'information banales (journal, télévision...).": 3,
                    "Le trouble gêne même l'entretien.": 4
                }
            },
            # Global assessment
            {
                "id": "ERD15",
                "number": 15,
                "text": "Appréciation générale du ralentissement",
                "domain": "global",
                "options": {
                    "Nul.": 0,
                    "Doute.": 1,
                    "Net.": 2,
                    "Important.": 3,
                    "Très grave.": 4
                },
                "note": "Global assessment - not included in total score calculation"
            }
        ]
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate ERD total score.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing total score, domain scores, and interpretation.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        item_scores = {}
        
        # Domain scores (items 1-14 only, not ERD15)
        domains = {
            "motor": 0,
            "cognitive": 0
        }
        
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            response_text = responses[q_id]
            if response_text not in question["options"]:
                raise ValueError(
                    f"Invalid response for question {q_id}. "
                    f"Expected one of the defined options."
                )
            
            score = question["options"][response_text]
            item_scores[q_id] = score
            
            # Add to total (ERD15 is global, not included in total)
            if q_id != "ERD15":
                total_score += score
                domain = question.get("domain")
                if domain in domains:
                    domains[domain] += score

        # ERD15 is the global assessment
        global_assessment = item_scores["ERD15"]
        
        interpretation = self._interpret_score(total_score)
        retardation_level = self._get_retardation_level(total_score)

        return {
            "total_score": total_score,
            "max_score": 56,  # 14 items × 4 points (ERD15 not included)
            "interpretation": interpretation,
            "retardation_level": retardation_level,
            "global_assessment": global_assessment,
            "global_assessment_text": self._interpret_global(global_assessment),
            "domain_scores": domains,
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret ERD total score."""
        if score == 0:
            return "Aucun ralentissement psychomoteur"
        elif score <= 10:
            return "Ralentissement psychomoteur absent ou minimal"
        elif score <= 20:
            return "Ralentissement psychomoteur léger"
        elif score <= 35:
            return "Ralentissement psychomoteur modéré"
        else:
            return "Ralentissement psychomoteur sévère"

    def _get_retardation_level(self, score: int) -> str:
        """Get retardation level."""
        if score == 0:
            return "none"
        elif score <= 10:
            return "minimal"
        elif score <= 20:
            return "mild"
        elif score <= 35:
            return "moderate"
        else:
            return "severe"

    def _interpret_global(self, global_score: int) -> str:
        """Interpret global assessment (ERD15)."""
        interpretations = {
            0: "Nul",
            1: "Doute",
            2: "Net",
            3: "Important",
            4: "Très grave"
        }
        return interpretations.get(global_score, "Unknown")

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "ECHELLE DE RALENTISSEMENT DEPRESSIF (Widlöcher)\n\n"
            "Évaluation par le clinicien du ralentissement psychomoteur observé lors de l'entretien.\n\n"
            "Pour chaque item, coter de 0 à 4 selon l'intensité du ralentissement observé."
        )


if __name__ == '__main__':
    erd = ERDQuestionnaire()
    print(f"Questionnaire: {erd.name}")
    print(f"Number of items: {erd.num_items}")
    print()
    
    # Test: Moderate retardation
    test_responses = {}
    for i in range(1, 16):
        q_id = f"ERD{i}"
        # Get first question for this ID
        question = next(q for q in erd.questions if q["id"] == q_id)
        # Use the second option (score 1) for most items
        options_list = list(question["options"].keys())
        test_responses[q_id] = options_list[2] if len(options_list) > 2 else options_list[1]
    
    result = erd.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Retardation Level: {result['retardation_level']}")
    print(f"Interpretation: {result['interpretation']}")
    print(f"Global Assessment (ERD15): {result['global_assessment']} - {result['global_assessment_text']}")
    print(f"Motor domain: {result['domain_scores']['motor']}")
    print(f"Cognitive domain: {result['domain_scores']['cognitive']}")
    print()
    print("✓ ERD implementation complete - 15 items, psychomotor retardation assessment")


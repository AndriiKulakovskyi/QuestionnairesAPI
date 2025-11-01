import random
from typing import Any, Dict, List

class EQQuestionnaire:
    """EQ - Empathy Quotient
    
    Self-report questionnaire measuring empathy in adults, developed by Baron-Cohen & Wheelwright.
    
    Structure:
    - 60 items total:
      • 21 empathy items (scored)
      • 19 reverse-scored empathy items
      • 20 filler items (not scored)
    
    Scoring:
    - Empathy items: "Strongly Agree" = 2, "Slightly Agree" = 1, else = 0
    - Reverse items: "Strongly Disagree" = 2, "Slightly Disagree" = 1, else = 0
    - Filler items: Not scored
    - Total score: 0-80
    - Clinical cutoffs:
      < 30: Below average empathy (may suggest autism/Asperger's)
      30-52: Average range
      > 52: Above average empathy
    
    Clinical Use:
    - Autism/Asperger's screening
    - Empathy assessment
    - Theory of Mind research
    - Emotional intelligence studies
    """

    def __init__(self):
        self.name = "EQ - Empathy Quotient"
        self.description = "Échelle de quotient d'empathie (Baron-Cohen)."
        self.num_items = 60
        self.used_in_applications = ['asperger']
        
        # Empathy items (1-indexed): score "Strongly/Slightly Agree"
        self.empathy_items = [1, 6, 19, 22, 25, 26, 35, 36, 37, 38, 41, 42, 43, 44, 52, 54, 55, 57, 58, 59, 60]
        
        # Reverse items (1-indexed): score "Strongly/Slightly Disagree"
        self.reverse_items = [4, 8, 10, 11, 12, 14, 15, 18, 21, 27, 28, 29, 32, 34, 39, 46, 48, 49, 50]
        
        # Filler items: 2, 3, 5, 7, 9, 13, 16, 17, 20, 23, 24, 30, 31, 33, 40, 45, 47, 51, 53, 56
        
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 60 EQ items."""
        
        options = {
            "Fortement d'accord": 1,
            "Légèrement d'accord": 2,
            "Légèrement en désaccord": 3,
            "Fortement en désaccord": 4
        }
        
        # All 60 items from the form
        items_text = [
            "Je peux facilement dire si quelqu'un veut engager une conversation avec moi",
            "Je préfère les animaux aux humains",
            "J'essaie de suivre les tendances actuelles et la mode",
            "Je trouve difficile d'expliquer à d'autres des choses que je comprends facilement quand ils ne le comprennent pas du premier coup",
            "Je rêve la plupart des nuits",
            "J'ai vraiment plaisir à prendre soin des autres",
            "J'essaie de résoudre par moi-même mes problèmes plutôt que d'en discuter avec d'autres",
            "J'ai du mal à savoir quoi faire dans une situation sociale",
            "Je suis au meilleur de moi-même le matin",
            "Les gens me disent souvent que j'affirme trop mes opinions lors de discussions",
            "Ca ne me tracasse pas trop si je suis en retard à un rendez-vous avec un ami",
            "Parce que les amitiés et les rapports sociaux sont trop difficiles, je tends à les éviter",
            "Je ne violerai jamais une loi, si mineure soit elle",
            "Je trouve souvent difficile de juger si quelque chose est grossier ou poli",
            "Dans une conversation, je tends à me concentrer sur mes propres pensées plutôt que sur ce que mon interlocuteur pourrait penser",
            "Je préfère les farces aux jeux de mots",
            "Je vis la vie au jour le jour plutôt qu'en me projetant dans l'avenir",
            "Quand j'étais enfant, j'aimais couper des vers de terre pour voir ce qui se passait",
            "Je comprends si quelqu'un dit quelque chose mais veut en dire une autre",
            "Je tends à avoir des opinions très fortes au sujet de la moralité",
            "Il m'est souvent difficile de savoir pourquoi certaines choses dérangent tant les autres personnes",
            "Je trouve facile de me mettre dans la peau de quelqu'un d'autre",
            "Je pense que les bonnes manières sont les choses les plus importantes que les parents peuvent enseigner à leurs enfants",
            "J'aime faire des choses à l'improviste",
            "J'arrive facilement à prédire ce que les gens vont ressentir",
            "Je repère rapidement dans un groupe une personne se sent mal à l'aise",
            "Si je dis quelque chose qui offense quelqu'un, je me dis que c'est son problème pas le mien",
            "Si quelqu'un me demande si j'aime sa coupe de cheveux, je lui réponds franchement même si c'est pour lui dire que je ne l'aime pas",
            "Je ne peux pas toujours comprendre pourquoi une personne s'est sentie offensée par une remarque",
            "Les gens me disent souvent que je suis très imprévisible",
            "J'aime être le centre de l'attention quelque soit la situation",
            "Voir les personnes pleurer ne me dérange pas vraiment",
            "J'aime avoir des discussions au sujet de la politique",
            "Je suis très brusque, ce que certains pourraient prendre pour de l'impolitesse, bien que ce ne soit pas intentionnel de ma part",
            "Je n'ai pas tendance à trouver les situations sociales compliquées",
            "On me dit souvent que je suis bon pour deviner ce que les gens ressentent ou pensent",
            "Quand je parle avec les gens, j'ai tendance à parler plus de leur expérience personnelle que de la mienne",
            "Ça me bouleverse de voir souffrir un animal",
            "Je suis capable de prendre des décisions sans être influencé par les sentiments d'autrui",
            "Je ne peux pas me détendre tant que je n'ai pas fait tout ce que j'avais projeté de faire dans la journée",
            "Je peux facilement dire si quelqu'un est intéressé ou ennuyé par ce que je suis en train de dire",
            "Je suis bouleversé lorsque je vois des gens souffrir aux informations à la télévision",
            "Habituellement mes amis se confient à moi car ils disent que je suis très compréhensif",
            "Je peux sentir si je dérange même si on ne me le dit pas",
            "Je commence souvent de nouveaux passe-temps, mais je m'en lasse rapidement et je passe à autre chose",
            "Les gens me disent que je vais trop loin dans mes taquineries",
            "Je serais trop nerveux pour aller sur de grandes montagnes russes",
            "Certains disent souvent que je suis insensible bien que je ne sache pas toujours pourquoi",
            "Si je vois un étranger dans un groupe, je pense que c'est au groupe de faire un effort pour qu'il se joigne à eux",
            "Je reste habituellement détaché émotionnellement lorsque je regarde film",
            "J'aime être très organisé au quotidien et je fais souvent une liste de choses que j'ai à faire",
            "Je peux facilement et intuitivement percevoir ce que quelqu'un ressent",
            "Je n'aime pas prendre de risque",
            "Je peux aisément comprendre ce dont une autre personne a envie de parler",
            "Je peux dire si quelqu'un masque ses réelles émotions",
            "Avant de prendre une décision, je pèse toujours le pour et le contre",
            "Je ne sais pas comment fonctionnent les règles des situations sociales",
            "Je suis bon pour deviner ce que quelqu'un veut faire",
            "Je tends à me sentir concerné lorsque mes amis ont des problèmes",
            "Je peux habituellement apprécier le point de vue d'autrui, si je ne suis pas d'accord"
        ]
        
        questions = []
        for i in range(1, 61):
            item_type = "empathy" if i in self.empathy_items else ("reverse" if i in self.reverse_items else "filler")
            
            questions.append({
                "id": f"EMPAT{i}",
                "number": i,
                "text": items_text[i-1],
                "type": item_type,
                "options": options
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate EQ total score."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        item_scores = {}
        empathy_score = 0
        reverse_score = 0
        
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            response_text = responses[q_id]
            if response_text not in question["options"]:
                raise ValueError(f"Invalid response for question {q_id}")
            
            response_value = question["options"][response_text]
            score = 0
            
            if question["type"] == "empathy":
                # Score "Strongly Agree" (1) = 2 points, "Slightly Agree" (2) = 1 point
                if response_value == 1:
                    score = 2
                elif response_value == 2:
                    score = 1
                empathy_score += score
            elif question["type"] == "reverse":
                # Score "Strongly Disagree" (4) = 2 points, "Slightly Disagree" (3) = 1 point
                if response_value == 4:
                    score = 2
                elif response_value == 3:
                    score = 1
                reverse_score += score
            # Filler items don't score
            
            item_scores[q_id] = score
            total_score += score

        interpretation = self._interpret_score(total_score)

        return {
            "total_score": total_score,
            "max_score": 80,
            "empathy_items_score": empathy_score,
            "reverse_items_score": reverse_score,
            "interpretation": interpretation,
            "clinical_significance": self._get_clinical_significance(total_score),
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret EQ total score."""
        if score < 30:
            return "Empathie en dessous de la moyenne (peut suggérer TSA)"
        elif score <= 52:
            return "Empathie dans la moyenne"
        else:
            return "Empathie au-dessus de la moyenne"

    def _get_clinical_significance(self, score: int) -> str:
        """Get clinical significance category."""
        if score < 30:
            return "low"
        elif score <= 52:
            return "average"
        else:
            return "high"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Ce questionnaire mesure votre quotient d'empathie.\n"
            "Pour chaque affirmation, indiquez dans quelle mesure vous êtes d'accord:\n"
            "- Fortement d'accord\n"
            "- Légèrement d'accord\n"
            "- Légèrement en désaccord\n"
            "- Fortement en désaccord\n\n"
            "Répondez spontanément sans trop réfléchir."
        )


if __name__ == '__main__':
    eq = EQQuestionnaire()
    print(f"Questionnaire: {eq.name}")
    print(f"Number of items: {eq.num_items}")
    print(f"Empathy items: {len(eq.empathy_items)}")
    print(f"Reverse items: {len(eq.reverse_items)}")
    print()
    
    # Test: Average empathy
    test_responses = {}
    for i in range(1, 61):
        q_id = f"EMPAT{i}"
        # Give mixed responses to simulate average empathy
        if i % 2 == 0:
            test_responses[q_id] = "Légèrement d'accord"
        else:
            test_responses[q_id] = "Légèrement en désaccord"
    
    result = eq.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Empathy items: {result['empathy_items_score']}")
    print(f"Reverse items: {result['reverse_items_score']}")
    print(f"Clinical Significance: {result['clinical_significance']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("✓ EQ implementation complete - 60 items, empathy quotient assessment")


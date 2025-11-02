import unittest

from questionnaires.altman import AltmanQuestionnaire


class AltmanQuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = AltmanQuestionnaire()

    def test_questions_definition(self):
        questions = self.questionnaire.questions
        self.assertEqual(len(questions), 5)

        expected_ids = [f"radhtml_altman{i}" for i in range(1, 6)]
        self.assertListEqual([q['id'] for q in questions], expected_ids)

        first_question = questions[0]
        self.assertEqual(
            first_question['text'],
            "Je ne me sens pas plus heureux(se) ou plus joyeux(se) que d'habitude",
        )
        self.assertEqual(first_question['topic'], 'Humeur euphorique')

        for question in questions:
            self.assertEqual(set(question['options'].keys()), {'a', 'b', 'c', 'd', 'e'})
            self.assertEqual(set(question['options'].values()), {0, 1, 2, 3, 4})
            self.assertEqual(len(question['labels']), 5)

    def test_instructions(self):
        instructions = self.questionnaire.get_instructions()
        self.assertTrue(instructions.startswith("Consignes"))
        self.assertIn("Choisir la proposition", instructions)
        self.assertIn("« Fréquemment » signifie la plupart du temps", instructions)

    def test_calculate_score_all_a(self):
        responses = {
            'radhtml_altman1': 'a',
            'radhtml_altman2': 'a',
            'radhtml_altman3': 'a',
            'radhtml_altman4': 'a',
            'radhtml_altman5': 'a',
        }

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['total_score'], 0)
        self.assertEqual(result['range'], '0-20')
        self.assertEqual(
            result['interpretation'],
            "Score négatif (0/20) - Pas d'hypomanie/manie",
        )

    def test_calculate_score_all_e(self):
        responses = {
            'radhtml_altman1': 'e',
            'radhtml_altman2': 'e',
            'radhtml_altman3': 'e',
            'radhtml_altman4': 'e',
            'radhtml_altman5': 'e',
        }

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['total_score'], 20)
        self.assertEqual(
            result['interpretation'],
            "Score positif (20/20) - Hypomanie/manie probable. Une évaluation clinique approfondie est recommandée.",
        )

    def test_calculate_score_missing_item(self):
        responses = {
            'radhtml_altman1': 'a',
            'radhtml_altman2': 'a',
            'radhtml_altman3': 'a',
            'radhtml_altman4': 'a',
        }

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn("Item 5", " ".join(result['errors']))


if __name__ == '__main__':
    unittest.main()


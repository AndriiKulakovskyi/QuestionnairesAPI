import unittest

from questionnaires.mdq import MDQQuestionnaire


class MDQQuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = MDQQuestionnaire()

    def _all_yes_responses(self):
        responses = {q['id']: 'Oui' for q in self.questionnaire.questions if q['type'] == 'yes_no'}
        responses['rad_mdq3'] = 'Problème moyen'
        return responses

    def test_questions_structure(self):
        questions = self.questionnaire.questions
        self.assertEqual(len(questions), 15)

        first_question = questions[0]
        self.assertEqual(first_question['number'], '1a')
        self.assertIn('Vous vous sentiez si bien', first_question['text'])
        self.assertEqual(first_question['type'], 'yes_no')
        self.assertEqual(first_question['options'], {'Oui': 1, 'Non': 0})

        second_step = questions[-2]
        self.assertEqual(second_step['id'], 'rad_mdq2')
        self.assertEqual(second_step['type'], 'yes_no')

        impairment_question = questions[-1]
        self.assertEqual(impairment_question['id'], 'rad_mdq3')
        self.assertEqual(impairment_question['type'], 'severity')
        self.assertEqual(
            list(impairment_question['options'].keys()),
            ['Pas de problème', 'Problème mineur', 'Problème moyen', 'Problème sérieux'],
        )

    def test_instructions(self):
        instructions = self.questionnaire.get_instructions()
        self.assertTrue(instructions.startswith("Questionnaire « TROUBLE de l'HUMEUR »"))
        self.assertIn('Résultat positif', instructions)

    def test_positive_screen(self):
        responses = self._all_yes_responses()
        # Ensure at least 7 symptoms marked yes (already all yes)
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['symptom_count'], 13)
        self.assertTrue(result['co_occurrence'])
        self.assertEqual(result['impairment_level'], 'Problème moyen')
        self.assertTrue(result['screen_positive'])
        self.assertIn('Dépistage POSITIF', result['interpretation'])

    def test_negative_due_to_symptom_count(self):
        responses = self._all_yes_responses()
        # Flip several symptoms to "Non" to drop below threshold
        low_symptom_ids = [
            'rad_mdq_remonte',
            'rad_mdq_humeur',
            'rad_mdq_assurance',
            'rad_mdq_sommeil',
            'rad_mdq_parler',
            'rad_mdq_pensee',
            'rad_mdq_concentration',
        ]
        for symptom_id in low_symptom_ids:
            responses[symptom_id] = 'Non'

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertLess(result['symptom_count'], 7)
        self.assertFalse(result['screen_positive'])
        self.assertIn('Critères non remplis', result['interpretation'])

    def test_missing_required_response(self):
        responses = self._all_yes_responses()
        responses.pop('rad_mdq2')

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn('Question 2', ' '.join(result['errors']))


if __name__ == '__main__':
    unittest.main()


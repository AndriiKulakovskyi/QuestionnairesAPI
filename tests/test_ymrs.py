import unittest

from questionnaires.ymrs import YMRSQuestionnaire


class YMRSQuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = YMRSQuestionnaire()

    def _all_responses(self, letter: str = 'a') -> dict:
        return {q['id']: letter for q in self.questionnaire.questions}

    def test_question_structure(self):
        questions = self.questionnaire.questions
        self.assertEqual(len(questions), 11)
        self.assertEqual(questions[0]['text'], "Elevation de l'humeur")
        self.assertEqual(set(questions[0]['options'].keys()), {'a', 'b', 'c', 'd', 'e'})
        self.assertEqual(questions[-1]['id'], 'radhtml_ymrs11')

    def test_instructions_present(self):
        instructions = self.questionnaire.get_instructions()
        self.assertIn('Guide pour attribuer des points aux items', instructions)
        self.assertIn('Les descriptions données sont des guides', instructions)

    def test_score_all_minimum(self):
        responses = self._all_responses('a')
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['score'], 0)
        self.assertEqual(result['interpretation'], 'Euthymie')

    def test_double_weight_items(self):
        responses = self._all_responses('a')
        responses['radhtml_ymrs5'] = 'd'  # base 3 -> doubled to 6

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['score'], 6)

    def test_score_all_maximum(self):
        responses = self._all_responses('e')
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['score'], 60)
        self.assertEqual(result['interpretation'], 'Episode maniaque')

    def test_validation_missing_item(self):
        responses = self._all_responses('b')
        responses.pop('radhtml_ymrs3')

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn("L'item 3", ' '.join(result['errors']))

    def test_validation_invalid_letter(self):
        responses = self._all_responses('a')
        responses['radhtml_ymrs2'] = 'z'

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn('Valeur invalide pour l\'item 2', result['errors'])


if __name__ == '__main__':
    unittest.main()


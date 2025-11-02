import unittest

from questionnaires.madrs import MADRSQuestionnaire


class MADRSQuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = MADRSQuestionnaire()

    def _all_scores(self, value: int) -> dict:
        return {question['id']: value for question in self.questionnaire.questions}

    def test_questions_structure(self):
        questions = self.questionnaire.questions
        self.assertEqual(len(questions), 10)

        first_question = questions[0]
        self.assertEqual(first_question['number'], 1)
        self.assertTrue(first_question['text'].startswith('Tristesse apparente'))
        self.assertEqual(first_question['type'], 'radio')
        self.assertEqual(set(first_question['options'].keys()), set(range(7)))

        last_question = questions[-1]
        self.assertEqual(last_question['id'], 'MADRS10')
        self.assertIn('Idées de suicide', last_question['text'])
        self.assertEqual(set(last_question['options'].keys()), set(range(7)))

    def test_instructions(self):
        instructions = self.questionnaire.get_instructions()
        self.assertTrue(instructions.startswith('CONSIGNES'))
        self.assertIn("Cocher pour chaque item", instructions)

    def test_calculate_score_all_zero(self):
        responses = self._all_scores(0)
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['score'], 0)
        self.assertEqual(result['interpretation'], 'Absence de dépression ou rémission')

    def test_calculate_score_moderate(self):
        responses = self._all_scores(3)
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        # 10 items * score 3 each = 30
        self.assertEqual(result['score'], 30)
        self.assertEqual(result['interpretation'], 'Dépression modérée')

    def test_interpretation_severe(self):
        responses = self._all_scores(6)
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['score'], 60)
        self.assertEqual(result['interpretation'], 'Dépression sévère')

    def test_validation_missing_item(self):
        responses = self._all_scores(1)
        responses.pop('MADRS5')

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn("L'item 5", ' '.join(result['errors']))

    def test_validation_invalid_value(self):
        responses = self._all_scores(1)
        responses['MADRS1'] = 7

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn('Valeur invalide pour l\'item 1', result['errors'])


if __name__ == '__main__':
    unittest.main()


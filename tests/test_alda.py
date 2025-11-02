import unittest

from questionnaires.alda import AldaScaleQuestionnaire


class AldaScaleQuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = AldaScaleQuestionnaire()

    def _base_responses(self) -> dict:
        responses = {
            "ALDA_ON_LITHIUM": "Oui",
            "ALDA_A": 8,
            "ALDA_B1": 0,
            "ALDA_B2": 1,
            "ALDA_B3": 1,
            "ALDA_B4": 0,
            "ALDA_B5": 0,
        }
        return responses

    def test_screening_question_defined(self):
        screening = self.questionnaire.screening_question
        self.assertEqual(screening['id'], 'ALDA_ON_LITHIUM')
        self.assertEqual(screening['type'], 'yes_no')
        self.assertEqual(set(screening['options'].keys()), {'Oui', 'Non'})

    def test_instructions_mentions_screening_and_criteria(self):
        instructions = self.questionnaire.get_instructions()
        self.assertIn('Le patient est-il actuellement traité par lithium', instructions)
        self.assertIn('Le critère B est utilisé pour établir', instructions)

    def test_calculate_score_valid(self):
        responses = self._base_responses()
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['score_a'], 8)
        self.assertEqual(result['score_b'], 2)
        self.assertEqual(result['total_score'], 6)
        self.assertEqual(result['response_category'], 'Réponse partielle')

    def test_calculate_score_non_treated_returns_invalid(self):
        responses = self._base_responses()
        responses['ALDA_ON_LITHIUM'] = 'Non'

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIsNone(result['total_score'])
        self.assertIn('n\'est pas actuellement traité par lithium', ' '.join(result['errors']))

    def test_calculate_score_missing_values(self):
        responses = self._base_responses()
        responses.pop('ALDA_B3')

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn('ALDA_B3', ' '.join(result['errors']))

    def test_calculate_score_invalid_a(self):
        responses = self._base_responses()
        responses['ALDA_A'] = 11

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn('critère a', ' '.join(result['errors']).lower())

    def test_random_responses_include_screening(self):
        responses = self.questionnaire.get_random_responses()
        self.assertIn('ALDA_ON_LITHIUM', responses)
        self.assertEqual(responses['ALDA_ON_LITHIUM'], 'Oui')


if __name__ == '__main__':
    unittest.main()


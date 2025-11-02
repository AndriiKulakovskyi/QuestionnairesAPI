import copy
import unittest

from questionnaires.qids_sr16 import QIDSSR16Questionnaire


class QIDSSR16QuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = QIDSSR16Questionnaire()

    def _base_responses(self) -> dict:
        responses = {f'QIDS{i}': 0 for i in range(1, 17)}
        # Ensure optional paired items are present
        responses['QIDS6'] = 0
        responses['QIDS7'] = 0
        responses['QIDS8'] = 0
        responses['QIDS9'] = 0
        return responses

    def test_question_count_and_structure(self):
        questions = self.questionnaire.questions
        self.assertEqual(len(questions), 16)
        self.assertEqual(questions[0]['text'], 'Endormissement')
        self.assertEqual(questions[0]['number'], 1)
        option_sample = questions[0]['options']
        self.assertIn(0, option_sample)
        self.assertTrue(option_sample[0].startswith('a '))

    def test_instructions(self):
        instructions = self.questionnaire.get_instructions()
        self.assertTrue(instructions.startswith('Consignes'))
        self.assertIn('Les réponses sont exclusives les unes des autres.', instructions)

    def test_validate_responses_requires_appetite_and_weight(self):
        responses = self._base_responses()
        # Remove appetite/weight pairs to trigger validation errors
        responses.pop('QIDS6')
        responses.pop('QIDS7')
        responses.pop('QIDS8')
        responses.pop('QIDS9')

        validation = self.questionnaire.validate_responses(responses)
        self.assertFalse(validation['valid'])
        self.assertIn('Au moins un des items 6 (Diminution de l\'appétit) ou 7 (Augmentation de l\'appétit) doit être renseigné', validation['errors'])
        self.assertIn('Au moins un des items 8 (Perte de poids) ou 9 (Prise de poids) doit être renseigné', validation['errors'])

    def test_calculate_score_all_zero(self):
        responses = self._base_responses()

        result = self.questionnaire.calculate_score(copy.deepcopy(responses))

        self.assertTrue(result['valid'])
        self.assertEqual(result['score'], 0)
        self.assertEqual(result['interpretation'], 'Absence de dépression')
        self.assertEqual(result['subscores']['sleep'], 0)
        self.assertEqual(result['subscores']['weight'], 0)
        self.assertEqual(result['subscores']['psychomotor'], 0)

    def test_calculate_score_official_domains(self):
        responses = {
            'QIDS1': 1,
            'QIDS2': 2,
            'QIDS3': 0,
            'QIDS4': 3,
            'QIDS5': 1,
            'QIDS6': 2,
            'QIDS7': 1,
            'QIDS8': 0,
            'QIDS9': 3,
            'QIDS10': 2,
            'QIDS11': 1,
            'QIDS12': 3,
            'QIDS13': 2,
            'QIDS14': 1,
            'QIDS15': 0,
            'QIDS16': 2,
        }

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['score'], 18)
        self.assertEqual(result['interpretation'], 'Dépression sévère')
        self.assertEqual(result['subscores']['sleep'], 3)
        self.assertEqual(result['subscores']['weight'], 3)
        self.assertEqual(result['subscores']['psychomotor'], 2)
        self.assertEqual(result['subscores']['depressed_mood'], 1)
        self.assertEqual(result['subscores']['concentration'], 2)
        self.assertEqual(result['subscores']['guilt'], 1)
        self.assertEqual(result['subscores']['suicidal_ideation'], 3)

    def test_calculate_score_handles_missing_optional_pair(self):
        responses = self._base_responses()
        responses['QIDS6'] = 3
        responses.pop('QIDS7')

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['subscores']['weight'], 3)


if __name__ == '__main__':
    unittest.main()


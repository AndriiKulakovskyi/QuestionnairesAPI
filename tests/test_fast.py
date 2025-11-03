import unittest

from questionnaires.fast import FASTQuestionnaire


class FASTQuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = FASTQuestionnaire()

    def _responses_with_value(self, label: str) -> dict:
        return {item['id']: label for item in self.questionnaire.get_all_items()}

    def test_instructions_present(self):
        instructions = self.questionnaire.get_instructions()
        self.assertIn('Consignes', instructions)
        self.assertIn('score total ≥ 12', instructions)

    def test_scores_all_zero(self):
        responses = self._responses_with_value('Aucune difficulté')
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['total_score'], 0)
        self.assertFalse(result['functional_impairment'])
        for domain in result['domain_scores'].values():
            self.assertEqual(domain['score'], 0)

    def test_scores_all_severe(self):
        responses = self._responses_with_value('Difficulté sévère')
        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['total_score'], 72)
        self.assertTrue(result['functional_impairment'])
        self.assertIn('Dysfonctionnement fonctionnel sévère', result['interpretation'])

    def test_relations_domain_sum(self):
        responses = self._responses_with_value('Aucune difficulté')
        relations_ids = [
            'rad_relations_conserve',
            'rad_relations_participe',
            'rad_relations_bonnes',
            'rad_relations_habiter',
            'rad_relations_sexualite',
            'rad_relations_interet',
        ]
        for item_id in relations_ids:
            responses[item_id] = 'Difficulté modérée'

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        relations_score = result['domain_scores']['Relations Interpersonnelles']['score']
        self.assertEqual(relations_score, len(relations_ids) * 2)

    def test_missing_item_returns_errors(self):
        responses = self._responses_with_value('Aucune difficulté')
        responses.pop(next(iter(responses)))

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertGreater(len(result['errors']), 0)


if __name__ == '__main__':
    unittest.main()


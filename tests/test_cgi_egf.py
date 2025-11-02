import unittest

from questionnaires.cgi_egf import CGIEGFQuestionnaire


class CGIEGFQuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = CGIEGFQuestionnaire()

    def test_instructions_contains_sections(self):
        instructions = self.questionnaire.get_instructions()
        self.assertIn('CGI - 1ère partie', instructions)
        self.assertIn('CGI - 2ème partie', instructions)
        self.assertIn('Index thérapeutique', instructions)
        self.assertIn('EGF - Consignes', instructions)

    def test_calculate_score_valid(self):
        responses = {
            'radhtml_cgi_1': '4',
            'egf_score': '75',
            'radhtml_cgi_2': '2',
            'rad_cgi_3_effet_therapeutique': 'Modéré',
            "rad_cgi_3_effet_secondaire": "N'interfèrent pas significativement avec le fonctionnement du patient",
        }

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertEqual(result['cgi_severity'], 4)
        self.assertEqual(result['cgi_improvement'], 2)
        self.assertEqual(result['egf_score'], 75)
        self.assertEqual(result['therapeutic_index']['index_value'], 6)

    def test_missing_severity_invalid(self):
        responses = {
            'egf_score': '58'
        }

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn('CGI-S manquant', ' '.join(result['errors']))

    def test_egf_out_of_range(self):
        responses = {
            'radhtml_cgi_1': '3',
            'egf_score': '150'
        }

        result = self.questionnaire.calculate_score(responses)

        self.assertFalse(result['valid'])
        self.assertIn('EGF doit être compris entre 1 et 100', result['errors'])

    def test_therapeutic_index_non_evalue(self):
        responses = {
            'radhtml_cgi_1': '2',
            'rad_cgi_3_effet_therapeutique': 'Non évalué',
            "rad_cgi_3_effet_secondaire": "Aucun",
        }

        result = self.questionnaire.calculate_score(responses)

        self.assertTrue(result['valid'])
        self.assertIsNone(result['therapeutic_index']['index_value'])
        self.assertEqual(result['therapeutic_index']['interpretation'], 'Index non évalué')


if __name__ == '__main__':
    unittest.main()


import unittest

from questionnaires.wais4 import WAIS4Test


class WAIS4TestTests(unittest.TestCase):
    def setUp(self):
        self.assessment = WAIS4Test()

    def test_matrices_raw_and_standard(self):
        scores = [1] * 26
        result = self.assessment.calculate_matrices(scores, standard_score=12)
        self.assertEqual(result['raw_total'], 26)
        self.assertAlmostEqual(result['z_score'], round((12 - 10) / 3, 2))

    def test_processing_speed(self):
        result = self.assessment.calculate_processing_speed(
            code_correct=70,
            code_incorrect=3,
            symbol_correct=60,
            symbol_incorrect=1,
            code_standard=11,
            symbol_standard=9,
        )
        self.assertEqual(result['code']['raw_total'], 70)
        self.assertEqual(result['symboles']['raw_total'], 60)
        self.assertEqual(result['composite']['standard_sum'], 20)

    def test_digit_span(self):
        forward = [(1, 1)] * 8
        backward = [(1, 0)] * 8
        sequencing = [(0, 0)] * 8
        result = self.assessment.calculate_digit_span(forward, backward, sequencing)
        self.assertEqual(result['forward']['raw_total'], 16)
        self.assertEqual(result['backward']['raw_total'], 8)
        self.assertEqual(result['total_raw'], 24)
        self.assertIsNotNone(result['span_difference'])

    def test_cobra(self):
        responses = [3] * 16
        result = self.assessment.calculate_cobra(responses)
        self.assertEqual(result['total'], 48)
        self.assertIn('sévères', result['interpretation'])

    def test_cvlt_learning(self):
        raw = {
            'rappel1': 5,
            'rappel2': 7,
            'rappel3': 9,
            'rappel4': 10,
            'rappel5': 11,
            'rappel_libre_court': 8,
            'primacy': 0.6,
            'recency': 0.5,
        }
        result = self.assessment.calculate_cvlt(raw)
        self.assertEqual(result['total_learning'], 42)
        self.assertEqual(result['learning_slope'], 6)

    def test_trail_making_difference(self):
        data = {
            'time_a': 30.5,
            'time_b': 75.0,
            'errors_a_corrected': 1,
            'errors_b_corrected': 3,
        }
        result = self.assessment.calculate_trail_making(data)
        self.assertAlmostEqual(result['difference']['time_b_minus_a'], 44.5)
        self.assertEqual(result['difference']['errors_b_minus_a'], 2)

    def test_stroop_structure(self):
        plates = {
            'plate_a': {'raw': 90, 'age_corrected': 95},
            'plate_b': {'raw': 80, 'age_corrected': 85},
            'plate_c': {'raw': 60, 'age_corrected': 70},
            'interference': {'t_score': 45},
        }
        result = self.assessment.calculate_stroop(plates)
        self.assertEqual(result['plate_a']['raw_total'], 90)
        self.assertEqual(result['interference']['t_score'], 45)

    def test_fluences_summary(self):
        letter = {
            'total_correct': 18,
            'percentile': 40,
            'z_score': -0.5,
        }
        category = {
            'total_correct': 22,
            'percentile': 55,
            'z_score': 0.1,
        }
        result = self.assessment.calculate_fluences(letter, category)
        self.assertEqual(result['letter']['total_correct'], 18)
        self.assertEqual(result['category']['percentile'], 55)

    def test_scip_summary(self):
        subtests = {
            'memoire_verbale': {'raw': 24, 'z': 0.5},
            'memoire_travail': {'raw': 18, 'z': -0.8},
        }
        result = self.assessment.calculate_scip(subtests)
        self.assertEqual(result['memoire_travail']['raw_total'], 18)


if __name__ == '__main__':
    unittest.main()


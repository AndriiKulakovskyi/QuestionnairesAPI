import unittest

from questionnaires.wais3 import WAIS3Test


class WAIS3TestTests(unittest.TestCase):
    def setUp(self):
        self.assessment = WAIS3Test()

    def test_vocabulaire_total(self):
        scores = [2] * 33
        result = self.assessment.calculate_vocabulary(scores, standard_score=11)
        self.assertEqual(result['raw_total'], 66)
        self.assertAlmostEqual(result['z_score'], round((11 - 10) / 3, 2))

    def test_matrices(self):
        result = self.assessment.calculate_matrices([1] * 26)
        self.assertEqual(result['raw_total'], 26)
        self.assertAlmostEqual(result['completion_rate'], 1.0)

    def test_processing_speed(self):
        result = self.assessment.calculate_processing_speed(
            code_correct=80,
            code_incorrect=4,
            symbol_correct=70,
            symbol_incorrect=2,
            code_standard=12,
            symbol_standard=10,
        )
        self.assertEqual(result['code']['raw_total'], 80)
        self.assertEqual(result['composite']['standard_sum'], 22)

    def test_digit_span(self):
        forward = [(1, 1)] * 8
        backward = [(1, 0)] * 8
        result = self.assessment.calculate_digit_span(forward, backward)
        self.assertEqual(result['forward']['raw_total'], 16)
        self.assertEqual(result['backward']['raw_total'], 8)
        self.assertIsNotNone(result['span_difference'])

    def test_cobra(self):
        responses = [0, 1, 2, 3] * 4
        result = self.assessment.calculate_cobra(responses)
        self.assertEqual(result['total'], sum(responses))

    def test_cvlt_learning(self):
        raw = {
            'rappel1': 5,
            'rappel2': 6,
            'rappel3': 7,
            'rappel4': 8,
            'rappel5': 10,
            'rappel_libre_court': 7,
            'primacy': 0.4,
            'recency': 0.5,
        }
        result = self.assessment.calculate_cvlt(raw)
        self.assertEqual(result['total_learning'], 36)
        self.assertEqual(result['learning_slope'], 5)

    def test_trail_making(self):
        data = {
            'time_a': 32,
            'time_b': 80,
            'errors_a_corrected': 0,
            'errors_b_corrected': 2,
        }
        result = self.assessment.calculate_trail_making(data)
        self.assertEqual(result['difference']['time_b_minus_a'], 48)
        self.assertEqual(result['difference']['errors_b_minus_a'], 2)

    def test_stroop(self):
        plates = {
            'plate_a': {'raw': 85},
            'plate_b': {'raw': 75},
            'plate_c': {'raw': 60},
            'interference': {'t_score': 42},
        }
        result = self.assessment.calculate_stroop(plates)
        self.assertEqual(result['plate_a']['raw_total'], 85)
        self.assertEqual(result['interference']['t_score'], 42)

    def test_fluences(self):
        letter = {'total_correct': 20, 'percentile': 40}
        category = {'total_correct': 24, 'percentile': 55}
        result = self.assessment.calculate_fluences(letter, category)
        self.assertEqual(result['letter']['total_correct'], 20)
        self.assertEqual(result['category']['percentile'], 55)

    def test_scip(self):
        subtests = {
            'memoire_verbale': {'raw': 24, 'z': 0.2},
            'fluence': {'raw': 18, 'z': -0.4},
        }
        result = self.assessment.calculate_scip(subtests)
        self.assertEqual(result['fluence']['raw_total'], 18)


if __name__ == '__main__':
    unittest.main()


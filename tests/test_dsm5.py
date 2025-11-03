import unittest

from questionnaires.dsm5 import DSM5Questionnaire


class DSM5QuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = DSM5Questionnaire()

    def _find_field(self, section_id: str, field_id: str):
        for section in self.questionnaire.get_sections():
            if section["id"] != section_id:
                continue
            for field in section["fields"]:
                if field["field"] == field_id:
                    return field
        self.fail(f"Field {field_id} not found in section {section_id}")

    def test_mood_section_contains_expected_field(self):
        field = self._find_field("mood_disorders", "rad_tbhum_existe")
        self.assertEqual(field["type"], "enum")
        self.assertIn("Oui", field["options"])

    def test_diva_scoring_reaches_threshold(self):
        responses = {"rad_diva": "Oui"}
        for i in range(1, 10):
            responses[f"rad_divadul_a{i}"] = "Oui" if i <= 6 else "Non"
            responses[f"rad_divaenf_a{i}"] = "Oui" if i <= 6 else "Non"
            responses[f"rad_divadul_hi{i}"] = True if i <= 7 else False
            responses[f"rad_divaenf_hi{i}"] = True if i <= 7 else False

        result = self.questionnaire.calculate_diva_scores(responses)

        self.assertTrue(result["valid"])
        inattention = result["domains"]["inattention"]
        self.assertEqual(inattention["contexts"]["adult"]["score"], 6)
        self.assertTrue(inattention["contexts"]["adult"]["meets_threshold"])
        self.assertTrue(inattention["meets_domain_threshold"])
        hyper = result["domains"]["hyperactivity_impulsivity"]
        self.assertEqual(hyper["contexts"]["adult"]["score"], 7)
        self.assertTrue(result["summary"]["meets_combined"])

    def test_diva_scoring_reports_missing_and_invalid(self):
        responses = {
            "rad_divadul_a1": "Oui",
            "rad_divadul_a2": "peut-être",
        }

        result = self.questionnaire.calculate_diva_scores(responses)

        self.assertFalse(result["valid"])
        self.assertTrue(any("missing" in error for error in result["errors"]))
        self.assertTrue(any("invalid" in error for error in result["errors"]))

    def test_calculate_score_wraps_diva_result(self):
        responses = {}
        wrapped = self.questionnaire.calculate_score(responses)
        self.assertIn("diva", wrapped)
        self.assertIn("valid", wrapped)


if __name__ == "__main__":
    unittest.main()


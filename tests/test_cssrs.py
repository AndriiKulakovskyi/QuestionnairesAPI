import unittest

from questionnaires.cssrs import CSSRSQuestionnaire


class CSSRSQuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.questionnaire = CSSRSQuestionnaire()

    def test_sections_structure(self):
        sections = self.questionnaire.get_sections()
        self.assertTrue(sections)
        section_ids = [section["id"] for section in sections]
        self.assertIn("ideation", section_ids)
        self.assertIn("intensity", section_ids)

    def test_cssrs1_definition(self):
        cssrs1 = next(q for q in self.questionnaire.questions if q["id"] == "CSSRS1")
        self.assertEqual(cssrs1["section"], "ideation")
        self.assertEqual(cssrs1["type"], "single_choice")
        option_labels = [option["label"] for option in cssrs1["options"]]
        self.assertIn("Oui", option_labels)
        self.assertIn("Non", option_labels)

    def test_intensity_frequency_options(self):
        cssrs8 = next(q for q in self.questionnaire.questions if q["id"] == "CSSRS8")
        values = {option["value"] for option in cssrs8["options"]}
        self.assertEqual(values, {1, 2, 3, 4, 5})
        labels = {option["label"] for option in cssrs8["options"]}
        self.assertIn("Moins d'une fois par semaine", labels)
        self.assertIn("Plusieurs fois par jour", labels)

    def test_summarize_positive_ideation(self):
        responses = {
            "CSSRS1": 0,
            "CSSRS2": 1,
            "CSSRS3": 1,
            "CSSRS4": 0,
            "CSSRS5": 0,
            "CSSRS8": 3,
            "CSSRS9": 2,
            "CSSRS10": 4,
            "CSSRS11": 2,
            "CSSRS12": 4,
            "CSSRS13": 0,
            "CSSRS15": 0,
            "CSSRS16": 0,
            "CSSRS20": 0,
            "CSSRS21": 0,
        }
        summary = self.questionnaire.summarize(responses)
        self.assertTrue(summary["valid"])
        highest = summary["ideation"]["highest_positive_item"]
        self.assertIsNotNone(highest)
        self.assertEqual(highest["level"], 3)
        intensity = summary["ideation"]["intensity"]["frequency"]
        self.assertEqual(intensity["code"], 3)


if __name__ == "__main__":
    unittest.main()


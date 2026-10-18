
import unittest

from src.modules.market_minds import generate_marketing_plan
from src.modules.skill_bridge import generate_career_roadmap
from src.modules.opportunity_connector import suggest_opportunities


class TestMarketBridgeAI(unittest.TestCase):

    def test_marketing_plan(self):
        result = generate_marketing_plan(
            "Bakery", "Students and families", "Increase sales"
        )
        self.assertEqual(result["business"], "Bakery")
        self.assertTrue(len(result["actions"]) > 0)
        self.assertTrue(len(result["content_calendar"]) > 0)

    def test_career_roadmap(self):
        result = generate_career_roadmap(
            "Python, HTML", "Software Developer", "Beginner"
        )
        self.assertIn("Python", result["skills"])
        self.assertTrue(len(result["roadmap"]) > 0)

    def test_opportunity_suggestions(self):
        result = suggest_opportunities(
            "Online ordering website", "Python, web development"
        )
        self.assertIn("Python", result["skills"])
        self.assertTrue(len(result["project_ideas"]) > 0)

    def test_empty_marketing_input(self):
        with self.assertRaises(ValueError):
            generate_marketing_plan("", "Customers", "Increase sales")

    def test_empty_career_input(self):
        with self.assertRaises(ValueError):
            generate_career_roadmap("", "Software Developer", "Beginner")

    def test_empty_opportunity_input(self):
        with self.assertRaises(ValueError):
            suggest_opportunities("", "Python")


if __name__ == "__main__":
    unittest.main()

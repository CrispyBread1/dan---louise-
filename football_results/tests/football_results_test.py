import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    # Test we get the right result string for a final score dictionary representing -
    def setUp(self):
        self.result_1 = {"home_team": 0, "away_team": 1}
        self.result_2 = {"home_team": 1, "away_team": 0}
        self.result_3 = {"home_team": 1, "away_team": 1}
        # Home win
        # Away win
        # Draw

    def test_away_win(self):
        announcement = score_anouncer(self.result_1)
        self.assertEqual("Away Win", announcement)

    def test_home_win(self):
        announcement = score_anouncer(self.result_2)
        self.assertEqual("Home Win", announcement)

    def test_draw(self):
        announcement = score_anouncer(self.result_3)
        self.assertEqual("Draw", announcement)


    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_get_results(self):
        list_results = [self.result_1, self.result_2, self.result_3]
        announcemnt = get_results(list_results)
        self.assertEqual(["Away Win", "Home Win", "Draw"], announcemnt)

if __name__ == "__main__":
    unittest.main()

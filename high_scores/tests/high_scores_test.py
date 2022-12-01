import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.score_list = [100, 0, 90, 30, 60, 5, 90]
        self.score_list_two = [80, 95]
        self.score_list_three = [90]
    # Test latest score (the last thing in the list)
    # def test_latest_score(self):
    #     latest_score = get_latest_score(self.score_list)
    #     self.assertEqual(95, latest_score)
    
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        highest_score = personal_best(self.score_list)
        self.assertEqual(100, int(highest_score))

    # # Test top three from list of scores
    # def test_top_three_scores(self):
    #     three_list = top_three_scores(self.score_list)
    #     self.assertEqual([100, 95, 90], three_list)
    # Test ordered from highest tp lowest
    # def test_sort_scores(self):
    #     sort_scores(self.score_list)
    #     self.assertEqual([100, 95, 90, 60, 30, 5, 0], self.score_list)

    # Test top three when there is a tie
    # def test_top_three_when_tied(self):
    #     three_list = top_three_scores(self.score_list)
    #     self.assertEqual([100, 90, 90], three_list)
    # Test top three when there are less than three
    def test_top_three_when_less_than_three_scores(self):
        top_scores = top_three_scores(self.score_list_two)
        self.assertEqual([95, 80], top_scores)
    
    # Test top three when there is only one
    def test_top_three_when_one_score(self):
        top_scores = top_three_scores(self.score_list_three)
        self.assertEqual([90], top_scores)

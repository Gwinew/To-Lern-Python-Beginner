import unittest

from tennis import score_tennis

class TennisTest(unittest.TotalCase):

    def test_score_tennis(self):
        expected_score = "Love-All"
        player1_points = 0
        player2_points = 0
        test_cases = [
            (0,0, "Love-All"),
            (1,1, "Fifteen-All"),
            (2,2, "Thirty-All"),
            (2,1, "Thirty-Fifteen"),
            (3,1, "Forty-Fifteen"),
            (4,3, "Advantage Player 1")             # correct that
        ]
        for player1_points, player2_points, expected_score in test_cases:
            with self.subTest(f"{player1_points}, {player2_points} -> {expected_score}"):
                self.assertEqual(expected_score, score_tennis(player1_points, player2_points))


"""
in cmd:

coverage run -m unittest

coverage html
____________

pytest --cov-report html:cov_html --cov=tennis .
"""

# _____________
"""
Branch Coverage:

pytest --cov-report html:cov_html --cov-branch --cov=tennis .

Yellow - Conditional
Green - Statements executed when True
Red - Statement executed when False

Use Branch coverage but this is not 100% coverage is no guarantee
""""

from tennis import score_tennis

class TennisTest(unittest.TotalCase):

    def test_score_tennis(self):
        expected_score = "Love-All"
        player1_points = 0
        player2_points = 0
        test_cases = [
            (0,0, "Love-All"),
            (1,1, "Fifteen-All"),
            (2,2, "Thirty-All"),
            (2,1, "Thirty-Fifteen"),
            (3,1, "Forty-Fifteen"),
            (4,3, "Advantage Player 1"),
            (4,5, "Advantage Player 2"),
        ]
        for player1_points, player2_points, expected_score in test_cases:
            with self.subTest(f"{player1_points}, {player2_points} -> {expected_score}"):
                self.assertEqual(expected_score, score_tennis(player1_points, player2_points))


from unittest import TestCase

from src.DiceProject.DiceProject import get_winner_dice, count_wins, find_the_best_dice, compute_strategy


class TestDiceProject(TestCase):

    def test_given_dices_equals(self):
        given_dice1 = [1, 2, 3, 4, 5, 6]
        given_dice2 = [1, 2, 3, 4, 5, 6]
        self.assertEqual((15, 15), count_wins(given_dice1, given_dice2))

    def test_given_dice1_is_slightly_greater_than_dice2(self):
        given_dice1 = [1, 1, 1, 1, 1, 2]
        given_dice2 = [1, 1, 1, 1, 1, 1]
        self.assertEqual((6, 0), count_wins(given_dice1, given_dice2))

    def test_given_dice2_is_greater_than_dice1(self):
        given_dice1 = [1, 1, 6, 6, 8, 8]
        given_dice2 = [2, 2, 4, 4, 9, 9]
        self.assertEqual((16, 20), count_wins(given_dice1, given_dice2))

    def test_given_dice1_is_greater_than_dice2(self):
        given_dice1 = [2, 2, 4, 4, 9, 9]
        given_dice2 = [1, 1, 6, 6, 8, 8]
        self.assertEqual((20, 16), count_wins(given_dice1, given_dice2))

    def test_given_dices_ties(self):
        given_dice1 = [1, 2, 3, 4, 5, 6]
        given_dice2 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(-1, get_winner_dice(given_dice1, given_dice2))

    def test_given_dice1_wins_slightly(self):
        given_dice1 = [1, 1, 1, 1, 1, 2]
        given_dice2 = [1, 1, 1, 1, 1, 1]
        self.assertEqual(0, get_winner_dice(given_dice1, given_dice2))

    def test_given_dice2_wins(self):
        given_dice1 = [1, 1, 6, 6, 8, 8]
        given_dice2 = [2, 2, 4, 4, 9, 9]
        self.assertEqual(1, get_winner_dice(given_dice1, given_dice2))

    def test_given_dice1_wins(self):
        given_dice1 = [2, 2, 4, 4, 9, 9]
        given_dice2 = [1, 1, 6, 6, 8, 8]
        self.assertEqual(0, get_winner_dice(given_dice1, given_dice2))

    def test_given_dices_there_is_not_a_best(self):
        given_dices = [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
        self.assertEqual(-1, find_the_best_dice(given_dices))

    def test_given_dices_dice2_is_the_best(self):
        given_dices = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
        self.assertEqual(2, find_the_best_dice(given_dices))

    def test_given_dices_there_is_not_a_best_again(self):
        given_dices = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
        self.assertEqual(-1, find_the_best_dice(given_dices))

    def test_given_dices_there_is_madness(self):
        given_dices = [[3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3], [4, 3, 3, 3, 3, 3], [2, 3, 3, 3, 3, 3]]
        self.assertEqual(2, find_the_best_dice(given_dices))

    def test_given_dices_the_strategy_is_first_pick_dice_1(self):
        given_dices = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
        self.assertEqual({'choose_first': True, 'first_dice': 1}, compute_strategy(given_dices))

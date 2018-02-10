from unittest import TestCase

from src.Puzzle15.Puzzle15 import Puzzle15


class TestPuzzle15(TestCase):
    def test_is_odd_permutation(self):
        puzzle15 = Puzzle15()
        self.assertFalse(puzzle15.is_even_permutation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 14, 13]))

    def test_is_odd_permutation2(self):
        puzzle15 = Puzzle15()
        self.assertFalse(puzzle15.is_even_permutation([5, 1, 8, 4, 9, 6, 3, 11, 10, 2, 15, 7, 13, 14, 12]))

    def test_is_odd_permutation3(self):
        puzzle15 = Puzzle15()
        self.assertFalse(puzzle15.is_even_permutation(list(range(1, 30)) + [32, 31]))

    def test_is_even_permutation(self):
        puzzle15 = Puzzle15()
        self.assertTrue(puzzle15.is_even_permutation([2, 6, 3, 4, 9, 11, 7, 8, 1, 13, 14, 12, 5, 10, 15]))

    def test_is_even_permutation2(self):
        puzzle15 = Puzzle15()
        self.assertTrue(puzzle15.is_even_permutation([5, 1, 4, 8, 9, 6, 3, 11, 10, 2, 15, 7, 13, 14, 12]))

    def test_is_even_permutation3(self):
        puzzle15 = Puzzle15()
        self.assertTrue(puzzle15.is_even_permutation(list(range(1, 30))))

    def test_is_even_permutation4(self):
        puzzle15 = Puzzle15()
        self.assertTrue(puzzle15.is_even_permutation([0, 3, 2, 4, 5, 6, 7, 1, 9, 8]))

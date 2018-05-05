from unittest import TestCase

from src.GaleShapley.GaleShapley import GaleShapley


class TestGaleShapley(TestCase):
    def test_run_1_pair(self):
        result = GaleShapley.stableMatching(1, [[0]], [[0]])
        self.assertEqual(result, [0])
        print(result)

    def test_run_2_pairs(self):
        result = GaleShapley.stableMatching(2, [[0, 1], [1, 0]], [[0, 1], [1, 0]])
        self.assertEqual(result, [0, 1])
        print(result)

    def test_run_2_pairs2(self):
        result = GaleShapley.stableMatching(2, [[1, 0], [0, 1]], [[1, 0], [0, 1]])
        self.assertEqual(result, [1, 0])
        print(result)

    def test_run_3_pairs(self):
        result = GaleShapley.stableMatching(3, [[0, 1, 2], [1, 2, 0], [2, 0, 1]], [[0, 1, 2], [1, 2, 0], [2, 0, 1]])
        self.assertEqual(result, [0, 1, 2])
        print(result)

    def test_run_3_pairs2(self):
        result = GaleShapley.stableMatching(3, [[2, 1, 0], [1, 2, 0], [2, 0, 1]], [[0, 1, 2], [1, 2, 0], [2, 0, 1]])
        self.assertEqual(result, [0, 1, 2])
        print(result)

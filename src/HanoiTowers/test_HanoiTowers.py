from unittest import TestCase

from src.HanoiTowers.HanoyTowers import HanoiTowers


class TestHanoiTowers(TestCase):
    def test_run_1_disk(self):
        instance = HanoiTowers(1)
        moves = instance.run()
        self.assertEqual(moves, 1)

    def test_run_2_disk(self):
        instance = HanoiTowers(2)
        moves = instance.run()
        self.assertEqual(moves, 3)

    def test_run_3_disk(self):
        instance = HanoiTowers(3)
        moves = instance.run()
        self.assertEqual(moves, 7)

    def test_run_4_disk(self):
        instance = HanoiTowers(4)
        moves = instance.run()
        self.assertEqual(moves, 15)

    def test_run_5_disk(self):
        instance = HanoiTowers(5)
        moves = instance.run()
        self.assertEqual(moves, 31)

    def test_run_6_disk(self):
        instance = HanoiTowers(6)
        moves = instance.run()
        self.assertEqual(moves, 63)

    # def test_run_n_disk(self):
    #     for x in range(1, 21):
    #         instance = HanoiTowers(x)
    #         moves = instance.run()
    #         print(moves)
    #         self.assertEqual(moves, pow(2, x) - 1)

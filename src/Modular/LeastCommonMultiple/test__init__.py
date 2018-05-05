from unittest import TestCase

from src.Modular.LeastCommonMultiple import lcm


class TestSuite(TestCase):

    def test_lcm(self):
        expected_lcm = 6
        self.assertEqual(expected_lcm, lcm(2, 3))

    def test_lcm2(self):
        expected_lcm = 12
        self.assertEqual(expected_lcm, lcm(4, 6))

    def test_lcm3(self):
        expected_lcm = 30
        self.assertEqual(expected_lcm, lcm(10, 15))

    def test_lcm4(self):
        expected_lcm = 70
        self.assertEqual(expected_lcm, lcm(35, 70))

    def test_lcm5(self):
        expected_lcm = 27720
        self.assertEqual(expected_lcm, lcm(1980, 1848))

    def test_lcm6(self):
        expected_lcm = 27720
        self.assertEqual(expected_lcm, lcm(27720, 27720))

    def test_lcm6(self):
        expected_lcm = 48
        self.assertEqual(expected_lcm, lcm(24, 16))

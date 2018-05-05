from unittest import TestCase

from src.Modular.DiophantiteEquation import diophantine


class TestSuite(TestCase):

    def test(self):
        expected = -7, 14
        current = diophantine(10, 6, 14)
        print(current)
        self.assertEqual(expected, current)

    def test2(self):
        expected = (9, -12)
        current = diophantine(391, 299, -69)
        print(current)
        self.assertEqual(expected, current)

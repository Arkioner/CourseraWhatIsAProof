from unittest import TestCase

from src.Modular.ModularDivision import divide


class TestSuite(TestCase):

    def test_divide(self):
        expected = 8
        self.assertEqual(expected, divide(2, 7, 9))

    def test_divide2(self):
        expected = 8
        self.assertEqual(expected, divide(7, 2, 9))

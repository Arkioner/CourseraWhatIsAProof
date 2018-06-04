from unittest import TestCase

from src.Modular.FastModularExponentiation import FastModularExponentiation


class TestSuite(TestCase):

    def test_0(self):
        self.assertEqual(1, FastModularExponentiation(2, 3, 7))
    def test_1(self):
        self.assertEqual(1, FastModularExponentiation(2, 238, 239))
    def test_2(self):
        self.assertEqual(2, FastModularExponentiation(2, 953, 239))
    def test_3(self):
        self.assertEqual(1, FastModularExponentiation(34, 60, 77))
    def test_4(self):
        self.assertEqual(9, FastModularExponentiation(7, 128, 11))
    def test_5(self):
        self.assertEqual(3, FastModularExponentiation(3, 199234232323233, 17))

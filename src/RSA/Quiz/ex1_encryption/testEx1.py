from unittest import TestCase

from src.RSA.Quiz.ex1_encryption import Encrypt


class TestEx1(TestCase):
    def test_run_1(self):
        p = 5
        q = 7
        module = p * q
        exponent = 34
        c1 = Encrypt("Hola", module, exponent)
        c2 = Encrypt("Hola", module, exponent)
        self.assertEqual(c1, c2)

    def test_run_2(self):
        p = 5
        q = 2
        module = p * q
        exponent = 9
        c1 = Encrypt("CHAO", module, exponent)
        c2 = Encrypt("CHAO", module, exponent)
        self.assertEqual(c1, c2)

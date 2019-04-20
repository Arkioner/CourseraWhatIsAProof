from unittest import TestCase

from src.RSA.Quiz.QuizUtils import QuizUtils
from src.RSA.Quiz.ex2_decryption import Decrypt


class TestEx2(TestCase):
    def test_run_1(self):
        m = "Hola"
        p = 1000000007
        q = 1000000009
        exponent = 23917
        module = p * q
        c1 = QuizUtils.Encrypt(m, module, exponent)
        m1 = Decrypt(c1, p, q, exponent)
        self.assertEqual(m, m1)

    def test_run_2(self):
        m = "Attack"
        p = 1000000007
        q = 1000000009
        exponent = 23917
        module = p * q
        c1 = QuizUtils.Encrypt(m, module, exponent)
        m1 = Decrypt(c1, p, q, exponent)
        self.assertEqual(m, m1)

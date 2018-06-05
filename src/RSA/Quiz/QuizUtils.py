import sys
import threading


class QuizUtils:
    def __init__(self):
        sys.setrecursionlimit(10 ** 7)
        threading.stack_size(2 ** 27)

    @staticmethod
    def ConvertToInt(message_str):
        res = 0
        for i in range(len(message_str)):
            res = res * 256 + ord(message_str[i])
        return res

    @staticmethod
    def ConvertToStr(n):
        res = ""
        while n > 0:
            res += chr(n % 256)
            n //= 256
        return res[::-1]

    @staticmethod
    def PowMod(a, n, mod):
        if n == 0:
            return 1 % mod
        elif n == 1:
            return a % mod
        else:
            b = QuizUtils.PowMod(a, n // 2, mod)
            b = b * b % mod
            if n % 2 == 0:
                return b
            else:
                return b * a % mod

    @staticmethod
    def ExtendedEuclid(a, b):
        if b == 0:
            return (1, 0)
        (x, y) = QuizUtils.ExtendedEuclid(b, a % b)
        k = a // b
        return (y, x - k * y)

    @staticmethod
    def InvertModulo(a, n):
        (b, x) = QuizUtils.ExtendedEuclid(a, n)
        if b < 0:
            b = (b % n + n) % n
        return b

    @staticmethod
    def Decrypt(ciphertext, p, q, exponent):
        # Substitute this implementation with your code from question 2 of the "RSA Quiz".
        return QuizUtils.ConvertToStr(QuizUtils.PowMod(ciphertext, exponent, p * q))

    @staticmethod
    def Encrypt(message, modulo, exponent):
        return QuizUtils.PowMod(QuizUtils.ConvertToInt(message), exponent, modulo)

    @staticmethod
    def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
        # Substitute this implementation with your code from question 3 of the "RSA Quiz".
        if ciphertext == QuizUtils.Encrypt(potential_messages[0], modulo, exponent):
            return potential_messages[0]
        return "don't know"

    @staticmethod
    def DecipherSmallPrime(ciphertext, modulo, exponent):
        # Substitute this implementation with your code from question 4 of the "RSA Quiz".
        return QuizUtils.ConvertToStr(QuizUtils.PowMod(ciphertext, exponent, p * q))

    @staticmethod
    def IntSqrt(n):
        low = 1
        high = n
        iterations = 0
        while low < high and iterations < 5000:
            iterations += 1
            mid = (low + high + 1) // 2
            if mid * mid <= n:
                low = mid
            else:
                high = mid - 1
        return low

    @staticmethod
    def DecipherSmallDiff(ciphertext, modulo, exponent):
        # Substitute this implementation with your code from question 5 of the "RSA Quiz".
        small_prime = QuizUtils.IntSqrt(modulo)
        big_prime = modulo // small_prime
        return QuizUtils.Decrypt(ciphertext, small_prime, big_prime, exponent)

    @staticmethod
    def GCD(a, b):
        if b == 0:
            return a
        return QuizUtils.GCD(b, a % b)

    @staticmethod
    def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                              second_exponent):
        # Substitute this implementation with your code from question 6 of the "RSA Quiz".
        for common_prime in range(2, 1000000):
            if first_modulo % common_prime == 0 and second_modulo % common_prime == 0:
                q1 = first_modulo // common_prime
                q2 = second_modulo // common_prime
                return (QuizUtils.Decrypt(first_ciphertext, common_prime, q1, first_exponent),
                        QuizUtils.Decrypt(second_ciphertext, common_prime, q2, second_exponent))
        return ("unknown message 1", "unknown message 2")

    @staticmethod
    def ChineseRemainderTheorem(n1, r1, n2, r2):
        (x, y) = QuizUtils.ExtendedEuclid(n1, n2)
        return ((r2 * x * n1 + r1 * y * n2) % (n1 * n2) + (n1 * n2)) % (n1 * n2)

    @staticmethod
    def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
        # Substitute this implementation with your code from question 7 of the "RSA Quiz".
        r = QuizUtils.ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
        return QuizUtils.ConvertToStr(QuizUtils.IntSqrt(first_ciphertext * second_ciphertext))

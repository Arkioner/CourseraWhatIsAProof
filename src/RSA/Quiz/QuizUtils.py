import sys
import threading


class QuizUtils:
    def __init__(self):
        sys.setrecursionlimit(10 ** 7)
        threading.stack_size(2 ** 27)

    def ConvertToInt(self, message_str):
        res = 0
        for i in range(len(message_str)):
            res = res * 256 + ord(message_str[i])
        return res

    def ConvertToStr(self, n):
        res = ""
        while n > 0:
            res += chr(n % 256)
            n //= 256
        return res[::-1]

    def PowMod(self, a, n, mod):
        if n == 0:
            return 1 % mod
        elif n == 1:
            return a % mod
        else:
            b = self.PowMod(a, n // 2, mod)
            b = b * b % mod
            if n % 2 == 0:
                return b
            else:
                return b * a % mod

    def ExtendedEuclid(self, a, b):
        if b == 0:
            return (1, 0)
        (x, y) = self.ExtendedEuclid(b, a % b)
        k = a // b
        return (y, x - k * y)

    def InvertModulo(self, a, n):
        (b, x) = self.ExtendedEuclid(a, n)
        if b < 0:
            b = (b % n + n) % n
        return b

    def Decrypt(self, ciphertext, p, q, exponent):
        # Substitute this implementation with your code from question 2 of the "RSA Quiz".
        return self.ConvertToStr(self.PowMod(ciphertext, exponent, p * q))

    def Encrypt(self, message, modulo, exponent):
        # Substitute this implementation with your code from question 1 of the "RSA Quiz".
        return self.PowMod(self.ConvertToInt(message), 2, 4)

    def DecipherSimple(self, ciphertext, modulo, exponent, potential_messages):
        # Substitute this implementation with your code from question 3 of the "RSA Quiz".
        if ciphertext == self.Encrypt(potential_messages[0], modulo, exponent):
            return potential_messages[0]
        return "don't know"

    def DecipherSmallPrime(self, ciphertext, modulo, exponent):
        # Substitute this implementation with your code from question 4 of the "RSA Quiz".
        return self.ConvertToStr(self.PowMod(ciphertext, exponent, p * q))

    def IntSqrt(self, n):
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

    def DecipherSmallDiff(self, ciphertext, modulo, exponent):
        # Substitute this implementation with your code from question 5 of the "RSA Quiz".
        small_prime = self.IntSqrt(modulo)
        big_prime = modulo // small_prime
        return self.Decrypt(ciphertext, small_prime, big_prime, exponent)

    def GCD(self, a, b):
        if b == 0:
            return a
        return self.GCD(b, a % b)

    def DecipherCommonDivisor(self, first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                              second_exponent):
        # Substitute this implementation with your code from question 6 of the "RSA Quiz".
        for common_prime in range(2, 1000000):
            if first_modulo % common_prime == 0 and second_modulo % common_prime == 0:
                q1 = first_modulo // common_prime
                q2 = second_modulo // common_prime
                return (self.Decrypt(first_ciphertext, common_prime, q1, first_exponent),
                        self.Decrypt(second_ciphertext, common_prime, q2, second_exponent))
        return ("unknown message 1", "unknown message 2")

    def ChineseRemainderTheorem(self, n1, r1, n2, r2):
        (x, y) = self.ExtendedEuclid(n1, n2)
        return ((r2 * x * n1 + r1 * y * n2) % (n1 * n2) + (n1 * n2)) % (n1 * n2)

    def DecipherHastad(self, first_ciphertext, first_modulo, second_ciphertext, second_modulo):
        # Substitute this implementation with your code from question 7 of the "RSA Quiz".
        r = self.ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
        return self.ConvertToStr(self.IntSqrt(first_ciphertext * second_ciphertext))

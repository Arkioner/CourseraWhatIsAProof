from src.RSA.Quiz.QuizUtils import QuizUtils
from src.RSA.Quiz.ex1_encryption import Encrypt

PowMod = QuizUtils.PowMod
ConvertToStr = QuizUtils.ConvertToStr
InvertModulo = QuizUtils.InvertModulo
ExtendedEuclid = QuizUtils.ExtendedEuclid


def Decrypt(ciphertext, p, q, exponent):
    mod = (p - 1) * (q - 1)
    d = ExtendedEuclid(exponent, mod)
    return ConvertToStr(PowMod(ciphertext, exponent*d, p*q))


a = 3
b = 7
c = InvertModulo(a, b)
print(c)

p = 1000000007
q = 1000000009
exponent = 23917
modulo = p * q
ciphertext = Encrypt("attack", modulo, exponent)
message = Decrypt(ciphertext, p, q, exponent)
print(message)
from src.RSA.Quiz.QuizUtils import QuizUtils

PowMod = QuizUtils.PowMod
ConvertToStr = QuizUtils.ConvertToStr
InvertModulo = QuizUtils.InvertModulo


def Decrypt(ciphertext, p, q, exponent):
    mod = (p - 1) * (q - 1)
    d = InvertModulo(exponent, mod)
    return ConvertToStr(PowMod(ciphertext, d, p*q))

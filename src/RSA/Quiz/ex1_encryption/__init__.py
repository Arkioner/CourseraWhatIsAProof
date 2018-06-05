from src.RSA.Quiz.QuizUtils import QuizUtils

PowMod = QuizUtils.PowMod
ConvertToInt = QuizUtils.ConvertToInt


def Encrypt(message, modulo, exponent):
    return PowMod(ConvertToInt(message), exponent, modulo)

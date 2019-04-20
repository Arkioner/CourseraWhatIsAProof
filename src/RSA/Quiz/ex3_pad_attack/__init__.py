from src.RSA.Quiz.QuizUtils import QuizUtils

Encrypt = QuizUtils.Encrypt


def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    for messages in potential_messages:
        if ciphertext == Encrypt(messages, modulo, exponent):
            return messages
    return "don't know"


modulo = 101
exponent = 12
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSimple(ciphertext, modulo, exponent, ["attack", "don't attack", "wait"]))

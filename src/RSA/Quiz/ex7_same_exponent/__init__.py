from src.RSA.Quiz.QuizUtils import QuizUtils

Encrypt = QuizUtils.Encrypt
ChineseRemainderTheorem = QuizUtils.ChineseRemainderTheorem
ConvertToStr = QuizUtils.ConvertToStr
IntSqrt = QuizUtils.IntSqrt

def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
    r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
    return ConvertToStr(IntSqrt(r))


p1 = 790383132652258876190399065097
q1 = 662503581792812531719955475509
p2 = 656917682542437675078478868539
q2 = 1263581691331332127259083713503
n1 = p1 * q1
n2 = p2 * q2
ciphertext1 = Encrypt("attack", n1, 2)
ciphertext2 = Encrypt("attack", n2, 2)
message = DecipherHastad(ciphertext1, n1, ciphertext2, n2)
print(message)

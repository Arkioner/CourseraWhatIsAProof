from src.RSA.Quiz.QuizUtils import QuizUtils

Encrypt = QuizUtils.Encrypt
Decrypt = QuizUtils.Decrypt
IntSqrt = QuizUtils.IntSqrt

def DecipherSmallDiff(ciphertext, modulo, exponent):
    upper_bound = IntSqrt(modulo)
    lower_bound = upper_bound - 5000
    for small_prime in range(upper_bound, lower_bound, -1):
        if modulo % small_prime == 0:
            big_prime = modulo // small_prime
            return Decrypt(ciphertext, small_prime, big_prime, exponent)


p = 1000000007
q = 1000000009
n = p * q
e = 239
ciphertext = Encrypt("attack", n, e)
message = DecipherSmallDiff(ciphertext, n, e)
print(ciphertext)
print(message)
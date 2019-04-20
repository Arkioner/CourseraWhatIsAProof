from src.RSA.Quiz.QuizUtils import QuizUtils

Encrypt = QuizUtils.Encrypt
Decrypt = QuizUtils.Decrypt
GCD = QuizUtils.GCD

def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                          second_exponent):

    common_prime = GCD(first_modulo, second_modulo)
    if first_modulo % common_prime == 0 and second_modulo % common_prime == 0:
        q1 = first_modulo // common_prime
        q2 = second_modulo // common_prime
        return (Decrypt(first_ciphertext, common_prime, q1, first_exponent),
                Decrypt(second_ciphertext, common_prime, q2, second_exponent))
    return ("unknown message 1", "unknown message 2")


# Example usage with common prime p and different second primes q1 and q2
p = 101
q1 = 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
q2 = 1000000007
first_modulo = p * q1
second_modulo = p * q2
first_exponent = 239
second_exponent = 17
first_ciphertext = Encrypt("attack", first_modulo, first_exponent)
second_ciphertext = Encrypt("wait", second_modulo, second_exponent)
print(DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                            second_exponent))
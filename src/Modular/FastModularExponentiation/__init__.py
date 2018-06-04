def FastModularExponentiation2(b, e, m):
    bin_exponent = bin(e)
    i = len(bin_exponent) - 2 - 1
    b = b % m
    c = 1
    k = i
    while k >= 0:
        if bin_exponent[k+2] == '1':
            c = c * (b ** (2**(i - k))) % m
        k -= 1
    return c % m

def FastModularExponentiation(b, e, m):
    b = b % m
    if e == 0:
        return 1
    if e == 1:
        return b
    if e & 1 == 0:
        last = FastModularExponentiation(b, e // 2, m)
        return (last * last) % m
    else:
        return (FastModularExponentiation(b, e - 1, m) * b) % m

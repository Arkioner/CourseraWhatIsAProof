def diophantine(a, b, c):
    assert a > 0 and b > 0
    gcdv, p, q = xgcd(a, b)

    i = c / (a*p + b*q)
    return p*i, q*i


def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def ChineseRemainderTheorem(n1, r1, n2, r2):
    (_, x, y) = xgcd(n1, n2)
    n = x * n1 * r2 + y * n2 * r1
    return n % (n1 * n2)


def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

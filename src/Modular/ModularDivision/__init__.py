def divide(a, b, n):
    assert a > 0 and b > 0
    if a > n:
        gcdv, x, y = xgcd(a, n)
    else:
        gcdv, x, y = xgcd(n, a)
    assert gcdv == 1

    return (b * y) % n


def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

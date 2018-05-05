from math import gcd


def lcm(a, b):
    assert a > 0 and b > 0
    if a == b:
        return a
    return (a * b) / gcd(a, b)


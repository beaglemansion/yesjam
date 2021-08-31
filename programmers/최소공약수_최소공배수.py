def gcd(a, b):
    if a % b == 0:
        return b, 0
    return b, a % b


def solution(n, m):
    a, b = max(n, m), min(n, m)

    while True:
        a, b = gcd(a, b)
        if b == 0:
            return [a, n * m / a]

def solution(n):
    a = 1
    while a ** 2 < 50000000000000:
        if n == a ** 2:
            return (a + 1) ** 2
        a += 1
    return -1


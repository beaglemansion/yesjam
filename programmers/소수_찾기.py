# 에라토스테네스의 체
import math


def solution(n):
    total = [i for i in range(2, n + 1)]
    root = math.floor(math.sqrt(n))  # root = int(n**0.5) 루트 씌우고, 정수화시키기
    not_sosu = []
    for root_loop in range(2, root + 1):
        # total = set(total) - set([root_loop*i for i in range(2, math.floor(n/root_loop) + 1)])
        # 아랫줄 대신 써도 정답은 맞는데 매번 배수를 빼는 작업하므로 속도가 더 느린듯
        [not_sosu.append(root_loop * i) for i in range(2, math.floor(n / root_loop) + 1)]

    return len(set(total) - set(not_sosu))


answer = solution(100000)
print(answer)
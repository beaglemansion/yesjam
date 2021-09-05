def solution(n):
    answer = list(map(lambda x: int(x), list(str(n))))
    answer.reverse()
    return answer
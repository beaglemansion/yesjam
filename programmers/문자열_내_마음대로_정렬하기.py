

def solution(strings, n):
    strings = sorted(strings) # 먼저 순서대로 정렬 후
    answer = sorted(strings, key=lambda x: x[n]) # n번째 인덱스로 재정렬

    return answer
"""
한 줄로 for+if
https://leedakyeong.tistory.com/entry/python-for%EB%AC%B8-if%EB%AC%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%EC%BD%94%EB%94%A9%ED%95%98%EA%B8%B0

"""
# list?
def solution(arr, divisor):
    answer = []

    [answer.append(i) for i in arr if i % divisor == 0]

    if len(answer) == 0:
        answer = [-1]

    answer.sort()

    return answer
"""
    map(적용 함수, 대상 리스트) = map 객체
    map객체는 list와 유사한 구조. map객체를 sum함수 사용하여 모두 더함
    나눈 나머지가 0이면 True, 0이 아니면 False
"""


def solution(x):
    return True if x % sum(map(int, list(str(x)))) == 0 else False

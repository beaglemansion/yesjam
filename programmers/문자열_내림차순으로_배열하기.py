
# 문자열 내림차순으로 배치하기
# = 문자열 올림차순으로 배치하고 뒤집기
def solution(s):
    a = [i for i in s]
    a.sort()
    a.reverse()
    b = ''.join(a)
    return b


# 문자열을 바로 리스트로 만들 수 있다..충격
s = 'Zbcdefg'
print(list(s))
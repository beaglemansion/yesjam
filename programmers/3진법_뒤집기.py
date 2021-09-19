import string

# n진법 숫자로 변환
tmp = string.digits+string.ascii_lowercase


def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]


def solution(n):
    answer = ''
    list3 = list(convert(n, 3))
    list3.reverse()
    for num in list3:
        answer += num
    return int(answer, 3)

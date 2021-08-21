def solution(s):
    result = []
    for word in s.split(' '):
        a = []
        for idx, val in enumerate(word):
            # 짝수
            if idx % 2 == 0:
                a.append(val.upper())
            # 홀수
            else:
                a.append(val.lower())
        result.append(''.join(a))

    return ' '.join(result)
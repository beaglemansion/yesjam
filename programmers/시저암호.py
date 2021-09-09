def solution(s, n):
    abc = "abcdefghijklmnopqrstuvwxyz" * 2
    answer = ""
    for i in list(s):
        if i == ' ':
            answer += ' '
        elif i == abc[list(abc).index(i.lower())]:
            # 소문자일경우
            answer += abc[list(abc).index(i.lower()) + n]
        else:
            # 대문자일경우
            answer += abc[list(abc).index(i.lower()) + n].upper()

    return answer
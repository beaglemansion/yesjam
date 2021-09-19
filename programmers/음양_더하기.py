def solution(absolutes, signs):
    answer = 0
    for num in zip(absolutes, signs):
        if num[1] == True:
            answer += num[0]
        else:
            answer -= num[0]

    return answer
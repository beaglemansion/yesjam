def solution(array, commands):
    answer = []

    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        array2 = sorted(array[i - 1:j])
        answer.append(array2[k - 1])

    return answer
def solution(arr1, arr2):
    answer = []

    for n in range(len(arr1)):
        list_1 = arr1[n]
        list_2 = arr2[n]
        temp = []
        for m in range(len(list_1)):
            temp.append(list_1[m] + list_2[m])
        answer.append(temp)

    return answer
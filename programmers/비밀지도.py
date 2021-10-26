<<<<<<< HEAD
# 비밀지도
def get_row(n, arr):
    new_arr = []
    
    for i in arr:
        row = bin(i).split('0b')[1]
        while len(row) < n:
            row = '0' + row
        new_arr.append(row)

    return new_arr


def solution(n, arr1, arr2):
    answer = []
    arr3 = get_row(n, arr1)
    arr4 = get_row(n, arr2)

    for i in range(n):
        tmp = ''
        for j in range(n): 
            if int(arr3[i][j]) or int(arr4[i][j]):
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
=======
# 비밀지도
def get_row(n, arr):
    new_arr = []
    
    for i in arr:
        row = bin(i).split('0b')[1]
        while len(row) < n:
            row = '0' + row
        new_arr.append(row)

    return new_arr


def solution(n, arr1, arr2):
    answer = []
    arr3 = get_row(n, arr1)
    arr4 = get_row(n, arr2)

    for i in range(n):
        tmp = ''
        for j in range(n): 
            if int(arr3[i][j]) or int(arr4[i][j]):
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
>>>>>>> 9f0a732a5bb807b56858d206df774c3c61b32825
    return answer
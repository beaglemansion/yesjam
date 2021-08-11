# 자괴감
def solution(n, lost, reserve):
    student = [1 for i in range(n)]

    for i in range(n):
        if i + 1 in reserve:
            student[i] = student[i] + 1
        if i + 1 in lost:
            student[i] = student[i] - 1

    for i in range(n):
        if i == 0 and student[0] == 2 and student[1] == 0:
            student[0] = 1
            student[1] = 1

        if i != 0 and student[i] == 2 and student[i - 1] == 0:
            student[i - 1] = 1
            student[i] = 1

        if i != 0 and i != len(student) - 1 and student[i] == 2 and student[i + 1] == 0:
            student[i + 1] = 1
            student[i] = 1

        if i == len(student) - 1 and student[i] == 2 and student[i - 1] == 0:
            student[i] = 1
            student[i - 1] = 1

    answer = n
    for i in range(n):
        if student[i] == 0:
            answer -= 1

    return answer
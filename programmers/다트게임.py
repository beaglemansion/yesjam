<<<<<<< HEAD
# 다트게임
def solution(dartResult):
    answer_list = []
    dartResult = dartResult.replace("10", "B")
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for i in dartResult:
        if i.isdigit() or i=='B':
            if i == 'B':
                answer_list.append(10)
            else:
                answer_list.append(int(i))
        elif i in ['S', 'D', 'T']:
            num = answer_list.pop()
            answer_list.append(num ** bonus[i])
        elif i == '#':
            answer_list[-1] *= -1
        elif i == '*':
            num = answer_list.pop()
            if len(answer_list):
                answer_list[-1] *= 2
            answer_list.append(2 * num)
    return sum(answer_list)

# import re

# def solution(dartResult):    
#     filter = re.compile('[0-9]{1,2}')
#     score = filter.findall(dartResult)
#     print(score)
    
#     # 보너스|옵션 구하기
#     first = dartResult.split(score[1])[0].split(score[0])[1]
#     second = dartResult.split(score[1])[1].split(score[2])[0]
#     third = dartResult.split(score[1])[1].split(score[2])[1]
#     print(first, second, third)
    
#     # 보너스 계산
#     answer_list = []
#     for idx, val in enumerate([first, second, third]):
#         if 'S' in val:
#             res = int(score[idx]) ** 1
#         elif 'D' in val:
#             res = int(score[idx]) ** 2
#         elif 'T' in val:
#             res = int(score[idx]) ** 3
#         else:
#             res = score[idx]
#         answer_list.append(res)
#     print(answer_list)
    
#     # 옵션 계산
#     for idx, val in enumerate([first, second, third]):
#         if '*' in val:
#             try:
#                 answer_list[idx] = answer_list[idx] * 2
#                 if idx > 0:
#                     answer_list[idx-1] = answer_list[idx-1] * 2
#             except:
#                 pass
#         elif '#' in val:
#             try:
#                 answer_list[idx] = answer_list[idx] * -1
#             except:
#                 pass
#     print(answer_list)
    
=======
# 다트게임
def solution(dartResult):
    answer_list = []
    dartResult = dartResult.replace("10", "B")
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for i in dartResult:
        if i.isdigit() or i=='B':
            if i == 'B':
                answer_list.append(10)
            else:
                answer_list.append(int(i))
        elif i in ['S', 'D', 'T']:
            num = answer_list.pop()
            answer_list.append(num ** bonus[i])
        elif i == '#':
            answer_list[-1] *= -1
        elif i == '*':
            num = answer_list.pop()
            if len(answer_list):
                answer_list[-1] *= 2
            answer_list.append(2 * num)
    return sum(answer_list)

# import re

# def solution(dartResult):    
#     filter = re.compile('[0-9]{1,2}')
#     score = filter.findall(dartResult)
#     print(score)
    
#     # 보너스|옵션 구하기
#     first = dartResult.split(score[1])[0].split(score[0])[1]
#     second = dartResult.split(score[1])[1].split(score[2])[0]
#     third = dartResult.split(score[1])[1].split(score[2])[1]
#     print(first, second, third)
    
#     # 보너스 계산
#     answer_list = []
#     for idx, val in enumerate([first, second, third]):
#         if 'S' in val:
#             res = int(score[idx]) ** 1
#         elif 'D' in val:
#             res = int(score[idx]) ** 2
#         elif 'T' in val:
#             res = int(score[idx]) ** 3
#         else:
#             res = score[idx]
#         answer_list.append(res)
#     print(answer_list)
    
#     # 옵션 계산
#     for idx, val in enumerate([first, second, third]):
#         if '*' in val:
#             try:
#                 answer_list[idx] = answer_list[idx] * 2
#                 if idx > 0:
#                     answer_list[idx-1] = answer_list[idx-1] * 2
#             except:
#                 pass
#         elif '#' in val:
#             try:
#                 answer_list[idx] = answer_list[idx] * -1
#             except:
#                 pass
#     print(answer_list)
    
>>>>>>> 9f0a732a5bb807b56858d206df774c3c61b32825
#     return sum(answer_list)
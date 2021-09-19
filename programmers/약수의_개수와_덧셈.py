def solution(left, right):
    answer = 0
    num_list = [i for i in range(left, right+1)]
    for num in num_list:
        divisor_list = []
        for i in range(1,num+1):
            if num % i == 0:
                divisor_list.append(i)
        if len(divisor_list) % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer
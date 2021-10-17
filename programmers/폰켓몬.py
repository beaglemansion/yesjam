<<<<<<< HEAD
def solution(nums):
    num_set = len(set(nums))   
    select = len(nums) / 2  
    answer = 0

    if select > num_set: # 집합보다 선택해야햐는 숫자가 더 클 경우
        answer = num_set
    else:
        answer = select

=======
def solution(nums):
    num_set = len(set(nums))   
    select = len(nums) / 2  
    answer = 0

    if select > num_set: # 집합보다 선택해야햐는 숫자가 더 클 경우
        answer = num_set
    else:
        answer = select

>>>>>>> 1c791cb9259b73a4f58e761276d1fb1732a1001e
    return answer
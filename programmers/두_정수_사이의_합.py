a = 3
b = 5

def solution(a, b):
    answer = 0
    c = a
    numbers = []
    while True:
        if a > b:
            numbers.append(c)
            c -= 1
        elif a == b:
            numbers.append(c)
            break
        else:
            numbers.append(c)
            c += 1
        if c == b:
            numbers.append(c)
            break

    answer = sum(numbers)

    return answer

# range도 sum이 가능하다...
def sol2(a,b):
    return sum(range(min(a,b),max(a,b)+1))

def solution(d, budget):
    result = 0
    for req in sorted(d):
        if budget >= req:
            budget -= req
            result += 1

    return result
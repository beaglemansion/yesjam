def solution(price, money, count):
    geld = 0
    for i in range(1, count+1):
        geld += i*price

    return 0 if money >= geld else geld-money
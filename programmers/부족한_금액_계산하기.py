<<<<<<< HEAD
def solution(price, money, count):
    geld = 0
    for i in range(1, count+1):
        geld += i*price

=======
def solution(price, money, count):
    geld = 0
    for i in range(1, count+1):
        geld += i*price

>>>>>>> 9f0a732a5bb807b56858d206df774c3c61b32825
    return 0 if money >= geld else geld-money
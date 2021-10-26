<<<<<<< HEAD
def solution(s):
    
    num_dict = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    for i in num_dict.keys():
        if i in s:
            s = s.replace(i, num_dict[i])
    
=======
def solution(s):
    
    num_dict = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    for i in num_dict.keys():
        if i in s:
            s = s.replace(i, num_dict[i])
    
>>>>>>> 9f0a732a5bb807b56858d206df774c3c61b32825
    return int(s)
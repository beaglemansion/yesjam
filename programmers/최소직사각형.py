<<<<<<< HEAD
def solution(sizes):
    w_list = []
    h_list = []
    for i in sizes:
        card = sorted(i, reverse=True)
        w_list.append(card[0])
        h_list.append(card[1])

=======
def solution(sizes):
    w_list = []
    h_list = []
    for i in sizes:
        card = sorted(i, reverse=True)
        w_list.append(card[0])
        h_list.append(card[1])

>>>>>>> 9f0a732a5bb807b56858d206df774c3c61b32825
    return sorted(w_list, reverse=True)[0] * sorted(h_list, reverse=True)[0]
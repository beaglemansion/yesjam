def solution(sizes):
    w_list = []
    h_list = []
    for i in sizes:
        card = sorted(i, reverse=True)
        w_list.append(card[0])
        h_list.append(card[1])

    return sorted(w_list, reverse=True)[0] * sorted(h_list, reverse=True)[0]
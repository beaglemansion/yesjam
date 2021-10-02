from pprint import pprint


def solution(board, moves):
    bucket = []
    pprint(board)
    count = 0

    for move in moves:
        for check in range(len(board)):
            if board[check][move - 1] == 0:
                pass
            else:
                Puppe = board[check][move - 1]
                bucket.append(Puppe)
                board[check][move - 1] = 0
                break
        if len(bucket) >= 2 and bucket[-2] == bucket[-1]:
            bucket = bucket[:-2]
            count += 1

    pprint(board)

    return count * 2
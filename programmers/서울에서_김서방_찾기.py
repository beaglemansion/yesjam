def solution(seoul):

    return '김서방은 %d에 있다' % seoul.index('Kim')
    # 또는
    # return '김서방은 %d에 있다' % [ idx for idx, val in enumerate(seoul) if val == 'Kim'][0]


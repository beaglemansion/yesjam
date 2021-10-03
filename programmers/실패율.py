def solution(N, stages):
    fail = dict()

    for stage in range(1, N + 1):
        fail_cnt = 0
        challange_cnt = 0
        for person in stages:
            if stage == person:
                fail_cnt += 1
            if stage <= person:
                challange_cnt += 1
        try:
            fail[stage] = fail_cnt / challange_cnt
        except:
            fail[stage] = 0

    return sorted(fail, key=lambda x: fail[x], reverse=True)

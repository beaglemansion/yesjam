import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    regex_1 = re.compile('[0-9a-z-_.]')
    new_id = ''.join(regex_1.findall(new_id))

    # 3단계
    new_id = re.sub('[.]{2,}', '.', new_id)

    # 4단계
    new_id = re.sub('^[.]|[.]$','', new_id)

    # 5단계
    if new_id == '':
        new_id = 'a'

    # 6단계
    new_id = re.sub('[.]$','', new_id[:15])

    # 7단계
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]

    return new_id


answer = solution('abcdefghijklmn.p')
print(answer)
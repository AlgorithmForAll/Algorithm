"""
불량 사용자
https://programmers.co.kr/learn/courses/30/lessons/64064
"""
from itertools import product


def solution(user_id, banned_id):
    blen = len(banned_id)
    data = [[] for _ in range(blen)]
    for user in user_id:
        ulen = len(user)
        for bix, ban in enumerate(banned_id):
            if ulen == len(ban):
                for i in range(ulen):
                    if ban[i] != "*" and ban[i] != user[i]:
                        break
                else:
                    data[bix].append(user)

    answer = set()
    for case in product(*data):
        if len(set(case)) == blen:
            answer.add(tuple(sorted(list(case))))
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]), 2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]), 2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]), 3)

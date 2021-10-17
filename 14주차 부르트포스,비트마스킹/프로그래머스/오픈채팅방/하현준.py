"""
오픈채팅방
https://programmers.co.kr/learn/courses/30/lessons/42888
"""
from collections import defaultdict


def solution(record):
    answer = []
    data = defaultdict(str)

    for r in record:
        r = r.split()
        com, uid = r[0], r[1]
        if com != "Leave":
            data[uid] = r[2]

    for r in record:
        r = r.split()
        com, uid = r[0], r[1]
        if com == "Enter":
            answer.append(f"{data[uid]}님이 들어왔습니다.")
        elif com == "Leave":
            answer.append(f"{data[uid]}님이 나갔습니다.")
    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

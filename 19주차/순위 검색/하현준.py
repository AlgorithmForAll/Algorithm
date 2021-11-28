"""
순위 검색
https://programmers.co.kr/learn/courses/30/lessons/72412
"""
from itertools import combinations
from collections import defaultdict


def lower_bound(data, target):
    lo = 0
    hi = len(data)
    while lo < hi:
        mid = (lo + hi) // 2
        if target <= data[mid]:
            hi = mid
        else:
            lo = mid + 1
    return len(data) - lo


def solution(info, query):
    answer = []
    data = defaultdict(list)
    for inf in info:
        inf = inf.split()

        data["".join(inf[:-1])].append(int(inf[-1]))
        for i in range(1, 5):
            for case in combinations([0, 1, 2, 3], i):
                temp = inf[:-1]
                for c in case:
                    temp[c] = "-"
                data["".join(temp)].append(int(inf[-1]))

    for k in data.keys():
        data[k].sort()

    for q in query:
        q = q.split()
        squery = q[0] + q[2] + q[4] + q[6]
        score = int(q[-1])
        answer.append(lower_bound(data[squery], score))

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))

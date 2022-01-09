"""
메뉴 리뉴얼
https://programmers.co.kr/learn/courses/30/lessons/72411
"""
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    data = defaultdict(set)
    result = defaultdict(list)
    orders = [set(x) for x in orders]
    
    for c in course:
        for i in range(len(orders)):
            for case in combinations(orders[i], c):
                data["".join(sorted(list(case)))].add(i)
                for j in range(len(orders)):
                    if i != j and set(case) <= orders[j]:
                        data["".join(sorted(list(case)))].add(j)

    for k, v in data.items():
        if len(v) >= 2:
            result[len(k)].append([len(v), k])

    for k, v in result.items():
        v.sort(key=lambda x: -int(x[0]))
        max_count = v[0][0]
        for val in v:
            if val[0] == max_count:
                answer.append(val[1])
                
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	, [2, 3, 4]	))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	, [2, 3, 5]	))
print(solution(["XYZ", "XWY", "WXA"]	, [2, 3, 4]	))

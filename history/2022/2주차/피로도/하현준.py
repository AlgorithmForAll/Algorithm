"""
피로도
https://programmers.co.kr/learn/courses/30/lessons/87946
"""
from itertools import combinations, permutations


# 시간초과 -> 케이스 12
def solution1(k, dungeons):
    min_k = min(list(zip(*dungeons))[0])

    def dfs(now_k, visited):
        if now_k < min_k:
            return len(visited)

        result = 0
        for i in range(len(dungeons)):
            minimum, cost = dungeons[i]
            if minimum <= now_k:
                result = max(result, dfs(now_k - cost, visited | {i}))
        return result

    answer = dfs(k, set())
    return answer


def solution(k, dungeons):
    count = 0
    for i in range(1, len(dungeons) + 1):
        for case in combinations(dungeons, i):
            for pcase in permutations(case):
                pcount = 0
                now_k = k
                for minimum, cost in pcase:
                    if now_k >= minimum:
                        now_k -= cost
                        pcount += 1
                count = max(count, pcount)
    return count


print(solution(80, [[80, 20], [50, 40], [30, 10]]), 3)

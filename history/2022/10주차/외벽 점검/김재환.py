"""
정답 보고 풀었음.....너무 어렵다.....
https://guccin.tistory.com/152

"""
from itertools import permutations


def solution(n, weak, dist):
    INF = 1000000000
    answer = INF
    Map = list(weak)
    for i in weak:
        Map.append(i+n)
    _dist = list(permutations(dist))

    for si in range(len(weak)):

        for pi in _dist:
            dist = pi
            count = 0
            nextpoint = -1
            for i in range(si, si+len(weak)):  # 몇번수행하는가
                # 조건
                if nextpoint >= Map[i]:
                    continue
                if count >= len(dist):
                    count = INF
                    break
                nextpoint = Map[i] + dist[count]
                count += 1
            answer = min(answer, count)
    if answer == INF:
        return -1
    return answer

"""
징검다리
https://programmers.co.kr/learn/courses/30/lessons/43236?language=python3
"""


def solution(distance, rocks, n):
    lo = 0
    hi = distance
    rlen = len(rocks)
    rocks.sort()
    while lo + 1 < hi:
        mid = (lo + hi) // 2

        remove = 0
        current = 0
        next_id = 0
        while next_id < rlen:
            if abs(rocks[next_id] - current) < mid:
                next_id += 1
                remove += 1
            else:
                current = rocks[next_id]
                next_id += 1
        print(f"{lo=} {mid=} {hi=} {remove=}")
        if remove > n:
            hi = mid
        else:
            lo = mid

    return lo


print(solution(25, [2, 14, 11, 21, 17], 2))

"""
  2  8   3   3   4   4
0, 2, 11, 14, 17, 21, 25
"""

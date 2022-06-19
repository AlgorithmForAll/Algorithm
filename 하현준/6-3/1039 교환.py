"""
https://www.acmicpc.net/problem/1039
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")
INF = -float('inf')

for _ in range(10):
    answer = INF
    visited = set()
    n, k = map(int, input().split())
    m = len(str(n))

    temp = False
    q = deque([[n, k]])
    while q:
        num, count = q.popleft()
        if count == 0:
            answer = max(answer, num)
            temp = True
            continue

        lnum = list(str(num))
        for i in range(m - 1):
            for j in range(i + 1, m):

                lnum[i], lnum[j] = lnum[j], lnum[i]
                if lnum[0] != "0" and ("".join(lnum), i, j, count) not in visited:
                    visited.add(("".join(lnum), i, j, count))
                    q.append([int("".join(lnum)), count - 1])
                lnum[j], lnum[i] = lnum[i], lnum[j]

    print(answer if answer != INF and temp else -1)

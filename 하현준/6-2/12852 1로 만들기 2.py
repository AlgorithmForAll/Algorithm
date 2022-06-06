"""
https://www.acmicpc.net/problem/12852
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")
inf = float('inf')


def bfs():
    q = deque([[n, 0, []]])

    while q:
        num, count, history = q.popleft()
        if dp[num] > count:
            dp[num] = count
        else:
            continue

        if num == 1:
            history.append(1)
            print(count)
            print(*history, sep=" ")
            return
        if num % 2 == 0:
            q.append([num // 2, count + 1, history + [num]])
        if num % 3 == 0:
            q.append([num // 3, count + 1, history + [num]])
        q.append([num - 1, count + 1, history + [num]])


for _ in range(3):
    n = int(input())
    dp = [inf for _ in range(n+1)]
    bfs()
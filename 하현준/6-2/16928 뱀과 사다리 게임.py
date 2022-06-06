"""
https://www.acmicpc.net/problem/16928
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")

for _ in range(2):
    n, m = map(int, input().split())
    data = [0 for _ in range(101)]
    visited = [0 for _ in range(101)]
    for _ in range(n + m):
        a, b = map(int, input().split())
        data[a] = b

    q = deque([[1, 0]])
    while q:
        x, count = q.popleft()
        if x == 100:
            print(count)
            break

        for i in range(1, 7):
            xx = x + i
            if 1 <= xx <= 100:
                if data[xx] != 0:
                    xx = data[xx]
                if visited[xx] == 0:
                    visited[xx] = 1
                    q.append([xx, count + 1])
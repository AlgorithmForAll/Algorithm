"""
스타트링크
https://www.acmicpc.net/problem/5014
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")

for _ in range(10):
    inf = float('inf')
    f, s, g, u, d = map(int, input().split())
    answer = inf
    floors = [inf for _ in range(f + 1)]
    floors[s] = 0
    q = deque([[s, 0]])

    while q:
        now, bcount = q.popleft()
        if now == g:
            answer = min(answer, bcount)
            break
        if 0 < now - d <= f and floors[now - d] == inf:
            floors[now - d] = bcount + 1
            q.append([now - d, bcount + 1])
        if 0 < now + u <= f and floors[now + u] == inf:
            floors[now + u] = bcount + 1
            q.append([now + u, bcount + 1])

    print(answer if answer != inf else "use the stairs")

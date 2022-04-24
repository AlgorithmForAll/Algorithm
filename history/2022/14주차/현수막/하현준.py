"""
현수막
https://www.acmicpc.net/problem/14716
"""
from collections import deque

import sys

sys.stdin = open("../input.txt")
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]
m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
count = 0
for i in range(m):
    for j in range(n):
        if data[i][j] == 1 and visited[i][j] == 0:
            count += 1
            visited[i][j] = 1
            q = deque([[i, j]])
            while q:
                x, y = q.popleft()
                for k in range(8):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0 <= xx < m and 0 <= yy < n:
                        if visited[xx][yy] == 0 and data[xx][yy] == 1:
                            visited[xx][yy] = 1
                            q.append([xx, yy])

print(count)

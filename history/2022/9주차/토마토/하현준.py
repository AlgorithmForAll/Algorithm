"""
토마토
https://www.acmicpc.net/problem/7569
"""

import sys
from collections import deque

sys.stdin = open("../input.txt")
input = sys.stdin.readline
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(q, visited):
    if zero == 0:
        return 0

    q = deque(q)
    count = 0
    while q:
        z, x, y, day = q.popleft()
        for k in range(6):
            xx = x + dx[k]
            yy = y + dy[k]
            zz = z + dz[k]
            if 0 <= xx < n and 0 <= yy < m and 0 <= zz < h:
                if visited[zz][xx][yy] == 0 and tomatoes[zz][xx][yy] != -1:
                    count += 1
                    if count == zero:
                        return day + 1
                    visited[zz][xx][yy] = 1
                    q.append([zz, xx, yy, day + 1])
    return -1


for _ in range(int(input())):
    m, n, h = map(int, input().split())
    zero = 0
    q = []
    tomatoes = []
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

    for z in range(h):
        tomatoes.append([list(map(int, input().split())) for _ in range(n)])
        for x in range(n):
            for y in range(m):
                if tomatoes[z][x][y] == 1:
                    visited[z][x][y] = 1
                    q.append([z, x, y, 0])
                elif tomatoes[z][x][y] == 0:
                    zero += 1

    print(bfs(q, visited))

"""
아기 상어 2
https://www.acmicpc.net/problem/17086
"""
import sys

sys.stdin = open("../../input.txt")

from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def get_dist(x, y):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    q = deque([[x, y, 0]])
    while q:
        x, y, dist = q.popleft()
        if [x, y] in sharks:
            return dist
        for k in range(8):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if visited[xx][yy] == 0:
                    visited[xx][yy] = 1
                    q.append([xx, yy, dist + 1])
    return 0

for _ in range(2):
    n, m = map(int, input().split())
    sharks = []
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        for j in range(m):
            if graph[i][j] == 1:
                sharks.append([i, j])

    answer = -1
    distance = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                answer = max(answer, get_dist(i, j))

    print(answer)

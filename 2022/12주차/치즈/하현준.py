"""
치즈
https://www.acmicpc.net/problem/2636
"""
import sys
from collections import deque

sys.stdin = open("../input.txt")

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def mark_air():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([[0, 0]])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if visited[xx][yy] == 0 and (graph[xx][yy] == 0 or graph[xx][yy] == -1):
                    visited[xx][yy] = 1
                    graph[xx][yy] = -1
                    q.append([xx, yy])


def melting(cheese):
    to_melt = []
    remain = []
    for cx, cy in cheese:
        air = False
        for k in range(4):
            xx = cx + dx[k]
            yy = cy + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if graph[xx][yy] == -1:
                    air = True
                    break

        if air:
            to_melt.append([cx, cy])
        else:
            remain.append([cx, cy])

    for mx, my in to_melt:
        graph[mx][my] = -1

    return remain


n, m = map(int, input().split())
cheese = []
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 2
            cheese.append([i, j])

count = 0
remain_cheese = 0
while cheese:
    remain_cheese = len(cheese)
    count += 1
    mark_air()
    cheese = melting(cheese)

print(count)
print(remain_cheese)

"""
보물섬
https://www.acmicpc.net/problem/2589
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")


def solution(lx, ly):
    max_dist = -1
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[lx][ly] = 1
    q = deque([[lx, ly]])
    while q:
        max_dist += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0 <= xx < n and 0 <= yy < m:
                    if graph[xx][yy] == "L" and visited[xx][yy] == -1:
                        visited[xx][yy] = 1
                        q.append([xx, yy])
    return max_dist


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
inf = float('inf')
n, m = map(int, input().split())
temp = []
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "L":
            temp.append([i, j])

lands = []
for tx, ty in temp:  # 완탐은 탐색 데이터의 범위를 줄이는게 관건
    if tx * ty == 0:
        lands.append([tx, ty])
    else:
        check = False
        for k in range(4):
            ii = tx + dx[k]
            jj = ty + dy[k]
            if 0 <= ii < n and 0 <= jj < m:
                if graph[ii][jj] == "W":
                    check = True
                    break
        if check:
            lands.append([tx, ty])

result = -inf
for lx, ly in lands:
    result = max(result, solution(lx, ly))
print(result)

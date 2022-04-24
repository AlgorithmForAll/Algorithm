"""
다리 만들기
https://www.acmicpc.net/problem/2146
"""
import sys

sys.stdin = open("../input.txt")
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def check(x, y):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n:
            if graph[xx][yy] == 0:
                return True
    return False


def get_island_points():
    points = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                q = deque([[i, j]])
                island = [[i, j]]

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < n and 0 <= yy < n:
                            if visited[xx][yy] == 0 and graph[xx][yy] == 1:
                                visited[xx][yy] = 1
                                q.append([xx, yy])
                                island.append([xx, yy])

                spoint = []
                for ix, iy in island:
                    if check(ix, iy):
                        spoint.append([ix, iy])

                if spoint:
                    points.append([spoint, island])

    return points


def get_dist(x, y, island):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    q = deque([[x, y, 0]])
    while q:
        for _ in range(len(q)):
            x, y, dist = q.popleft()
            if graph[x][y] == 1 and [x, y] not in island:
                return dist - 1
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0 <= xx < n and 0 <= yy < n:
                    if visited[xx][yy] == 0:
                        visited[xx][yy] = 1
                        q.append([xx, yy, dist + 1])
    return 0


for _ in range(100):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    points = get_island_points()
    answer = float('inf')
    for point, island in points:
        for px, py in point:
            dist = get_dist(px, py, island)
            answer = min(answer, dist)
    print(answer)

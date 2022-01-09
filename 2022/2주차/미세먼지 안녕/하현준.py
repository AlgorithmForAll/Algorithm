"""
미세먼지 안녕
https://www.acmicpc.net/problem/17144
"""
from collections import defaultdict
import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
circulate = [[(-1, 0), (0, 1), (1, 0), (0, -1)],
             [(1, 0), (0, 1), (-1, 0), (0, -1)]]

R, C, T = map(int, input().split())
air_cleaner = []
graph = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if graph[i][0] == -1:
        air_cleaner.append([i, 0])

for _ in range(T):
    # spread
    data = defaultdict(int)
    for di in range(R):
        for dj in range(C):
            if graph[di][dj] > 0:
                dcount = 0
                dmount = graph[di][dj] // 5
                for i in range(4):
                    xx = di + dx[i]
                    yy = dj + dy[i]
                    if 0 <= xx < R and 0 <= yy < C:
                        if [xx, yy] not in air_cleaner:
                            dcount += 1
                            data[(xx, yy)] += dmount
                data[(di, dj)] -= dcount * dmount

    for k, v in data.items():
        graph[k[0]][k[1]] += v

    # air cirulate
    for i in range(2):
        c = 0
        ax, ay = air_cleaner[i]
        cx, cy = circulate[i][c]
        xx = ax + cx
        yy = ay + cy

        if i == 0:
            while True:
                nx = xx + cx
                ny = yy + cy
                if [nx, ny] == [ax, ay]:
                    graph[xx][yy] = 0
                    break
                if 0 <= nx <= ax and 0 <= ny < C:
                    graph[xx][yy] = graph[nx][ny]
                else:
                    c += 1
                    if c == 4:
                        break
                    cx, cy = circulate[i][c]
                    nx = xx + cx
                    ny = yy + cy
                    graph[xx][yy] = graph[nx][ny]
                xx = nx
                yy = ny
        else:
            while True:
                nx = xx + cx
                ny = yy + cy
                if [nx, ny] == [ax, ay]:
                    graph[xx][yy] = 0
                    break
                if ax <= nx < R and 0 <= ny < C:
                    graph[xx][yy] = graph[nx][ny]
                else:
                    c += 1
                    if c == 4:
                        break
                    cx, cy = circulate[i][c]
                    nx = xx + cx
                    ny = yy + cy
                    graph[xx][yy] = graph[nx][ny]
                xx = nx
                yy = ny

print(sum(sum(graph, [])) + 2)

"""
Puyo Puyo
https://www.acmicpc.net/problem/11559
"""

import sys
from collections import deque

sys.stdin = open("../input.txt")


def solution():
    count = 0
    while True:
        blows = []
        visited = [[0 for _ in range(12)] for _ in range(6)]
        for i in range(6):
            for j in range(12):
                if graph[i][j] != "" and visited[i][j] == 0:
                    visited[i][j] = 1
                    q = deque([[i, j]])
                    puyo = graph[i][j]
                    temp = [[i, j]]
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if 0 <= xx < 6 and 0 <= yy < 12:
                                if visited[xx][yy] == 0 and graph[xx][yy] == puyo:
                                    visited[xx][yy] = 1
                                    q.append([xx, yy])
                                    temp.append([xx, yy])

                    if len(temp) >= 4:
                        blows.append(temp)

        if blows:
            count += 1
            for blow in blows:
                for bx, by in blow:
                    graph[bx][by] = ""
            for r in range(6):
                gtemp = list("".join(graph[r]))
                graph[r] = ["" for _ in range(12 - len(gtemp))] + gtemp
        else:
            return count


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
graph = []
for i in range(12):
    temp = []
    for j in list(input()):
        temp.append("" if j == "." else j)
    graph.append(temp)

graph = list(map(list, zip(*graph)))

print(solution())

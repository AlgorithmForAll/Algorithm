"""
https://www.acmicpc.net/problem/2933
"""
import sys
from collections import deque

sys.stdin = open("../input.txt")


def get_clusters():
    clusters = []
    visited = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "x" and visited[i][j] == 0:
                cluster = [[i, j]]
                q = deque([[i, j]])
                visited[i][j] = 1

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < r and 0 <= yy < c:
                            if visited[xx][yy] == 0 and graph[xx][yy] == "x":
                                visited[xx][yy] = 1
                                q.append([xx, yy])
                                cluster.append([xx, yy])
                clusters.append(cluster)
    return clusters


def check(cluster, gap):
    for cx, cy in cluster:
        if graph[cx + gap][cy] == "x":
            return False
    return True


def draw(cluster, gap):
    for cx, cy in cluster:
        graph[cx + gap][cy] = "x"


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(100):
    r, c = map(int, input().split())
    graph = [list(input()) for _ in range(r)]
    n = int(input())
    heights = list(map(int, input().split()))

    for i in range(n):
        h = heights[i] - 1
        idx = r - h - 1
        if i % 2 == 0:
            for j in range(c):
                if graph[idx][j] == "x":
                    graph[idx][j] = "."
                    break
        else:
            for j in range(c):
                if graph[idx][c - j - 1] == "x":
                    graph[idx][c - j - 1] = "."
                    break

        clusters = get_clusters()
        for cluster in clusters:
            # erase
            for cx, cy in cluster:
                graph[cx][cy] = "."

            # falling
            hdata = list(zip(*cluster))[0]
            highest = min(hdata)
            lowest = max(hdata)

            if lowest != r - 1:
                gap = r - lowest
                if gap == 0:
                    draw(cluster, 0)
                for g in range(1, gap + 1):
                    if lowest + g >= r or not check(cluster, g):
                        draw(cluster, g - 1)
                        break
            else:
                draw(cluster, 0)

    for gp in graph:
        print("".join(gp))

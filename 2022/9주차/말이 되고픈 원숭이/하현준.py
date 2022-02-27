"""
말이 되고픈 원숭이
https://www.acmicpc.net/problem/1600
"""
import sys
from collections import deque

sys.stdin = open("../input.txt")
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
hx = [-2, -2, -1, 1, 2, 2, 1, -1]
hy = [-1, 1, 2, 2, 1, -1, -2, -2]
inf = float('inf')


def bfs():
    visited = [[[inf for _ in range(k + 2)] for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 0
    visited[0][0][1] = 0
    q = deque([[0, 0, 0, 0]])

    while q:
        x, y, kcount, move = q.popleft()
        if [x, y] == [h - 1, w - 1]:
            return move

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < h and 0 <= yy < w:
                if visited[xx][yy][kcount] > move + 1 and graph[xx][yy] == 0:
                    visited[xx][yy][kcount] = move + 1
                    q.append([xx, yy, kcount, move + 1])

        if kcount < k:
            for i in range(8):
                xx = x + hx[i]
                yy = y + hy[i]
                if 0 <= xx < h and 0 <= yy < w:
                    if visited[xx][yy][kcount + 1] > move + 1 and graph[xx][yy] == 0:
                        visited[xx][yy][kcount + 1] = move + 1
                        q.append([xx, yy, kcount + 1, move + 1])
    return -1


for _ in range(int(input())):
    k = int(input())
    w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]
    print(bfs())

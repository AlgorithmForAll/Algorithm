"""
로봇 청소기
https://www.acmicpc.net/problem/14503
"""
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def left(direct):
    if direct == 0:
        return 3
    if direct == 1:
        return 0
    if direct == 2:
        return 1
    if direct == 3:
        return 2


def dfs(x, y, direct, num):
    if visited[x][y] == 0:
        visited[x][y] = num

    temp_d = direct
    for _ in range(4):
        temp_d = left(temp_d)
        xx = x + dx[temp_d]
        yy = y + dy[temp_d]
        if graph[xx][yy] == 0 and visited[xx][yy] == 0:
            return dfs(xx, yy, temp_d, num + 1)

    kx = x - dx[direct]
    ky = y - dy[direct]
    if graph[kx][ky] == 0:
        return dfs(kx, ky, direct, num)


for _ in range(int(input())):
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dfs(r, c, d, 1)
    print(max(sum(visited, [])))

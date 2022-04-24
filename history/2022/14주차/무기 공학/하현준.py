"""
무기 공학
https://www.acmicpc.net/problem/18430
"""
import sys

sys.stdin = open("../input.txt")

sys.setrecursionlimit(10 ** 5)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, score):
    global answer
    if x == n:
        answer = max(answer, score)
        return

    if 0 <= x < n and 0 <= y < m:
        print(x, y, f"{visited[x][y]=}")
        print(*visited, sep="\n")
        print(score)
        print()
        if visited[x][y] == 0:
            for i in range(4):
                ax = x + dx[i % 4]
                ay = y + dy[i % 4]
                bx = x + dx[(i + 1) % 4]
                by = y + dy[(i + 1) % 4]
                if (0 <= ax < n and 0 <= ay < m) and (0 <= bx < n and 0 <= by < m):
                    if visited[ax][ay] == 0 and visited[bx][by] == 0:
                        visited[x][y] = 1
                        visited[ax][ay] = 1
                        visited[bx][by] = 1
                        dfs(x, y + 1, score + data[ax][ay] + (data[x][y] * 2) + data[bx][by])
                        visited[ax][ay] = 0
                        visited[bx][by] = 0
                        visited[x][y] = 0
        dfs(x, y + 1, score) # 부메랑을 만들지 못한 경우, 방문했던 곳인지 아닌지는 중요하지 않음
    elif y >= m:
        dfs(x + 1, 0, score)


for _ in range(1):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0
    dfs(0, 0, 0)
    print(answer)

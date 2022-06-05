"""
https://www.acmicpc.net/problem/1103
참고 : https://hillier.tistory.com/65
"""
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 6)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
INF = float('inf')


def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        xx = x + dx[i] * int(board[x][y])
        yy = y + dy[i] * int(board[x][y])
        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] != "H":
            if dp[xx][yy] < count + 1:
                if visited[xx][yy] == 0:
                    dp[xx][yy] = count + 1
                    visited[xx][yy] = 1
                    dfs(xx, yy, count + 1)
                    visited[xx][yy] = 0
                else:
                    print(-1)
                    exit()


for _ in range(100):
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]

    sx, sy = 0, 0
    visited[sx][sy] = 1
    dp[sx][sy] = 1

    answer = 0
    dfs(sx, sy, 0)
    print(answer + 1)

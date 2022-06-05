import sys
sys.setrecursionlimit(10**6)

dy = [-1, 1, 0, 0]  # 상하 좌우
dx = [0, 0, -1, 1]


def dfs(y, x):
    global state
    if not(0 <= y < N and 0 <= x < M) or board[y][x] == 'H':
        return 0

    if visited[y][x]:
        state = True
        return -1
    if dp[y][x] != -1:
        return dp[y][x]

    visited[y][x] = True

    X = int(board[y][x])
    for i in range(4):
        dp[y][x] = max(dp[y][x], dfs(y+dy[i]*X, x+dx[i]*X)+1)
        if state:
            return -1
    visited[y][x] = False

    return dp[y][x]


N, M = map(int, input().split())
board = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
state = False
print(dfs(0, 0))

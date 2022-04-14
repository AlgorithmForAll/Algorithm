"""

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0 for i in range(N+1)]]
for i in range(N):
    tmp = list(map(int, input().split()))
    dp.append([0] + tmp)
for i in range(2, N+1):
    dp[1][i] += dp[1][i-1]
    dp[i][1] += dp[i-1][1]

for i in range(2, N+1):
    for j in range(2, N+1):
        dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# padding 추가하기
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    tmp = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(tmp)

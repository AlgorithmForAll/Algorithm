import sys
input = sys.stdin.readline 


N, M = map(int, input().split())

array = []
for i in range(N):
    array.append(list(map(int, input().split())))
    
dp = [[0 for i in range(N+1)] for i in range(N+1)]

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + array[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))
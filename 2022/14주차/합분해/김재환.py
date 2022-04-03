"""
조합x
모듈러 분배법칙
주어진 수는 차례대로 증가함
백트래킹으로 풀이 가능, K도 200까지라 recurlimit도 200밖에 안됨
"""
N, K = map(int, input().split())


dp = [[0 for i in range(K+1)] for i in range(N+1)]
for i in range(1, K+1):
    dp[1][i] = i
for j in range(1, N+1):
    dp[j][1] = 1

for i in range(2, N+1):
    for j in range(2, K+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        dp[i][j] %= 1000000000
print(dp[N][K])

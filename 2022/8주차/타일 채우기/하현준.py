"""
타일 채우기
https://www.acmicpc.net/problem/2133
"""

n = int(input())
dp = [0 for _ in range(n + 5)]
dp[2] = 3
for i in range(4, n + 1):
    if i % 2 == 0:
        dp[i] = 3 * dp[i - 2]
        for j in range(i - 4, -1, -2):
            dp[i] += 2 * dp[j]
        dp[i] += 2

print(dp[n])

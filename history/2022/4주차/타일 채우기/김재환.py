"""
dp를 생각은 어렵지 않으나
규칙을 찾는게 까다로웠다.
"""
N = int(input())

dp = [0 for i in range(30+1)]
dp[0] = 1
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = 3 * dp[i-2]
    for j in range(4, i+1, 2):
        dp[i] += 2 * dp[i-j]
print(dp[N])

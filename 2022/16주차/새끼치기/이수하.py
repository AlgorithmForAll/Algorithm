import sys
input = sys.stdin.readline


N = int(input())
dp = [0 for i in range(21)]
dp[0] = 1
dp[1] = 1
for i in range(2, 21):
    if i%2 == 0:
        dp[i] = dp[i-1]*2 - dp[i-4] - dp[i-5]
    else:
        dp[i] = dp[i-1]*2
     
print(dp[N])
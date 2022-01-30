"""
"""
import sys
input = sys.stdin.readline
N = int(input())

dp = [[0 for i in range(2)] for i in range(3)]
tmp = list(map(int, input().split()))

dp[0] = [tmp[0], tmp[0]]
dp[1] = [tmp[1], tmp[1]]
dp[2] = [tmp[2], tmp[2]]
for i in range(1, N):
    tmp = list(map(int, input().split()))
    # 1
    t = dp[0] + dp[1]
    t1max = tmp[0] + max(t)
    t1min = tmp[0] + min(t)

    # 2
    t = dp[0] + dp[1] + dp[2]
    t2max = tmp[1] + max(t)
    t2min = tmp[1] + min(t)
    # 3
    t = dp[1] + dp[2]
    t3max = tmp[2] + max(t)
    t3min = tmp[2] + min(t)
    dp = [[t1max, t1min], [t2max, t2min], [t3max, t3min]]
tmp = dp[0]+dp[1]+dp[2]
print(max(tmp), min(tmp))

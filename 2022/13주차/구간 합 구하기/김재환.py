"""
dp 스멜난다.
왜냐하면 N<1000000인데 구간합이 K<=10000 이므로 매번 구하면 1,000,000 * 10,000이 되어 너무 100억이 되버림

"""
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

nums = [0]
dp = [0 for i in range(N+1)]
for i in range(1, N+1):
    tmp = int(input())
    nums.append(tmp)
    dp[i] += dp[i-1] + tmp
for _ in range(M+K):
    c, i, v = map(int, input().split())

    if c == 1:  # 변환
        diff = v - nums[i]
        for j in range(i, len(nums)):
            dp[j] += diff
    else:  # 합구하기
        print(dp[v] - dp[i-1])

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(len(cost))]
result = sum(cost)
for i in range(1, n + 1):
    for j in range(len(dp[1])):
        if cost[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            # i번째 어플 비활성화 여부
            dp[i][j] = max(dp[i - 1][j - cost[i]] + memory[i], dp[i - 1][j])
        if dp[i][j] >= m:
            result = min(result, j)
if m == 0:
    print(0)
else:
    print(result)

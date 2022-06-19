#7579 앱

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int,input().split())
    memory = [0] + list(map(int, input().split()))
    cost = [0] + list(map(int, input().split()))
    len_cost = len(cost)
    result = sum(cost)    
    dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(len_cost + 1)]

    for i in range(1, len_cost):
        for j in range(len(dp[1])):
            if cost[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - cost[i]] + memory[i], dp[i - 1][j])

            if dp[i][j] >= m:
                result = min(result, j)
    if m != 0:
        print(result)
    else:
        print(0)

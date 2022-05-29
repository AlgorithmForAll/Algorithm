"""
참고: https://claude-u.tistory.com/445
"""
n, m = map(int, input().split())
app = list(map(int, input().split()))
cost = list(map(int, input().split()))
D = [[0 for __ in range(sum(cost)+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, sum(cost)+1):
        if cost[i-1] > j:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(D[i-1][j], D[i-1][j-cost[i-1]]+app[i-1])
for i in range(1, sum(cost)+1):
    if D[n][i] >= m:
        print(i)
        break


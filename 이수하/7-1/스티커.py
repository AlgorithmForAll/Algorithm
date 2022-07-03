import sys
input = sys.stdin.readline


T = int(input())
for i in range(T):
    N = int(input())
    
    arr = []
    for j in range(2):
        arr.append(list(map(int, input().split())))
    
    dp = [[0]*N for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    
    for i in range(1, N):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + arr[0][i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + arr[1][i])
        
    print(max(dp[0][-1], dp[1][-1]))
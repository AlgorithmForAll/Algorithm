'''
dp 문제
최소값
'''

import sys
input = sys.stdin.readline


N, K = map(int, input().split())

coin = []
for i in range(N):
    coin.append(int(input()))

dp = [ 10001 for i in range(K+1)]

dp[0] = 0
for i in coin:
    for j in range(i, K+1):
        if dp[j-i] != 10001:
            dp[j] = min(dp[j], dp[j-i]+1)
if dp[K] == 10001:
    print(-1)    
else:   
    print(dp[K])
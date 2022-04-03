"""
합분해
https://www.acmicpc.net/problem/2225
참고 : https://suri78.tistory.com/105
"""
import sys
import os


os.system("cls")
sys.stdin = open("BOJ\input.txt")

for _ in range(2):
    n, k = map(int, input().split())
    dp = [[1 for _ in range(n + 1)] for _ in range(k)]
    for i in range(1, k):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
    print(dp[k - 1][n])

"""
동전 2
https://www.acmicpc.net/problem/2294
참고 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=occidere&logNo=220794872664

dp[목표금액]
"""
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline

inf = 100001
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [inf for _ in range(k + 1)]
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)  # 1 : coin원짜리 동전 1개

print(dp[-1] if dp[-1] != inf else -1)

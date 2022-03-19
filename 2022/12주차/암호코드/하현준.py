"""
암호코드
https://www.acmicpc.net/problem/2011
"""

import sys

sys.stdin = open("BOJ\input.txt")
snum = [str(i + 1) for i in range(26)]


for _ in range(int(input())):
    cipher = input()
    if cipher == "":
        print(0)
    elif cipher[0] not in snum:
        print(0)
    else:
        n = len(cipher)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if cipher[i - 1:i] in snum:
                dp[i] += dp[i - 1]
            if cipher[i - 2:i] in snum:
                dp[i] += dp[i - 2]
        print(dp[n] % 1000000)

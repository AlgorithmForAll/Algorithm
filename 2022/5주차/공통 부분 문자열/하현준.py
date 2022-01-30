"""
공통 부분 문자열
https://www.acmicpc.net/problem/5582
LCS 알고리즘 외우자 그냥
"""
import sys

sys.stdin = open("../input.txt")

answer = 0
A = input()
B = input()
dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
            answer = max(answer, dp[i + 1][j + 1])

print(answer)

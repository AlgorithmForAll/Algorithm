"""
https://www.acmicpc.net/problem/14002
"""
import sys

sys.stdin = open("../input.txt")

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

# i위치까지의 증가 부분 수열 길이 구하기
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
m_len = max(dp)
print(m_len)

# 수열 출력하기
data = []
for i in range(n - 1, -1, -1):
    if dp[i] == m_len:
        m_len -= 1
        data.append(arr[i])

print(*data[::-1], sep=" ")

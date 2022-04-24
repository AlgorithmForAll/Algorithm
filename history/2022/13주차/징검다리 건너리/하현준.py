"""
징검다리 건너기
https://www.acmicpc.net/problem/21317
"""

import sys

sys.stdin = open("BOJ\input.txt")
sys.setrecursionlimit(10 ** 6)


def dfs(stone, bcount, cost):
    if stone == n - 1:
        dp[stone] = min(dp[stone], cost)
        return

    # 작은 점프, 큰 점프
    for gap in range(1, 3):
        next_stone = stone + gap
        new_cost = cost + jdata[stone][gap - 1]
        if 0 <= next_stone < n:
            dfs(next_stone, bcount, new_cost)
    # 매우 큰 점프
    if bcount == 1:
        next_stone = stone + 3
        new_cost = cost + k
        if 0 <= next_stone < n:
            dfs(next_stone, 0, new_cost)


inf = float('inf')
n = int(input())
jdata = [list(map(int, input().split())) for _ in range(n - 1)]
k = int(input())
dp = [inf for _ in range(n)]
dp[0] = 0
dfs(0, 1, 0)
print(dp[-1])

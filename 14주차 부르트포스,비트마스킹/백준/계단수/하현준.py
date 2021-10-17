"""
계단 수
https://www.acmicpc.net/problem/1562
참고 : https://peisea0830.tistory.com/56
"""


def dfs(x, visited):
    xlen = len(str(x))
    end = int(str(x)[-1])

    if xlen > n:
        return 0

    if xlen == n:
        if visited == (1 << 10) - 1:
            return 1
        return 0

    if dp[xlen][end][visited] != -1:
        return dp[xlen][end][visited]

    count = 0
    for i in [-1, 1]:
        num = end + i
        if 0 <= num < 10:
            count += dfs(int(f"{x}{num}"), visited | (1 << num))
    dp[xlen][end][visited] = count
    return dp[xlen][end][visited]


n = int(input())
total = 0
dp = [[[-1 for _ in range(1 << 10)] for _ in range(10)] for _ in range(n + 1)]
for begin in range(1, 10):
    total += dfs(begin, 2 ** begin)
print(total % 10 ** 9)

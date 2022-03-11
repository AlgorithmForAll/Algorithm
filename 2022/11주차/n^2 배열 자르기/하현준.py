"""
2 x n 타일링
https://programmers.co.kr/learn/courses/30/lessons/12900
"""


def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % (10 ** 9 + 7)
    return dp[-1] % (10 ** 9 + 7)


print(solution(4), 5)
print(solution(60000))

"""
등굣길
https://programmers.co.kr/learn/courses/30/lessons/42898
"""
dx = [0, 1]
dy = [1, 0]


def solution(m, n, puddles):
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    def dfs(x, y):
        if not (0 <= x < n and 0 <= y < m):
            return 0
        if [y + 1, x + 1] in puddles:
            return 0
        if [x, y] == [n - 1, m - 1]:
            return 1

        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 0
        for i in range(2):
            dp[x][y] += dfs(x + dx[i], y + dy[i]) % (10 ** 9 + 7)

        return dp[x][y]

    answer = dfs(0, 0)
    return answer


print(solution(4, 3, [[2, 2]]), 4)
print(solution(4, 3, [[2, 2], [3, 2]]), 4)

"""
[카카오 인턴] 경주로 건설
https://programmers.co.kr/learn/courses/30/lessons/67259
"""
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dd = [0, 1, 2, 3]
INF = float('inf')


def solution(board):
    answer = float('inf')
    n = len(board)
    dp = [[[INF for _ in range(n)] for _ in range(n)] for _ in range(4)]  # 4방향에 대한 dp
    q = deque([[0, 0, 0, -1]])
    while q:
        x, y, cost, old_direct = q.popleft()

        if [x, y] == [n - 1, n - 1]:
            answer = min(answer, cost)
            continue

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n:
                new_direct = dd[i]
                new_cost = cost + 100 if old_direct == -1 or old_direct == new_direct else cost + 600
                if board[xx][yy] == 0 and dp[new_direct][xx][yy] > new_cost:
                    dp[new_direct][xx][yy] = new_cost
                    q.append([xx, yy, new_cost, new_direct])
    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 900)
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]), 2100)
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]]), 3200)
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]), 3800)
print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]), 3000)

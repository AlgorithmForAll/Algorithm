"""
블록 이동하기
https://programmers.co.kr/learn/courses/30/lessons/60063
"""
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

rotate = [
    [[[-1, -1, -1, 0], [1, -1, 1, 0]], [[-1, 1, -1, 0], [1, 1, 1, 0]]],
    [[[-1, 1, 0, 1], [-1, -1, 0, -1]], [[1, -1, 0, -1], [1, 1, 0, 1]]]
]


def solution(board):
    n = len(board)

    def bfs():
        visited = set()
        visited.add(((0, 0), (0, 1)))
        q = deque([[[(0, 0), (0, 1)], 0]])
        while q:
            robot, count = q.popleft()
            if (n - 1, n - 1) in robot:
                return count

            check = 0 if robot[0][0] == robot[1][0] else 1  # 0 : 세로, 1 :  가로

            for standard in range(2):  # 왼쪽 기준, 오른쪽 기준
                sx, sy = robot[standard]  # 기준
                xx, yy = robot[~standard]  # 반대쪽
                for i in range(2):  # 회전 2회
                    rx, ry, cx, cy = rotate[check][standard][i]
                    xxrx = xx + rx
                    yyry = yy + ry
                    if 0 <= xxrx < n and 0 <= yyry < n:
                        if board[xx + cx][yy + cy] == 0 and board[xxrx][yyry] == 0:
                            temp = tuple(sorted([(sx, sy), (xxrx, yyry)]))
                            if temp not in visited:
                                visited.add(temp)
                                q.append([list(temp), count + 1])

            sx, sy = robot[0]
            xx, yy = robot[1]
            for i in range(4):  # 상하좌우
                xxdx = xx + dx[i]
                yydy = yy + dy[i]
                sxdx = sx + dx[i]
                sydy = sy + dy[i]
                if (0 <= xxdx < n and 0 <= yydy < n) and (0 <= sxdx < n and 0 <= sydy < n):
                    if board[xxdx][yydy] == 0 and board[sxdx][sydy] == 0:
                        temp = tuple(sorted([(sxdx, sydy), (xxdx, yydy)]))
                        if temp not in visited:
                            visited.add(temp)
                            q.append([list(temp), count + 1])

    return bfs()


print(solution(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 0]]), 33)
print(solution(
    [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]), 11)
print(solution(
    [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
), 21)
print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]), 7)

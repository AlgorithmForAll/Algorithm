"""
퍼즐 조각 채우기
https://programmers.co.kr/learn/courses/30/lessons/84021
"""

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def get_pieces(n, data):
    pieces = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and data[i][j] == 1:
                visited[i][j] = 1
                q = deque([[i, j]])
                piece = [[i, j]]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < n and 0 <= yy < n:
                            if visited[xx][yy] == 0 and data[xx][yy] == 1:
                                visited[xx][yy] = 1
                                q.append([xx, yy])
                                piece.append([xx, yy])

                xs, ys = list(zip(*piece))
                mxs, mys = max(xs), max(ys)
                offx, offy = min(xs), min(ys)
                piece = [[px - offx, py - offy] for px, py in piece]

                pn = max(abs(mxs - offx + 1), abs(mys - offy + 1))
                result = []
                for a in range(pn):
                    temp = []
                    for b in range(pn):
                        temp.append(1 if [a, b] in piece else 0)
                    result.append(temp)

                pieces.append(result)
    return pieces


def insert_check(n, i, j, game_board, tp):
    tn = len(tp)
    fill = []
    for x in range(tn):
        for y in range(tn):
            if tp[x][y] == 1:
                xx = x + i
                yy = y + j
                if 0 <= xx < n and 0 <= yy < n:
                    if game_board[xx][yy] == 0:
                        game_board[xx][yy] += 1
                        fill.append([xx, yy])
                    else:
                        return fill, False
                else:
                    return fill, False
    return fill, True


def padding_check(n, game_board, fill):
    for fx, fy in fill:
        for k in range(4):
            fxx = fx + dx[k]
            fyy = fy + dy[k]
            if 0 <= fxx < n and 0 <= fyy < n:
                if game_board[fxx][fyy] != 1:
                    return False
    return True


def simulate(n, tp, game_board):
    t = len(tp)
    for i in range(1-t, n):
        for j in range(1-t, n):
            for _ in range(4):
                fill, check = insert_check(n, i, j, game_board, tp)
                if check:
                    if padding_check(n, game_board, fill):
                        return len(fill)
                    else:
                        for fx, fy in fill:
                            game_board[fx][fy] -= 1
                else:
                    for fx, fy in fill:
                        game_board[fx][fy] -= 1

                tp = list(map(list, zip(*tp[::-1])))
    return 0


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    table_piece = get_pieces(len(table), table)

    for tp in table_piece:
        answer += simulate(n, tp, game_board)

    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]), 14)
print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]), 0)
print(solution([[1, 0, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 1, 1], [1, 0, 1]]), 6)
print(solution(
    [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
     [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
     [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
     [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
    [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
     [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]),
    54)
"""
[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1]
[0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
[0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1]
[0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0]
[1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0]
[0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0]
[0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1]
[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
"""
"""
[1차] 프렌즈4블록
https://programmers.co.kr/learn/courses/30/lessons/17679
"""
dx = [0, 1]
dy = [1, 0]


def solution(m, n, board):
    board = list(map(list, zip(*[list(x) for x in board])))
    while True:
        blocks = []
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] != "_":
                    data = [[i, j]]
                    for k in range(2):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0 <= x < n and 0 <= y < m:
                            if board[x][y] != "_" and board[x][y] == board[i][j]:
                                data.append([x, y])
                    if len(data) == 3 and board[i + 1][j + 1] == board[i][j]:
                        data.append([i + 1, j + 1])
                        blocks.append(data)
        if not blocks:
            break
        for block in blocks:
            for bx, by in block:
                board[bx][by] = ""
        for i in range(n):
            board[i] = "".join(board[i])
            board[i] = list("_" * (m - len(board[i])) + board[i])

    return sum(board, []).count("_")


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]), 14)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]), 15)

def solution(board):
    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1
    for d in board:
        maxv = max(d)
        answer = max(answer, maxv)

    return answer**2

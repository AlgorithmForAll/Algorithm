def solution(board):
    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = 1 + min(board[i-1][j-1], board[i-1][j], board[i][j-1])
    for i in range(len(board)):
        if max(board[i]) > answer:
            answer = max(board[i])
    return answer**2
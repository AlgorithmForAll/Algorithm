def solution(board):
    row = len(board)
    col = len(board[0])
    answer = 0

    dp = [[0] * col for _ in range(row)]
    # 만들 수 있는 정사각형 변의 길이 구하기
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    # 테이블에서 최댓값 찾기
    for i in range(row):
        for j in range(col):
            answer = max(answer, dp[i][j])

    return pow(answer, 2)
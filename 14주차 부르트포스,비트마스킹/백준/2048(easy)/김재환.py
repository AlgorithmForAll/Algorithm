N = int(input())
Board = []

for _ in range(N):
    Board.append(list(map(int, input().split())))


def add(board, dir):
    if dir == 0:  # 동
        for i in range(N):
            for j in range(N-1, 0, -1):
                if board[i][j] == 0:  # 값을 가져오기
                    n = j-1
                    while 0 <= n:
                        if board[i][n] != 0:  # 값이 있으면 가져오기
                            board[i][j] = board[i][n]
                            board[i][n] = 0
                            break
                        n -= 1
                if board[i][j] != 0:  # 값이 있으면 비교시작
                    n = j-1
                    while 0 <= n:
                        if board[i][n] == 0:  # 다음으로
                            n -= 1
                        elif board[i][j] == board[i][n]:  # 값이 같으면 합치기
                            board[i][j] += board[i][n]
                            board[i][n] = 0
                            break
                        elif board[i][j] != board[i][n]:  # 값이 다르면 버리기
                            break
    elif dir == 1:  # 서
        for i in range(N):
            for j in range(N-1):
                if board[i][j] == 0:  # 값을 가져오기
                    n = j+1
                    while n < N:
                        if board[i][n] != 0:  # 값이 있으면 가져오기
                            board[i][j] = board[i][n]
                            board[i][n] = 0
                            break
                        n += 1
                if board[i][j] != 0:  # 값이 있으면 비교시작
                    n = j+1
                    while n < N:
                        if board[i][n] == 0:  # 다음으로
                            n += 1
                        elif board[i][j] == board[i][n]:  # 값이 같으면 합치기
                            board[i][j] += board[i][n]
                            board[i][n] = 0
                            break
                        elif board[i][j] != board[i][n]:  # 값이 다르면 버리기
                            break
    elif dir == 2:  # 남
        for j in range(N):
            for i in range(N-1, 0, -1):
                if board[i][j] == 0:  # 값을 가져오기
                    n = i-1
                    while 0 <= n:
                        if board[n][j] != 0:  # 값이 있으면 가져오기
                            board[i][j] = board[n][j]
                            board[n][j] = 0
                            break
                        n -= 1
                if board[i][j] != 0:  # 값이 있으면 비교시작
                    n = i-1
                    while 0 <= n:
                        if board[n][j] == 0:  # 다음으로
                            n -= 1
                        elif board[i][j] == board[n][j]:  # 값이 같으면 합치기
                            board[i][j] += board[n][j]
                            board[n][j] = 0
                            break
                        elif board[i][j] != board[n][j]:  # 값이 다르면 버리기
                            break
    else:  # 북
        for j in range(N):
            for i in range(N-1):
                if board[i][j] == 0:  # 값을 가져오기
                    n = i+1
                    while n < N:
                        if board[n][j] != 0:  # 값이 있으면 가져오기
                            board[i][j] = board[n][j]
                            board[n][j] = 0
                            break
                        n += 1
                if board[i][j] != 0:  # 값이 있으면 비교시작
                    n = i+1
                    while n < N:
                        if board[n][j] == 0:  # 다음으로
                            n += 1
                        elif board[i][j] == board[n][j]:  # 값이 같으면 합치기
                            board[i][j] += board[n][j]
                            board[n][j] = 0
                            break
                        elif board[i][j] != board[n][j]:  # 값이 다르면 버리기
                            break


def maxval(board):
    big = 0
    for i in range(N):
        for j in range(N):
            big = max(big, board[i][j])
    return big


def copyBoard(board):
    tmp = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = board[i][j]
    return tmp


Big = 0


def DFS(Board):
    global Big
    s = [[Board, -1]]
    while s:
        board, cnt = s.pop()
        if cnt == 5:
            # 최고값을 찾아보기
            Big = max(Big, maxval(b))
            continue
        for i in range(4):
            # board copy
            b = copyBoard(board)
            add(b, i)
            s.append([b, cnt+1])


DFS(Board)
# print(Big)
#add(Board, 3)
print(Big)

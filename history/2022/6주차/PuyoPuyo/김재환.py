"""
1. 터뜨리기 가능한지 확인 => DFS로 필요한 부분들을 확인한다. 12*6만큼 반복(visited필요함)
    성공시 true반환
    실패시 false반환
2. 모든 값 내려오기 (그냥 전부 내려오게 함)
"""


board = []
for i in range(12):
    board.append(list(input()))

count = 0


def DFS(start, visited):
    s = [start]

    dy = [-1, 1, 0, 0]  # 상하 좌우
    dx = [0, 0, -1, 1]

    visited[start[0]][start[1]] = 1
    color = board[start[0]][start[1]]

    sameColor = [start]

    while s:
        t = s.pop()
        y, x = t

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if (0 <= ny < 12) and (0 <= nx < 6) and board[ny][nx] == color and visited[ny][nx] == 0:
                sameColor.append([ny, nx])
                s.append([ny, nx])
                visited[ny][nx] = 1

    if len(sameColor) >= 4:  # 실제 4개 이상 존재하여 제거진행
        for i in sameColor:
            y, x = i
            board[y][x] = '.'
        return True
    else:
        return False


def puyoPop():

    visited = [[0 for i in range(6)]for i in range(12)]
    deleteCount = 0
    # DFS로 제거하기
    for i in range(12):
        for j in range(6):
            if board[i][j] != "." and visited[i][j] == 0:
                if DFS([i, j], visited):
                    deleteCount += 1
    if deleteCount > 0:
        return True
    else:
        return False


def slideDown():  # 모든 데이터를 아래로 밀어준다.

    for j in range(6):

        s = 10
        d = 11
        while s >= 0 and d > 0:
            if board[d][j] == ".":  # 서치 시작
                if board[s][j] != ".":
                    board[d][j] = board[s][j]
                    board[s][j] = '.'
                    d -= 1
                    s -= 1
                else:
                    s -= 1
            else:
                d -= 1
                s -= 1


while puyoPop():
    count += 1
    slideDown()
print(count)

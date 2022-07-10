"""
참고:
https://developer-ellen.tistory.com/64
(급박하게 시작하느라 시간 단축을 위해 참고를 해가면서 풀었습니다ㅠㅠ)
"""

direction = {}
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
pan = [[[] for _ in range(n)] for _ in range(n)]
horse = [0]

for i in range(1, k+1):
    a, b, c = map(int, input().split())
    pan[a-1][b-1].append(i)
    horse.append([a-1, b-1, c])

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


count = 0
while count <= 1000:
    count += 1
    for i in range(1, k+1):
        a, b, c = horse[i]
        nx = a + dx[c]
        ny = b + dy[c]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2: #파란색인 경우 방향 바꾸기
            if c == 1:
                c = 2
            elif c == 3:
                c = 4
            elif c == 2:
                c = 1
            elif c == 4:
                c = 3
            horse[i][2] = c
            nx = a + dx[c]  #한번 더 전진
            ny = b + dy[c]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
                continue

        horse_up = [] #현재 말부터 그 위의 말들 다 쌓아올리기
        for idx, num in enumerate(pan[a][b]): #현재 말 위에있는 말들 움직이도록 설계
            if num == i:
                horse_up.extend(pan[a][b][idx:])
                pan[a][b] = pan[a][b][:idx] #남아있는 말들
                break

        if board[nx][ny] == 1: #빨간색일 경우 뒤집어놓음
            horse_up = horse_up[-1::-1]

        for h in horse_up:  #말 전체 이동
            horse[h][0], horse[h][1] = nx, ny
            pan[nx][ny].append(h)

        if len(pan[nx][ny]) >= 4: #4개의 말이 쌓이는 순간 게임 종료
            print(count)
            exit(0)

print(-1)
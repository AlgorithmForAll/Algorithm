'''
문제를 잘 읽자
- 매번 로봇 리스트의 x,y,direction 값 체크
- 한번 이동할 때 마다 업데이트
- x,y 좌표 [B-y][x-1]
'''

import sys
input = sys.stdin.readline


A, B = map(int, input().split())
N, M = map(int, input().split())

land = [[0 for i in range(A)] for i in range(B)]

location = {'N': 0, 'W': 1, 'S': 2, 'E': 3}

# 북 서 남 동 NWSE
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 로봇의 초기 위치
robot_list = [0]
for i in range(1, N+1):
    x, y, direction = map(str, input().split())
    x = int(x)
    y = int(y)
    
    robot_list.append([B-y, x-1, location[direction]])
    land[B-y][x-1] = i

# 로봇 명령
orders = []
for i in range(M):
    robot, command, repeat = map(str, input().split())

    orders.append([int(robot), command, int(repeat)])

check = True
flag = False
for order in orders:
    robot, command, repeat = order

    if command == 'F':
        for i in range(repeat):
            x, y, direction = robot_list[robot]

            nx = x + dx[direction]
            ny = y + dy[direction]
            
            if 0 > nx or nx >= B or 0 > ny or ny >= A:
                flag = True
                print(f'Robot {robot} crashes into the wall')
                exit()
            if land[nx][ny] != 0:
                flag = True
                print(f'Robot {robot} crashes into robot {land[nx][ny]}')
                exit()
                
            land[x][y] = 0
            land[nx][ny] = robot
            robot_list[robot] = [nx, ny, direction]
    # 회전
    elif command == 'R':
        x, y, direction = robot_list[robot]
        direction = (direction + 3*repeat)%4
        robot_list[robot] = [x, y, direction]
        
    elif command == 'L':
        x, y, direction = robot_list[robot]
        direction = (direction + 1*repeat)%4
        robot_list[robot] = [x, y, direction]
    
    if flag:
        check = False
        break
   
if check:
    print("OK")
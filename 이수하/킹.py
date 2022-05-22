'''
시뮬레이션 문제
행의 시작이 8부터 => 8-i
'''

import sys
input = sys.stdin.readline


# 방향 
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

# 방향 dict
direc = {'R': 0, 'L':1, 'B': 2, 'T': 3, 'RT': 4, 'LT': 5, 'RB': 6, 'LB': 7}

chess = [[0 for i in range(8)] for i in range(8)]

king, rock, N = map(str, input().split())

king = king.strip()
rock = rock.strip()
N = int(N)

# 돌 위치
chess[8-int(rock[1])][ord(rock[0])-65] = 1

location = [[8-int(king[1]), ord(king[0])-65]]
rock_location = [[8-int(rock[1]), ord(rock[0])-65]]

for i in range(N):
    command = input().rstrip()
    
    x, y = location.pop()

    nx = x + dx[direc[command]]
    ny = y + dy[direc[command]]
    
    if nx > 7 or nx < 0 or ny > 7 or ny < 0:
        location.append([x, y])
        continue
    if chess[nx][ny] == 1:
        r_nx = nx + dx[direc[command]]
        r_ny = ny + dy[direc[command]]
        if r_nx > 7 or r_nx < 0 or r_ny > 7 or r_ny < 0:
            location.append([x, y])
            continue
        else:
            rock_location.pop()
            chess[nx][ny] = 0
            chess[r_nx][r_ny] = 1
            rock_location.append([r_nx, r_ny])
            location.append([nx, ny])
    else:
        location.append([nx, ny])
    
king = [chr(location[0][1]+65), 8 - location[0][0]]
rock = [chr(rock_location[0][1]+65), 8 - rock_location[0][0]]

print(''.join(map(str, king)))
print(''.join(map(str, rock)))
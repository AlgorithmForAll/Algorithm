'''
밖에서 안으로 돌기
right, down, left, up 방향에 따라 값 넣기

넣다가 자연수 찾으면 자연수값 좌표 저장해놓기
'''

import sys
input = sys.stdin.readline


N = int(input())
num = int(input())

box = [[0 for i in range(N)] for i in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0

index = N * N
box[x][y] = index

check = 0

# 자연수 좌표 저장할 변수
a = 0
b = 0

index -= 1

while index > 0:
    nx = x + dx[check]
    ny = y + dy[check]
    
    if 0 <= nx < N and 0 <= ny < N and not box[nx][ny]:
        box[nx][ny] = index
        if num == index:
            a = nx
            b = ny
        x = nx
        y = ny
        index -= 1
    else:
        check = (check+1)%4

for i in range(N):
    print(*box[i])

print(a+1, b+1)
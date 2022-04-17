'''
아기상어2
(N,M)의 직사각형에서, 1과의 거리가 가장 먼 거리(대각선 포함)
'''
from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N,M = map(int,input().split())
	arr = list(list(map(int,input().split())) for _ in range(N))
	distance = [[-1] * M for _ in range(N)] #visited 겸 거리 
	dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

	# 상어 위치 구하기 
	sharks = deque()
	for i in range(N):
		for j in range(M):
			if arr[i][j] == 1:
				sharks.append((i,j))
				distance[i][j] = 0
	
	while sharks:
		cx,cy = sharks.popleft()
		for k in range(8):
			nx = cx + dir[k][0]
			ny = cy + dir[k][1]
			if nx < 0 or nx >= N or ny < 0 or ny >= M:
				continue

			if distance[nx][ny] == -1:
				distance[nx][ny] = distance[cx][cy] + 1
				sharks.append((nx,ny))
			
	print(max(map(max,distance)))

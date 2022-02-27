#1600 말이 되고픈 원숭이
# (0,0) -> (N-1,N-1)으로 이동해야 하고, 인접 칸으로 이동할 수 있고, 최대 K번을 말처럼 이동할 수 있다.(한칸 앞으로, 방향 바꿔서 두 칸 앞으로). 도착 지점까지 갈 수 있는 최소 이동 횟수는 ?
# 알고리즘 : BFS 
# 헷갈렸던 것 : 2차원 배열 한번에 입력받을 때, 첫번째 list는 []이 아닌 list()로 받아야 함
# **실패**

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
dir = [[-1,0], [0,1], [1,0], [0,-1]]

if __name__ == "__main__":
	K = int(input())
	W,H = map(int,input().split())
	arr = [list(map(int,input().split())) for _ in range(H)]

	answer = INF
	visited = [ [0] * W for _ in range(H)]
	q = deque()
	q.append( [0,K,0,0] ) #이동횟수,말로 이동가능한 횟수, (현재 좌표)

	while q:
		cnt,pk,cx,cy = q.popleft()
		nx = 0
		ny = 0
		# 도착 
		if (cx == H-1 and cy == W-1):
			answer = min(answer,cnt)
			break
		
		# 인접 이동 
		for k in range(4):
			nx = cx + dir[k][0]
			ny = cy + dir[k][1]
			if nx < 0 or nx >= H or ny < 0 or ny >= W:
				continue
			if arr[nx][ny] == 0:
				visited[nx][ny] += 1
				q.append([cnt+1,pk,nx,ny])
			#	print("11" + str(list([cnt+1,pk,nx,ny])))


		# 말처럼 이동
		if pk > 0:
			for k in range(4):
				for j in range(2):
					if j == 0:
						nx = cx + dir[k][0] + (2 * (dir[(k+1)%4][0]))
						ny = cy + dir[k][1] + (2 * (dir[(k+1)%4][1]))
					else:
						nx = cx + dir[k][0] + (2 * (dir[(k+3)%4][0]))
						ny = cy + dir[k][1] + (2 * (dir[(k+3)%4][1]))
					
					if nx < 0 or nx >= H or ny < 0 or ny >= W:
						continue
					
					visited[nx][ny] += 1
					q.append([cnt+1,pk-1,nx,ny])
				#	print("22" + str(list([cnt+1,pk-1,nx,ny])))

	if answer == INF:
		print('-1')
	else:
		print(answer)
	
			
	


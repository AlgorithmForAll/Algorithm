'''
14503 로봇청소기
구현
'''
import sys
input = sys.stdin.readline

if __name__ == "__main__":
	dir = [[-1,0],[0,1],[1,0],[0,-1]]
	N,M = map(int,input().split())
	sr,sc,sdir = map(int,input().split())
	arr = list(list(map(int,input().split())) for _ in range(N))
	visited = [[False] * M for _ in range(N)]
	
	#현재 지점부터 탐색 시작
	def go(cr, cc, cd, cnt):
		if visited[cr][cc] == False:
			visited[cr][cc] = True #현재 지점 청소
			cnt += 1

		flag = False #다음 청소 지점 탐색
		for k in range(-1,-5,-1):
			nd = (cd + k + 4) % 4
			nr = cr + dir[nd][0] 
			nc = cc + dir[nd][1]
			if nr < 0 or nr >= N or nc <= 0 or nc >= M:
				continue

			if arr[nr][nc] == 0 and visited[nr][nc] == False:
				flag = True
				cr = nr
				cc = nc
				cd = nd
				go(cr,cc,cd,cnt)
				break
		
		#네 방향 모두 청소가 이미 되어있거나 벽인 경우, 한 칸 후진한 후 2번으로 돌아간다  
		if flag == False:
			cr = cr - dir[cd][0]
			cc = cc - dir[cd][1]
			if arr[cr][cc] == 0:
				go(cr,cc,cd,cnt)
			else:
				print(cnt)
		
	go(sr,sc,sdir,0)

'''
1939 중량제한
공장이 있는 두 섬까지 한번의 이동에서 옮길 수 있는 최대 중량값을 구하라
알고리즘 : BFS / 이진탐색
고민되었던 부분 : 처음에 최단경로랑 헷갈렸지만, 원하는 것이 최단 경로가 아닌 최대 중량값이므로 그래프 탐색(bfs,dfs)로 구현
				  그래프 탐색은 목적지에 도달할 수 있는지 판단하는 기준으로 쓰이고, 최대 중량값을 구하는 건 이분탐색으로 구함 
처음 알았던 부분 : BFS + 이진탐색 같이 쓰는 방식 
'''
from collections import deque
import sys
input = sys.stdin.readline

# mid값을 증량값으로 했을 때 목적지까지 도달 가능한지 check
def bfs(mid):
	visited = [False] * (N+1)
	q = deque()
	q.append(st)
	visited[st] = True

	while q:
		cur = q.popleft()
		if cur == ed:
			return True

		for nex, ncost in graph[cur]:
			if visited[nex] == False and mid <= ncost:
				q.append(nex)
				visited[nex] = True
	return False


if __name__ == "__main__":
	N, M = map(int,input().split())
	graph = [[] for _ in range(N+1)] #각 섬에 연결되어있는 섬 정보 리스트
	answer = 0
	for _ in range(M):
		a,b,c = map(int,input().split())
		graph[a].append((b,c))
		graph[b].append((a,c))
	
	for i in range(1,N+1):
		graph[i].sort()
	
	st,ed = map(int,input().split())
	left,right = 1, int(1e9)
	while left <= right:
		mid = (left + right) // 2
		if bfs(mid) == True:
			answer = max(answer,mid)
			left = mid + 1
		else:
			right = mid - 1
	
	print(answer)
		

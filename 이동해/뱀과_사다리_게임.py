from collections import deque

n, m = map(int, input().split())
ladders = {}
snakes = {}

for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b

graph = [0] * 101
visited = [False] * 101 

def bfs(x):
    queue = deque()
    queue.append((x))
    while queue:
        x = queue.popleft()

        if x == 100:
            print(graph[x])
            break

        for i in range(1, 7):
            # 주사위 굴리기
            nx = x + i
            if nx <= 100 and not visited[nx]:
                # 뱀이 있으면 바로 이동
                if nx in snakes:
                    nx = snakes[nx]
                
                # 사다리가 있으면 바로 이동
                if nx in ladders:
                    nx = ladders[nx]

                # 다시 한 번 범위 확인 후 방문처리
                if not visited[nx]:
                    graph[nx] = graph[x] + 1
                    visited[nx] = True
                    queue.append(nx)            
bfs(1)

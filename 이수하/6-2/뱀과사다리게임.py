from collections import deque
import sys
input = sys.stdin.readline


def bfs(board):
    queue = deque()
    queue.append(board)
    check[board] = 0
    
    while queue:
        board = queue.popleft()
        for i in range(1, 7):
            N = board+i
            if N > 100:
                continue
            
            temp = graph[N]
            if check[temp] == -1:
                queue.append(temp)
                check[temp] = check[board]+1
                
                if temp == 100:
                    return
                
N, M = map(int, input().split())
graph = [i for i in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    graph[x] = y
    
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v
    
check = [-1]*101

bfs(1)

print(check[100])
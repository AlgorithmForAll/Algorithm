import sys
input = sys.stdin.readline


def dfs(graph, v, visited):
    global K
    global count

    visited[v] = True
    
    if not graph[v]:
        count += 1
        return
    
    for i in graph[v]:
        if i == K:
            if len(graph[v]) == 1:
                count += 1
            else: continue
        elif not visited[i]:
            dfs(graph, i, visited)
                
N = int(input())
d = list(map(int, input().split()))
K = int(input())

graph = [[] for i in range(N)]
count = 0

for i in range(N):
    if d[i] == -1:
        root = i
    else:
        graph[d[i]].append(i)

visited = [False] * (N+1)

if K == root:
    print(0)
else:
    dfs(graph, root, visited)
    print(count)
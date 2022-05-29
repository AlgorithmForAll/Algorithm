"""
유니온 파인드 조지고 서로다른거 뽑기 안됨
"""
import sys
input = sys.stdin.readline


N = int(input())
adj = {}
for n in range(N-2):
    a, b = map(int, input().split())
    if a not in adj:
        adj[a] = [b]
    else:
        adj[a].append(b)

    if b not in adj:
        adj[b] = [a]
    else:
        adj[b].append(a)
if len(adj) == 0:
    print("1 2")
    exit()


def DFS(visited, node):
    s = [node]
    visited[node] = 1
    while s:
        node = s.pop()
        visited[node] = 1

        for child in adj[node]:
            if visited[child] == 0:
                s.append(child)


visited = [0 for i in range(N+1)]

DFS(visited, list(adj.keys())[0])

for i in range(1, N+1):
    if visited[i] != 1:
        print(list(adj.keys())[0], i)
        exit()

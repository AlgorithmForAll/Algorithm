"""
ㄷ => DFS로 돌면서 깊이 3이면 count증가하고 종료
ㅈ => 교점이 3이상인 경우 연관 점C3으로 개수 구하기
"""
from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())
adj = {}
for _ in range(N-1):
    a, b = map(int, input().split())
    if a in adj:
        adj[a].append(b)
    else:
        adj[a] = [b]
    if b in adj:
        adj[b].append(a)
    else:
        adj[b] = [a]

count = 0

visited = [0 for i in range(N+1)]


def DFS(node, depth, visited):
    global d
    if depth == 3:
        d += 1
        return

    for nextNode in adj[node]:
        if visited[nextNode] == 0:
            visited[nextNode] = 1
            DFS(nextNode, depth+1, visited)

            visited[nextNode] = 0


d = 0
g = 0

visited[a] = 1
# 트리의 지름 끝점 구하기


# d 구하기
recur(1, 0, visited)
if d > g*3:
    print("D")
elif d < g*3:
    print("G")
else:
    print("DUDUDUNGA")

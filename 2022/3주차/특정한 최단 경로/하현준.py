"""
특정한 최단 경로
https://www.acmicpc.net/problem/1504
"""
import heapq


def dijkstra(start):
    distance = [float('inf') for _ in range(n + 1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node, ncost in path[now]:
            cost = dist + ncost
            if distance[node] > cost:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

    return distance


answer = -1
n, e = map(int, input().split())
path = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    path[a].append([b, c])
    path[b].append([a, c])
v1, v2 = map(int, input().split())

data = [dijkstra(i) for i in [1, v1, v2]]

answer = min(
    data[0][v1] + data[1][v2] + data[2][n],
    data[0][v2] + data[2][v1] + data[1][n]
)

print(answer if answer != float('inf') else -1)

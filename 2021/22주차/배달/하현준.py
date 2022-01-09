"""
배달
https://programmers.co.kr/learn/courses/30/lessons/12978
"""
import heapq

INF = float('inf')


def solution(N, road, K):
    answer = 0
    path = [[] for _ in range(N + 1)]
    for a, b, c in road:
        path[a].append([b, c])
        path[b].append([a, c])

    q = []
    distance = [INF for _ in range(N + 1)]
    distance[1] = 0
    heapq.heappush(q, (0, 1))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, ncost in path[now]:
            cost = dist + ncost
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, [cost, next_node])

    for d in distance[1:]:
        if d <= K:
            answer += 1
    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3), 4)
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4), 4)

"""
합승 택시 요금
https://programmers.co.kr/learn/courses/30/lessons/72413
"""
import heapq


def solution(n, s, a, b, fares):
    def dijkstra(start):
        distance = [INF for _ in range(n + 1)]
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue

            for node, ndist in path[now]:
                if distance[node] > dist + ndist:
                    distance[node] = dist + ndist
                    heapq.heappush(q, (distance[node], node))
        return distance

    INF = float('inf')
    answer = INF
    path = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        path[c].append([d, f])
        path[d].append([c, f])

    data = [[]] + [dijkstra(i) for i in range(1, n + 1)]
    for i in range(1, n + 1):
        answer = min(answer, data[i][s] + data[i][a] + data[i][b])
    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]), 82)
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]), 14)
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]),
      18)

inf = float('inf')
n, m = map(int, input().split())

edge = []
dist = [inf] * (n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((a, b, c))


def bellman(start):
    dist[start] = 0
    for v in range(n):
        for i in range(m):
            s = edge[i][0]
            c = edge[i][2]
            e = edge[i][1]
            if dist[s] != inf and dist[e] > c + dist[s]:
                dist[e] = c + dist[s]
                if v == n-1:
                    return True
    return False


if bellman(1):
    print(-1)
else:
    for i in range(2, len(dist)):
        print(dist[i]) if dist[i] != inf else print(-1)

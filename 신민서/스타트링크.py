def bfs(q, u, d, s, g, f):
    visited = [-1] * (f+1)
    visited[s] = 0
    q.append(s)
    while q:
        p = q.pop(0)
        if p+u <= f and visited[p+u] == -1:
            visited[p+u] = visited[p] + 1
            q.append(p+u)
        if p-d > 0 and visited[p-d] == -1:
            visited[p-d] = visited[p] + 1
            q.append(p-d)
    if visited[g] != -1:
        return visited[g]
    else:
        return 'use the stairs'

f, s, g, u, d = map(int, input().split())
q = []
print(bfs(q, u, d, s, g, f))
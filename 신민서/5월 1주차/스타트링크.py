"""
전형적인 그래프 탐색 문제.
f 크기의 배열을 생성한 다음에 s부터 시작해서 큐에 넣어주고 g에 도달할 때까지 bfs를 반복해주면 된다.
"""
def bfs(q, u, d, s, g, f):
    visited = [-1] * (f+1)
    visited[s] = 0
    q.append(s) #시작점 큐에 추가
    while q:
        p = q.pop(0)
        if p+u <= f and visited[p+u] == -1: #u를 더한게 제일 꼭대기 층보다 작거나 같고 p+u를 방문하지 않았을 경우
            visited[p+u] = visited[p] + 1
            q.append(p+u)
        if p-d > 0 and visited[p-d] == -1: #d만큼 뺀게 1보다 크거나 같고 p-d를 방문한 적이 없을 때.
            visited[p-d] = visited[p] + 1
            q.append(p-d)
    if visited[g] != -1:
        return visited[g]
    else: #visited[g]가 -1이면 도달할 수 없는 경우이다.
        return 'use the stairs'

f, s, g, u, d = map(int, input().split())
q = []
print(bfs(q, u, d, s, g, f))
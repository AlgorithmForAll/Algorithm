"""
1. 각 육지의 서로다른 표시해주기
2. 가로의 경우 ,세로의 경우 다리의 코스트와 방향구하기
3. 하나씩 뽑으면서 유니온 파인드로 MST 구현하기
"""

import heapq
N, M = map(int, input().split())
Map = []
for i in range(N):
    tmp = list(map(int, input().split()))
    Map.append(tmp)


def DFS(land, start, visited):
    dy = [-1, 1, 0, 0]  # 상하 좌우
    dx = [0, 0, -1, 1]
    visited[start[0]][start[1]] = land
    s = [start]
    while s:
        y, x = s.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < N) and (0 <= nx < M) and Map[ny][nx] != 0 and visited[ny][nx] == 0:
                s.append([ny, nx])
                visited[ny][nx] = land


# 대륙 마킹하기
visited = [[0 for i in range(M)] for i in range(N)]
land = 1
for i in range(N):
    for j in range(M):
        if Map[i][j] != 0 and visited[i][j] == 0:
            DFS(land, [i, j], visited)
            land += 1
_Map = visited
# 가로의 가능한 수 구하기
hq = []
for i in range(N):
    for j in range(M):
        if _Map[i][j] != 0 and (0 < j+1 < M) and _Map[i][j+1] == 0:  # 육지끝에서 육지로 이동
            cost = 0
            nj = j+1
            while (0 < nj < M) and _Map[i][nj] == 0:
                cost += 1
                nj += 1
            if nj != M and cost >= 2:
                heapq.heappush(hq, [cost, _Map[i][j], _Map[i][nj]])
        if _Map[i][j] != 0 and (0 < i+1 < N) and _Map[i+1][j] == 0:  # 세로의 가능한 수 구하기
            cost = 0
            ni = i+1
            while (0 < ni < N) and _Map[ni][j] == 0:
                cost += 1
                ni += 1
            if ni != N and cost >= 2:
                heapq.heappush(hq, [cost, _Map[i][j], _Map[ni][j]])
# 유니오 파인드 가즈아


def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, cost, A, B):
    A = find(parent, A)
    B = find(parent, B)
    if A == B:  # 같은 노드에 속한 경우
        return False
    elif A < B:
        parent[B] = A
    else:
        parent[A] = B
    return True


parent = [i for i in range(land)]
final = 0
while hq:
    cost, A, B = heapq.heappop(hq)
    if union(parent, cost, A, B):
        final += cost
for i in range(1, land):
    find(parent, i)
    if parent[i] != 1:
        print(-1)
        exit()
print(final)

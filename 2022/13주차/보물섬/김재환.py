"""
BFS로 최솟값 구하는건 팩트인데
문제는 이걸 모든 노드에서 판단하는게 불가능하다.
따라서 서로 멀어야 하기 때문에 바다와 접한 모든 노드를 기준으로 BFS 삽질을 한다.
그럼 답이 나온다. 시간복잡도가 안나와서 계속 고민하다 말림
"""


from collections import deque
R, C = map(int, input().split())
M = []

dy = [-1, 1, 0, 0]  # 상하 좌우
dx = [0, 0, -1, 1]
L = []
for i in range(R):
    tmp = list(input())
    M.append(tmp)


def DFS(start, visited):
    s = [start]
    tmp = []
    while s:
        y, x = s.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if M[ny][nx] == 'W' and visited[ny][nx] == 0:
                    s.append((ny, nx))
                    visited[ny][nx] = 1
                elif M[ny][nx] == 'L':
                    tmp.append((ny, nx))
    return tmp


wvisited = [[0 for i in range(C)] for i in range(R)]

for i in range(R):
    for j in range(C):
        if M[i][j] == 'L':
            if i == 0 or j == 0:
                L.append((i, j))
        # 바다에 접한 친구들넣기
        elif M[i][j] == 'W' and wvisited[i][j] == 0:
            L += DFS([i, j], wvisited)
L = list(set(L))


def BFS(leaf):
    q = deque([leaf])

    visited = [[0 for i in range(C)] for i in range(R)]
    visited[leaf[0]][leaf[1]] = 1
    time = -1
    while q:
        time += 1
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < R and 0 <= nx < C and M[ny][nx] == 'L' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
    return time


answer = 0
# 리프부터 돌면서 BFS
for leaf in L:
    answer = max(answer, BFS(leaf))
print(answer)

from collections import deque


def DFS(Map):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]  # 동서 남북
    INF = 100000000

    visited = [[[INF for i in range(len(Map))]
                for i in range(len(Map))] for i in range(4)]

    q = deque([])  # 동 시작, 남 시작
    for z in range(4):
        visited[z][0][0] = 0
    # 0행1열 초기화
    if Map[0][1] != 1:
        q.append([0, 1, 0, 100])
        visited[0][1][0] = 100

    # 1행0열 초기화
    if Map[1][0] != 1:
        q.append([1, 0, 2, 100])
        visited[2][1][0] = 100

    while q:
        y, x, d, c = q.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < len(Map)) and (0 <= nx < len(Map)) and Map[ny][nx] == 0:
                if d != i:
                    nc = c + 600
                else:
                    nc = c + 100

                if visited[i][ny][nx] > nc:
                    q.append([ny, nx, i, nc])
                    visited[i][ny][nx] = nc
    for z in range(4):
        if INF > visited[z][len(Map)-1][len(Map)-1]:
            INF = visited[z][len(Map)-1][len(Map)-1]
    print(INF)
    return INF


def solution(board):
    answer = 0
    return DFS(board)


"""
from collections import deque
def DFS(Map):
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    INF = 100000000

    visited = [[INF for i in range(len(Map))] for i in range(len(Map))]
    
    q = deque([[1,0,1,100],[0,1,0,100]]) # y,x,d(0:수평, 1:수직)
    
    cost = []
    
    while q:
        y,x,d,c = q.popleft()
        
        if [y,x] == [len(Map)-1, len(Map)-1]:
            cost.append(c)
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0<=ny<len(Map)) and (0<=nx<len(Map)) and Map[ny][nx] == 0:
                if isHorizan(y,x,ny,nx)==d: # 같은 방향
                    q.append([ny,nx,d,c+100])
                else: # 다른방향
                    q.append([ny,nx,d^1,c+600])
    return min(cost)
                

def isHorizan(y,x, ny, nx):
    if y == ny and x != nx: # 수평
        return 0
    else: # 수직
        return 1
        

def solution(board):
    answer = 0
    return DFS(board)
"""

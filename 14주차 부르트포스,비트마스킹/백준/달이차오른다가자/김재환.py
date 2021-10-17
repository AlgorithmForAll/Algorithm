"""
최소이동횟수: BFS
키를 먹고 이동하는 경우가 필요해서 visited없음

1. 열쇠정보 update, 문을 만날때 어떻게 할것인가
2. 지나온 길을 되돌아가는 경우 발생

열쇠정보->비트마스크
방문기록-> 열쇠획득시에 방문기록 따져야함.
    => 열쇠획득시 새로운 방문기록을 사용하여 다음 단계로
    => 삼차원으로 만들기
    => [x][y][key]
"""
from collections import deque


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            sy, sx = i, j
            board[i][j] = '.'


def BFS(y, x):
    dy = [0, 0, 1, -1]  # 동서남북
    dx = [1, -1, 0, 0]
    check = [[[False]*(1 << 6) for _ in range(M)] for _ in range(N)]
    check[y][x][0] = True  # 0은 키가 하나도 없다는것

    q = deque([[y, x, 0, 0]])
    while q:
        y, x, cnt, key = q.popleft()
        if board[y][x] == '1':
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if not check[ny][nx][key]:  # 가지 않은 경우
                    if board[ny][nx] == '1' or board[ny][nx] == '.':
                        check[ny][nx][key] = True
                        q.append([ny, nx, cnt+1, key])
                    elif 'a' <= board[ny][nx] <= 'f':  # 키를 만나는경우
                        check[ny][nx][key] = True
                        new = ord(board[ny][nx])-ord('a')
                        new = key | (1 << new)
                        q.append([ny, nx, cnt+1, new])
                    elif 'A' <= board[ny][nx] <= 'F':
                        if key & (1 << ord(board[ny][nx])-ord('A')):
                            check[ny][nx][key] = True
                            q.append([ny, nx, cnt+1, key])
    return -1


print(BFS(sy, sx))

"""
from collections import deque
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
Map = []
Start = []
for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j] == '0':
            Start = [i, j]
    Map.append(tmp)
small = 1000000000000

print(Start, Map)


def BFS(start, key, move):
    global small
    print("start:", start, key, move)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q = deque([])
    visited = [[0 for i in range(M)] for i in range(N)]
    visited[start[0]][start[1]] = 1
    q.append([start, key, move])

    while q:
        print("q:", q)
        t, k, m = q.popleft()
        print("t:", t)
        y, x = t
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if (0 <= ny < N) and (0 <= nx < M) and visited[ny][nx] == 0:
                if Map[ny][nx] == '1':
                    print("111111", ny, nx, m+1)
                    small = min(small, m + 1)
                    return
                if Map[ny][nx] == '.' or Map[ny][nx] == '0':
                    visited[ny][nx] = 1
                    q.append([[ny, nx], k, m + 1])
                elif ord('A') <= ord(Map[ny][nx]) <= ord('F'):  # 문 인경우(A-F)
                    if k[ord(Map[ny][nx])-ord('A')] == 1:  # 키가 존재하는데 안쓴경우
                        k[ord(Map[ny][nx])-ord('A')] = 2  # 사용처리
                        BFS([ny, nx], list(k), m+1)  # 문제 막힐수 있음
                        k[ord(Map[ny][nx])-ord('A')] = 1  # 사용처리
                    elif k[ord(Map[ny][nx])-ord('A')] == 2:  # 이미 열려있다고 판단
                        visited[ny][nx] = 1
                        q.append([[ny, nx], k, m + 1])
                elif ord('a') <= ord(Map[ny][nx]) <= ord('f'):  # 키인경우
                    if k[ord(Map[ny][nx])-ord('a')] == 0:
                        k[ord(Map[ny][nx])-ord('a')] = 1
                        BFS([ny, nx], list(k), m+1)
                        k[ord(Map[ny][nx])-ord('a')] = 0
                    else:  # 이미 키를 가진상태 -> 넘어가야함
                        visited[ny][nx] = 1
                        q.append([[ny, nx], k, m + 1])
    return -1


BFS(Start, [0 for i in range(ord('a')-97, ord('f')-96)], 0)
print(small)
"""

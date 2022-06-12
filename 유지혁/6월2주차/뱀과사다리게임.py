#16928 뱀과 사다리 게임
# 게임판이 주어지고, 주사위를 굴려 나온 수만큼 이동한다.게임판의 상태가 주어졌을 때, 1번에서 시작해서 100번 칸에 도착하기 위해 굴려야하는 주사위의 최소 횟수 

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    visited = [False for _ in range(101)]
    answer = int(1e9)

    # 사다리, 뱀 위치 저장
    N, M = map(int,input().split())
    jump = [ 0 for _ in range(101)]

    for _ in range(N):
        x, y = map(int,input().split())
        jump[x] = y

    for _ in range(M):
        x, y = map(int, input().split())
        jump[x] = y

    # bfs
    q = deque()
    q.append((1,0)) #현재위치, 이동 거리
    visited[1] = True 

    while q:
        tmp = q.popleft()
        cx, cdir = tmp[0], tmp[1]

        if cx == 100:
            answer = cdir
            break
        
        for k in range(1,7):
            nx = cx + k

            if nx > 100 or visited[nx] == True:
                continue 
            
            visited[nx] = True
            if jump[nx] != 0:
                nx = jump[nx]
            
            q.append((nx, cdir + 1))

    print(answer)

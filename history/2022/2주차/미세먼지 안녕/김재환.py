"""
1. 미세먼지 확산
    1. 새로운 배열로 생성해서 반환
    2. 
2. 공기청정기 1초 가동
    2.1. 위쪽(반시계)
        공기청정기쪽으로 들어오면 먼지 제거
    2.2. 아래쪽(시계)
        공기청정기쪽으로 들어오면 먼지 제거
3. T번 반복
"""

R,C,T = map(int,input().split())
Map = []
for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        if tmp[j]== -1:
            down = [i,j]
    Map.append(tmp)

def diffusion(oriM):
    subM = [[ 0 for i in range(C)] for i in range(R)]
    dy = [-1,1,0,0]
    dx = [0,0,-1,1] # 상하좌우
    for i in range(R):
        for j in range(C):
            if oriM[i][j] > 0 :
                count = 0
                for _ in range(4):
                    ny = i + dy[_]
                    nx = j + dx[_]
                    if (0<=ny<R) and (0<=nx<C) and oriM[ny][nx] != -1: # 확산 가능
                        count+=1
                        subM[ny][nx] += oriM[i][j]//5
                subM[i][j] += oriM[i][j] -oriM[i][j]//5 * count
    return subM

def puri(oriM):
    # 위쪽 청소
    # 오른쪽 이동 C만큼, 위로 R-1만큼, 왼쪽으로 C만큼, 아래로 R-1만큼
    tmp = oriM[0][0]
    up = [down[0]-1, down[1]]
    for j in range(C-1):
        oriM[0][j] = oriM[0][j+1]
    for i in range(up[0]):
        oriM[i][C-1] = oriM[i+1][C-1]
    for j in range(C-1,0,-1):
        oriM[up[0]][j] = oriM[up[0]][j-1]
    for i in range(up[0], 0, -1):
        oriM[i][0]=oriM[i-1][0]
    oriM[1][0] = tmp

    # 아래쪽 청소
    tmp = oriM[R-1][0]
    for j in range(C-1):
        oriM[R-1][j] = oriM[R-1][j+1]
    for i in range(R-1, down[0], -1):
        oriM[i][C-1] = oriM[i-1][C-1]
    for j in range(C-1, 0, -1):
        oriM[down[0]][j] = oriM[down[0]][j-1]
    for i in range(down[0],R-2):
        oriM[i][0] = oriM[i+1][0]
    oriM[R-2][0] = tmp
    
    # 공기청정기 부분 초기화
    oriM[up[0]][up[1]] =-1
    oriM[down[0]][down[1]] =-1
    return oriM

def getSum(oriM):
    total = 0
    for t in oriM:
        total += sum(t)
    return total + 2


for _ in range(T):
    Map = diffusion(Map)
    Map = puri(Map)
print(getSum(Map))
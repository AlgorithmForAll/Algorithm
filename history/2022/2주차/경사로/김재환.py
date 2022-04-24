"""
경사로는 낮은 칸에 놓임, 연속된 칸에 경사로 바닥이 접해야함.
높이 차는 1이어야함.

1. 행 판별
2. 열 판별
"""

N,L = map(int, input().split())

MAP = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    MAP.append(tmp)

def checkRow(path):
    visited = [0 for i in range(len(path))]
    for i in range(len(path)-1):
        if path[i] < path[i+1] and path[i]+1 == path[i+1]: # 차이가 왼쪽이 1 작은 경우
            # L 만큼 같은지 판별
            if 0 <= i-L+1:
                for l in range(i, i-L,-1):
                    if path[i] == path[l] and visited[l]==0:
                        visited[l] = 1
                        continue
                    else:
                        return False
            else:
                return False
        elif path[i] > path[i+1] and path[i] == path[i+1]+1: # 왼쪽이 1 큰경우
            if i+L <= N-1:
                for l in range(i+1,i+1+L):
                    if path[i]-1 == path[l] and visited[l]==0:
                        visited[l] = 1
                        continue
                    else:
                        return False
            else:
                return False
        elif path[i] == path[i+1]:
            continue
        else:
            return False
    return True

# 행체크
count = 0
for i in range(N):
    if checkRow(MAP[i]):
        count+=1
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(MAP[j][i])
    if checkRow(tmp):
        count+=1

print(count)
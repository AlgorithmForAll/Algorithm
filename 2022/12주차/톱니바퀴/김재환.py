"""
S,N은 서로 다르므로 다른 방향으로 돈다.
같은 극은 움직이지 않는다.

"""
from collections import deque
R = 2
L = 6

topni = [[]]
for i in range(4):
    tmp = deque(list(map(int, list(input()))))
    topni.append(tmp)


def spin(q, spin):
    if spin == 1:  # 시계방향
        q.appendleft(q.pop())
    else:
        q.append(q.popleft())


t = int(input())
tl = []
for _ in range(t):
    N, D = map(int, input().split())
    # 관계 구하기
    check = [0 for i in range(5)]
    check[N] = D
    # 왼쪽으로 가기
    for i in range(N, 1, -1):
        if topni[i][L] == topni[i-1][R]:
            break
        else:
            if check[i] == 1:
                check[i-1] = -1
            else:
                check[i-1] = 1
    # 오른쪽
    for i in range(N, 4):
        if topni[i][R] == topni[i+1][L]:
            break
        else:
            if check[i] == 1:
                check[i+1] = -1
            else:
                check[i+1] = 1
    for i in range(1, 5):
        if check[i] != 0:
            spin(topni[i], check[i])

score = topni[1][0]
score += topni[2][0]*2
score += topni[3][0]*4
score += topni[4][0]*8
print(score)

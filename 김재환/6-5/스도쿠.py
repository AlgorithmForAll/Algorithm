"""
스도쿠문제
완탐으로 모든 경우를 찾기 + 사전식으로 앞서는것 찾기(작은수에 우선순위 두기)
DFS로 i행 j로 순서대로 돌기

python으로 시간토과나서 pypy로 제출함
"""


def DFS(ei):
    global Map
    global empty

    if ei == len(empty):
        for m in Map:
            print("".join(map(str, m)))
        exit()
    i, j = empty[ei]
    # print("empty!!", i, j)

    possible = set()
    # 행 체크
    for ti in range(9):
        if Map[ti][j] != 0:
            possible.add(Map[ti][j])
    # 열 체크
    for tj in range(9):
        if Map[i][tj] != 0:
            possible.add(Map[i][tj])
    # 블록 체크
    ii = i // 3
    jj = j // 3
    for ti in range(ii*3, (ii+1)*3):
        for tj in range(jj*3, (jj+1)*3):
            if Map[ti][tj] != 0:
                possible.add(Map[ti][tj])
    candidate = []
    for ti in range(1, 10):
        if ti not in possible:
            candidate.append(ti)

    if len(candidate) == 0:
        return

    for number in candidate:
        Map[i][j] = number
        DFS(ei+1)
        Map[i][j] = 0


Map = []
empty = []
for i in range(9):
    tmp = list(map(int, input()))
    Map.append(tmp)
    for j in range(9):
        if tmp[j] == 0:
            empty.append([i, j])
DFS(0)

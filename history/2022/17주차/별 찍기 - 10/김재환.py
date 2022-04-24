N = int(input())

Map = [['*' for i in range(N)] for i in range(N)]


def star(N, A):
    if N == 1:
        return
    _N = int(N/3)

    # 공백 만들어주기
    y, x = A[0]+_N, A[1]+_N
    for i in range(_N):
        for j in range(_N):
            Map[y+i][x+j] = ' '
    # 재귀 돌리기
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            _A = [A[0]+i*_N, A[1]+j*_N]
            star(_N, _A)


star(N, [0, 0])

for m in Map:
    print("".join(m))

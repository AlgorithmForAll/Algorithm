"""
패딩 입히고 쭉돌림
조건에 부합하면 최댓값과 비교후 갱신
회전후 돌림 * 4
반복
"""

tat = [
    [[1, 1, 1, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0], ],  # 길쭉이
    [[1, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0], ],  # 네모
    [[1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0], ],  # L
    [[1, 0, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0], ],  # ㄱㄴ
    [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0], ],  # ㅗ
]


def roll(map):
    n = len(map)
    tmp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if map[i][j] == 1:
                tmp[j][n-i-1] = 1
    return tmp


def mirror(map):
    n = len(map)
    hortmp = [[0 for i in range(n)] for i in range(n)]
    vertmp = [[0 for i in range(n)] for i in range(n)]
    # horizantal
    for i in range(n):
        for j in range(n):
            if map[i][j] == 1:
                hortmp[i][n-j-1] = 1
                vertmp[n-i-1][j] = 1
    return hortmp, vertmp


N, M = map(int, input().split())
Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))

max_val = 0

for i in range(N-3):
    for j in range(M-3):
        # 테트로미노 하나씩
        for ta in tat:
            for _ in range(3):
                tas = mirror(ta)
                for ta in tas:
                    total = 0
                    for ti in range(4):
                        for tj in range(4):
                            if ta[ti][tj] == 1:
                                total += Map[ti+i][tj+j]
                    max_val = max(max_val, total)
                ta = roll(ta)
print(max_val)

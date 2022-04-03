"""
모든 케이스를 다해야할거 같은데
이거 어케 푸는거여 dp인가?
"""

Map = []
N, M = map(int, input().split())
for i in range(N):
    Map.append(list(map(int, input().split())))


def findMax(i, j):
    print(i, j)
    big = 0

    big = max(big, Map[i][j] + Map[i][j+1]*2 + Map[i+1][j+1])
    big = max(big, Map[i][j+1] + Map[i+1][j+1]*2 + Map[i+1][j])
    big = max(big, Map[i][j] + Map[i+1][j]*2 + Map[i+1][j+1])
    big = max(big, Map[i][j]*2 + Map[i][j+1] + Map[i+1][j])
    print("big:", big)
    return big


big = 0

for i in range(N-1):
    for j in range(M-1):
        big = max(big, findMax(i, j))
print(big)

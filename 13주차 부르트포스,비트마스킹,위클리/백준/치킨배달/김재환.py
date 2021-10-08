from itertools import combinations
N, M = map(int, input().split())

house = []
chick = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            house.append([i, j])
        if tmp[j] == 2:
            chick.append([i, j])

coms = list(combinations(chick, M))

small = []
for com in coms:
    # 집들과 거리 구하기
    ccl = 0
    for i in range(len(house)):
        hy, hx = house[i]
        length = 100000000
        for c in com:
            cy, cx = c
            length = min(length, abs(cy-hy)+abs(cx-hx))
        ccl += length
    small.append(ccl)
print(min(small))

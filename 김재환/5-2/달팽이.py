
N = int(input())
target = int(input())

Map = [[0 for i in range(N)] for i in range(N)]

start = int((N-1)/2)
index = 1
y, x = start, start
final = [y, x]
for _ in range(int((N+1)/2)):
    if _ == 0:
        Map[y][x] = index
        if index == target:
            final = [y+1, x+1]
        index += 1
        y -= 1
        continue
    # 상
    for i in range(_*2):
        Map[y][x] = index
        if index == target:
            final = [y+1, x+1]
        index += 1
        x += 1
    x -= 1
    y += 1
    # 우
    for i in range(_*2):
        Map[y][x] = index
        if index == target:
            final = [y+1, x+1]
        index += 1
        y += 1
    # 하
    y -= 1
    x -= 1
    for i in range(_*2):
        Map[y][x] = index
        if index == target:
            final = [y+1, x+1]
        index += 1
        x -= 1
    x += 1
    y -= 1
    # 좌
    for i in range(_*2):
        Map[y][x] = index
        if index == target:
            final = [y+1, x+1]
        index += 1
        y -= 1
for M in Map:
    print(" ".join(map(str, M)))
print(" ".join(map(str, final)))

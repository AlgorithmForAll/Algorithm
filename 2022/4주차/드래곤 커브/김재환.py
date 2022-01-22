N = int(input())


def spin(tmp, lastDot):
    tl = len(tmp)
    for ti in range(tl-1, -1, -1):
        ly, lx = lastDot
        y, x, d = tmp[ti]
        d = (d+1) % 4  # 방향만 스핀
        tmp.append((ly, lx, d))

        if d == 0:
            lastDot = (ly, lx+1)
        elif d == 1:
            lastDot = (ly-1, lx)
        elif d == 2:
            lastDot = (ly, lx-1)
        else:
            lastDot = (ly+1, lx)
    return lastDot


Map = [[0 for i in range(102)] for i in range(102)]
for i in range(N):
    x, y, d, g = map(int, input().split())

    tmp = [(y, x, d)]
    if d == 0:
        lastDot = (y, x+1)
    elif d == 1:
        lastDot = (y-1, x)
    elif d == 2:
        lastDot = (y, x-1)
    else:
        lastDot = (y+1, x)

    for j in range(g):
        lastDot = spin(tmp, lastDot)

    for dot in tmp:
        y, x, d = dot
        Map[y][x] = 1
    Map[lastDot[0]][lastDot[1]] = 1

count = 0
for i in range(102):
    for j in range(102):
        if Map[i][j] == 1 and Map[i][j+1] == 1 and Map[i+1][j] == 1 and Map[i+1][j+1] == 1:
            count += 1
print(count)

"""from re import T


N = int(input())


def setting(tmp, lastDot):
    print("setting")
    result = []
    for t in tmp:
        y, x = t
        y += -lastDot[0]
        x += -lastDot[1]
        result.append((y, x))
    print("setting:", result)
    return result


def spin(tmp):
    print("spin~")  # (y,x) -> (x,y)
    result = []
    for t in tmp:
        y, x = t
        result.append((x, -y))
    print(result)
    return result


def reset(tmp, lastDot):
    print("reset 기존 값으로")
    result = []
    for t in tmp:
        y, x = t
        y += lastDot[0]
        x += lastDot[1]
        result.append((y, x))
    print("res:", result)
    return result


def findLastDot(tmp):  # 최대 만번 돈다.
    print("find Dot!:", tmp)
    for i in range(len(tmp)):
        y, x = tmp[i]
        count = 0
        for j in range(len(tmp)):
            ny, nx = tmp[j]
            if (ny == y and abs(nx-x) == 1) or (nx == x and abs(ny-y) == 1):
                count += 1
        print(y, x, ", count:", count)
        if count == 1 and [y, x] != [0, 0]:
            print("find!", y, x)
            lastDot = (y, x)
            break
    print("lastDot is :", lastDot)
    return lastDot


Map = [[0 for i in range(100)] for i in range(100)]
dot = set()

totalDot = set()
for i in range(N):
    x, y, d, g = map(int, input().split())

    tmp = [(y, x)]
    if d == 0:
        lastDot = (y, x+1)
    elif d == 1:
        lastDot = (y-1, x)
    elif d == 2:
        lastDot = (y, x-1)
    else:
        lastDot = (y+1, x)

    tmp.append(lastDot)
    print("tmp:", tmp)
    for j in range(g):
        print("lastDot:", lastDot)
        settmp = setting(tmp, lastDot)

        spintmp = spin(settmp)
        nextLastDot = findLastDot(spintmp)

        sumtmp = list(set(spintmp+settmp))
        resulttmp = reset(sumtmp, lastDot)

        lastDot = (nextLastDot[0]+lastDot[0], nextLastDot[1] + lastDot[1])
        tmp = resulttmp
    for t in resulttmp:
        y, x = t
        Map[y][x] = 1
        totalDot.add((y, x))
for _ in Map:
    print(_)
print("total:", totalDot)
dy = [1, 0, 1]  # 남,동,동남
dx = [0, 1, 1]
rec = 0
for t in totalDot:
    y, x = t
    count = 0
    for i in range(3):
        ny = y+dy[i]
        nx = x+dx[i]
        if (0 <= ny <= 100) and (0 <= nx <= 100) and Map[ny][nx] == 1:
            count += 1
    if count == 3:
        rec += 1
print(rec)
"""

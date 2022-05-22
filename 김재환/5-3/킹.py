"""
구현문제

A1 A2 5
B
L
LB
RB
LT
"""


def getPoint(st):
    col = st[0]
    row = st[1]

    _row = 8-int(row)
    _col = ord(col) - ord("A")
    return [_row, _col]


def getLocation(point):
    row = point[0]
    col = point[1]

    _row = str(8 - int(row))
    _col = chr(ord("A")+col)
    return _col+_row


D = {"R": [0, 1], "L": [0, -1], "B": [1, 0], "T": [-1, 0],
     "RT": [-1, 1], "LT": [-1, -1], "RB": [1, 1], "LB": [1, -1]}

K, S, N = map(str, input().split())
KP = getPoint(K)
SP = getPoint(S)

for n in range(int(N)):
    tmp = input()

    ky, kx = KP
    sy, sx = SP

    dy, dx = D[tmp]

    ky += dy
    kx += dx

    if ((0 <= ky < 8) and (0 <= kx < 8)) == False:
        continue

    if ky == sy and kx == sx:  # 돌을 밀수 있다.
        sy += dy
        sx += dx

    if ((0 <= sy < 8) and (0 <= sx < 8)) == False:
        continue

    SP = [sy, sx]
    KP = [ky, kx]
print(getLocation(KP))
print(getLocation(SP))

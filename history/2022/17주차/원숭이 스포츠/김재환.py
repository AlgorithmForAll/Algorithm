"""
분할정복
"""
N = int(input())

games = ["" for i in range(7)]


def calc(layer, start, end):
    if layer == 7:
        return

    mid = int((start+end)/2)

    for i in range(start, mid):
        games[layer] += "A"
    for i in range(mid, end):
        games[layer] += "B"

    calc(layer+1, start, mid)
    calc(layer+1, mid, end)


calc(0, 0, N)
s = ""
temp = ""
for i in range(N):
    s += "B"
    if i == 0:
        temp += "A"
    else:
        temp += "B"
for i in range(7):
    if games[i] == s:
        print(temp)
    else:
        print(games[i])

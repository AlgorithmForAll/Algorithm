"""
1. 그래프 만들기
2. 말동작을 어떻게 할지
3. 여러개의 케이스가 존재하고 거기서 최댓값을 구해야함.
"""
adj = {}
_adj = {}


def makeGraph():
    for i in range(21):
        adj[i*2] = (i+1)*2


_adj[10] = 13
_adj[13] = 16
_adj[16] = 19
_adj[19] = 25
_adj[20] = 22
_adj[22] = 24
_adj[24] = 25
_adj[28] = 27
_adj[27] = 26
_adj[26] = 25
_adj[25] = 30
_adj[30] = 35
_adj[35] = 40
_adj[40] = 42


tmp = list(map(int, input().split()))
visited = {}
big = 0


class Mal():
    def __init__(self):
        self.mals = [0, 0, 0, 0]
        self.total = 0
        self.malsLocation = [0, 0, 0, 0]


def isDuplicate(i, mals, malsLocation, next):
    for j in range(4):
        if i == j:
            continue
        if mals[j] == next and malsLocation[j] == malsLocation[i]:
            return True
    return False


def calc(n, mal):
    global big
    if len(tmp) == n:
        return
    for i in range(4):
        _mals = list(mal.mals)
        _total = int(mal.total)
        _malsLocation = list(mal.malsLocation)
        next = _mals[i]
        d = tmp[n]
        if next == -1:
            continue

        if _malsLocation[i] == 0:
            if next in [10, 20]:
                tmpAdj = _adj
                _malsLocation[i] = 1
            elif next == 30:
                d -= 1
                next = 28
                tmpAdj = _adj
                _malsLocation[i] = 1
            else:
                tmpAdj = adj
                _malsLocation[i] = 0
        else:
            tmpAdj = _adj

        for _ in range(d):
            next = tmpAdj[next]
            if next == 42:  # 도착한 경우
                break

        if next >= 40:
            _malsLocation[i] = 0

        if isDuplicate(i, _mals, _malsLocation, next):
            continue

        if next == 42:  # 도착한 경우
            _mals[i] = -1
            _malsLocation[i] = 0
        else:
            _mals[i] = next
            _total += next

        newMal = Mal()
        newMal.mals = list(_mals)
        newMal.total = int(_total)
        newMal.malsLocation = list(_malsLocation)
        if big < _total:
            big = _total
        calc(n+1, newMal)


makeGraph()
calc(0, Mal())
print(big)

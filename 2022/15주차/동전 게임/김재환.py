"""
2가지의 경우의 수 존재
1. 올 H
2. 올 T
3. 불가능 ? 이걸 어케 찾지?


"""


def change(Map):
    _Map = [[0 for i in range(3)]for i in range(3)]
    for i in range(3):
        for j in range(3):
            if Map[i][j] == 'H':
                _Map[i][j] = 1
            else:
                _Map[i][j] = 0
    return _Map


def isAll(Map):
    one = Map[0][0]
    for i in range(3):
        for j in range(3):
            if Map[i][j] != one:
                return False
    return True


def recur(Maplist, count):

    tmp = []
    for Map in Maplist:
        Map = list(map(list, Map))
        if isAll(Map):
            return count
        # 세로 변환
        for i in range(3):
            for j in range(3):
                Map[i][j] ^= 1
            if tuple(map(tuple, Map)) not in s:  # 다음 연산을 위해 삽입
                tmp.append(tuple(map(tuple, Map)))  # deep copy
                s.add(tuple(map(tuple, Map)))
            for j in range(3):
                Map[i][j] ^= 1
        # 가로 변환
        for j in range(3):
            for i in range(3):
                Map[i][j] ^= 1
            if tuple(map(tuple, Map)) not in s:  # 다음 연산을 위해 삽입
                tmp.append(tuple(map(tuple, Map)))
                s.add(tuple(map(tuple, Map)))
            for i in range(3):
                Map[i][j] ^= 1
        # 크로스
        for i in range(3):
            Map[i][i] ^= 1
        if tuple(map(tuple, Map)) not in s:  # 다음 연산을 위해 삽입
            tmp.append(tuple(map(tuple, Map)))
            s.add(tuple(map(tuple, Map)))
        for i in range(3):
            Map[i][i] ^= 1

        for i in range(3):
            Map[i][2-i] ^= 1
        if tuple(map(tuple, Map)) not in s:  # 다음 연산을 위해 삽입
            tmp.append(tuple(map(tuple, Map)))
            s.add(tuple(map(tuple, Map)))
        for i in range(3):
            Map[i][2-i] ^= 1
    if len(tmp) == 0:
        return -1
    return recur(tmp, count+1)


s = set()

T = int(input())
for t in range(T):
    Map = []
    for i in range(3):
        Map.append(input().split())
    Map = change(Map)
    count = recur([Map], 0)
    print(count)
    s.clear()

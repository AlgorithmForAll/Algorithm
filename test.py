"""
쉼터,산봉우리 => 휴식가능
intensity => 휴식없는 기간 =>
intensity가 최소가 되는 등산코드 => 총 경로는 노상관
MST를 변형 + BFS
"""
import heapq


def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, A, B):
    A = find(parent, A)
    B = find(parent, B)

    if A <= B:
        parent[B] = A
    else:
        parent[A] = B


def solution(n, paths, gates, summits):
    answer = []
    hq = []
    # init()
    for path in paths:
        i, j, w = path
        heapq.heappush(hq, [w, i, j])

    parent = [i for i in range(n+1)]

    ms = set()
    mg = set()
    maxw = 0
    last = -1
    tmp = set()
    total = 0
    while hq:
        w, i, j = heapq.heappop(hq)
        total += w
        print("wij:", w, i, j)
        maxw = max(maxw, w)
        union(parent, i, j)
        if i in gates:
            mg.add(i)
        if j in gates:
            mg.add(j)
        if i in summits:
            ms.add(i)
        if j in summits:
            ms.add(j)

        if len(ms) > 0 and len(mg) > 0:
            print("ms:", ms)
            print("mg:", mg)

            # gates의 부모를 구한다.
            gateP = set()
            for gate in mg:
                gateP.add(find(parent, gate))
            # summits의 부모를 구함
            for summit in ms:
                sp = find(parent, summit)
                if sp in gateP:
                    if last == -1:
                        tmp.add((summit, maxw, total))
                        last = maxw
                    elif last == maxw:
                        tmp.add((summit, maxw, total))

            print("tmp:", tmp)
    tmp = list(tmp)
    tmp.sort(key=lambda x: (x[1], x[0]))
    print(tmp)
    return tmp[0]


# solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [
#     3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3],	[5])
# solution(7,	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2],
#          [3, 7, 4], [5, 6, 6]],	[1], [2, 3, 4])
solution(7,	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [
         4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])

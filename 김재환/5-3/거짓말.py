"""
완탐으로 돌려도 그렇게 많지 않다.

4 3
0
2 1 2
1 3
3 2 3 4
"""

N, M = map(int, input().split())
F = [0 for i in range(N+1)]
TRUE = list(map(int, input().split()))
adj = {}
for i in range(1, N+1):
    adj[i] = []

P = []
for m in range(M):
    PARTY = list(map(int, input().split()))
    P.append(PARTY)
    # 인접한 애들 구해준다.
    for i in range(1, PARTY[0]+1):
        for j in range(1, PARTY[0]+1):
            if i != j:
                adj[PARTY[i]].append(PARTY[j])


def DFS(th):  # 진실 퍼뜨리기 th:진실을 아는 사람
    for nextHuman in adj[th]:
        if F[nextHuman] != 1:
            F[nextHuman] = 1
            DFS(nextHuman)


if TRUE[0] != 0:
    for th in TRUE[1:]:
        F[th] = 1
        DFS(th)
count = M
for party in P:

    for i in range(1, party[0]+1):
        if F[party[i]] == 1:
            count -= 1
            break
print(count)

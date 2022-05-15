"""
gcd 해서 부모, 인자 만들어주기
"""

N = int(input())

R = {}


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


visited = [0 for i in range(N)]
adj = {}


def dfs(cur, val):
    visited[cur] = 1
    R[cur] *= val

    for node in adj[cur]:
        if visited[node] == 0:
            dfs(node, val)


for n in range(N-1):
    a, b, p, q = map(int, input().split())

    if a not in R:
        R[a] = 1
    if b not in R:
        R[b] = 1
    if a not in adj:
        adj[a] = []
    if b not in adj:
        adj[b] = []

    g = gcd(R[a], R[b])
    am = R[b]/g * p
    bm = R[a]/g * q
    g = gcd(am, bm)
    visited = [0 for i in range(N)]
    dfs(a, am / g)
    dfs(b, bm / g)

    adj[a].append(b)
    adj[b].append(a)

answer = [0 for i in range(N)]
for node in R.keys():
    answer[node] = int(R[node])
print(" ".join(map(str, answer)))

"""
gcd 해서 부모, 인자 만들어주기
https://latter2005.tistory.com/63

"""
N = int(input())
R = {}


def gcd(a, b):  # 최대 공약수를 찾아준다.
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


visited = [0 for i in range(N)]
adj = {}


def dfs(cur, val):  # DFS를 통해 연결된 모든 노드에 비율을 곱해서 반영해준다.
    visited[cur] = 1
    R[cur] *= val

    for node in adj[cur]:
        if visited[node] == 0:  # 들르지 않았다는 것은 비율 갱신을 해주어야 한다는 의미다.
            dfs(node, val)


for n in range(N-1):
    a, b, p, q = map(int, input().split())

    if a not in R:  # 해당 칵테일의 비율을 1로 초기화 왜냐면 나중에 p,q로 비율 맞출거니까
        R[a] = 1
    if b not in R:
        R[b] = 1
    if a not in adj:
        adj[a] = []
    if b not in adj:
        adj[b] = []

    g = gcd(R[a], R[b])  # 최대 공약수를 구한다.
    # 처음 나온 값이면 비율이 1이고 연산이 된 값이면 다른 값임. 비율을 맞추기 위해 최소 공배수로 만든다.
    am = R[b]/g * p
    bm = R[a]/g * q
    # 1,1    3,1
    # am = 1*3
    # bm = 1*1
    g = gcd(am, bm)  # 비율에 대해서
    visited = [0 for i in range(N)]
    dfs(a, am / g)  # 핸재 노드에 am/g를 곱해야 적절한 비율이 된다.
    dfs(b, bm / g)

    adj[a].append(b)  # 나중에 연결된 노드들에 대해 전부 비율을 다시 맞춰주기 위해 연결시켜준다.
    adj[b].append(a)

answer = [0 for i in range(N)]
for node in R.keys():
    answer[node] = int(R[node])
print(" ".join(map(str, answer)))

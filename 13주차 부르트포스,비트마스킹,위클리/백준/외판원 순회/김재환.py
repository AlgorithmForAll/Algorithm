N = int(input())
adj = []
for i in range(N):
    adj.append(list(map(int, input().split())))

INF = int(1e9)
# dp 초기화
dp = [[INF] * (1 << N) for _ in range(N)]


def dfs(last, btm):  # DFS
    if btm == (1 << N) - 1:     # 모든 도시를 방문했다면
        if adj[last][0]:
            return adj[last][0]
        else:
            return INF
    if dp[last][btm] != INF:  # 이미 최소비용이 계산된경우
        return dp[last][btm]

    for i in range(1, N):
        if not adj[last][i]:  # 가는 경로가 없으면 넘어감
            continue
        if btm & (1 << i):  # 이미 방문한 도시라면 넘어감
            continue
        dp[last][btm] = min(dp[last][btm], dfs(i, btm | (1 << i))+adj[last][i])
    return dp[last][btm]


dfs(0, 1)
print(dfs(0, 1))
"""
'''
TSP 외판원 순회문제
한 지점에서 출발하여 모든 도시를 돌아 출발지로 돌아오기
이때 한번 간 도시는 다시 갈 수 없고
이때 가장 적은 비용이 드는 여행 구하기

'''
N = int(input())
adj = []
for i in range(N):
    adj.append(list(map(int, input().split())))

# 초기 출발지 정하기 출발지는 0

small = 10000000000


def DFS(now, length, visited):
    global small
    if sum(visited) == N:
        small = min(small, adj[now][0]+length)
    # 방문하지 않은 경우에 돌아가도록 만든다.
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            DFS(i, adj[now][i]+length, list(visited))
            visited[i] = 0


visited = [0 for i in range(N)]
visited[0] = 1
for i in range(1, N):
    DFS(0, 0, list(visited))
print(small)
"""

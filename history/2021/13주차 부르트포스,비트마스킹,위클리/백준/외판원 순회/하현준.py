"""
외판원 순회
https://www.acmicpc.net/problem/2098
"""


n = int(input())
inf = float('inf')
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[inf for _ in range(1 << n)] for _ in range(n)]


def dfs2(x, visited):  # x : 현재 방문한 노드, visited : 지금까지 방문 노드를 담고있는 기록
    if dp[x][visited] != inf:  # 겪은 상황일 경우
        return dp[x][visited]

    if visited == (1 << n) - 1:  # 모든 노드를 방문한 경우
        if data[x][first] != 0:  # 다시 최초 출발지로 돌아가야 한다. x -> first
            return data[x][first]
        else:
            return inf

    min_val = inf
    for to in range(n):  # 전체 노드 방문
        if to == first:  # 최초 출발지는 제외
            continue
        if data[x][to] == 0:  # x->to의 길이 없는 경우 제외
            continue
        if visited & (1 << to) != 0:  # 방문기록에 존재하는 지점(to)은 제외
            continue
        min_val = min(min_val, data[x][to] + dfs2(to, visited | (1 << to)))

    dp[x][visited] = min_val
    return min_val


first = 2  # 최초 출발지 0 ~ n-1 중 임의의 노드를 선택 (무엇을 선택해도 결과는 같다)
print(dfs2(first, 2 ** first))

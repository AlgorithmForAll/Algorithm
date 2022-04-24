"""
다익스트라 쓰려다 까먹음....
"""


def solution(N, road, K):
    answer = 0
    INF = 500000
    Map = [[INF for i in range(N+1)] for i in range(N+1)]
    # 전처리
    for i in road:
        a, b, c = i
        if Map[a][b] > c:
            Map[a][b] = c
            Map[b][a] = c
        Map[a][a] = 0
        Map[b][b] = 0
    # 프로이드
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if Map[i][k] + Map[k][j] < Map[i][j]:
                    Map[i][j] = Map[i][k] + Map[k][j]
    print(Map)
    for i in range(1, N+1):
        if Map[1][i] <= K:
            answer += 1
    return answer

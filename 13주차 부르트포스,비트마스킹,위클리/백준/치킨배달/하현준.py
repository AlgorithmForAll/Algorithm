"""
치킨 배달
https://www.acmicpc.net/problem/15686
"""
from itertools import combinations

INF = float('inf')
n, m = map(int, input().split())
answer = INF
graph = []
chicken = []
houses = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i, j])
        elif graph[i][j] == 1:
            houses.append([i, j])

for case in combinations(chicken, m):
    ctemp = 0
    for house in houses:
        htemp = INF
        for chick in case:
            htemp = min(htemp, abs(house[0] - chick[0]) + abs(house[1] - chick[1]))
        ctemp += htemp
    answer = min(answer, ctemp)
print(answer)

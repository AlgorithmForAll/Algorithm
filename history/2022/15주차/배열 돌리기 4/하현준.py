"""
배열 돌리기 4
https://www.acmicpc.net/problem/17406
"""
from itertools import permutations
import copy
import sys

sys.stdin = open("../input.txt")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
oper = [list(map(int, input().split())) for _ in range(k)]
answer = float('inf')
for case in permutations(oper):
    tgraph = copy.deepcopy(graph)
    for r, c, s in case:
        r -= 1
        c -= 1
        x1, y1 = r - s, c - s
        x2, y2 = r + s, c + s

        x = x2 - x1
        y = y2 - y1
        while x > 0 and y > 0:

            loop = [x, y, x, y]
            before = tgraph[x1][y1]
            for i in range(4):
                for _ in range(loop[i]):
                    x1 += dx[i]
                    y1 += dy[i]
                    new = tgraph[x1][y1]
                    tgraph[x1][y1] = before
                    before = new
            x -= 2
            y -= 2
            x1 += 1
            y1 += 1
    answer = min(answer, min([sum(g) for g in tgraph]))
print(answer)

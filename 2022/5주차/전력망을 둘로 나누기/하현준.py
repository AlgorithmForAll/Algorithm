"""
전력망을 둘로 나누기
https://programmers.co.kr/learn/courses/30/lessons/86971
"""

from collections import defaultdict


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)
    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa


def get_tree(n, wires, check):
    parent = [i for i in range(n + 1)]
    for i in range(len(wires)):
        if i != check:
            v1, v2 = wires[i]
            if find(parent, v1) != find(parent, v2):
                union(parent, v1, v2)

    return parent


def solution(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        parent = get_tree(n, wires, i)
        data = defaultdict(int)
        for j in range(1, n + 1):
            data[find(parent, j)] += 1
        data = list(data.values())
        answer = min(answer, abs(data[0] - data[1]))
    return answer

print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]), 3)
print(solution(4, [[1, 2], [2, 3], [3, 4]]), 0)
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]), 1)
print(solution(2, [[1, 2]]), 0)

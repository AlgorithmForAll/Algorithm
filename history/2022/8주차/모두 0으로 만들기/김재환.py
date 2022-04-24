"""
트리 : 여러 노드가 한 노드를 가리킬 수 없는 구조, 서로 다른 노드를 잇는 길은 하나뿐. 사이클이 없다.
DFS의 재귀 제한은 1000번 -> recur x
이차배열은 너무 커서 시간제한 뜸
후위순회해야함.

알고보니 마지막에 각 노드의 값을 확인해야하는 것이었다....
"""

import sys
sys.setrecursionlimit(10 ** 6)

count = 0


def DFS(adj, parent, node, visited, a):
    visited[node] = 1
    # 리프 노드가 아닌경우
    for child in adj[node]:
        if visited[child] == 0:
            DFS(adj, node, child, visited, a)
    if node == 0:
        return
    # 연산하기
    tmp = a[node]
    a[parent] += tmp
    a[node] = 0
    global count
    count += abs(tmp)


def solution(a, edges):
    answer = -2
    adj = {}
    for e in edges:
        A, B = e
        if A in adj:
            adj[A].append(B)
        else:
            adj[A] = [B]
        if B in adj:
            adj[B].append(A)
        else:
            adj[B] = [A]

    visited = [0 for i in range(len(a))]
    DFS(adj, -1, 0, visited, a)

    if sum(a) != 0:
        return -1

    return count


solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]])
solution([-2, 8, -5, -5, -3, 0, 5, 2], [[0, 1], [0, 2],
         [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]])

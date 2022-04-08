"""
트리
https://www.acmicpc.net/problem/1068
"""
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 6)


def dfs_leaf(now):
    if not child_node[now] or len(set(child_node[now]) - deleted) == 0:
        leaf.add(now)
        return

    for node in child_node[now]:
        if visited[node] == 0:
            visited[node] = 1
            dfs_leaf(node)
            visited[node] = 0


def dfs_delete(now):
    if not child_node[now]:
        deleted.add(now)
        return

    for node in child_node[now]:
        if visited[node] == 0:
            visited[node] = 1
            deleted.add(node)
            dfs_delete(node)
            visited[node] = 0


for _ in range(100):
    n = int(input())
    parent = list(map(int, input().split()))
    to_delete = int(input())
    roots = []
    leaf = set()
    deleted = {to_delete}
    child_node = [[] for _ in range(n)]
    for i, p in enumerate(parent):
        if p == -1:
            roots.append(i)
        else:
            child_node[p].append(i)
    visited = [0 for _ in range(n)]
    visited[to_delete] = 1
    dfs_delete(to_delete)

    visited = [0 for _ in range(n)]
    for root in roots:
        visited[root] = 1
        dfs_leaf(root)

    print(len(leaf - deleted))

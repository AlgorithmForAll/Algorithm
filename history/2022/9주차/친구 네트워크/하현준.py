"""
친구 네트워크
https://www.acmicpc.net/problem/4195
"""
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a
        data[a] += data[b]
    print(data[a])

for _ in range(int(input())):
    f = int(input())
    parent = dict()
    data = dict()
    for i in range(f):
        f1, f2 = input().split()
        if f1 not in parent:
            parent[f1] = f1
            data[f1] = 1

        if f2 not in parent:
            parent[f2] = f2
            data[f2] = 1
        union_parent(parent, f1, f2)

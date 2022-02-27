"""
유니온 파인드의 심화 버전 느낌?
기준은 알파벳 순서로 기준잡기

Group Number dic
Parent dic
"""

from collections import defaultdict
import sys
#input = sys.stdin.readline

P = {}
N = {}


def find(node):  # 루트 노드 찾아주기
    if P[node] == node:
        return node
    P[node] = find(P[node])  # 상위의 모든 노드를 찾아서 갱신시켜준다.
    return P[node]  # 찾은 부모 노드를 반환해준다.


def union(A, B):
    A = find(A)  # 루트 노드를 찾는다.
    B = find(B)

    if A == B:
        return N[A]
    elif A < B:
        P[B] = A
        N[A] += N[B]
        return N[A]
    else:
        P[A] = B
        N[B] += N[A]
        return N[B]


T = int(input())
for i in range(T):
    F = int(input())

    N = {}
    P = {}
    for j in range(F):
        A, B = input().split()
        # 초기화 하기
        if A not in P:
            P[A] = A
        if B not in P:
            P[B] = B
        if A not in N:
            N[A] = 1
        if B not in N:
            N[B] = 1
        # 합치기
        result = union(A, B)
        print(result)

"""
모든 순열
https://www.acmicpc.net/problem/10974
"""
from itertools import permutations

n = int(input())
for case in list(permutations([i for i in range(1, n + 1)], n)):
    print(" ".join([str(i) for i in case]))

# 풀이 실패

import math

n = int(input())
mass = [1] * n
for _ in range(n - 1):
    a, b, p, q = map(int, input().split())
    mass[b] = mass[a] * (q / p)

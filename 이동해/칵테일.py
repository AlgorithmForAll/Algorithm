import math

n = int(input())
mass = [1] * n
for _ in range(n - 1):
    a, b, p, q = map(int, input().split())
    mass[b] = mass[a] * (q / p)

lcm = mass[0]
for i in range(1, n - 1): 
    lcm = math.lcm(mass[i], lcm)

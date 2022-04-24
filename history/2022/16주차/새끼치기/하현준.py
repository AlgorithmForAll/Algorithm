"""
새끼치기
https://www.acmicpc.net/problem/17291
"""
import sys

sys.stdin = open("../../input.txt")

n = int(input())
born = [0 for _ in range(n + 1)]
born[0] = 1
born[1] = 1
for i in range(1, n):
    born[i + 1] = 2 * (born[i])
    if i - 3 >= 0 and (i - 2) % 2 == 1:
        born[i + 1] -= born[i - 3]
    if i - 4 >= 0 and (i - 3) % 2 == 0:
        born[i + 1] -= born[i - 4]
print(born[n])

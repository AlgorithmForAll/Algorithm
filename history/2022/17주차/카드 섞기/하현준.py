"""
https://www.acmicpc.net/problem/21315
"""
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 5)

n = int(input())
cards = list(map(int, input().split()))


def dfs(i, k, end):
    global original
    if i > k + 1 or end < 0:
        return

    change = original[:end]
    temp = []
    for _ in range(2 ** (k - i + 1)):
        if change:
            temp.append(change.pop())

    original = temp[::-1] + change + original[end:]
    dfs(i + 1, k, 2 ** (k - i + 1))


newk = 1
for i in range(1, n + 1):
    if 2 ** i < n:
        newk = i
    else:
        break

for a in range(1, newk + 1):
    for b in range(1, newk + 1):
        original = [o for o in range(1, n + 1)]
        for k in [a, b]:
            dfs(1, k, n)

        if original == cards:
            print(a, b)
            exit()

"""
차이를 최대로
https://www.acmicpc.net/problem/10819
"""
from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
answer = 0
for case in permutations(data, n):
    temp = 0
    for i in range(n - 1):
        temp += abs(case[i + 1] - case[i])
    answer = max(answer, temp)
print(answer)

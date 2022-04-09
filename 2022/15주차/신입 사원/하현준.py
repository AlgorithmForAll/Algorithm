"""
신입 사원
https://www.acmicpc.net/problem/1946
"""
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline
answer = []
for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: (x[0]))
    count = 1
    standard = data[0]
    for i in range(1, n):
        if not (standard[0] < data[i][0] and standard[1] < data[i][1]):
            count += 1
            standard = data[i]

    answer.append(count)
print(*answer, sep="\n")

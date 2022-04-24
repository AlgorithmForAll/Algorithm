"""
ATM
https://www.acmicpc.net/problem/11399
"""
import sys

sys.stdin = open("../input.txt")
for _ in range(int(input())):
    n = int(input())
    pdata = list(map(int, input().split()))
    pdata.sort()
    total = 0
    temp = 0
    for i in range(n):
        temp += pdata[i]
        total += temp
    print(total)

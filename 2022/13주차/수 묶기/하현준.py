"""
수 묶기
https://www.acmicpc.net/problem/1744
"""
import sys

sys.stdin = open("../input.txt")
for _ in range(int(input())):
    n = int(input())
    parr = []
    marr = []
    zarr = []
    for _ in range(n):
        x = int(input())
        if x > 0:
            parr.append(x)
        elif x == 0:
            zarr.append(x)
        elif x < 0:
            marr.append(x)
    parr.sort(reverse=True)
    marr.sort()
    result = 0
    premain = 0
    mremain = 0

    for i in range(0, len(parr), 2):
        temp = parr[i:i + 2]
        if len(temp) == 2:
            if 1 in temp:
                result += temp[0] + temp[1]
            else:
                result += temp[0] * temp[1]
        elif temp:
            premain = temp[0]

    for i in range(0, len(marr), 2):
        temp = marr[i:i + 2]
        if len(temp) == 2:
            result += temp[0] * temp[1]
        elif temp:
            mremain = temp[0]

    if mremain == 0 or zarr:
        result += premain
    else:
        result += (premain + mremain)
    print(result)

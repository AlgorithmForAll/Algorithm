"""
부분 문자열
https://www.acmicpc.net/problem/16916
"""
import sys

sys.stdin = open("../input.txt")


def get_pattern_data():
    data = [0 for _ in range(len(p))]
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = data[j - 1]
        if p[i] == p[j]:
            j += 1
            data[i] = j
    return data


for _ in range(int(input())):
    s = input()
    p = input()
    pdata = get_pattern_data()
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = pdata[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                print(1)
                break
            else:
                j += 1
    else:
        print(0)

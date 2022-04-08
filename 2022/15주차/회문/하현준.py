"""
회문
https://www.acmicpc.net/problem/17609
"""
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline


def solution():
    i = 0
    j = n - 1
    while i < j:
        if data[i] != data[j]:
            break
        else:
            i += 1
            j -= 1
    else:
        return 0

    # i 제거
    old_i = i
    old_j = j
    i += 1
    if i < j and i < n-1 and data[i] == data[j]:
        while i < j:
            if data[i] != data[j]:
                i = old_i
                j = old_j
                break
            else:
                i += 1
                j -= 1
        else:
            return 1
    else:
        i = old_i
    # j 제거
    j -= 1
    if i < j and j >= 0 and data[i] == data[j]:
        while i < j:
            if data[i] != data[j]:
                return 2
            else:
                i += 1
                j -= 1
        else:
            return 1
    else:
        return 2


for _ in range(int(input())):
    data = input().rstrip()
    n = len(data)
    print(solution())

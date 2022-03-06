"""
찾기
https://www.acmicpc.net/problem/1786
"""
import sys

sys.stdin = open("../input.txt")


def get_pattern_data():
    data = [0 for _ in range(0, len(P))]
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = data[j - 1]
        if P[i] == P[j]:
            j += 1
            data[i] = j
    return data


def kmp(pdata):
    result = []
    count = 0

    j = 0
    for i in range(0, len(T)):
        while j > 0 and T[i] != P[j]:
            j = pdata[j - 1]

        if T[i] == P[j]:
            if j == (len(P) - 1):
                result.append(i - len(P) + 2)
                count += 1
                j = pdata[j]
            else:
                j += 1

    print(count)
    for element in result:
        print(element)


for _ in range(int(input())):
    T = input()
    P = input()
    kmp(get_pattern_data())
"""
단어 수학
https://www.acmicpc.net/problem/1339
"""
import sys

sys.stdin = open("../input.txt")

for _ in range(int(input())):
    n = int(input())
    data = [[0 for _ in range(10)] for _ in range(ord("A"), ord("Z") + 1)]
    alphabets = [input() for _ in range(n)]
    alpha_map = dict()
    alpha = []
    num = 9
    total = 0

    for alphabet in alphabets:
        m = len(alphabet)
        for idx, val in enumerate(alphabet):
            data[ord(val) - ord("A")][m - idx - 1] += 1

    for i in range(ord("A"), ord("Z") + 1):
        weight = sum([data[i - ord("A")][x] * (10 ** (x + 1)) for x in range(10)])
        if weight > 0:
            alpha.append([weight, chr(i)])

    alpha.sort(key=lambda x: -x[0])
    for i in range(len(alpha)):
        alpha_map[alpha[i][1]] = num
        num -= 1

    for alphabet in alphabets:
        for k, v in alpha_map.items():
            alphabet = alphabet.replace(k, str(v))
        total += int(alphabet)

    print(total)

"""
ZOAC 3
https://www.acmicpc.net/problem/20436
"""
import sys

sys.stdin = open("../input.txt")

keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
ja = "qwertasdfgzxcv"
mo = "yuiophjklbnm"
location = dict()
for i in range(3):
    for j in range(len(keyboard[i])):
        location[keyboard[i][j]] = [i, j]

for _ in range(1):
    l, r = input().split()
    data = input()
    result = 0
    lx, ly = location[l]
    rx, ry = location[r]
    for i, d in enumerate(data):
        dx, dy = location[d]

        ldist = abs(lx - dx) + abs(ly - dy)
        rdist = abs(rx - dx) + abs(ry - dy)
        if d in mo:
            result += rdist + 1
            rx, ry = dx, dy
        elif d in ja:
            result += ldist + 1
            lx, ly = dx, dy

    print(result)

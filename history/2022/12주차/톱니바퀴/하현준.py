"""
톱니바퀴
https://www.acmicpc.net/problem/14891
"""
import sys
from collections import deque

sys.stdin = open("../input.txt")

for _ in range(int(input())):
    def dfs(clock, rotate):
        for i in [-1, 1]:
            near = clock + i
            if 0 <= near < 4:
                if check[near] == 0:
                    if data[clock][2 * i] != data[near][2 * (-i)]:
                        check[near] = -rotate
                        dfs(near, -rotate)


    data = [deque(list(input())) for _ in range(4)]
    for _ in range(int(input())):
        t, d = map(int, input().split())
        check = [0 for _ in range(4)]
        check[t - 1] = d
        dfs(t - 1, d)
        for i in range(4):
            data[i].rotate(check[i])

    answer = 0
    for i in range(4):
        if data[i][0] == '1':
            answer += 2 ** i
    print(answer)

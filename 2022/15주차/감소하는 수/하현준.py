"""
감소하는 수
https://www.acmicpc.net/problem/1038
"""
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 5)


def dfs(count):
    global answer, arr
    if len(arr) > 10:
        answer = -1
        return
    if count == n:
        answer = int("".join(map(str, arr[::-1])))
        return

    if arr[0] + 1 < arr[1]:
        arr[0] += 1
        dfs(count + 1)
    else:
        arr[0] += 1
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                arr[i + 1] += 1
                for j in range(i + 1):
                    arr[j] = j
                if arr[i + 1] > 9:
                    arr = [x for x in range(len(arr) + 1)]
            else:
                break
        dfs(count + 1)


for _ in range(10):
    n = int(input())
    arr = [0, 1]
    answer = 0
    if 0 <= n < 10:
        print(n)
    else:
        dfs(10)
        print(answer)

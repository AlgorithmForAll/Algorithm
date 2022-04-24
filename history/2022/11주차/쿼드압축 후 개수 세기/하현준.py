"""
쿼드압축 후 개수 세기
https://programmers.co.kr/learn/courses/30/lessons/68936
"""
import sys

sys.setrecursionlimit(10 ** 7)


def solution(arr):
    def dfs(x, y, num):
        if [x, y] == [x + num - 1, y + num - 1]:
            return arr[x][y]

        temp = [
            dfs(x, y, int(num / 2)),
            dfs(x, y + int(num / 2), int(num / 2)),
            dfs(x + int(num / 2), y, int(num / 2)),
            dfs(x + int(num / 2), y + int(num / 2), int(num / 2))
        ]
        try:
            temp = sum(temp, [])
        except TypeError:
            pass

        if len(set(temp)) == 1:
            return list(set(temp))

        return temp

    n = len(arr)
    result = dfs(0, 0, n)
    return [result.count(0), result.count(1)]


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]), [4, 9])
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]), [10, 15])

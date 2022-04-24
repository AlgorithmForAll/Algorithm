"""
삼각 달팽이
https://programmers.co.kr/learn/courses/30/lessons/68645
"""

dx = [1, 0, -1]
dy = [0, 1, -1]


def solution(n):
    data = [[0 for _ in range(i)] for i in range(1, n + 1)]
    j = 0
    num = 1
    x, y = -1, 0
    for i in range(n, 0, -1):
        for _ in range(i):
            x += dx[j]
            y += dy[j]
            data[x][y] = num
            num += 1
        j = (j + 1) % 3

    return sum(data, [])


print(solution(4), [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
print(solution(5), [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
print(solution(6), [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11])

"""
아이템 줍기
https://programmers.co.kr/learn/courses/30/lessons/87694
힌트 : 그래프를 2배 키워라
"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cx = [-1, -1, -1, 0, 0, 1, 1, 1]
cy = [-1, 0, 1, -1, 1, -1, 0, 1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    def check(x, y):
        if graph[x][y] == -1:
            return False
        for i in range(8):
            xx = x + cx[i]
            yy = y + cy[i]
            if graph[xx][yy] == -1:
                return True
        return False

    def dfs(x, y, dist, visited):
        if [x, y] == [itemX, itemY]:
            return dist

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if (xx, yy) not in visited and check(xx, yy):
                graph[x][y] = min(graph[x][y], dfs(xx, yy, dist + 1, visited | {(xx, yy)}))

        return graph[x][y]

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    graph = [[-1 for _ in range(2 * 51)] for _ in range(2 * 51)]
    for x1, y1, x2, y2 in rectangle:
        for x in range(2 * x1, 2 * x2 + 1):
            for y in range(2 * y1, 2 * y2 + 1):
                graph[x][y] = float('inf')

    answer = dfs(characterX, characterY, 0, {(characterX, characterY)})
    return answer // 2


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8), 17)
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1), 11)
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7), 9)
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10), 15)
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3), 10)

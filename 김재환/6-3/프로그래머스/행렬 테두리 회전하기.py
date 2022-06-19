def spin(Map, y1, x1, y2, x2):
    start = Map[y1][x1]
    # 왼쪽
    row = y2-y1
    col = x2-x1
    y, x = y1, x1
    small = start
    for i in range(row):
        Map[y][x] = Map[y+1][x]
        small = min(small, Map[y+1][x])
        y += 1
    for j in range(col):
        Map[y][x] = Map[y][x+1]
        small = min(small, Map[y][x+1])
        x += 1
    for i in range(row):
        Map[y][x] = Map[y-1][x]
        small = min(small, Map[y-1][x])
        y -= 1
    for j in range(col):
        Map[y][x] = Map[y][x-1]
        small = min(small, Map[y][x-1])
        x -= 1
    Map[y][x+1] = start
    small = min(small, Map[y][x+1])
    return small


def solution(rows, columns, queries):
    answer = []
    Map = [[0 for i in range(columns)] for i in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            Map[i][j] = num
            num += 1
    for q in queries:
        y1, x1, y2, x2 = q
        answer.append(spin(Map, y1-1, x1-1, y2-1, x2-1))

    return answer

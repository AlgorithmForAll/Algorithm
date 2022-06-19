def solution(rows, columns, queries):
    answer = []
    cnt = 1
    graph = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt += 1
    for x1, y1, x2, y2 in queries:
        test = graph[x1 - 1][y2 - 1]
        arr = []
        arr.append(test)
        for j in range(y2 - 1, y1 - 1, -1):
            arr.append(graph[x1 - 1][j])
            graph[x1 - 1][j] = graph[x1 - 1][j - 1]
        for j in range(x1 - 1, x2 - 1):
            arr.append(graph[j][y1 - 1])
            graph[j][y1 - 1] = graph[j + 1][y1 - 1]
        for j in range(y1 - 1, y2 - 1):
            arr.append(graph[x2 - 1][j])
            graph[x2 - 1][j] = graph[x2 - 1][j + 1]
        for j in range(x2 - 1, x1 - 1, -1):
            arr.append(graph[j][y2 - 1])
            graph[j][y2 - 1] = graph[j - 1][y2 - 1]
        graph[x1][y2 - 1] = test

        answer.append(min(arr))
    return answer
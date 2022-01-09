"""
행렬 테두리 회전하기
https://programmers.co.kr/learn/courses/30/lessons/77485
"""


def solution(rows, columns, queries):
    answer = []
    graph = [[x+1 for x in range(columns*i, columns + columns*i)]
             for i in range(rows)]
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        
        rgraph = list(map(list, zip(*graph)))
        temp = [
            graph[x1][y1:y2+1],
            rgraph[y2][x1+1:x2],
            graph[x2][y1:y2+1][::-1],
            rgraph[y1][x1+1:x2][::-1]
        ]

        temp = sum(temp, [])
        answer.append(min(temp))
        temp.insert(0, temp.pop())

        for y in range(y1, y2+1):
            graph[x1][y] = temp.pop(0)
        for x in range(x1+1, x2):
            graph[x][y2] = temp.pop(0)
        for y in range(y2, y1-1, -1):
            graph[x2][y] = temp.pop(0)
        for x in range(x2-1, x1, -1):
            graph[x][y1] = temp.pop(0)

    return answer


print(solution(5, 3, []))
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]	))
print(
    solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]	))
# print(solution(100, 97, [[1, 1, 100, 97]]))

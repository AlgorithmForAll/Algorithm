def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    return answer


'''def DFS(i, visited, computers):
    s = [i]
    while s:
        t = s.pop()
        visited[t] = 1
        for ni in range(len(computers)):
            if ni == t:
                continue
            if computers[t][ni] == 1 and visited[ni] == 0:  # 붙이기 가능
                s.append(ni)


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0:
            DFS(i, visited, computers)
            answer += 1
    return answer'''


#print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))

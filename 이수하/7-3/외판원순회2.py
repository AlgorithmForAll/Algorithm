import sys

def dfs(start, next, value, visited):
    global result

    if len(visited) == N:
        if arr[next][start] != 0:
            result = min(result, value + arr[next][start])
        return

    for i in range(N):
        if arr[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + arr[next][i], visited)
            visited.pop()

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

result = sys.maxsize

for i in range(N):
    dfs(i, i, 0, [i])

print(result)
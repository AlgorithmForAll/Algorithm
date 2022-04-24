
def dfs(start, arr, visited, number):
    visited[start] = True
    if number == 4:
        print(1)
        exit()
    for i in arr[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, arr, visited, number+1)
            visited[i] = False

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n):
    visited[i] = True
    dfs(i, arr, visited, 0)
    visited[i] = False
print(0)
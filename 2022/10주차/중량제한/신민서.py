from collections import deque, defaultdict

q = deque([])
n, m = map(int, input().split())
weight = []
arr = defaultdict(list) #defaultdict를 활용한 bfs 연습.

def bfs(mid, a, b):
    q.append(a)
    visited = [a]
    while q:
        v = q.popleft()
        for i in range(len(arr[v])):
            if arr[v][i][1] >= mid and arr[v][i][0] not in visited:
                visited.append(arr[v][i][0])
                q.append(arr[v][i][0])
    if b not in visited:
        return False
    return True

for mm in range(m):
    a, b, c = map(int, input().split())
    arr[a-1].append([b-1, c])
    arr[b-1].append([a-1, c])
    weight.append(c)
a, b = map(int, input().split())
weight.sort()
left = 0
right = len(weight)-1
answer = 0
while left <= right:
    mid = (left + right) // 2
    imsi = weight[mid]
    torf = bfs(imsi, a-1, b-1)
    if torf:
        answer = weight[mid]
        left = mid + 1
    else:
        right = mid - 1

print(answer)


from collections import deque
n, k = map(int, input().split())

m = max(n, k)
position = [0] * 100001
visited = [0] * 100001

def bfs():
    queue = deque([n])

    while queue:
        x = queue.popleft()
        if x == k:
            break
        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx < 100001 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)
                # 현재 위치 표시
                position[nx] = x

# 최단시간 구하기     
bfs()

count = visited[k]
temp = []
for _ in range(count + 1):
    temp.append(k)
    k = position[k]

print(count)
print(*reversed(temp))

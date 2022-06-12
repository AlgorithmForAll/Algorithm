from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
queue = deque()
visited = [False] * (N+1)

queue.append([N, [N]])

while(queue):
    num, result = queue.popleft()
    
    if num == 1:
        print(len(result)-1)
        print(*result)
        break
    if not visited[num]:
        visited[num] = True
        if num % 3 == 0:
            queue.append([num//3, result + [num//3]])
        if num % 2 == 0:
            queue.append([num//2, result + [num//2]])
        queue.append([num-1, result+[num-1]])
            
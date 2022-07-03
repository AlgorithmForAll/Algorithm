import math
import heapq
import sys
input = sys.stdin.readline
  

N = int(input())
stars = []
graph = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]

for i in range(N):
    stars.append(list(map(float, input().split())))
    
for i in range(len(stars)):
    for j in range(i+1, len(stars)):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        cost = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2)) 
        graph[i].append([cost, j])
        graph[j].append([cost, i])

def find():
    result = 0
    queue = []
    queue.append([0, 1])

    while queue:
      cost, node = heapq.heappop(queue)

      if not visited[node]:
        visited[node] = True
        result += cost
        
        for next_cost, next_node in graph[node]:
          heapq.heappush(queue, (next_cost, next_node))

    return result

print(format(find(), ".2f"))
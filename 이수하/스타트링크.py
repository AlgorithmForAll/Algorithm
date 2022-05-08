from collections import deque


def bfs(F, S, G, U, D):
    queue = deque([[S,0]])
    visited = {S}

    while queue:
        floor, count = queue.popleft()
        
        if floor == G:
            return count
        if floor + U <= F and floor + U not in visited:
            queue.append([floor + U, count + 1])
            visited.add(floor + U)
        if floor - D >= 1 and floor - D not in visited:
            queue.append([floor - D, count + 1])
            visited.add(floor - D)

    return "use the stairs"

F, S, G, U, D = map(int, input().split())

print(bfs(F, S, G, U, D))
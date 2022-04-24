"""
DFS로 진행하는 경우 거의 시퀀스
DFS하니까 메모리 초과남
이분 탐색 각인데? 아니네;;
근데 왜 DFS하면 안풀리고 BFS하면 풀리냐;;;
최솟값이라 그냥 BFS 로 무지성 돌리면 되는건가?
"""
from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [0 for i in range(F+1)]


def BFS(start):

    q = deque([start])
    count = -1

    while q:
        count += 1
        for i in range(len(q)):
            f = q.popleft()
            if f > F or f < 1:
                continue
            if f == G:
                return count
            if 1 <= f-D and visited[f-D] == 0:
                visited[f-D] = 1
                q.append(f-D)
            if F >= f+U and visited[f+U] == 0:
                visited[f+U] = 1
                q.append(f+U)
    return -1


count = BFS(S)
if count == -1:
    print("use the stairs")
else:
    print(count)

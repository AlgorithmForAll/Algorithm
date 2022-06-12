#12852 1로 만들기 2
# BFS 혹은 DP
# 배열값만 출력 시 print(*arr)

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    q = deque()
    q.append((N, [N]))
    visited = [0] * (N + 1)
    
    while q :
        cn, arr = q.popleft()
        if cn == 1:
            print(len(arr) - 1)
            print(*arr)
            break

        if visited[cn] == 0:
            visited[cn] = 1

            if cn % 3 == 0:
                q.append(((cn//3), arr + [cn//3]))

            if cn % 2 == 0:
                q.append(((cn//2), arr + [cn//2]))

            q.append((cn-1,arr + [cn-1]))

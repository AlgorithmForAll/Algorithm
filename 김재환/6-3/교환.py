from collections import deque


def BFS(N, K):

    q = deque([N])

    while q:
        S = set()
        # print(q)
        if K == 0:
            return q
        for _ in range(len(q)):
            num = q.popleft()

            for i in range(len(N)):
                for j in range(i+1, len(N)):
                    tmp = list(num)
                    tmp[i] = num[j]
                    tmp[j] = num[i]
                    if tmp[0] == '0':
                        continue
                    S.add("".join(tmp))
        # print(S)
        q += list(S)
        K -= 1
    return q


N, K = map(int, input().split())
tmp = BFS(str(N), K)
# print(tmp)
if len(tmp) == 0:
    print(-1)
else:
    tmp = list(map(int, tmp))
    print(max(tmp))

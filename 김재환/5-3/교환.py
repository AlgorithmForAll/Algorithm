"""
데이터가 작고 K가 10 이하이므로
완탐으로 풀린다. 따라서 BFS로 매번 모든 경우를 찾고 해당 값 중에 가장 큰것을 선택하여 갱신
매번 최대를 구하는게 아니라 K번실행하는 경우의 최댓값을 구해야한다.
"""
from collections import deque

N, K = map(int, input().split())


def BFS(k, start):

    q = deque([start])
    count = 0

    while q:
        if count == k:  # K번 진행한 경우 해당 값들중에 최댓값을 반환한다.
            return max(q)
        setq = set()
        for _ in range(len(q)):
            target = q.popleft()
            target = list(str(target))
            for i in range(len(str(start))):
                for j in range(i+1, len(str(start))):
                    tmp = list(target)
                    tmp[i] = target[j]
                    tmp[j] = target[i]  # i,j값을 교환한다.
                    if tmp[0] == '0':  # 앞자리가 0인경우 값을 저장하지 않는다
                        continue
                    setq.add(int("".join(tmp)))  # set에 다음에 나올 수 있는 값을 저장한다.
        q += (list(setq))
        count += 1


tmp = BFS(K, N)
if tmp == None:
    print(-1)
else:
    print(tmp)

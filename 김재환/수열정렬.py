"""
우선순위를 이용해서 해결
3
2 3 1
=> 실제 풀이는 정렬만으로도 풀 수 있음
"""
import heapq

hq = []

N = int(input())
A = list(map(int, input().split()))

for n in range(N):
    heapq.heappush(hq, [A[n], n])

P = [0 for i in range(N)]
i = 0
while hq:
    val, o = heapq.heappop(hq)
    P[o] = i
    i += 1
print(" ".join(list(map(str, P))))

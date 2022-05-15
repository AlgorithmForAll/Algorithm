"""
해설 봤는데 이해가 잘 안감....
"""

N, M = map(int, input().split())
RN = [0 for i in range(N)]
L = []
for n in range(N):
    tmp = list(map(int, input()))
    RN[n] = M - sum(tmp)
    L.append(tmp)
K = int(input())
final = 0
for n in range(N):
    rn = RN[n]
    if K >= rn and rn % 2 == K % 2:
        count = 1
        for i in range(N):
            if n == i:
                continue
            if L[i] == L[n]:
                count += 1
        final = max(final, count)

print(final)

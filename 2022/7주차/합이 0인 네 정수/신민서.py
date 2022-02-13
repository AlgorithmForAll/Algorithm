from collections import defaultdict
answer = 0
n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
d = [0] * n
for i in range(n):
    a[i], b[i], c[i], d[i] = map(int, input().split())

added = defaultdict()

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] + b[j] not in added:
            added[a[i]+b[j]] = 1
        else:
            added[a[i]+b[j]] += 1

for i in range(len(c)):
    for j in range(len(d)):
        if -(c[i]+d[j]) in added:
            answer += added[-(c[i]+d[j])]

print(answer)
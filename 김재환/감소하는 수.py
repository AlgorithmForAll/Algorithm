"""
조합으로도 풀리는 문제였네.....
"""
from itertools import combinations
N = int(input())

tmp = []
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        _comb = list(comb)
        _comb.sort(reverse=True)
        tmp.append(int("".join(map(str, _comb))))
tmp.sort()

if N < len(tmp):
    print(tmp[N])
else:
    print(-1)

from itertools import permutations
N = int(input())
tmp = list(map(int, input().split()))

tmp = list(permutations(tmp, len(tmp)))

big = 0
for t in tmp:
    total = 0
    for i in range(len(t)-1):
        total += abs(t[i]-t[i+1])
    big = max(big, total)
print(big)

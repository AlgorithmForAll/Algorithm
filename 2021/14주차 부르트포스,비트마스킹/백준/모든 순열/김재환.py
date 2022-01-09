from itertools import permutations

n = int(input())
tmp = list(permutations([i for i in range(1, n+1)], n))
for i in tmp:
    for j in i:
        print(j, end=' ')
    print()

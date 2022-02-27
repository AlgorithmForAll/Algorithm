t = int(input())

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = parent[x]
        number[x] = number[x] + number[y]

for tt in range(t):
    parent = {}
    number = {}
    f = int(input())
    for ff in range(f):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)
        print(number[parent[x]])
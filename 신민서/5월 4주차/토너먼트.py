n, first, second = map(int, input().split())
r = 1
while min(first, second) % 2 != 1 or min(first, second)+1 != max(first, second):
    if first % 2 == 1:
        first += 1
    if second % 2 == 1:
        second += 1
    first //= 2
    second //= 2
    r += 1
print(r)
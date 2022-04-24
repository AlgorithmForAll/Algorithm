N, L = map(int, input().split())
tmp = list(map(int, input().split()))
tmp.sort()

for fr in tmp:
    if fr <= L:
        L += 1
    else:
        break
print(L)

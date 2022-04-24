
N, T = map(int, input().split())

tmp = []
for _ in range(N):
    tmp.append(int(input()))
tmp.sort(key=lambda x: -x)

coin = 0
for i in tmp:
    mok = T // i
    if mok != 0:
        T -= mok*i
        coin += mok
print(coin)

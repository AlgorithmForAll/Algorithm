
st = input()


def kmp_tb(st):
    tb = [0 for i in range(len(st)+1)]
    j = 0
    for i in range(1, len(st)):
        while 0 < j and st[i] != st[j]:
            j = tb[j-1]
        if st[i] == st[j]:
            j += 1
            tb[i] = j
    return tb


big = 0
for i in range(len(st)):
    big = max(big, max(kmp_tb(st[i:])))
print(big)

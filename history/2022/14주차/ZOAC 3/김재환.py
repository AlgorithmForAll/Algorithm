lch = [['q', 'w', 'e', 'r', 't'],
       ['a', 's', 'd', 'f', 'g'],
       ['z', 'x', 'c', 'v']]
rch = [['y', 'u', 'i', 'o', 'p'],
       ['h', 'j', 'k', 'l'],
       ['b', 'n', 'm']]
M = {}
for i in range(len(lch)):
    for j in range(len(lch[i])):
        M[lch[i][j]] = ['l', [i, j]]

for i in range(len(rch)):
    for j in range(len(rch[i])):
        M[rch[i][j]] = ['r', [i, j]]

L, R = input().split()
L = M[L][1]
R = M[R][1]

count = 0
for ch in list(input()):

    ty, tx = M[ch][1]

    if M[ch][0] == 'l':
        ly, lx = L
        dy = abs(ly-ty)
        dx = abs(lx-tx)
        count += (dy+dx+1)
        L = [ty, tx]
    else:
        ry, rx = R
        dy = abs(ry-ty)
        dx = abs(rx-tx)
        count += (dy+dx+1)
        R = [ty, tx]
print(count)

direction = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T':[0, 1], 'RT':[1, 1], 'LT':[-1, 1], 'RB':[1, -1], 'LB':[-1, -1]}
a_to_n = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
king, stone, n = input().split()
n = int(n)
kx, ky = a_to_n[king[0]], king[1]
sx, sy = a_to_n[stone[0]], stone[1]
for i in range(n):
    inp = input()
    direct = direction[inp]
    if 1 <= int(kx) + int(direct[0]) <= 8 and 1 <= int(ky) + int(direct[1]) <= 8:
        if int(sx) == int(kx) + int(direct[0]) and int(sy) == int(ky) + int(direct[1]):
            if not 1 <= int(sx) + int(direct[0]) <= 8 or not 1 <= int(sy) + int(direct[1]) <= 8:
                pass
            else:
                kx, ky, sx, sy = int(kx) + int(direct[0]), int(ky) + int(direct[1]), int(sx) + int(direct[0]), int(sy) + int(direct[1])
        else:
            kx, ky = int(kx) + int(direct[0]), int(ky) + int(direct[1])
print(chr(kx+64) + str(ky))
print(chr(sx+64) + str(sy))
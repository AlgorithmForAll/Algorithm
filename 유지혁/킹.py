#1063 킹
# 구현 
import sys
input = sys.stdin.readline

info = {"R": (0, 1), "L": (0, -1), "B": (1, 0), "T": (-1, 0),
    "RT": (-1, 1), "LT": (-1, -1),"RB": (1, 1), "LB": (1, -1)}

if __name__ == "__main__":
    king, stone, N = input().split()
    kx, ky = 8-int(king[1]), ord(king[0])-ord("A")
    sx, sy = 8-int(stone[1]), ord(stone[0])-ord("A")
    for _ in range(int(N)):
        cmd = input().strip()
        dx, dy = info[cmd]
        if not (0 <= kx + dx < 8 and 0 <= ky + dy < 8):
            continue
        kx += dx
        ky += dy
        if (kx, ky) == (sx, sy):
            if not (0 <= sx + dx < 8 and 0 <= sy + dy < 8):
                kx -= dx
                ky -= dy
                continue
            sx += dx
            sy += dy
       
    print(chr(ord("A") + ky) + str(8 - kx))
    print(chr(ord("A") + sy) + str(8 - sx))

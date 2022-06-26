
"""
이분탐색?????
meet the middle

N이 30인경우 가능한 케이스는 2^30 => 너무 많아서 일일히 확인 못함
2개로 그룹을 쪼개고 가능한 합이 C보다 작으면 가능한 케이스로 분류
만약 A그룹의 케이스와 B그룹의 케이스를 나누고 나면 B그룹에서 가능한 개수를 구하기 위해 이분탐색을 적용하여 경우의 수 계산
"""

N, C = map(int, input().split())
W = list(map(int, input().split()))

AW = W[:len(W)//2]
BW = W[len(W)//2:]


def bruteForce(i, length, w, TW, group):
    if i == length:
        if w <= C:
            group.append(w)
        return
    bruteForce(i+1, length, w+TW[i], TW, group)
    bruteForce(i+1, length, w, TW, group)


def binSearch(G, t):
    L = 0
    R = len(G)-1
    F = -1
    while L <= R:
        M = (L+R)//2
        if t >= G[M]:
            L = M+1
            F = M
        else:
            R = M-1
    if F == -1:
        return 0
    else:
        return F+1


AG = []
BG = []
bruteForce(0, len(AW), 0, AW, AG)
bruteForce(0, len(BW), 0, BW, BG)
AG.sort()
BG.sort()

count = 0
for i in range(len(AG)):
    sw = AG[i]
    tw = C-sw
    count += binSearch(BG, tw)
print(count)

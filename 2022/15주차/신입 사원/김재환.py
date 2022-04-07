import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    tmp = []
    for n in range(N):
        tmp.append(list(map(int, input().split())))
    tmp.sort()
    limit = tmp[0][1]
    for i in range(1, len(tmp)):
        if tmp[i][1] > limit:
            N -= 1
        else:
            limit = tmp[i][1]
    print(N)

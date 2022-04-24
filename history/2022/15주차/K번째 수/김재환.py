N = int(input())
K = int(input())

L = 1
R = N*N

while L <= R:
    M = (L+R)//2

    print("m:", M)
    count = 0
    for i in range(1, N+1):
        count += min(M//i, N)
    print("c:", count)

    if K > count:
        L = M+1
    else:
        R = M-1

print(L)

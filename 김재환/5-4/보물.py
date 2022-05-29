"""
5
1 1 1 6 0
2 7 8 3 1
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
C = []
for n in range(N):
    C.append(A[n] * B[n])
print(sum(C))

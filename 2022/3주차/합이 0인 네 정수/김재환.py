"""
정렬 + 이분 탐색 + 두 포인터 + 중간에서 만나기 = 미친문제
"""
N = int(input())
A = []
B = []
C = []
D = []
for i in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
A.sort()
B.sort()
C.sort()
D.sort()
print(A)
print(B)
print(C)
print(D)

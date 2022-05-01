import sys
input = sys.stdin.readline

A, B = input().split()

final = 0
for si in range(len(B) - len(A)+1):
    count = 0
    for i in range(len(A)):
        if A[i] == B[si+i]:
            count += 1
    final = max(final, count)
print(len(A)-final)

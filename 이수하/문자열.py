import sys
input = sys.stdin.readline


A, B = map(str, input().split())

arr = []
for i in range(len(B)-len(A)+1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            count += 1
    arr.append(count)

print(min(arr))
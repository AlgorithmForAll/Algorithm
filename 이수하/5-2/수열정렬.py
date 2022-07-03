'''
문자열 문제
'''
import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

A = sorted(arr)

P = []
for i in range(N):
    index = A.index(arr[i])
    P.append(index)
    A[index] = -1
    
print(' '.join(map(str, P)))
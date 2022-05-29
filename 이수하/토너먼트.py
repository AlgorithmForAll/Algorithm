'''
브루트포스
'''

import sys
input = sys.stdin.readline


N, A, B = map(int, input().split())

count = 0
while A != B:
    A -= A//2
    B -= B//2
    
    count += 1

print(count)
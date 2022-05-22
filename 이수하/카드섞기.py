'''
시뮬레이션 + 완전탐색
사이클이 존재하면 -1
'''

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

count = 0

new_P = P.copy()
check = [0]*N

# 조건에 만족할 떄 까지
while [0, 1, 2]*(N//3) != P:
    for i in range(N):
        check[S[i]] = P[i]
    
    P = check
    check = [0] * N
    
    count += 1
    
    # 사이클이 존재하면 break
    if new_P == P:
        count = -1
        break

print(count)
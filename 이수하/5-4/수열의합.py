'''
수학 문제
N = (x+1)+(x+2)...+(x+L)
N = Lx + L(L+1)/2
조건 1. 2<=L<=100
조건 2. L 이 가장 짧고 연속된 음이 아닌 정수
'''

import sys
input = sys.stdin.readline

N, L = map(int, input().split())

num = []
for i in range(L, 101):
    lx = N - i*(i+1)/2
    
    if lx % i == 0:
        lx = int(lx/i)
        if lx >= -1:
            for j in range(1, i+1):
                print(lx+j, end=" ")
            break

else:
    print(-1)
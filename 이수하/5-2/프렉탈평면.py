'''
재귀랑 분할정복
시간 * N 가 크기
r1, r2 ~ c1,c2 크기만큼 반복
검정색 체크 범위 size*(N-K)//2 ~ size*(N+K)//2
'''
import sys
input = sys.stdin.readline

def fractal(width, r, c):
    if width == 1:
        return 0
    
    size = width // N
    
    if r >= size*(N-K)//2 and r < size*(N+K)//2 and c >= size*(N-K)//2 and c < size*(N+K)//2:
        return 1
    
    return fractal(size, r%size, c%size)

s, N, K, R1, R2, C1, C2 = map(int, input().split())

size = 1

while s != 0:
    size *= N
    s -= 1

for i in range(R1, R2+1):
    for j in range(C1, C2+1):
        print(fractal(size, i, j), end="")
    print()

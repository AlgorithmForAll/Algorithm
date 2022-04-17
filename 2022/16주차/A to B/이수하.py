import sys
input = sys.stdin.readline


A, B = map(int, input().split())

count = 1
while A != B:
    if A > B or (B % 2 != 0 and B % 10 != 1):
        count = -1
        break
    elif B % 10 == 1:
        B //= 10
        count += 1
    elif B % 2 == 0:
        B //= 2
        count += 1
        
print(count)
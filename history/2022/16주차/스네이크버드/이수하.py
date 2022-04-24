import sys
input = sys.stdin.readline


N, L = map(int, input().split())
snake = list(map(int, input().split()))

for i in sorted(snake):
    if L >= i:
        L += 1
    else:
        break

print(L)
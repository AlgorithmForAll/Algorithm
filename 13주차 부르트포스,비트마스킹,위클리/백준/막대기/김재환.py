N = int(input())
i = 0
while N != 0:
    if N % 2 == 1:
        i += 1
    N = N//2
print(i)

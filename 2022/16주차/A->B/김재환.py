A, B = map(int, input().split())

C = B
count = 0
while A < C:
    count += 1
    if C % 2 == 0:
        C = int(C/2)
    elif str(C)[-1] == '1':
        C = int(str(C)[:-1])
    else:
        break
if C != A:
    print(-1)
    exit()
print(count+1)

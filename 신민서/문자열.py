a, b = input().split()

answer = 0
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            answer += 1
    print(answer)
    exit()

smaller = a if len(a) < len(b) else b
bigger = a if smaller == b else b

answer = 50
for i in range(len(bigger) - len(smaller) + 1):
    temp = 0
    for j in range(i, i+len(smaller)):
        if bigger[j] != smaller[j-i]:
            temp += 1
    answer = min(answer, temp)
print(answer)




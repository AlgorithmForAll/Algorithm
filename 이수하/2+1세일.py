import sys
input = sys.stdin.readline


N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

arr = sorted(array)

count = len(arr)//3
rest = len(arr)%3

sum = 0
while len(arr)>0:
    if len(arr) == 1:
        a = arr.pop()
        sum += a
        break
    else:
        a = arr.pop()
        b = arr.pop()
        sum += a
        sum += b
        if len(arr) == 0:
            break
        arr.pop()

print(sum)
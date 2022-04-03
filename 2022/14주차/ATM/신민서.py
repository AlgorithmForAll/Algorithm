n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
for i in range(n):
    for j in range(i+1):
       answer += arr[j]

print(answer)
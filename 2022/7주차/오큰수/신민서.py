n = int(input())
inp = list(map(int, input().split()))
stack = []
arr = [-1] * n
stack.append(inp[-1]) #제일 오른쪽 값 추가
for i in range(n-2, -1, -1):
    while stack and stack[-1] <= inp[i]:
        stack.pop()
    if stack:
        arr[i] = stack[-1]
    stack.append(inp[i])

for a in arr:
    print(a, end=' ')
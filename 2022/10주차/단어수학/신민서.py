n = int(input())
arr = dict()
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] not in arr:
            arr[s[j]] = 1 * 10**(len(s)-j-1)
        else:
            arr[s[j]] += 1 * 10 ** (len(s)-j-1)

arr = sorted(arr.values(), reverse=True)
answer = 0
num = 9
for i in range(len(arr)):
    arr[i] *= num
    num -= 1
    answer += arr[i]

print(answer)



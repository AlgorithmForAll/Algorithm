from copy import deepcopy

def check():
    for i in range(len(narr)):
        if narr[i] not in final[i%3]:
            return False
    return True

n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
final = [[] for _ in range(3)]

for i in range(len(s)):
    final[p[i]].append(s[i])

arr = deepcopy(s)
narr = deepcopy(arr)
r = 0
while not check():
    arr = deepcopy(narr)
    for i in range(len(s)):
        narr[s[i]] = arr[i]
    if narr == s:
        r = -1
        break
    r += 1
print(r)
"""
10
1 2 3 4 5 6 7 8 9 10
"""
import sys
input = sys.stdin.readline

N = int(input())
target = list(map(int, input().split()))
target.sort()

count = 0
for i in range(N):
    tmp = target[:i] + target[i+1:]
    L, R = 0, len(tmp)-1
    while L < R:
        t = tmp[L] + tmp[R]
        if t == target[i]:
            count += 1
            break
        elif t > target[i]:
            R -= 1
        else:
            L += 1
print(count)

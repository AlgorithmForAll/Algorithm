from collections import deque
import sys
input = sys.stdin.readline
MAX = 1023
dp = [[] for i in range(MAX)]


def solve():
    if 0 <= N <= 10:
        print(N)
        return
    
    queue = deque()
    for i in range(1, 10):
        queue.append(i)
        dp[i] = i

    check = 9
    while check <= N and queue:
        num = queue.popleft()
        last = num%10
        for i in range(last):
            queue.append(num*10 + i)
            check += 1
            dp[check] = num*10 + i
    if check >= N and dp[N] != 0:
        print(dp[N])
    else:
        print(-1)

N = int(input())
solve()
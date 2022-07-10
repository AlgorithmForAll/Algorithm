"""
https://www.acmicpc.net/problem/1700
"""
import sys

sys.stdin = open("../input.txt")
n, k = map(int, input().split())
data = list(map(int, input().split()))

plug = []
count = 0

for i in range(k):
    tool = data[i]

    if tool in plug:
        continue
    elif len(plug) < n:
        plug.append(tool)
    else:
        temp = dict(zip(plug, [101 for _ in range(n)]))
        for j in range(i + 1, k):
            nxt_tool = data[j]
            if nxt_tool in plug:
                temp[nxt_tool] = min(temp[nxt_tool], j)

        temp = list(temp.items())
        temp.sort(key=lambda x: x[1])
        temp.pop()
        plug = [data[i]]
        count += 1
        for p, np in temp:
            plug.append(p)


print(count)

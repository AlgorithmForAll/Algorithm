"""
5
-1 0 0 1 1
2
일자인 경우 예외가 존재한다.
"""
import sys
sys.setrecursionlimit(100000)
N = int(input())
parent = list(map(int, input().split()))
root = 0
adj = {}
for i in range(-1, N):
    adj[i] = []
for i in range(len(parent)):
    if parent[i] == -1:
        root = i
    adj[parent[i]].append(i)

delLeaf = int(input())
count = 0


def DFS(node):
    global count

    isLeaf = True
    for child in adj[node]:
        if child == delLeaf:
            continue
        else:
            isLeaf = False
            DFS(child)
    if node != -1 and isLeaf == True:
        count += 1


DFS(-1)
print(count)

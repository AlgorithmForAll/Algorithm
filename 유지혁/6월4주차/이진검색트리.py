#5639 이진 검색 트리
# DFS

import sys
sys.setrecursionlimit(10**9)


def go(start, end):
    if start > end:
        return
    
    root = graph[start]
    tmp = end + 1
    for i in range(start + 1, end + 1):
        if root < graph[i]:
            tmp = i
            break
            
    go(start + 1, tmp - 1)
    go(tmp,end)
    print(root)
   
if __name__ == "__main__":
    graph = []
    while True:
        try:
            graph.append(int(input()))
        except:
            break
    go(0, len(graph) - 1)


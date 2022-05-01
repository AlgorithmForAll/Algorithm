"""
참고: https://imzzan.tistory.com/40
처음에 tree를 이중리스트로 만들어서 원하는 지우고 싶은 노드를 delete 배열에 포함시키고 지우려 했지만 실패했다.
(방법이 살짝 잘못된 것 같다.)
"""
import sys

n = int(input())
tree = [[] for _ in range(n)]
p = list(map(int,sys.stdin.readline().split()))
for i in range(n):
    tree[i] = p[i]
remove = int(input())

def delete(remove):
    tree[remove] = -2
    for i in range(n):
        if tree[i] == remove:
            tree[i] = -2
            delete(i)
delete(remove)
cnt = 0
for i in range(n):
    if tree[i] != -2:
        err = 0
        for j in tree:
            if j == i:
                err = 1
                break
        if err == 0:
            cnt += 1
print(cnt)
"""
트라이 도전~

"""
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, key, flag=False):
        self.key = key
        self.end = flag
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node(None)  # 루트라서 비어있는놈 제작

    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in cur.children:
                cur.children[ch] = Node(ch)
            else:  # 체크한다.
                if cur.children[ch].end == True:
                    return False
            cur = cur.children[ch]  # 포인터를 하위로 바꿔줌
            if i == len(word)-1:  # 마지막 단어인경우
                cur.end = True
        return True


T = int(input())
for _ in range(T):
    N = int(input())
    nl = []

    for i in range(N):
        nl.append(input().strip())
    nl.sort()
    tree = Trie()
    flag = True
    for word in nl:
        if tree.search(word) == False:
            flag = False
    if flag == False:
        print("NO")
    else:
        print("YES")

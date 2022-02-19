"""
전화번호 목록
https://www.acmicpc.net/problem/5052
참고 : https://velog.io/@gojaegaebal/210126-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%8050%EC%9D%BC%EC%B0%A8-%ED%8A%B8%EB%9D%BC%EC%9D%B4Trie-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0feat.-Class
Trie 자료구조!
"""

import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if curr_node.data is not None:
                return False
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string
        return True


def solution(tel):
    data = Trie()
    for telnum in tel:
        if not data.insert(telnum):
            return "NO"
    return "YES"


for _ in range(int(input())):
    n = int(input())
    tel = [input().rstrip() for _ in range(n)]
    tel.sort(key=len)
    print(solution(tel))

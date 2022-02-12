"""
길 찾기 게임
https://programmers.co.kr/learn/courses/30/lessons/42892
참고 : https://www.youtube.com/watch?v=K6ZpR22qF1M
"""
import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y > other.y

    def __str__(self):
        return f"[{self.data} {self.x} {self.y} left={self.left} right={self.right}]"


def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)


def preorder(param, node):
    if node is None:
        return
    param.append(node.data)
    preorder(param, node.left)
    preorder(param, node.right)


def postorder(param, node):
    if node is None:
        return

    postorder(param, node.left)
    postorder(param, node.right)
    param.append(node.data)


def solution(nodeinfo):
    n = len(nodeinfo)
    data = []
    for i in range(n):
        x, y = nodeinfo[i]
        data.append(Node(i + 1, x, y))

    data.sort()
    root = data[0]

    for i in range(1, n):
        addNode(root, data[i])

    answer = [[], []]
    preorder(answer[0], root)
    postorder(answer[1], root)
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]),
      [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]])

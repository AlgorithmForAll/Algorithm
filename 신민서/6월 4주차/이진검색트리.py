class Tree:
    def __init__(self, value): #한 노드의 초기 left와 right는 None으로, value는 자기 자신으로
        self.left = None
        self.right = None
        self.value = value

    def insertion(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insertion(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insertion(value)

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

binaryTree = Tree(preorder[0])

for i in range(1, len(preorder)):
    binaryTree.insertion(preorder[i])

binaryTree.postorder()
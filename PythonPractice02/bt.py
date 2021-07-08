from stack import Stack
from collections import deque
import math
class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        # def traverse_inorder(self):
        #    if self.left:
        #      self.left.traverse_inorder()
        #    print(self.value, end=" > ")
        #    if self.right:
        #        self.right.traverse_inorder()

    def __init__(self):
        self.root = None
 
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" > ")
            self._inorder(node.right)

    def _preorder(self, node):
        if node:
            print(node.value, end=" > ")
            self._preorder(node.left)
            self._preorder(node.right)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value, end=" > ")

    def traverse_inorder(self):
        print("inorder")
        self._inorder(self.root)
        print()
    
    def traverse_preorder(self):
        print("preorder")
        self._preorder(self.root)
        print()
    
    def traverse_postorder(self):
        print("postorder")
        self._postorder(self.root)
        print()

    def dfs(self):
        print("dfs: ",end="")
        stack = Stack()
        stack.push(self.root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                print(node.value, end=" > ")
                stack.push(node.right)
                stack.push(node.left)

    def bfs(self):
        print("bfs: ",end="")
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if node:
                print(node.value, end=" > ")
                queue.append(node.left)
                queue.append(node.right)
    
    def _height(self, node):
        if not node:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height)+1

    def height(self):
        return self._height(self.root)
#           A
#       B       C
#     D   E   F   G
#      H     I J   

tree = BinaryTree()
tree.root = BinaryTree.Node("A")
node1 = BinaryTree.Node("B")
node2 = BinaryTree.Node("C")
node3 = BinaryTree.Node("D")
node4 = BinaryTree.Node("E")
node5 = BinaryTree.Node("F")
node6 = BinaryTree.Node("G")
node7 = BinaryTree.Node("H")
node8 = BinaryTree.Node("I")
node9 = BinaryTree.Node("J")
node10 = BinaryTree.Node("K")

tree.root.left = node1
tree.root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node3.right = node7

node5.left = node8
node5.right = node9

node8.left = node10

tree.traverse_inorder()
tree.traverse_preorder()
tree.traverse_postorder()
tree.dfs()
print()
tree.bfs()
print()
print(tree.height())
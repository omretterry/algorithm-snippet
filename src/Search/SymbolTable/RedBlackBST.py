# 红黑树
# 优点：最优的查找插入效率
# 链接需要额外的空间（同BST）
# 首先需要理解2-3树的节点拓展策略

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from helper.TreeNode import RBTreeNode


class RedBlackBst():
    def __init__(self):
        self.root = None

    def size(self, node):
        if node is None:
            return 0
        return node.size

    # 指向当前节点的链接是否为红链接
    def isRed(self, node):
        if node is None:
            return False
        return node.color is RBTreeNode.RED

    # 红链接右旋转
    def rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = x.right.color
        x.right.color = RBTreeNode.RED
        node.size, x.size = x.size, node.size
        return x

    # 红链接左旋转
    def rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = x.left.color
        x.left.color = RBTreeNode.RED
        node.size, x.size = x.size, node.size
        return x

    # 反转节点颜色
    def flipColor(self, node):
        node.left.color = not node.left.color
        node.right.color = not node.right.color
        node.color = not node.color
        return node

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = RBTreeNode.BLACK

    def _put(self, node, key, value):
        if node is None:
            return RBTreeNode(key, value)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.val = val

        # 红黑树节点操作
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            node = self.flipColor(node)

        node.size = self.size(node.left) + self.size(node.right) + 1
        return node


rbbst = RedBlackBst()
testData = [
    (4, 'F'),
    (2, 'E'),
    (5, 'A'),
    (1, 'B'),
    (6, 'C'),
]
for item in testData:
    print('put:', item[0], ":", item[1])
    rbbst.put(item[0], item[1])
